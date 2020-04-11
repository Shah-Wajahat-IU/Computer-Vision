import  cv2
import numpy as np

def click_mouse_event(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y),3,(0,0,255) ,-1)
        point.append( (x,y) )
        if len(point)>=2:
            cv2.line(img,point[-1],point[-2], (255,255,0),5)
        cv2.imshow('image',img)

img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)
point=[]
cv2.setMouseCallback("image",click_mouse_event)
cv2.waitKey(0)
cv2.destroyAllWindows()





