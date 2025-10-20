import qrcode
from PIL import Image

img = qrcode.make('blah')
img.save('blah.png')

test = Image.open("blah.png")
test.show()