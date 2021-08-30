# randomimge

If you need an image to test a computer vision algorithm, a web service or a neural network, then use this package to get a random image from https://picsum.photos/.

## Installation

Install directly from github:
```bash
python -m pip install git+https://github.com/yashenkoxciv/randomimage
```

Install from cloned repository:
```bash
git clone https://github.com/yashenkoxciv/randomimage
cd torchvision_features_extraction
python -m pip install .
```

## Usage

Simplest use case:
```python
from randomimage import get_random_image

image = get_random_image()

image.show()
```
It returns image with width and height between 150 and 300.

# TODO

* add more getters (see https://picsum.photos/ API)
* add saving to .randomimage.json (ids and other params of image getter)
