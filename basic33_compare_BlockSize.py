import cv2 
import matplotlib.pyplot as plt

# อ่านภาพ
image_path = r"image\ant.jpg"
img = cv2.imread(image_path, 0)

# กำหนดขนาด Block
size = [3, 5, 9, 17,1023]

# แสดงภาพต้นฉบับ
plt.figure(figsize=(10, 6))
plt.subplot(321)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.xticks([]), plt.yticks([])

# แสดงผลลัพธ์ด้วยค่า BlockSize ต่าง ๆ
for i in range(len(size)):
    result = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, size[i], 1
    )
    plt.subplot(322 + i)
    plt.title(f"BlockSize: {size[i]}")
    plt.imshow(result, cmap="gray")
    plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
