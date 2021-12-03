import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import time

start_time = time.time()
print("start")

img_rgb = cv.imread('smash2.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('pepper.png', 0)

w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF)
threshold = 0.5
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv.imwrite('res.png',img_rgb)

print("--- %s seconds ---" % (time.time() - start_time))