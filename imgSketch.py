
import cv2





# 1. Import the image.
image = cv2.imread("spiderman.png")
# 2. Add grey filter.
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 3. Add inverted filter.
invert = cv2.bitwise_not(grey_img)
# 4. Add Blur effect.
blur = cv2.GaussianBlur(invert, (21, 21), 0)

invertedblur = cv2.bitwise_not(blur)
# 5. Export the sketch image.
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

cv2.imwrite("sketch.png", sketch)

