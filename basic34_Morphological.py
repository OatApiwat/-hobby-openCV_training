import cv2
import matplotlib.pyplot as plt
import numpy as np

# โหลดภาพในโหมด grayscale (0)
img = cv2.imread(r"D:\Python_course\python-opencv\python-opencv\image\noise.png", 0)

# Thresholding
thresh, result = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)

# สร้าง Kernel สำหรับ Morphological Operations
kernel = np.ones((2, 2), np.uint8)

# การขยายภาพ (Dilation)
dilation = cv2.dilate(result, kernel, iterations=5)

# Opening (ลบจุดเล็กๆ)
opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel, iterations=7)

# Closing (เติมเต็มช่องว่าง)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=5)

# การกร่อนภาพ (Erosion)
erosion = cv2.erode(closing, kernel, iterations=7)

# กำหนดชื่อของภาพที่จะแสดง
titles = ["ORIGINAL", "THRESH", "DILATION", "EROSION", "OPENING", "CLOSING"]
images = [img, result, dilation, erosion, opening, closing]

# แสดงผลภาพทั้งหมด
for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap="gray")  # ใช้ cmap="gray" สำหรับภาพ grayscale
    plt.title(titles[i])
    plt.xticks([])  # ลบขีด x-axis
    plt.yticks([])  # ลบขีด y-axis

# แสดงภาพทั้งหมด
plt.show()
