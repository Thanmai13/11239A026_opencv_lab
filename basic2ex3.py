import cv2
input_path = input("Enter input image path: ")
img = cv2.imread(input_path)
if img is None:
    print("Error: Image not found!")
else:
    cv2.imwrite("output.jpg", img)
    cv2.imwrite("output.png", img)
    cv2.imwrite("output.bmp", img)
    cv2.imwrite("output.tif", img)
    print("Image converted and saved as:")
    print("output.jpg, output.png, output.bmp, output.tif")
