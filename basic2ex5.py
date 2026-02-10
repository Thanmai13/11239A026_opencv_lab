import cv2
path = input("Enter image path: ")
img = cv2.imread(path)
if img is None:
    print("Error: Image not found!")
else:
    print("Image shape (Height, Width, Channels):", img.shape)
    x = int(input("Enter x starting point:"))
    y = int(input("Enter y starting point:"))
    w = int(input("Enter width: "))
    h = int(input("Enter height: "))
    cropped = img[y:y+h, x:x+w]
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped Image", cropped)
    cv2.imwrite("cropped_output.jpg", cropped)
    print("cropped image saved as cropped_output.jpg")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
