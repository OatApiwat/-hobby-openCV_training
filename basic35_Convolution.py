#ตัวกรอง Convolution ด้วย Filter2D
import cv2
import numpy as np
import matplotlib.pyplot as plt

# โหลดภาพในโหมด grayscale (0)
img = cv2.imread(r"image\noise.png")

#filter
filter2d = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

#blur
mean = cv2.blur(img,(13,13))

#median
mblur=cv2.medianBlur(img,13)

# GaussianBlur is popular
gblur = cv2.GaussianBlur(img,(7,7),0) #sigma

titles = ["ORIGINAL","FILTER2D","MEAN","MEDIAN BLUR","GAUSSIAN BLUR"]
images = [img,filter2d,mean,mblur,gblur]

for  i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
