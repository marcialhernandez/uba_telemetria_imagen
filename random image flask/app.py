from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def random_image():
    image_folder = 'static/images'  # Ruta a la carpeta con las imágenes
    images = os.listdir(image_folder)
    random_image = random.choice(images)
    image_path = f'static/images/{random_image}'
    return render_template('D://04-Lau//AI TRAIN//AI PROJECT//random image flask//template//index.html', image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
