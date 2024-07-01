from random import randint

# zadanie 1 +
def zad1():
    put = 'C:\\Users\\79045\\Desktop\\бессоные ночи\\структуры\\лабы\\лаба 2\\'
    putaa = 'asd.txt'
    putbb = 'ass'
    ttx = '.txt'
    with open (put + putbb + ttx, 'w+') as b:
        for i in range(randint(1, 300)):
            b.write(str(randint(-100, 100)) + '\n')


    with open(put + putbb + ttx, 'r') as a:
        aa = a.readlines()
        ass, count = [], 0

        for i in range(len(aa)):
            ass.append(aa[i].replace('\n', ''))
            ass[i] = int(ass[i])
            if ass[i] < 0: count += 1
        pass
    print(count)


# zadanie 2
# 2	Разработать и отладить процедуры, добавляющие заданную букву в произвольное место символьного файла. 
def zad2():
    put = 'C:\\Users\\79045\\Desktop\\бессоные ночи\\структуры\\лабы\\лаба 2\\'
    putaa = 'asd'
    putbb = 'ass'
    ttx = '.txt'
    aa = []
    with open(put + putaa + ttx, 'r') as a:
        aa = a.readlines()
        for i in aa: print(str(aa.index(i) + 1) + ') ' + i)

    c = input('Введите букву, которую вы вставите в  файл, кроме \: ')
    d = int(input('Введите в какую строку и в каком месте вы хотите ставить символ: '))
    # c, d = '333', 45
    e = ''.join(aa)
    with open(put + putaa + ttx, 'r+') as a:
        a.seek(0)
        a3 = e[:d] + c + e[d:]
        a.write(a3)
        pass


# zadanie 3
# 3	Создать на диске Текстовый файл, ввести в него произвольный текст, затем вывести n строку текста, предусмотреть возможность отсутствия строки с таким номером.
def zad3():
    put = 'C:\\Users\\79045\\Desktop\\бессоные ночи\\структуры\\лабы\\лаба 2\\'
    putaa = 'asd'
    putaaa = 'asdsada'
    putbb = 'ass'
    ttx = '.txt'
    spis = []

    a3 = open(put + putaaa + ttx, 'w+')
    n = int(input("введите желаемое количество строк: "))

    for i in range(n):
        a3.writelines(input("Введите строку {}: ".format(i + 1)) + '\n')

    a3.close()

    a33 = open(put + putaaa + ttx, 'r+')
    for i in a33.readlines():
        spis.append(i)
        print(i)
    
    a33.close()
    childporn = int(input("Введите нужную строчку: "))

    if childporn > n:
        print("Такого номера строки нет")
    else:
        print(spis[childporn - 1])
    pass


# zadanie 4
# 4	Реализовать функцию поиска в Текстовом файле подстроки. Результатом поиска является пара значений номер сроки – номер позиции. Предусмотреть возможность более одного совпадения.
def zad4():
    put = 'C:\\Users\\79045\\Desktop\\s\\'
    putaa = 'asd'
    putbb = 'ass'
    ttx = '.txt'
    sik = input('Введите то, что надо найти: ')
    asd = []

    f = open(put + putaa + ttx, 'r+')
    for i in f.readlines():
        asd.append(i)
        print(i)
    f.close()

    a = True
    while a:
        for index, line in enumerate(asd):
            if sik in line:
                print('Строка- {}, индексы с {} до {}'.format(index+1, line.find(sik)+1, line.find(sik) + 1 + len(sik)))
                line = line[:line.find(sik)] + line[line.find(sik) + len(sik):]
        if sik not in asd:
            a = False

    pass


# zadanie 5
# 5	Задать текстовый файл. Написать функцию определяющую количество уникальных слов в файле. Написать функцию определяющую количество повторов каждого слова, содержащегося в файле.
def zad5():
    put = 'C:\\Users\\79045\\Desktop\\бессоные ночи\\структуры\\лабы\\лаба 2\\'
    putaa = 'asd'
    putbb = 'ass'
    ttx = '.txt'
    text = open(put + putaa + ttx, "r")
    d = dict()

    for line in text:
        line = line.strip().lower()
        words = line.split()

        for word in words:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1

    for key in list(d.keys()):
        print(key, ":", d[key])
    text.close()


if __name__ == "__main__":
    # zad1() # +
    # zad2() # +
    # zad3() # +
    zad4() # доделать, чтобы повторении 
    # zad5() # +
    pass