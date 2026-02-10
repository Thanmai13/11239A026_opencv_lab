import cv2
import numpy as np
# Create a blank white image
img = np.ones((600, 800, 3), dtype=np.uint8) * 255
# Draw a line
cv2.line(img, (50, 50), (300, 50), (0, 0, 255), 3)
# Draw a rectangle
cv2.rectangle(img, (50, 100), (300, 250), (255, 0, 0), 3)
# Draw a filled rectangle
cv2.rectangle(img, (350, 100), (550, 250), (0, 255, 0), -1)
# Draw a circle
cv2.circle(img, (150, 400), 80, (0, 0, 0), 3)
# Draw a filled circle
cv2.circle(img, (450, 400), 80, (255, 0, 255), -1)
# Draw an ellipse
cv2.ellipse(img, (650, 400), (100, 50), 0, 0, 360, (0, 128, 255), 3)
# Draw a polygon (triangle)
pts = np.array([[650, 100], [600, 250], [700, 250]], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 0), 3)
# Add text
cv2.putText(img, "OpenCV Shapes", (250, 550),
cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 3)
cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
