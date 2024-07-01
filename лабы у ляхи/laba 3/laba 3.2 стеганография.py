def close(): 
    with open('photo\\gta sa.bmp', 'rb') as i, open("restored_secret.bmp", 'wb') as ou: ou.write(i.read())

def encode():
    # открываем исходное изображение
    container_image = open("photo\\black.bmp", "rb")
    container_image_byte_array = bytearray(container_image.read())
    container_image.close()

    # открываем секретное изображение
    secret_image = open("photo\\gta sa.bmp", "rb")
    

    header = secret_image.read(54)
    
    secret_image_byte_array = bytearray(secret_image.read())
    secret_image.close()

    # выбираем место для встраивания (отступ)
    word_offset = 10  # BMP-файл начинается с двух двухбайтовых слов
    pixel_offset = 54  # в BMP-файле цветовая палитра и дополнительная информация идут первыми 54 байта
    offset = word_offset + pixel_offset

    # вычисляем длину секретного изображения
    secret_image_size = len(secret_image_byte_array)

    # стеганографический алгоритм
    for i in range(secret_image_size):
        if (i + offset) + 2 < len(container_image_byte_array):
            container_image_byte_array[i + offset] = ((container_image_byte_array[i + offset] & 0xFE) | (secret_image_byte_array[i] >> 7))
            container_image_byte_array[(i + offset) + 1] = ((container_image_byte_array[(i + offset) + 1] & 0xFE) | ((secret_image_byte_array[i] >> 6) & 0x01))
            container_image_byte_array[(i + offset) + 2] = ((container_image_byte_array[(i + offset) + 2] & 0xFE) | ((secret_image_byte_array[i] >> 5) & 0x01))
        else:
            print(f"Unable to hide byte {i} (out of range).")
            break

    # сохраняем измененный контейнер в новый файл
    with open("result.bmp", "wb") as f:
        f.write(container_image_byte_array)



def decode():
    # открываем полученный стегоизображение (контейнер)
    container_image = open("result.bmp", "rb")
    container_image_byte_array = bytearray(container_image.read())
    container_image.close()

    # выбираем место для извлечения (отступ)
    word_offset = 10  # BMP-файл начинается с двух двухбайтовых слов
    pixel_offset = 54  # в BMP-файле цветовая палитра и дополнительная информация идут первыми 54 байта
    offset = word_offset + pixel_offset

    # вычисляем длину секретного изображения
    secret_image_size = 0
    for i in range(32):
        secret_image_size |= (container_image_byte_array[word_offset + i] & 0x01) << i

    # извлекаем секретное изображение
    secret_image_byte_array = bytearray()
    for i in range(secret_image_size):
        if (i*3 + offset + 2) < len(container_image_byte_array):
            byte = ((container_image_byte_array[i*3 + offset] & 0x01) << 7) \
                    | ((container_image_byte_array[i*3 + offset + 1] & 0x01) << 6) \
                    | ((container_image_byte_array[i*3 + offset + 2] & 0x01) << 5)
            secret_image_byte_array.append(byte)
        else:
            print(f"Unable to extract byte {i} (out of range).")
            break

    # сохраняем извлеченное секретное изображение в новый файл
    with open("extracted_secret.bmp", "wb") as f:
        f.write(secret_image_byte_array)

    # открываем получившийся файл
    extracted_image = open("extracted_secret.bmp", "rb")
    extracted_image_byte_array = bytearray(extracted_image.read())
    extracted_image.close()

    # сохраняем извлеченное изображение в новом файле
    with open("restored_secret.bmp", "wb") as f, open('photo\\gta sa.bmp', 'rb') as rise:
        f.write(rise.read(54))
        f.write(extracted_image_byte_array)
        

