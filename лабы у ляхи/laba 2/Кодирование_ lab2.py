
import numpy as np
import struct

#Задание 1
with open('photo\\RGB.bmp', "rb") as f:
    file_data = f.read()
header_data = struct.unpack('<2sIHHIIIIHHIIIIII', file_data[:54])
print(header_data)
str1 = str(header_data)
print(str1)

bmp = open('photo\\RGB.bmp', 'rb')
print('Type:', bmp.read(2).decode())
print('Size: %s' % struct.unpack('I', bmp.read(4)))
print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
print('Offset: %s' % struct.unpack('I', bmp.read(4)))
print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
print('Width: %s' % struct.unpack('I', bmp.read(4)))
print('Height: %s' % struct.unpack('I', bmp.read(4)))
print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))



# #________________________________________________________________________________




#Задание 2

with open('photo\\RGB.bmp', 'rb') as f:
    # Считываем заголовок BMP-файла
    bmp_header = f.read(54)
    width = int.from_bytes(bmp_header[18:22], byteorder='little')
    height = int.from_bytes(bmp_header[22:26], byteorder='little')
    bit_depth = int.from_bytes(bmp_header[28:30], byteorder='little')
    # Определяем размер пикселя в байтах
    pixel_size = bit_depth // 8

    # Считываем данные изображения
    data = f.read()

    # Разбиваем данные на три цветовых канала
    red_channel = []
    green_channel = []
    blue_channel = []
    for i in range(height):
        row_r = []
        row_g = []
        row_b = []
        for j in range(width):
            offset = i * width * pixel_size + j * pixel_size
            b = data[offset]
            g = data[offset + 1]
            r = data[offset + 2]
            row_r.append(r)
            row_g.append(g)
            row_b.append(b)
        red_channel.append(row_r)
        green_channel.append(row_g)
        blue_channel.append(row_b)

    # Сохраняем каждый канал в отдельный BMP-файл
    with open('red_channel.bmp', 'wb') as f_red:
        f_red.write(bmp_header)
        for row in red_channel:
            for pixel in row:
                f_red.write(bytes([0, 0, pixel]))


    with open('green_channel.bmp', 'wb') as f_green:
        f_green.write(bmp_header)
        for row in green_channel:
            for pixel in row:
                f_green.write(bytes([0, pixel, 0]))


    with open('blue_channel.bmp', 'wb') as f_blue:
        f_blue.write(bmp_header)
        for row in blue_channel:
            for pixel in row:
                f_blue.write(bytes([pixel, 0, 0]))


#_____________________________________________

# img = cv2.imread('photo\\rgb_kvadrat.bmp', cv2.IMREAD_GRAYSCALE)

#  img = cv2.imread('photo\\rgb_kvadrat.bmp', 0)
# out = []
# for k in range(8):
#     plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
#     res = cv2.bitwise_and(plane, img)
#     x = res * 255
#     cv2.imwrite(f'1slice_{k}.bmp', x)
#     cv2.imshow(f'1slice_{k}.bmp', x)
#     cv2.waitKey(0)


# img = cv2.imread('photo\\gta sa.bmp', 0)
# out = []
# for k in range(8):
#     plane = np.full((img.shape[0], img.shape[1]), 2 ** k, np.uint8)
#     res = cv2.bitwise_and(plane, img)
#     x = res * 255
#     cv2.imwrite(f'slice_{k}.bmp', x)
#     cv2.imshow(f'slice_{k}.bmp', x)
#     cv2.waitKey(0)