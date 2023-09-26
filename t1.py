import cv2

name = input("Enter your name: ")
output_path = f'C:\pycharm\CMRS\database/{name}.jpg'

cam = cv2.VideoCapture(0)
cv2.namedWindow("Take a Picture")
c = 0

while True:
    ret, frame = cam.read()

    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("Take a Picture", frame)
    k = cv2.waitKey(1)

    if k == 27:
        print("BISH")
        break
    elif k == 32:
        cv2.imwrite(output_path, frame)
        print(f"SAY GAYYY{output_path}")
        # c+=1

cam.release()
cv2.destroyAllWindows()
