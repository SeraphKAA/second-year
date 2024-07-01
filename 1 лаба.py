#вариант 16


def d3():
    a = input('Напишите первое предложение с пробелами между ними: ').lower().split()
    b = input('Напишите второе предложение с пробелами между ними: ').lower().split()
    a, b = set(a), set(b)
    print(a,"\n",  b)
    a &= b
    print(a)
    

def dob():      # часть 1 и 2 задания задания
    S = {}
    s = input("""Задайте символы для множества: """).lower()
    # S = set(s)

    return s
 
def prov(A):
    first_tup1 = []
    second_tup1 = []
    third_tup1 = []
    kirillica = ('фывапролджэячсмитьбюйцукенгшщзхъё')
    angl = ('qwertyuioasdfghjklzxcvbnm')
    for i in A:
        if i.isdigit():
            first_tup1.append(i)
        elif i in kirillica:
            second_tup1.append(i)
        elif i in angl:
            third_tup1.append(i)
        else:
            print("Вы ввели спец символы")
            continue

    first_tup, second_tup, third_tup = set(first_tup1), set(second_tup1), set(third_tup1)
    print(first_tup, second_tup, third_tup)


if __name__ == "__main__":
    # 1 +
    # 2 +
    # 3 +
    d3()
    # 4 +
    prov(set(dob()))   #+
