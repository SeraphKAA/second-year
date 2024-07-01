#цена, максимальная скорость, год выпуска и т. д
#*Создать класс Garage, содержащий массив/параметризованную коллекцию объектов этих классов в динамической памяти. 
#Предусмотреть возможность вывода характеристик объектов списка.
#Написать демонстрационную программу, в которой будут использоваться все методы классов.
#from tkinter import image_types
#from zlib import Z_DEFAULT_STRATEGY



from pydoc import visiblename


massiv = []

class Garage: 
    def __init__(self, price, speed, date):
        self.price = price
        self.speed = speed
        self.date = date
#        super().__init__(self.price, self.speed, self.date)

    def mas(self):
        pass


class Vehicle:
    def __init__(self, price, speed, date):
        super().__init__(price, speed, date)


class Car(Vehicle):
    def ford(self):
        return super().self.price, super().self.speed, super().self.date, print(self.price, self.speed, self.date)
        #print(self.price, self.speed, self.date), self.price, self.speed, self.date


class Lorry(Vehicle):
    def grus(self, m):
        self.weight = m
        return super().self.price, super().self.speed, super().self.date, super().self.weight, print(self.price, self.speed, self.date, self.weight)
        #print(self.price, self.speed, self.date, self.weight), self.price, self.speed, self.date, self.weight



massiv = [Car(100000, 120, '24.01.2001'), 
    Lorry(1000000, 80, '04.05.2008'),
    Car(4500000, 210, '09.12.2020')
    ]

#x = Car('100000', '120', '24.01.2001')


massiv[1].grus('4')

#blaaa = zap(massiv)
print(massiv, 'blaaa')


    

#    def grus(self, m):
#        self.weight = m
#        return self.price, self.speed, self.date, self.weight, print(self.price, self.speed, self.date, self.weight, '\n')

'''        while True:
            inp = input('Enter the "!" if u wont exit the loop else print Car or Lorry for that method what u wont: ')
            if inp == '!':
                break
            elif inp == 'Car':
                x.append(Car(int(input('Write the price of the car: ')), int(input('Write the max speed: ')), input('Write the release date: ')))
                return x, print(x)
            elif inp == 'Lorry':
                x.append(Lorry(int(input('Write the price of the lorry: ')), int(input('Write the max speed: ')), input('Write the release date: '), input('Write how much t or kg weight ur lorry: ')))
                return x, print(x)
        return x, print(x)
'''
'''
def zap(x):
    while True:
        inp = input('Enter the "!" if u wont exit the loop else print Car or Lorry for that method what u wont: ')
        if inp == '!':
            break
        elif inp == 'Car':
            x.append(Car(int(input('Write the price of the car: ')), int(input('Write the max speed: ')), input('Write the release date: ')))
            return x, print(x)
        elif inp == 'Lorry':
            x.append(Lorry(int(input('Write the price of the lorry: ')), int(input('Write the max speed: ')), input('Write the release date: '), input('Write how much t or kg weight ur lorry: ')))
            return x, print(x)
'''


#massiv.append(x.mas())
#Gar = Garage(4500000, 210, '09.12.2020')
#Gar.mas(massiv)
