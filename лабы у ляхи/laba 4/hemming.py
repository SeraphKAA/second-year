import math
import copy
from prettytable import PrettyTable

N = int(input("Длина кодируемой последовательности: "))
Set0 = input("Кодируемая последовательность: ")

ControlN = math.ceil(math.log2(N)) + 1 #для вычисления кол-ва контрольных битов
Set0 = [int(i) for i in Set0] #записываем интовые значения со строки
i = 1

need_mas = [] #набор цифр

print()
Len_Set0 = len(Set0)
while (i < Len_Set0):
    Set0.insert(i - 1, 0) #добавляем контрольные биты на нужны места
    Positions = [j + 1 for j in range(len(Set0))]
    need_mas = copy.deepcopy(Positions)
    i = i * 2
    Len_Set0 = len(Set0)


print('Таблица с контрольными битами')
table1 = PrettyTable(need_mas)
table1.add_row(Set0)
print(table1)
print()

MatrixEnc = [[] for i in range(ControlN)]
Boobs_of_binar = [bin(i)[2::] for i in Positions]

for i in range(len(Boobs_of_binar)):
    if (len(Boobs_of_binar[i]) < ControlN):
        Boobs_of_binar[i] = '0' * (ControlN - len(Boobs_of_binar[i])) + Boobs_of_binar[i]
Boobs_of_binar = [l[::-1] for l in Boobs_of_binar]

#выводит матрицу
for i in Boobs_of_binar:
    for j in range(len(i)):
        MatrixEnc[j].append(int(i[j]))

print()
#красивый вывод
print('Таблица с матрицей преобразования')
table2 = PrettyTable(need_mas)
table2.add_row(Set0)
for i in MatrixEnc:
    table2.add_row(i)
print(table2)

#r-очки
Rvalue = []
for i in range(ControlN):
    Res = 0
    for j in range(len(Set0)):
        Res += MatrixEnc[i][j] * Set0[j]
    Res = Res % 2
    Rvalue.append(Res)

print('r0..r'f"{len(Rvalue) - 1}", Rvalue)
print()

Set1 = copy.deepcopy(Set0)
i = 1
j1 = 0
while (i < len(Set1)):
    Set1[i - 1] = Rvalue[j1]
    j1 += 1
    i = i * 2

print("Матрица, с полученными контрольными битами")
table3 = PrettyTable(need_mas)
table3.add_row(Set1)
for i in MatrixEnc:
    table3.add_row(i)
print(table3)

#вторая половина лабы
print()

Set_new = input("Новая кодируемая последовательность: ")
Set_new = [int(i) for i in Set_new] #записываем интовые значения со строки

while len(Set_new) != len(need_mas):
        print(f"вводи {len(need_mas)} циферки!")
        Set_new = input("Новая кодируемая последовательность: ")
        Set_new = [int(i) for i in Set_new] #записываем интовые значения со строки

print()
print("Матрица с новой передаваемой последовательностью")
table4 = PrettyTable(need_mas)
table4.add_row(Set_new)
for i in MatrixEnc:
    table4.add_row(i)
print(table4)

Rvalue = []
for i in range(ControlN):
    Res = 0
    for j in range(len(Set_new)):
        Res += MatrixEnc[i][j] * Set_new[j]
    Res = Res % 2
    Rvalue.append(Res)
print('S0..S'f"{len(Rvalue) - 1}", Rvalue)
print()

#выясняем, в каком бите ошибка, если она есть

end = 0
number = 0

for i in Rvalue:

    end += i * 2 ** number
    number += 1

if end == 0:
    print("ошибок нет")
else:
    print(f'Ошибка в {end} бите')



