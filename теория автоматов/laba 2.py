import time
s = time.time()
n = 10 # n = int(input("Введите сколько чисел будет выводиться: "))
std, sm1, sm2 = [], "10", "01"
for i in range(0, n):
    std.append("0" + sm1 * i + "0")
    std.append("1" + sm2 * i + "1")
for j in std:
    if std.index(j) < n:
        print(str(std.index(j)+1)+")", j)
print(time.time() - s)