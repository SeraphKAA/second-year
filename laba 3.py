import time
# import timeit
from random import randint, shuffle
# import pandas as pd

# [+]: Метод  прямого выбора
def selection_sort(list):
    count = 0
    it = 0
    swap = 0
    first_timer = time.time()
    # for i in range(0, int(len(list) / 4 - 1)):  #тут изменять значения
    #     smll = i
    #     for j in range(i + 1, int(len(list) / 4)): #тут изменять значения
    for i in range(0, len(list) - 1):
        smll = i
        for j in range(i + 1, len(list)):
            it += 1
            if list[j] < list[smll]:
                count+= 1
                swap += 1
                smll = j
        list[i], list[smll] = list[smll], list[i]
    print("Кол-во операций сравнения:", count,"\nКол-во итераций:", it, "\nКол-во операций замен:", swap)
    print(time.time() - first_timer)
    

# [+]: Метод прямого включения
def direct_activasion_method(list):
    first_timer = time.time()
    count = 0
    it = 0
    swap = 0
    for i in range(len(list)):
        j = i + 1
        for j in range(j, len(list)):
            it += 1
    # for i in range(int(len(list) / 4)):       #тут изменять значения
    #     j = i + 1
    #     for j in range(j, int(len(list) / 4)): #тут изменять значения
            if list[i] < list[j]:
                count += 1
                swap += 1
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    print(time.time() - first_timer, '\n')
    print("Кол-во операций сравнения:", count,"\nКол-во итераций:", it, "\nКол-во операций замен:", swap)


# [+]: Метод прямого обмена
def buble(list):
    first_timer = time.time()
    count = 0
    it = 0
    swap = 0
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1):
            it += 1
    # for i in range(0, int(len(list) / 4 - 1)):          #тут изменять значения
    #     for j in range(0, int(len(list) / 4 - 1)):      #тут изменять значения
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
                swap += 1
    print(time.time() - first_timer, '\n')
    print("Кол-во операций сравнения:", count,"\nКол-во итераций:", it, "\nКол-во операций замен:", swap)

# [+]: Метод быстрой сортировки Хаора
def fast_sort_method(list, count, it, swap):
    G, E, L = [], [], []

    if len(list) > 1:
        temp = list[0]

        for x in range(len(list)):
            it.append(1)
        # for x in range(int(len(list) / 4)):      #тут изменять значения
            if list[x] < temp:
                swap += 1
                L.append(list[x])
                count.append(1)

            elif list[x] == temp:
                swap += 1
                count.append(1)
                E.append(list[x])

            elif list[x] > temp:
                swap += 1
                G.append(list[x])
                count.append(1)

        print("Кол-во операций сравнения:", len(count))
        print("Кол-во итераций:", len(it))
        print("Кол-во операций замен:", swap)
        return fast_sort_method(L, count, it, swap) + E + fast_sort_method(G, count, it, swap)
    else:
        return list
    

def mama(a):
    st = int(input('''Введите число от 0 до 5:
0 - внутренняя функция sort();
1 - первый метод;
2 - второй метод;
3 - третий метод;
4 - четвертый метод;
5 - выход из цикла: \n'''))
    
    match st:
        case 0: # 0.0 sec: при 2к элементов; ~0.0008 sec: при 10к элементах
            first_timer = time.time()
            a.copy().sort()
            print(time.time() - first_timer)

        case 1: # ~0.1 sec, ~910000 (910k) it: при 2к элементов
            selection_sort(a.copy())

        case 2: # ~0.15 sec, ~950000 (950k) it: при 2к элементов
            direct_activasion_method(a.copy())

        case 3: # ~0.28 sec, ~1000000 (1kk) it: при 2к элементов / при 10к 9 сек и 23кк ит
            buble(a)
        
        case 4: # ~0.003 sec, ~28k it: при 2к элементов
            first_timer = time.time()
            fast_sort_method(a.copy(), count = [], it = [], swap = 0)
            print(time.time() - first_timer)

        case 5:
            return 0
        
        case _:
            print("Круто ты написал конечно от 0 до 5, я даже удивляюсь с того, как таким можно быть\nАплодирую стоя, ахАХАХзАъАФЦПЗГЩЫПРШФЦГПАФЦУДЮАх\n\n")
    
    mama(a)

if __name__ == "__main__":
    s = 20
    a = [randint(0, 10000) for i in range(s)]
    sorr  = int(s * 0.75)
    b = a[:sorr]
    b.sort()
    c = a[sorr:]
    # shuffle(c)
    for i in c:
        b.append(i)

    mama(b)


    # a = b + c
    # print('\n', b, sorr)
    # a.sort()
    # a = a[s:] + a[:s]

# сделать эксель таблицу на все элементы и время








# def mainn(mas):
#     results = {}
#     results1 = {}

#     bubble = []
#     selection = []
#     insertion = []
#     quick = []

#     # Тестирование
#     for size in sizes:
#         for order in orders:
#             bubble_time = timeit.timeit(lambda: bubbleSort(mas.copy()), number=1)
#             selection_time = timeit.timeit(lambda: selectionSort(mas.copy()), number=1)
#             insertion_time = timeit.timeit(lambda: insertionSort(mas.copy()), number=1)
#             quick_time = timeit.timeit(lambda: quickSort(mas.copy()), number=1)
#             bubble.append(bubbleSort(mas.copy()))
#             selection.append(selectionSort(mas.copy()))
#             insertion.append(insertionSort(mas.copy()))
#             quick.append(quickSort(mas.copy()))

#             results[(size, order)] = {
#                 'Bubble Sort': bubble_time,
#                 'Selection Sort': selection_time,
#                 'Insertion Sort': insertion_time,
#                 'Quick Sort': quick_time
#             }

#             results1[(size, order)] = {
#                 'Bubble Sort': bubble,
#                 'Selection Sort': selection,
#                 'Insertion Sort': insertion,
#                 'Quick Sort': quick
#             }

#             bubble.clear()
#             selection.clear()
#             insertion.clear()
#             quick.clear()

#     # Сброс ограничений на количество выводимых рядов
#     pd.set_option('display.max_rows', None)

#     # Сброс ограничений на число столбцов
#     pd.set_option('display.max_columns', None)

#     # Сброс ограничений на количество символов в записи
#     pd.set_option('display.max_colwidth', None)

#     # Формирование таблицы результатов
#     df = pd.DataFrame.from_dict(results, orient = "index")
#     df1 = pd.DataFrame.from_dict(results1, orient = "index")
#     df.to_csv("C:\\Users\\79045\\Desktop\\бессонные ночи\\структуры\\лабы\\1.csv")
#     print(df)
#     print(df1)