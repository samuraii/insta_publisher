import os
import argparse

from helpers import square_image
from instabot import Bot
from dotenv import load_dotenv


def post_image(username, password, image_file):
    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_photo(f"images/{image_file}")

if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_name', required=True, type=str, help='Imgae name from images folder to post')
    args = parser.parse_args()
    square_image(f"images/{args.image_name}")
    post_image(os.getenv("USERNAME"), os.getenv("PASSWORD"), args.image_name)
