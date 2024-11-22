import cv2

#here with the help of videocapture function we easily ready any video.


def rescaleFrame(frame, scale= 0.75):
   width = int (frame.shape[1] * scale)
   height = int (frame.shape[0] * scale)
   dimensions = (width,height)
   return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

#reading video

cap = cv2.VideoCapture('video3.mp4')


while True:
    isTrue, frame =cap.read()
    frame_resized = rescaleFrame(frame)

    cv2.imshow('video', frame)
    cv2.imshow('video_resized',frame_resized)
    if cv2.waitKey(20) & 0xFF ==ord('d'):
     break
    cap.release()
    cv2.destroyAllWindows()

