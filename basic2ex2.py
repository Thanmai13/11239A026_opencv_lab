import cv2
path = input("Enter image path (jpg/png/bmp/tif): ")
img = cv2.imread(path)
if img is None:
    print("Error: Image not found!")
else:
    cv2.imshow("Image Display", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
