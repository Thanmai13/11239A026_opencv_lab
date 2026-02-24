import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gaussian blur before edge detection
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny Edge Detection
edges = cv2.Canny(blur, 50, 150)

cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges (Canny)", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
