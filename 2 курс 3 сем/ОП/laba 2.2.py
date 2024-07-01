'''
3	Время
Час, минута, секунда
Вычитание (результат: объект)
Сравнение (==, <, >)
__eq__(self, other), __lt__(self, other), __gt__(self, other)
Перегрузка =
'''

class Test(object):
    __DAY = 86400

    def __init__(self, x ,y, z):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z


    # def get_time(self):
    #     s = self.x % 60
    #     m = (self.x // 60) % 60
    #     h = (self.x // 3600) % 24
    #     return  f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    # @classmethod
    # def __get_formatted(cls, ab):
    #     return str(ab).rjust(2, '0')

    def __eq__(self, value) -> bool:
        if not isinstance(value, Test):
            raise ValueError('Не тот формат')
        return (self.x == value.x and       # == времени
                self.y == value.y and
                self.z == value.z)           

    def __lt__(self, value) -> bool:
        if not isinstance(value, Test):
            raise ValueError('Не тот формат у переменной')
        if self.x < value.x:                # < времени
            return self.x < value.x
        else:
            if self.y < value.y:
                return (self.x < value.x and
                        self.y < value.y)
            else:
                if self.z < value.z:
                    return (self.x < value.x and       
                            self.y < value.y and
                            self.z < value.z)
                else:
                    return (self.x < value.x and
                            self.y < value.y and
                            self.z < value.z)

    def __gt__(self, value) -> bool:
        if not isinstance(value, Test):
            raise ValueError('Не тот формат у переменной')
        if self.x > value.x:                # > времени
            return self.x > value.x
        else:
            if self.y > value.y:
                return (self.x > value.x and
                        self.y > value.y)
            else:
                if self.z > value.z:
                    return (self.x > value.x and       
                            self.y > value.y and
                            self.z > value.z)
                else:
                    return (self.x > value.x and
                            self.y > value.y and
                            self.z > value.z)

class Test1(Test):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def __sub__(self, value):
        if not isinstance(value, Test):
            raise ValueError('Не тот формат у переменной')
        
        if (self.x - value.x) < 0:
            return 'Часов в первой дате меньше чем во второй'
        else:
            murx1 = self.x - value.x
            if (self.y - value.y) < 0:
                murx1 -= 1
                mury1 = self.y - value.y
                mury1 += 60
            else:
                mury1 = self.y - value.y
                if (self.z - value.z) < 0:
                    mury1 -= 1
                    murz1 = self.z - value.z
                    murz1 += 60
                    return murx1, mury1, murz1, ': '
                else:
                    murz1 = self.z - value.z
                    return murx1, mury1, murz1, ': '
                

hour1 = 13
minute1 = 26
seconds1 = 31

hour2 = 15
minute2 = 22
seconds2 = 37

if __name__ == '__main__':
    X = Test1(hour1, minute1, seconds1)
    Y = Test1(hour2, minute2, seconds2)
    print('X = ', hour1, minute1, seconds1, '\nY = ', hour2, minute2, seconds2)
    print(X.__eq__(Y))
    print(X.__lt__(Y))
    print(X.__gt__(Y))
    print(Y.__sub__(X))
    print(X.__sub__(Y))
    print(Y.__sub__(Y))