import math
import matplotlib.pyplot as plt
from math import sqrt
import numpy as np
import random

#[+] Задание 1
x = np.linspace(-10, 20, 150)
u = 7
o = 4
y = [(1 / (o * sqrt(2 * math.pi))) * math.exp(-((i - u) ** 2 )/ (o ** 2)) for i in x]
y1 = [i * 0 for i in x]
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.text(-10, 0.001, 'График первый', color = 'gray')
plt.text(7, 0.1, 'График второй', color = 'black')
plt.plot(x, y, 'b', x, y1, 'r--')
plt.legend()
plt.show()

# [+] Задание 2
def f(x):
  result = []
  for i in x:
    result.append(random.uniform(-1,1))
  return result


x = np.arange(-10, 11, 1)
for i in range(10):
  plt.plot(x, f(x))

plt.show()

# [+] Задание 3
day = ['утро', 'день', 'ночь']
hour = [3, 5, 16]
plt.bar(day, hour)
plt.show()

# [+] Задание 4
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
z = x ** 2 -3 * x * y + y ** 2 + x + 2 * y + 5

ax.plot_surface(x, y, z)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# [+] Задание 5, Вариант - 13

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

x, y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
z = np.sin(np.sqrt(x ** 2 + y ** 2))
ax.plot_surface(x, y, z)
plt.xlabel('x')
plt.ylabel('y')
plt.show()








# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, projection='3d')

# x, y= np.meshgrid(np.linspace(-10, 50, 100), np.linspace(-10, 50, 100))
# #z = (x * (np.sqrt(y))) + (y * (np.sqrt(x)))
# z = x * np.sqrt(y) + y * np.sqrt(x)

# ax.plot_surface(x, y, z)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()