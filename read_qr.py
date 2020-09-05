from PIL import Image
from pyzbar.pyzbar import decode
# data = decode(Image.open('thresholded.png'))
data = decode(Image.open('pic/qr.png'))
print(data)
