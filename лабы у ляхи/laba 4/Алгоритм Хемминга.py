from random import randint
def visual():
    ar = arr[::-1]
    tt2, t0 = [], [[], [], [], [], []]; tt2.append([f"{i}" for i in range(12)]); tt2.append([f'{i}' for i in range(1, 13)])
    for i in range(len(ar)):
        t0[0].append(ar[i])


    for i in range(14):
        if i % 2 != 0:
            t0[1].append('_')
        else:
            t0[1].append("1")
        
    for i in range(14):
        if (i + 1) not in {2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23}:
            t0[2].append('_')
        else:
            t0[2].append("2")

    for i in range(14):
        if i >= 11:
            t0[3].append("3")
            break
        elif (i + 1) < 2 ** 2 or (i + 1) >= 2 ** 3:
            t0[3].append('_')
        else:
            t0[3].append("3")
    t0[3].append("3"); t0[3].append("3")

    for i in range(14):
        if (i + 1) < 2 ** 3 or (i + 1) > 2 ** 4:
            t0[4].append('_')
        else:
            t0[4].append("4")


    pow2 = []
    for i in range(14):
        if i == 0:
            pow2.append('0')
        elif i == 1:
            pow2.append('1')
        elif i == 3:
            pow2.append('2')
        elif i == 7:
            pow2.append('3')
        else:
            pow2.append('_')


    print(pow2, '\tСтепени 2'); print(tt2[0], '\tИндексы'); print(tt2[1], '\t№ бита\n' + '-' * 63); print(t0[0]); print(t0[1]); print(t0[2]); print(t0[3]); print(t0[4], '\n' * 2)



def calcRedundantBits(m): 
    for i in range(m):
        if(2**i >= m + i + 1):
            return i
 
def posRedundantBits(data, r):
    j, k = 0, 1
    m = len(data)
    res = ''

    for i in range(1, m + r+1):
        if(i == 2**j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1
 
    #подсчитывание и итерационные процессы протекают в обратном порядке поэтому разворачиваем его
    return res[::-1]
 

 
 
def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
 
            # если 1 в сложении по модулю 2 то 
            # находим значение val.
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
                # -1 * j задано, так как массив перевернут
 
        # объединение через срезы строки
        # (0 to n - 2^r) + val + (n - 2^r + 1 to n)
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i)+1:]
    return arr
 
 
def detectError(arr, nr):
    n = len(arr)
    res = 0
 
    # вычисление val
    for i in range(nr):
        val = 0
        for j in range(1, n + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(arr[-1 * j])
 
        # создание бинарного вида путем добавления val
 
        res = res + val*(10**i)
 
    # возвращаем в десятичную форму представления
    return int(str(res), 2)
 
 

data = ''
for i in range(10):
    data += str(randint(0, 1))
data = '1011001110'
print('Цепочка: ' + data[::-1] + '\n') 

m = len(data)
r = calcRedundantBits(m)

arr = posRedundantBits(data, r)
visual()



arr = calcParityBits(arr, r)

print("Что мы получили: " + arr[::-1]) 


arr = '101110011101'
print("Переданное слово с ошибкой " + arr[::-1])
correction = detectError(arr, r)
if(correction==0):
    print("нет ошибки")
else:
    print("позиция ошибки",len(arr)-correction+1," элемент справа")