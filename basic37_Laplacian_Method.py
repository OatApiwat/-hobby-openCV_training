#Laplacian_Method
import cv2 

img = cv2.imread("D:\Python_course\python-opencv\python-opencv\image\currency.jpg",0)
img = cv2.imread("D:\Project\camera\Picture_MA\image_001.jpg",0)
lap = cv2.Laplacian(img,-1)

cv2.imshow("Original",img)
cv2.imshow("Laplacian",lap)

cv2.waitKey(0)
cv2.destroyAllWindows()