import numpy as np
import random
import statistics as sat
import cv2
def sp_noise(image,prob):

    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def mfe(image):
    output = np.zeros(image.shape, np.uint8)
    image=np.pad(image, ((1, 1), (1, 1)), 'constant')
    # thres = 1 - prob
    for i in range(image.shape[0]-2):
        for j in range(image.shape[1]-2):
            output[i,j]=sat.median(
                    [image[i,j],image[i,j+1],image[i,j+2],
                     image[i+1, j], image[i+1,j+1], image[i+1, j+2],
                     image[i+2, j], image[i+2,j+1], image[i+2, j+2],
                    ]
                )
    return output
def dat_file(image,filename):
    pass
    fp = open(filename, "w")
    for j in range(image.shape[1]):
        for i in range(image.shape[0]):
            pass
            fp.write(str(format(image[i,j],"x")))
            fp.write("\n")
image = cv2.imread('image.jpg',0) # Only for grayscale image
image = cv2.resize(image, (128, 128), interpolation=cv2.INTER_AREA)
noise_img = sp_noise(image,0.02)
cv2.imwrite('sp_noise.jpg', noise_img,)
dat_file(noise_img,filename="img.dat")
mfe_image=mfe(noise_img)
cv2.imwrite('sp_mfe.jpg', mfe_image)
dat_file(mfe_image,filename="golden.dat")
