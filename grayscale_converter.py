from PIL import Image
from pathlib import Path


def convert(source, destination, name):
    img = Image.open(Path(source, name)).convert('L')
    Path(destination, source).mkdir(parents=True, exist_ok=True)
    img.save(Path(destination, source, name))
    return "{}, {} OK".format(source, name)
