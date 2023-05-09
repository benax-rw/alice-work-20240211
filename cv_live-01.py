import cv2

live_stream = cv2.VideoCapture(0)

while True:
    ret, frame = live_stream.read()
    edges = cv2.Canny(frame, 100, 200)
    cv2.imshow('Live Video Stream', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

live_stream.release()
cv2.destroyAllWindows()
