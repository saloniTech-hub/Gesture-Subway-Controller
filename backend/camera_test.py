import cv2

print("Starting camera test...")

cap = cv2.VideoCapture(0)

print("Camera opened:", cap.isOpened())

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to read frame")
        break

    cv2.imshow("Camera Test", frame)

    key = cv2.waitKey(1)

    if key == 27:
        print("ESC pressed")
        break

cap.release()
cv2.destroyAllWindows()

print("Program ended")