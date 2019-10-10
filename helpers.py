import os
import requests
from PIL import Image


def download_image(image_url, image_name):
    response = requests.get(image_url)
    os.makedirs('images', exist_ok=True)
    with open(f'images/{image_name}', 'wb') as file:
        file.write(response.content)


def get_file_extension(file_url):
    return file_url.split(".")[-1]


def square_image(image_file):
    image = Image.open(image_file)
    image.thumbnail((800, 800))
    coordinates = (0, 0, 600, 600)
    cropped = image.crop(coordinates)
    cropped.save(image_file)
