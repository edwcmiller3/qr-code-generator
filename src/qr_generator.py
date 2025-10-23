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
    file_name: str = f"{datetime.now().strftime("%Y%m%d-%H%M%S")}{ext}"

    try:
        path = _create_img_dir()
        qr.save(path + file_name)
    except:
        raise Exception("QR code could not be saved")


def show_qr_code(img: Image) -> None:
    img.show()


def create_qr_code(data: str) -> Image:
    qr = qrcode.make(data)
    return qr


def main():
    print(_create_img_dir())
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument('-s', '--save', action='store_true',
                        help='Save QR code to disk')
    parser.add_argument('data', type=str, help='Data to be encoded in QR code')
    args = parser.parse_args()

    qr_code: Image = create_qr_code(args.data)

    if args.save:
        save_qr_img(qr_code)

    show_qr_code(qr_code)


if __name__ == '__main__':
    main()
