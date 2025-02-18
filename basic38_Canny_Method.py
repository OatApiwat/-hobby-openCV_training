#Canny Method ใช้กับภาพที่มีสัญญาณรบกวนน้อย
import cv2 

img = cv2.imread("D:\Python_course\python-opencv\python-opencv\image\currency.jpg",0)
img = cv2.imread("D:\Project\camera\Picture_MA\image_001.jpg",0)

canny = cv2.Canny(img,50,200)

cv2.imshow("Original",img)
cv2.imshow("Canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()