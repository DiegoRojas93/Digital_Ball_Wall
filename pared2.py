import cv2
import numpy as np

camara = cv2.VideoCapture(0)

def salto():

  redBajo1 = np.array([0, 100, 20],np.uint8)
  redAlto1 = np.array([8, 255, 255],np.uint8)

  redBajo2 = np.array([175, 100, 20],np.uint8)
  redAlto2 = np.array([179, 255, 255],np.uint8)

  while True:
    ret, frame = camara.read()
    if ret == True:
      frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
      maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
      maskRed = cv2.add(maskRed1, maskRed2)

      maskRedvis = cv2.bitwise_and(frame, frame, mask = maskRed)

      cv2.imshow("maskRedvis", maskRedvis)
      cv2.imshow("maskRed", maskRed)
      cv2.imshow("frame", frame)
      if cv2.waitKey(30) & 0xFF == ord('q'):
        break
  camara.release()
  cv2.destroyAllWindows()