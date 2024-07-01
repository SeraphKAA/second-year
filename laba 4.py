from random import randint, shuffle
import time
from matplotlib import pyplot as plt
from datetime import datetime


def func1(list, element):
    global count
    first_timer = time.time()
    count = 0
    for i in range(len(list)):
        if list[i] == element:
            count += 1
            a = time.time() - first_timer
            # print(a, '\n' + str(i) + " - индекс элемента в массиве" + '\n' + str(count) + " - кол-во сравнений")
            return a, count
        else: 
            count += 1
    print("ничего не нашлось((\nПри этом было произведено {} сравнений".format(count))

        
def func2(list, element):
    first_timer = time.time()
    list.append(element)
    count = 0
    for i in range(len(list)):
        if list[i] == element:
            count += 1
            a = time.time() - first_timer
            # print(a, '\n' + str(i) + " - индекс элемента в массиве" + '\n' + str(count) + " - кол-во сравнений")
            return a, count
        else:
            count += 1

def func3(list, element, start_element = 0):
    # global timer, count
    list.sort()
    global count3
    count3 = 0
    first_timer = time.time()
    end_element = len(list) - 1
    
    while start_element <= end_element:
        middle_element = start_element + (end_element - start_element) // 2
        if list[middle_element] == element:
            count3 += 1
            timer = time.time() - first_timer
            # print(timer, '\n' + str(middle_element) + " - индекс элемента в массиве" + '\n' + str(count3) + " - кол-во сравнений")
            return middle_element
        
        elif list[middle_element] < element:
            start_element = middle_element + 1
            count3 += 1

        else:
            end_element = middle_element - 1
            count3 += 1


    return -1
    # count = 0
    # low = 0
    # high = len(list) - 1

    # while low <= high:
      
    #     middle = (low + high)//2
       
    #     if list[middle] == element:
    #         count += 1
    #         timer = time.time() - first_timer
    #         print(timer, '\n' + str(middle) + " - индекс элемента в массиве" + '\n' + str(count) + " - кол-во сравнений")
    #         return middle
        
    #     elif list[middle] > list.index(element):
    #         count += 1
    #         high = middle - 1                                        
    #     else:
    #         count += 1
    #         low = middle + 1
    # print("не нашло\n")


def mama(list, elem):
    a = int(input("""\nВыберите цифру от 1 до 4, что имеено вам нужно:
1 - линейный поиск;
2 - поиск с барьером;
3 - бинарный поиск;
все остальное - выход из цикла:
"""))

    match a:
        case 1:
            func1(list, elem)
        
        case 2:
            func2(list, elem)
        
        case 3:
            print(func3(list, elem))
        
        case _:
            return 0
    
    mama(list, elem)

def generate(a):
    c = []
    for j in range(len(a)):
        b = [i for i in range(a[j])]
        shuffle(b)
        c.append(b)
    return c

def mmr(mas, el, sizes):
    # global x, y
    x, y = [], []
    for i in mas:
        # print(i)
        timer1 = time.time()
        # el = i[90]
        func1(i, el)
        timer = abs(timer1- time.time())
        x.append(count)
        y.append(timer)
    # figure, axis = plt.subplot(2, figsize = (10, 8))
    # axis[0].plot(sizes, [sum(size)/ 5 for size in timer])
    # axis[0].set_xlabel('раз')
    # axis[0].set_ylabel('два')
    # axis[1].plot(sizes, [sum(co)/ 5 for co in x])
    # axis[1].set_xlabel('раз')
    # axis[1].set_ylabel('два')

    # сделать 2 плота относительно времени и относительно кол-ва итераций +
    print(x, y)
    plt.plot(sizes, x)
    plt.xlabel('sizes')
    plt.ylabel('counts')
    plt.show()
    plt.plot(sizes, y)
    plt.xlabel('sizes')
    plt.ylabel('times')
    plt.show()

def comprasion(list, element):
    final = []
    for i in range(2, 5):
        temp_time11, temp_count1 = func1(list[i], element)
        temp_time21, temp_count2  = func2(list[i], element)
        temp_time3 = time.time(); func3(list[i], element); temp_time31 = (abs(temp_time3 - time.time()))
        final.append([temp_count1, temp_time11]); final.append([temp_count2, temp_time21]); final.append([count3, temp_time31])
    
    print()

    for i in final:
        print(i)





if __name__ == "__main__":
    n = [100, 500, 1000, 5000, 10000]
    a = generate(n)
    el = int(input("Выберите элемент который надо найти: "))
    h = int(input("Выберите индекс, который соответсвует размерности массива: "))
    # mama(a[h], el)
    # mmr(a, el, n)
    comprasion(a, el)

# генерация 3 массивов и сортировка и смотр