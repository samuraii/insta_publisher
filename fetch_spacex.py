import requests
import argparse
from helpers import download_image


def get_launch_pictures(launch_name):
    url = f"https://api.spacexdata.com/v3/launches/{launch_name}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['links']['flickr_images']


def download_spacex_pictures(launch_name):
    for img_link in enumerate(get_launch_pictures(launch_name)):
        download_image(img_link[1], f"spaceX{img_link[0]}.jpg")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id', required=True, type=str, default='latest', help='Launch you want to fetch pictures')
    args = parser.parse_args()
    download_spacex_pictures(args.launch_id)
