# 4_insta_publisher

Project allows to fetch hubble and spacex images, and post them to instagram.

### Install

```
python3 -m venv env
sourcce env/bin/activate
pip install -U pip
pip install -r reuiqrements.txt
```

### Setup

Create file .env in the root folder and fill it with the following information

```
USERNAME={your instagram account}
PASSWORD={your instagram password}
```

### Usage

First fetch images from hubble or spacceX site.

```
python fetch_spacex.py --launch_id=latest
```

Post them to instagram by name from images folder.

```
python publish_pictures.py --image_name=spaceX5.jpg
```

## Profit.