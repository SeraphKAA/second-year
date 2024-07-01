class Vehicle:
    def __init__(self, name, speed, price) -> None:
        self.name = name
        self.speed = speed
        self.price = price
        
class Car(Vehicle):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def info(self):
        return 'Машина {1}, цена к-ой = {0} и скоростью {2}'.format(self.price, self.name, self.speed)

class Lorry(Vehicle):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def info(self):
        return 'Грузовик-кун {1}, цена к-ой = {0} и скоростью {2}'.format(self.price, self.name, self.speed)

class Bicycle(Vehicle):
    def __init__(self, *args) -> None:
        super().__init__(*args)
    def info(self):
        return 'Велосипед-майто-кун {1}, цена к-ой = {0} и скоростью {2}'.format(self.price, self.name, self.speed)


class Garage:
    def __init__(self, mas) -> None:
        self.mas = mas

    def zap(self):
        return [print(i.name, i.speed, i.price) for i in self.mas]

def zapoln(x):
    while True:
        inp = input('Enter the "!" if u wont exit the loop else print Car or Lorry for that method what u wont: ')
        if inp == '!':
            break

        elif inp == 'Car':
            x.append(Car(input('Write the name of the car: '), int(input('Write the max speed: ')), int(input('Write the price: '))))
            return x, print(x)

        elif inp == 'Lorry':
            x.append(Lorry(input('Write the name of the lorry: '), int(input('Write the max speed: ')), int(input('Write the price: '))))
            return x, print(x)

        elif inp == 'Bicycle':
            x.append(Bicycle(input('Write the name of the lorry: '), int(input('Write the max speed: ')), int(input('Write the price: '))))
            return x, print(x)


if __name__ == '__main__':
    x = Car('Toyota', 280, 200000)
    y = Bicycle('BMX', 60, 11000)
    z = Lorry('GAZ', 90, 100000)
    print('\n', x.info(), '\n'*2, y.info(), '\n'*2, z.info(), '\n')
    abc = [x, y, z]
    A = Garage(abc)
    zapoln(abc)
    A.zap()