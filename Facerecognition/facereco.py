import cv2
img = cv2.imread("group.jpg")

max_width = 800
if img.shape[1] > max_width:
    scale = max_width / img.shape[1]
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,   
    minNeighbors=3,       
    minSize=(30, 30)      
)

count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    count += 1
cv2.putText(img, f"Faces Detected: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

cv2.imwrite("group_faces_detected.jpg", img)
cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()