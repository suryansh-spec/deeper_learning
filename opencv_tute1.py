import cv2

"""""
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 200)

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(delay=1) & 0xff == ord("q"):
        break
"""""
img = cv2.imread("MSM2.png")
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey, (7,7),0)

cv2.imshow("grey image", img_grey)
cv2.imshow("blur image", img_blur)
cv2.waitKey(0)