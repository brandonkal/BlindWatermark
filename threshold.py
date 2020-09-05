import cv2
import sys

file = "/work/out_wm.png"
if len(sys.argv > 0):
    file = sys.argv[1]
img = cv2.imread(file, 0)

# Otsu's thresholding
ret2, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("/work/thresholded.png", th)
