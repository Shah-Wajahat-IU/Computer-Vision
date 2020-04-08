import cv2

img = cv2.imread('image.jpg') #for Defult image(RGB)
#img = cv2.imread('image.jpg',0) for gray image
#img = cv2.imread('image.jpg',1) For RGB image
print(img)

cv2.imshow("Image Display",img)

k=cv2.waitKey(0)
if k ==27:
    cv2.destroyAllWindows()
elif k == ord("s"):
    cv2.imwrite("images.png",img)
    cv2.destroyAllWindows()