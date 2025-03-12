import cv2
import os

# โหลดภาพ
image_path = r"image\gradient.png"
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    print(f"ไม่พบไฟล์ภาพที่: {image_path}")
    exit()

# ฟังก์ชันสำหรับอัปเดตค่าจาก Trackbar
def update_threshold(x):
    thresh_value = cv2.getTrackbarPos('Threshold', 'Threshold Adjuster')
    
    # การใช้ Threshold ในแต่ละโหมด
    _, th1 = cv2.threshold(gray_img, thresh_value, 255, cv2.THRESH_BINARY)
    _, th2 = cv2.threshold(gray_img, thresh_value, 255, cv2.THRESH_BINARY_INV)
    _, th3 = cv2.threshold(gray_img, thresh_value, 255, cv2.THRESH_TRUNC)
    _, th4 = cv2.threshold(gray_img, thresh_value, 255, cv2.THRESH_TOZERO)
    _, th5 = cv2.threshold(gray_img, thresh_value, 255, cv2.THRESH_TOZERO_INV)
    
    # แสดงภาพในแต่ละโหมด
    cv2.imshow("BINARY", th1)
    cv2.imshow("BINARY_INV", th2)
    cv2.imshow("TRUNC", th3)
    cv2.imshow("TOZERO", th4)
    cv2.imshow("TOZERO_INV", th5)

# สร้างหน้าต่างหลักสำหรับแสดงภาพ
cv2.namedWindow('Threshold Adjuster')

# สร้าง Trackbar เพื่อปรับค่า Threshold
cv2.createTrackbar('Threshold', 'Threshold Adjuster', 128, 255, update_threshold)

# แสดงภาพต้นฉบับ
cv2.imshow('Original', gray_img)

# เรียกใช้ฟังก์ชันเพื่ออัปเดต Threshold ครั้งแรก
update_threshold(128)

# รอให้กดปุ่ม 'q' เพื่อปิดโปรแกรม
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
