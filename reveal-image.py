import numpy as np
import cv2

img = cv2.imread('./result.jpeg')
upperImg = img.copy()
hiddenImg = img.copy()

def formatBinary(number):
    str = "{0:b}".format(number)
    while len(str) < 8:
        str = "0" + str
    return str

def main():
    for i in range(len(img)):
        for j in range(len(img[i])):
            for k in range(3):
                binary =  formatBinary(img[i][j][k])
                upperImg[i][j][k] = int(binary[0:4] + "0000", 2)
                hiddenImg[i][j][k] = int(binary[4:8] + "0000", 2)
    cv2.imwrite('./front.jpeg', upperImg)
    cv2.imwrite('./hidden.jpeg', hiddenImg)

main()
