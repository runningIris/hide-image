import numpy as np
import cv2

img = cv2.imread('./original.jpeg')
img_to_hide = cv2.imread('./to_hide.jpeg')

def formatBinary(number):
    str = "{0:b}".format(number)
    while len(str) < 8:
        str = "0" + str
    return str

def main():
    for i in range(len(img_to_hide)):
        for j in range(len(img_to_hide[i])):
            originPixel = img[i][j]
            toHidePixel =  img_to_hide[i][j]

            for k in range(3):
                highData = formatBinary(originPixel[k])[0:4]
                lowData = formatBinary(toHidePixel[k])[0:4]            
                img[i][j][k] = int(highData + lowData, 2)

    cv2.imwrite('./result.jpeg', img)

main()
