import cv2
from decouple import config

username = config('CAMERA_USERNAME')
password = config('CAMERA_PASSWORD')
hostname = config('CAMERA_HOSTNAME')

url = 'rtsp://' + username + ':' + password + '@' + hostname + '/cam/realmonitor?channel=1&subtype=0'

print(url)

vcap = cv2.VideoCapture(url)

cascadePath = "haarcascades/haarcascade_fullbody.xml"

haarCascade = cv2.CascadeClassifier(cascadePath)

while True:

    ret, frame = vcap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = haarCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=15,
        minSize=(30, 60)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('VIDEO', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
