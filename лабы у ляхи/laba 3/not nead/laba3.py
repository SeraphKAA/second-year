from lab3_2_decode import Decode
from lab3_2_encode import Encode

def Stego():
    #print("--Приветствую в моей программе шифровки сообщения в изображении. выберите нужное действие только тсссс!--")
    #print("1: Закодировать сообщение")
    #print("2: Прочитать сообщение")

    func = input("--Приветствую в моей программе шифровки сообщения в изображении. выберите нужное действие только тсссс!--\n1: Закодировать сообщение.\n2: Прочитать сообщение.\n")

    if func == '1':
        src = input("Введите путь до изображения в которое будем засовывать сообщение: ")
        message = input("Введите то самое сообщение для возлюбленной: ")
        dest = input("Введите путь нового файла с названием: ")
        print("Encoding...")
        Encode(src, message, dest)
        print("А теперь быстрее бегите отправлять эту фотографию!")

    elif func == '2':
        src = input("Введите путь изображения из которого будет дешифровывать сообщение. Только никому об этом! ")
        print("Decoding...")
        Decode(src)
        print("Наслаждайтесь полученным результатов, если, конечно, оно вам нравится)")

    else:
        print("ERROR: Invalid option chosen")

if __name__ == '__main__':
    Stego()

#C:\\Users\\пк\\Desktop\\1.png
#C:\\Users\\пк\\Desktop\\RGB.bmp














