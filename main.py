import numpy as np

import cv2


image = cv2.imread('abc.jpg')

grey_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('grey_img.png',grey_img )

invert = cv2.bitwise_not(grey_img)
cv2.imwrite('invert.png',invert )

blur = cv2.GaussianBlur(invert, (21,21),0)
cv2.imwrite('blur.png',blur )

inveredblur = cv2.bitwise_not(blur)
cv2.imwrite('inveredblur.png',inveredblur )

sketch = cv2.divide(grey_img, inveredblur, scale=256.0)

cv2.imwrite('sketch.png', sketch)





