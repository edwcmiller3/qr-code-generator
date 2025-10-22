import qrcode
from PIL.Image import Image
from datetime import datetime
import argparse
import os

# img = qrcode.make('blah')
# a = type(img)
# img.save('blah.png')

# test = Image.open("blah.png")
# test.show()


def _create_img_dir() -> str:
    current_dir: str = os.getcwd()
    img_dir: str = 'img/'
    full_dir: str = os.path.join(current_dir, img_dir)

    os.makedirs(os.path.dirname(full_dir), exist_ok=True)

    return full_dir


def create_qr_code(data: str, path: str) -> Image:
    qr = qrcode.make(data)
    ext = '.png'
    file_name: str = ext.join(datetime.now().strftime("%Y%m%d-%H%M%S"))

    qr.save(file_name)


def show_qr_code(img: Image) -> None:
    img.show()


def main():
    print(_create_img_dir())


if __name__ == '__main__':
    main()
