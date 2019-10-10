import requests
import argparse
from helpers import download_image, get_file_extension


def get_hubble_pictures(pic_id):
    url = f"http://hubblesite.org/api/v3/image/{pic_id}"
    response = requests.get(url)
    response.raise_for_status()
    links = []
    for file_data in response.json()['image_files']:
        file_url = "https://" + file_data['file_url'].replace("//imgsrc.hubblesite.org/hvi", "hubblesite.org")
        links.append(file_url)
    return links


def download_hubble_pictures(pic_id=1):
    for img_link in get_hubble_pictures(pic_id):
        download_image(img_link, f"Hubble{pic_id}.{get_file_extension(img_link)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_id', required=True, type=str, help='Imgae id to fetcch from hubble pictures')
    args = parser.parse_args()
    download_hubble_pictures(args.image_id)
