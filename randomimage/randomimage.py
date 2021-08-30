import io
import random
import logging
import requests
from PIL import Image

REQUEST_ROOT_URL_WH = 'https://picsum.photos/{width}/{height}'
REQUEST_ROOT_URL_S = 'https://picsum.photos/{side}'

MIN_W, MAX_W = 150, 300
MIN_H, MAX_H = 150, 300


def get_random_image(width: int = 0, height: int = 0) -> Image:
    # response url:
    # 'https://i.picsum.photos/id/965/200/300.jpg?hmac=16gh0rrQrvUF3RJa52nRdq8hylkBd-pL4Ff9kqsNRDQ'
    if width is None:
        width = random.randint(MIN_W, MAX_W)
    elif height is None:
        height = random.randint(MIN_H, MAX_H)

    request_url = REQUEST_ROOT_URL_WH.format(width=width, height=height)

    response = requests.get(request_url)

    res_url = response.url
    logging.debug(res_url)

    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))

    return image

