# from flask import Flask, request, render_template
# import base64
# from PIL import Image, ImageDraw, ImageFont
# import io
#
# app = Flask(__name__)
#
#
# @app.route('/makeimage', methods=['POST'])
# def make_image():
#     # Получаем значения width и height из запроса
#     width = int(request.form['width'])
#     height = int(request.form['height'])
#     text = request.form.get('text', '')  # Получаем текст (если он был передан)
#
#     # Создаем изображение с заданными параметрами
#     image = Image.new('RGB', (width, height), color='white')
#     draw = ImageDraw.Draw(image)
#
#     # Если указан текст, рисуем его на изображении
#     if text:
#         font = ImageFont.truetype("arial.ttf", 20)
#         text_width = draw.textlength(text, font)
#         # left, top,right,bottom = draw.textbbox((0, 0), text, font=font)
#         draw.text(((width-text_width)//2, 15), text, fill='black')
#
#     # Конвертируем изображение в байты формата JPEG и кодируем в base64
#     buffered = io.BytesIO()
#     image.save(buffered, format="JPEG")
#     image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
#
#     # Возвращаем шаблон с изображением в кодировке base64
#     return render_template('image.html', image_base64=image_base64)
#
# @app.route('/')
# def start():
#     return '1153278'

from flask import Flask, request, render_template
from PIL import Image, ImageDraw, ImageFont
import io
import base64

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/makeimage', methods=['POST'])
def make_image():
    # Получаем значения width и height из запроса
    width = int(request.form['width'])
    height = int(request.form['height'])
    text = request.form.get('text', '')  # Получаем текст (если он был передан)

    # Создаем изображение с заданными параметрами
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # Если указан текст, рисуем его на изображении
    if text:
        try:
            # Используем встроенный шрифт PIL в случае отсутствия arial.ttf
            font = ImageFont.truetype("arial.ttf", 20)
        except IOError:
            font = ImageFont.load_default()

        # Получаем размеры текста
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Рисуем текст по центру изображения
        draw.text(((width - text_width) // 2, (height - text_height) // 2), text, fill='black', font=font)

    # Конвертируем изображение в байты формата JPEG и кодируем в base64
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    image.save("./images/created_image.jpg")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    with open('render', 'w') as fp:
        fp.write(image_base64)
    # Возвращаем шаблон с изображением в кодировке base64
    return render_template('image.html', image_base64=image_base64)


if __name__ == '__main__':
    app.run(debug=True)


