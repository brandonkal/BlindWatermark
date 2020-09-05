import numpy as np
import cv2

img = cv2.imread("out_wm.png", 0)

# Otsu's thresholding
ret2, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("thresholded.png", th)
