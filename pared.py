import cv2

fuerza = 20

def salto():
    camara = cv2.VideoCapture(0)
    while True:
        ret, frame = camara.read()
        cv2.imshow("frame", frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    camara.release()
    cv2.destroyAllWindows()