# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cv2.namedWindow("Preview", cv2.WND_PROP_AUTOSIZE)
#cv2.setWindowProperty('test', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("Preview", cv2.flip(frame, 1))
    if not ret:
        break
    k = cv2.waitKey(1)

    if k == 27:      # ESC pressed
        print("ESC pressed, Closing...")
        break
    elif k == 32:    # SPACE pressed
        img_name = "camCalib_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()