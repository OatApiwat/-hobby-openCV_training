#เส้นเค้าโครง (Contour)
import cv2
import numpy as np
# img = cv2.imread("D:\Python_course\python-opencv\python-opencv\image\currency.jpg",0)
img = cv2.imread("D:\Python_course\python-opencv\python-opencv\image\currency.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gblur = cv2.GaussianBlur(gray,(3,3),0) #sigma


canny = cv2.Canny(gblur,50,200)

# สร้าง Kernel สำหรับ Morphological Operations
kernel = np.ones((5, 5), np.uint8)
kernel_2 = np.ones((3, 3), np.uint8)

# การขยายภาพ (Dilation)
dilation = cv2.dilate(canny, kernel_2, iterations=7)

# Opening (ลบจุดเล็กๆ)
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel_2, iterations=5)
# การกร่อนภาพ (Erosion)
erosion = cv2.erode(dilation, kernel_2, iterations=5)
# Closing (เติมเต็มช่องว่าง)
closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel_2, iterations=5)


# contours,hierarchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# cv2.drawContours(img,contours,-1,(255,0,0),1)
cv2.imshow("Output",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
