import qrcode
from PIL.Image import Image
from datetime import datetime
import argparse
import os


def _create_img_dir() -> str:
    current_dir: str = os.getcwd()
    img_dir: str = 'img/'
    full_dir: str = os.path.join(current_dir, img_dir)

    os.makedirs(os.path.dirname(full_dir), exist_ok=True)

    return full_dir


def save_qr_img(qr: Image) -> None:
    ext = '.png'
    file_name: str = ext.join(datetime.now().strftime("%Y%m%d-%H%M%S"))

    try:
        path = _create_img_dir()
        qr.save(path + file_name)
    except:
        raise Exception("QR code could not be saved")


def show_qr_code(img: Image) -> None:
    img.show()


def create_qr_code(data: str, path: str, save: bool) -> Image:
    qr = qrcode.make(data)


def main():
    print(_create_img_dir())


if __name__ == '__main__':
    main()