def decode1():
    
    # открываем измененный контейнер с секретным изображением
    container_image = open("result.bmp", "rb")
    container_image_byte_array = bytearray(container_image.read())
    container_image.close()

    # выбираем место, где находится секретное изображение (отступ)
    word_offset = 10  # BMP-файл начинается с двух двухбайтовых слов
    pixel_offset = 54  # в BMP-файле цветовая палитра и дополнительная информация идут первыми 54 байта
    offset = word_offset + pixel_offset
    # выбираем место, где находится секретное изображение (отступ)
    # offset = container_image_byte_array[10] + (container_image_byte_array[11] << 8)

    # вычисляем длину секретного изображения
    secret_image_size = int.from_bytes(container_image_byte_array[34:38], "little")

    # извлекаем секретное изображение
    secret_image_byte_array = bytearray()
    for i in range(secret_image_size):
        if (i + offset + 2) * 3 < len(container_image_byte_array):
            secret_image_byte_array.append((container_image_byte_array[(i + offset + 2) * 3] & 0x07) << 5 | (container_image_byte_array[(i + offset + 2) * 3 + 1] & 0x07) << 2 | (container_image_byte_array[(i + offset + 2) * 3 + 2] & 0x03))
        else:
            print(f"Unable to extract byte {i} (out of range).")
            break
    # сохраняем извлеченное изображение в новый файл
    with open("secret.txt", "wb") as f:
        f.write(secret_image_byte_array)
        
        # print(secret_image_byte_array[:50])

    


def decode2():
    pass


# encode()
decode()















# import base64, os


# def encode_image(input_img_name, output_img_name, spy_file, degree=4):
#     with open(spy_file, 'r') as spy, open(input_img_name, 'rb') as input_image, \
#             open(output_img_name, 'wb') as output_image:
#         bmp_header = input_image.read(54)
#         output_image.write(bmp_header)
#         spy_mask, img_mask = masks(degree)
#         while True:
#             symbol = spy.read(1)
#             if not symbol:
#                 break
#             symbol = ord(symbol)
#             for byte_amount in range(0, 8, degree):
#                 img_byte = int.from_bytes(input_image.read(1), byteorder='little') & img_mask
#                 bits = symbol & spy_mask
#                 bits >>= (8 - degree)
#                 img_byte |= bits
#                 output_image.write(img_byte.to_bytes(1, byteorder='little'))
#                 symbol <<= degree
#         output_image.write(input_image.read())
#     return True

# def decode_image(encoded_img, output_spy, pixels_to_read, degree=4):
#     with open(output_spy, 'w', encoding='utf-8') as spy, open(encoded_img, 'rb') as encoded_bmp:
#         encoded_bmp.seek(54)
#         _, img_mask = masks(degree)
#         img_mask = ~img_mask
#         read = 0
#         while read < pixels_to_read:
#             symbol = 0
#             for bits_read in range(0, 8, degree):
#                 img_byte = int.from_bytes(encoded_bmp.read(1), byteorder='little') & img_mask
#                 symbol <<= degree
#                 symbol |= img_byte
#             if chr(symbol) == '\n' and len(os.linesep) == 2:
#                 read += 1
#             read += 1
#             spy.write(chr(symbol))
#     return True

# def masks(degree):
#     spy_mask = 0xFF
#     img_mask = 0xFF
#     spy_mask <<= (8 - degree)
#     spy_mask %= 256
#     img_mask >>= degree
#     img_mask <<= degree
#     return spy_mask, img_mask

# encrypted = "encrypted.bmp"

close()


# while True:
#     print("||||STEGANOGRAPHY||||")
#     print("1. Зашифровать\n2. Получить зашифрованную картинку")
#     print("--------------------")
#     choose = int(input("Выберите опцию: "))
#     if choose == 1:
#         with open(input("введите имя картинки для шифрования: "), "rb") as f, open("spy.txt", "w") as f2:
#             to_encode_head = str(base64.b64encode(f.read(54)))[2:]
#             to_encode_bmp = str(base64.b64encode(f.read()))[2:]
#             f2.write(to_encode_head + to_encode_bmp)
#         encode_image('photo\\black.bmp', encrypted, "spy.txt")
#     elif choose == 2:
#         decode_image((input("введите имя файла для поиска зашифрованной картинки: ")), "ss.txt", os.stat("spy.txt").st_size)
#         with open("ss.txt", "r") as f:
#             decoded = b"" + base64.b64decode(f.read())
#         with open('all_after.1.bmp', "wb") as f:
#             f.write(decoded)
#     else:
#         break
