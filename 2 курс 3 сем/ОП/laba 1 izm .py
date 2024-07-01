class Rabota:
    def __init__(self, num, poruch, sodpor, date, datef, whovidal):
        self.num = num
        self.poruch = poruch
        self.sodpor = sodpor
        self.date = date
        self.datef = datef
        self.whovidal = whovidal
    
    def ra(self, perch):
        data = self.date.split('.')
        for i in range (0, 2):
            data[i] = int(data[i])
            
        per = perch.split(sep = ' ')
        per[0] = per[0].split(sep = '.')
        per[1] = per[1].split(sep = '.')
        
        for i in range (0, 2):
            for j in range(0, 2):
                per[i][j] = int(per[i][j])               
        if per[0][1] <= data[1] and data[1] <= per[1][1]:
            print('#'+str(self.num), 'поручение, которое было задано:', self.poruch)

        elif data[1] == per[0][1] or data[1] == per[1][1]:
            if per[0][0] <= data[0] and data[0] <= per[1][0]:
                print('#'+str(self.num), 'поручение, которое было задано:', self.poruch)
            
        else:
            print('not satisfy the condiction')
    
    def cond2(self, x):
        if self.whovidal == x:
            print('#'+str(self.num), 'поручение, которое было задано: ', self.poruch+', и кем было задано: '+self.whovidal)
        else:
            print('#'+str(self.num)+' not satisfy this condiction (about whovidal)')
            
            
            
def zap():
    por.append(Rabota(int(input("номер поручения: ")), input('поручение: '), input('подробности поручение: '), input('дата выдачи поручения: '), input('дата выполнения: '), input('кто выдал: ')))
    return por

perch = input('укажите диапазон дат: ')
x = input('Укажите должность человека который выдал задание: ')


por = [Rabota(1, 'принести молоко', "купить молоко в магазине", "29.10", "29.12", "директор"),
       Rabota(2, 'принести ручку', "найти ее в кладовке и принести", "16.08", "16.08", "бухгалтер"),
       Rabota(3, 'купить авиабилет', "купить авиабилет Ростов-Шереметьево на 20 апреля", "11.04", "15.04", "директор")
       ]


while True:
    if input('Enter the "!" if u wont exit the loop: ') == '!':
        break
    zap()


for i in range (len(por)):
    por[i].ra(perch)
    
print()

for i in range (len(por)):
    por[i].cond2(x)

#вызов отдельной функции и для каких по индексу в листе
print("\nВыберите какой метод вы хотите выбрать.")
print('ra/cond2.')
print('Если не хотите вызывать какую-то функцию, то пишите "0".')
ab = input('писать сюда: ')

print('Напишите с каких до каких индексов в листе вы хотите выполнить свой метод через точку.', 'Если что вот столько всего переменных в листе: '+str(len(por)))
cd = input("сюда: ")

cd = cd.split()
for i in range(len(cd)):
    cd[i] = int(cd[i])


#цикл для этого
while True:
    if ab == '0':
       print('Ничего не произошло как и хотел :)')
       break
    elif ab == 'ra':
        for i in range(len(por)):
            if i >= cd[0] and i <= cd[1]:
                por[i].ra(perch)
        break
    elif ab == 'cond2':
        for i in range(len(por)):
            if i >= cd[0] and i <= cd[1]:
                por[i].cond2(x)
        break
    else:
        print("ты ввел с ошибкой(")

