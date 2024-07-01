# 3	Время
# Час, минута, секунда
# Вычитание (результат: объект)
# Сравнение (==, <, >)
# __eq__(self, other), __lt__(self, other), __gt__(self, other)
# Перегрузка =


class Clock(object):
    __DAY = 86400

#    def __new__(self, seconds):
#        return self.__init__(seconds)

    def __init__(self, seconds):
        if not isinstance(seconds, int):
            raise TypeError('Переменная должна быть в int')
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return  f'{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}'

    @classmethod
    def __get_formatted(cls, ab):
        return str(ab).rjust(2, '0')    
    
    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Число должно быть в формате int/Clock!')    
        sr = other
        if isinstance(other, Clock):
            sr = other.seconds
        # if Clock(self.seconds - sr) < 0:
        #     return 'Часов в первой дате меньше чем во второй'
        try:
            return Clock(self.seconds - sr)
        except:
            return 'Часов в первой дате меньше чем во второй'


    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Число должно быть в формате int/Clock!')
        sr = other
        if isinstance(other, Clock):
            sr = other.seconds
        return Clock(self.seconds + sr)

    def __eq__(self, other) -> bool:
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Число должно быть в формате int/Clock!')
        sr = other
        if isinstance(other, Clock):
            sr = other.seconds
        return self.seconds == sr

    def __lt__(self, other) -> bool:
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Число должно быть в формате int/Clock!')
        sr = other
        if isinstance(other, Clock):
            sr = other.seconds
        return self.seconds < sr

    def __gt__(self, other) -> bool:
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('Число должно быть в формате int/Clock!')
        sr = other
        if isinstance(other, Clock):
            sr = other.seconds
        return self.seconds > sr

def perebor():
    cl1 = Clock(10000)
    print('Первое время: '+cl1.get_time())       #cl1

    cl2 = Clock(100)
    print('Второе время: '+cl2.get_time())       #cl2

    cl1 = cl1 - 1000
    print('Первое время - 1000 секунд: '+cl1.get_time())       #- per

    cl1 = cl1 - cl2
    print('Первое время - второе время: '+cl1.get_time())       #- other class

    cl3 = cl1 + cl2
    print('Первое время + второе время: '+cl3.get_time())       #add new class

    cl2 = cl2 - cl1
    print('Второе время - первое время: ', cl2.get_time())       #sub new class


    print(' == :', cl1 == cl2)           # ==
    print(' < :', cl1 < cl2)            # <
    print(' > :', cl1 > cl2)            # >



if __name__ == '__main__':
    perebor()