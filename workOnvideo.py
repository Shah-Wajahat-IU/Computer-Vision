import cv2

cap =cv2.VideoCapture(0,cv2.CAP_DSHOW);
fourcc=cv2.VideoWriter_fourcc(*'XVID')

out=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

while(True):
    ret,frame =cap.read()
    if ret == True:
        out.write(frame)

        width=cap.get(cv2.CAP_PROP_FRAME_WIDTH) # get video frame width
        height =cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # get video frame height

        print(width)
        print(height)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # get video color to grayscale
        cv2.imshow("Frame",gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()