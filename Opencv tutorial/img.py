# https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn 7:50

import cv2

#1: img laden in 1: greyscale, 2: normale kleur, 3: ignore transparency
#2: -1 cv2.IMREAD_COLOR,
#3: 0 cv2.IMREAD_GRAYSCALE
#4: 1 cv2.IMREAD_UNCHANGED
img = cv2.imread('assets/ajax.svg', 0)