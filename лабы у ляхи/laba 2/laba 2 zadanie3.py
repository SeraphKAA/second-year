# from PIL import Image

# def grayscale(image_path, new_image_path):
#     """Convert an image to grayscale"""
#     image = Image.open(image_path)
#     grayscale_image = Image.new('L', image.size)
#     width, height = image.size

#     for x in range(width):
#         for y in range(height):
#             # Get pixels and convert to grayscale
#             pixel = image.getpixel((x,y))
#             gray = int((pixel[0] + pixel[1] + pixel[2]) / 3)
#             grayscale_image.putpixel((x,y), gray)

#     grayscale_image.save(new_image_path)

import struct

# Открываем BMP файл для чтения
with open('photo\\RGB.bmp', 'rb') as f:
    # Считываем BMP заголовок из файла
    file_header = f.read(14)
    image_header = f.read(40)

    # Получаем ширину и высоту изображения
    width = struct.unpack('<i', image_header[4:8])[0]
    height = struct.unpack('<i', image_header[8:12])[0]

    # Получаем количество бит на пиксель и количество байт на строку
    bits_per_pixel = struct.unpack('<h', image_header[14:16])[0]
    bytes_per_row = ((bits_per_pixel * width + 31) // 32) * 4

    # Создаем новый BMP файл для записи grayscale изображения
    with open('grayscale.bmp', 'wb') as f_gray:
        # Записываем BMP заголовок в новый файл
        f_gray.write(file_header)
        f_gray.write(image_header)

        # Обрабатываем каждую строку изображения
        for y in range(height):
            # Обрабатываем каждый пиксель в строке
            for x in range(width):
                # Считываем значение пикселя
                pixel_offset = file_header[10] + image_header[0x0A]
                pixel_offset += y * bytes_per_row + x * bits_per_pixel // 8
                f.seek(pixel_offset)
                pixel_data = f.read(bits_per_pixel // 8)

                # Вычисляем яркость пикселя
                if bits_per_pixel == 24:
                    blue, green, red = struct.unpack('<BBB', pixel_data)
                    brightness = int(0.2126 * red + 0.7152 * green + 0.0722 * blue)
                    pixel_data = struct.pack('<BBB', brightness, brightness, brightness)

                # Записываем значение пикселя в новый файл
                f_gray.write(pixel_data)

bit_values = [250,230,180,130,150,100,50,10]


# Открываем исходное изображение
with open("grayscale.bmp", "rb") as img_file:
    # Считываем BMP-заголовок и данные о пикселях
    header = img_file.read(54)
    pixel_data = img_file.read()

    # Обрабатываем каждый битовый срез
    for bit_value in bit_values:
        # Применяем битовый срез к каждому пикселю
        pixel_data = bytes([p & bit_value for p in pixel_data])

        # Создаем новый BMP-файл и записываем в него заголовок и данные о пикселях
        with open(str(bit_value) + "bitslice.bmp", "wb") as out_file:
            out_file.write(header)
            out_file.write(pixel_data)







# # Открываем BMP-файл для чтения
# with open('photo\\RGB.bmp', 'rb') as f:
#     # Читаем заголовок BMP-файла
#     bmp_header = f.read(54)
#     # Распаковываем данные заголовка в кортеж
#     width = int.from_bytes(bmp_header[18:22], byteorder='little')
#     height = int.from_bytes(bmp_header[22:26], byteorder='little')
#     bits_per_pixel = int.from_bytes(bmp_header[28:30], byteorder='little')

#     print(width, height)
#     # Вычисляем размер одного байта в битах
#     bits_per_byte = 8
#     # Вычисляем количество байт, необходимых для хранения одного битового среза
#     bytes_per_slice = (width * bits_per_pixel + bits_per_byte - 1) // bits_per_byte

#     # Читаем оставшуюся часть BMP-файла (пиксели)
#     pixel_data = f.read()


# for i in range(8):
#     print(i)
#     # Создаем новый файл BMP с соответствующим именем
#     with open(f'image_bit{i}.bmp', 'wb') as f:
#         # Записываем заголовок BMP-файла
#         f.write(bmp_header)
#         # Записываем битовый срез
#         for j in range(height):
#             start = j * bytes_per_slice
#             end = start + bytes_per_slice
#             slice_data = pixel_data[start:end]
#             # Выполняем маску для выделения только нужного бита
#             mask = (1 << i)
#             slice_data = bytes((byte & mask) for byte in slice_data)
#             f.write(slice_data)


# # for i in range(8):
# #     grayscale(f"image_bit{i}.bmp", f"image_bit{i}.bmp")
