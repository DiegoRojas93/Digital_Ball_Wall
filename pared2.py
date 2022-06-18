import cv2
import numpy as np

camara = cv2.VideoCapture(0)

def salto():

  redBajo1 = np.array([0, 100, 20],np.uint8)
  redAlto1 = np.array([8, 255, 255],np.uint8)

  redBajo2 = np.array([160, 100, 20],np.uint8)
  redAlto2 = np.array([179, 255, 255],np.uint8)

  while True:
    ret, frame = camara.read()
    if ret == True:
      frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      maskRed1 = cv2.inRange(frameHSV, redBajo1, redAlto1)
      maskRed2 = cv2.inRange(frameHSV, redBajo2, redAlto2)
      maskRed = cv2.add(maskRed1, maskRed2)

      contornos, hierachy = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

      for c in contornos:
        area = cv2.contourArea(c)
        if area > 600:
          M=cv2.moments(c)
          if (M["m00"] == 0): M["m00"] = 1
          x = int(M["m10"]/M["m00"])
          y = int(M['m01']/M['m00'])
          cv2.circle(frame, (x,y), 7, (0, 255, 0), -1)
          font = cv2.FONT_HERSHEY_SIMPLEX
          cv2.putText(frame, '{},{}'.format(x,y),(x+10,y), font, 0.75, (0,255,0), 1, cv2.LINE_AA)
          nuevoContorno = cv2.convexHull(c)
          cv2.drawContours(frame, [nuevoContorno], 0, (0,0,255), 3)

      # cv2.imshow("maskRedvis", maskRedvis)
      # cv2.imshow("maskRed", maskRed)
      cv2.imshow("frame", frame)
      if cv2.waitKey(30) & 0xFF == ord('q'):
        break
  camara.release()
  cv2.destroyAllWindows()