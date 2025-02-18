#การใช้งาน Adaptive_Threshold
import cv2 
img = cv2.imread("image/ant.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh,th1 = cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
th3 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)
cv2.imshow("Origine",gray)
cv2.imshow("THRESH",th1)
cv2.imshow("MEAN",th2)
cv2.imshow("GAUSSIAN",th3)

cv2.waitKey(0)
cv2.destroyAllWindows()