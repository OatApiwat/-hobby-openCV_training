#เส้นเค้าโครง (Contour)
import cv2 

img = cv2.imread("D:\Python_course\python-opencv\python-opencv\image\currency.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# thresh,result = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
canny = cv2.Canny(img,50,200)
contours,hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(255,0,0),1)
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
