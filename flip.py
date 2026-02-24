import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

# Create flipped versions
flip_vertical = cv2.flip(img, 0)
flip_horizontal = cv2.flip(img, 1)
flip_both = cv2.flip(img, -1)

# Combine images
top_row = cv2.hconcat([img, flip_vertical])
bottom_row = cv2.hconcat([flip_horizontal, flip_both])
combined = cv2.vconcat([top_row, bottom_row])

# Show in one window
cv2.imshow("All Flips", combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
