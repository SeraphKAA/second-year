import numpy as np

class Matrix:
    def __init__(self, missa):
        self.missa = missa

    def __mul__(self, other):              #mul - умножение
        if isinstance(other, int):         #isinstance  - проверка матрицы
            return self.missa * other     

        if isinstance(other, Matrix):       #проверка является ли other классом, а именно Matrix
            return np.dot(self.missa, other.missa)
        
        else:
            return np.dot(self.missa, other)
            


x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
xx = 3
matrixxxx = Matrix(x)
m = Matrix(x1)
print(matrixxxx * x1)
print(matrixxxx * m)
print(matrixxxx * xx)