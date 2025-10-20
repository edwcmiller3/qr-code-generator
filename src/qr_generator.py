import qrcode
from PIL import Image
import argparse
import os

# img = qrcode.make('blah')
# a = type(img)
# img.save('blah.png')

# test = Image.open("blah.png")
# test.show()


def _create_img_dir() -> os.PathLike:
    current_dir: os.PathLike = os.getcwd()
    img_dir: str = 'img/'
    full_dir: os.PathLike = os.path.join(current_dir, img_dir)

    qr_dir: os.PathLike = os.makedirs(
        os.path.dirname(full_dir), exist_ok=True)

    return qr_dir


def create_qr_code(data: str) -> Image:
    pass


def show_qr_code(img: Image) -> None:
    img.show()

def main():
    print(_create_img_dir())


if __name__ == '__main__':
    main()
