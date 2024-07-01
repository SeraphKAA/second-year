from PIL import Image, ImageFilter, ImageFont, ImageDraw
import cv2
import numpy as np



filename1 = 'C:\\Users\\79045\\Desktop\\бессоные ночи\\сделанное дз\\2 курс 3 сем\\ОП\\5 лаба\\top.jpg'
filename2 = 'C:\\Users\\79045\\Desktop\\photo\\raiden.jpg'
loc = 'raiden.jpg'
# [+] pillow
class pil:
    def __init__(self, filename) -> None:
        self.filename = filename
    
    def zad_1(self):
        image = Image.open(self.filename)
        image = image.crop((50, 50, 554, 416))
        return image

    def zad_2(self, image):
        f = ImageFont.truetype("arial.ttf", 60)
        t = ImageDraw.Draw(image)
        t.text((60, 10), 'поставьте 100', font = f)
        t.ellipse((100, 100, 150, 200), fill='red', outline=(0, 0, 0))
        return image
    
    def zad_3(self, image):
        rg = image.crop((100, 100, 400, 400)).filter(ImageFilter.BLUR)
        image.paste(rg, (100, 100))
        return image

    def zad_4(self, image):
        image.save('123.jpg')


def pill():
    A = pil(filename1)
    f1 = A.zad_1()
    f1.show()
    
    f2 = A.zad_2(f1)
    f2.show()
    
    f3 = A.zad_3(f2)
    f3.show()
    
    f4 = A.zad_4(f3)


# [+] cvv

def cvv():
    # [+] Задание 1

    image = cv2.imread(filename2)       # 828, 1021
    image = image[0:1000, 0:800]
    
    cv2.imshow('Raiden', image)
    cv2.waitKey(0)
    cv2.imwrite('raiden2.jpg', image)

    # # [+] Задание 2

    # output = image.copy()
    cv2.putText(image, 'raiden gg', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 0), 10)        #текст
    cv2.rectangle(image, (0, 0), (827, 1000), (0, 0, 255), 2)      #прямоугольник
    
    cv2.imshow('Raiden', image)
    cv2.waitKey(0)
    cv2.imwrite('raiden2.jpg', image)
    
    # [+] Задание 3
    
    cropped = image[200:500, 200:500]
    cropped = cv2.GaussianBlur(cropped, (51, 51), 0)

    crop = cropped.copy()
    image1 = image.copy()


    roi = image1[200:500, 200:500]

    img2gray = cv2.cvtColor(crop,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    img2_fg = cv2.bitwise_and(crop, crop, mask = mask)

    dst = cv2.add(img1_bg,img2_fg)
    image1[200:500, 200:500] = dst

    # [+] Задание 4

    cv2.imshow('Raiden', image1)
    cv2.waitKey(0)
    cv2.imwrite('raiden2.jpg', image1)



if __name__ == '__main__':
    # pill()        #+
    cvv()         #+
