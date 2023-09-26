import cv2

name = input("Enter your name: ")
output_path = f'C:\pycharm\CMRS\database'

cam = cv2.VideoCapture(0)
cv2.namedWindow("Take a Picture")
c=0

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
        c+=1
        temp_output_path = f'{output_path}/{name}_{c}.jpg'
        cv2.imwrite(temp_output_path, frame)
        print(f"Image {c} saved as {temp_output_path}")

cam.release()
cv2.destroyAllWindows()
