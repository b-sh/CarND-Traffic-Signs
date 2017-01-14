import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import pickle


#image = mpimg.imread("img_signs/keepright.png")
#image = mpimg.imread("images/20170113_161710.jpg")

img_original=[]
img_resized=[]

#path="img_signs"
path="img_signs/"

for image in os.listdir(path):
    image = mpimg.imread(path+image)
    img_original.append(image)

    resized = cv2.resize(image, (32,32), interpolation = cv2.INTER_LINEAR)
    print('This image is:', type(image), 'with dimesions:', image.shape)
    print('This image is:', type(resized), 'with dimesions:', resized.shape)

    img_resized.append(resized)

img_list={}
img_list['orig']=img_original
img_list['resized']=img_resized

for img in img_list['orig']:
    plt.imshow(img)
    plt.show()

for img in img_list['resized']:
    plt.imshow(img)
    plt.show()

dout = open('my_test.p', 'wb')

# Pickle images
pickle.dump(img_list, dout)

dout.close()