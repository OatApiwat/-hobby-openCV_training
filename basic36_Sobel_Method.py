import cv2
import matplotlib.pyplot as plt

# โหลดภาพในโหมด grayscale
img = cv2.imread(r"D:\Python_course\python-opencv\python-opencv\image\currency.jpg", 0)

# Sobel Filter แนวแกน X
sobelX = cv2.Sobel(img, -1, 1, 0)
# Sobel Filter แนวแกน Y
sobelY = cv2.Sobel(img, -1, 0, 1)

# รวมผลลัพธ์จาก Sobel X และ Y
sobelXY = cv2.bitwise_or(sobelX, sobelY)

# แปลงผลลัพธ์จาก Sobel ให้อยู่ในช่วง 0-255 (ค่า abs เพื่อให้ค่าลบกลายเป็นบวก)
sobelX = cv2.convertScaleAbs(sobelX)
sobelY = cv2.convertScaleAbs(sobelY)
sobelXY = cv2.convertScaleAbs(sobelXY)

# จัดเตรียมชื่อและภาพสำหรับแสดง
images = [img, sobelX, sobelY, sobelXY]
titles = ["Original", "SobelX", "SobelY", "SobelXY"]

# แสดงผลภาพ
for i in range(len(images)):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
