import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg", 0)

# Resize image to 200x250
img_small = cv2.resize(img, (200, 250), interpolation=cv2.INTER_AREA)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Apply dilation
dilation = cv2.dilate(img_small, kernel, iterations=1)

# Create resizable windows BEFORE imshow
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dilation", cv2.WINDOW_NORMAL)

# Force window size
cv2.resizeWindow("Original", 200, 250)
cv2.resizeWindow("Dilation", 200, 250)

# Move windows (optional)
cv2.moveWindow("Original", 100, 100)
cv2.moveWindow("Dilation", 350, 100)

# Show images
cv2.imshow("Original", img_small)
cv2.imshow("Dilation", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
