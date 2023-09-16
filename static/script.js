const interactiveImage = document.getElementById("interactive-image");
const timer = document.getElementById("timer");
let startTime = Date.now();
let remainingTime = 60;

interactiveImage.addEventListener("mousedown", (event) => {
    const paint = document.createElement("div");
    paint.className = "paint";
    document.body.appendChild(paint);
    updatePaintPosition(event, paint);

    document.addEventListener("mousemove", (event) => {
        updatePaintPosition(event, paint);
    });

    document.addEventListener("mouseup", () => {
        document.removeEventListener("mousemove", updatePaintPosition);
        const currentTime = Date.now() - startTime;
        const interaction = {
            x: parseInt(paint.style.left, 0) , // Adjust for dot center
            y: parseInt(paint.style.top, 0) , // Adjust for dot center
            time: currentTime,
        };
        recordInteraction(interaction);
    });
});

function recordInteraction(interaction) {
    fetch("/record_interaction", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(interaction),
    });
}

function updatePaintPosition(event, paint) {
    const x = event.clientX - interactiveImage.getBoundingClientRect().left;
    const y = event.clientY - interactiveImage.getBoundingClientRect().top;
    paint.style.left = `${x - 15}px`; // Adjust for dot center
    paint.style.top = `${y - 15}px`; // Adjust for dot center
}

function updateTimer() {
    const elapsedTime = Math.floor((Date.now() - startTime) / 1000);
    remainingTime = Math.max(0, 60 - elapsedTime);
    timer.textContent = `Time left: ${remainingTime} seconds`;
    if (remainingTime === 0) {
        fetch("/save_interaction", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({}),
    });
        // Guardar el archivo JSON aquí cuando se agote el tiempo.
    }
}

setInterval(updateTimer, 1000);
