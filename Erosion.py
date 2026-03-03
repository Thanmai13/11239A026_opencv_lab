import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg", 0)

# Resize image to passport size (small)
img_small = cv2.resize(img, (200, 250), interpolation=cv2.INTER_AREA)

# Create kernel and apply erosion
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img_small, kernel, iterations=1)

# Create small fixed windows
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Erosion", cv2.WINDOW_NORMAL)

# Force window size (small like passport)
cv2.resizeWindow("Original", 200, 250)
cv2.resizeWindow("Erosion", 200, 250)

# Move windows (prevents fullscreen auto behavior)
cv2.moveWindow("Original", 100, 100)
cv2.moveWindow("Erosion", 350, 100)

# Show images
cv2.imshow("Original", img_small)
cv2.imshow("Erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
