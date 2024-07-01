class Rabota:
    def __init__(self, num, poruch, sodpor, date, datef, whovidal, perch):
        self.num = num
        self.poruch = poruch
        self.sodpor = sodpor
        self.date = date
        self.datef = datef
        self.whovidal = whovidal
        self.perch = perch
    
    def ra(self):
        data = self.date.split('.')
        for i in range (0, 2):
            data[i] = int(data[i])
            
        per = self.perch.split(sep = ' ')
        per[0] = per[0].split(sep = '.')
        per[1] = per[1].split(sep = '.')
        for i in range (0, 2):
            for j in range(0, 2):
                per[i][j] = int(per[i][j])
                
        print(per[0], per[1], data)
        if per[0][1] <= data[1] and data[1] >= per[1][1]:
            if per[0][0] <= data[0] and data[0] >= per[1][0]:
                print('#'+str(self.num), 'поручение, которое было задано:', self.poruch) 



perch = input('укажите диапазон дат: ')
'''
#диапазон дат
perch = input('укажите диапазон дат: ')
per = perch.split(sep = ' ')
per[0] = per[0].split(sep = '.')
per[1] = per[1].split(sep = '.')
for i in range (0, 2):
    for j in range(0, 2):
        per[i][j] = int(per[i][j])
'''


por = [Rabota(1, 'принести молоко', "купить молоко в магазине", "29.10", "29.12", "директор", perch),
       Rabota(2, 'принести ручку', "найти ее в кладовке и принести", "16.08", "16.08", "бухгалтер", perch),
       Rabota(3, 'купить авиабилет', "купить авиабилет Ростов-Шереметьево на 20 апреля", "11.04", "15.04", "директор", perch)
       ]


for i in range (len(por)):
    por[i].ra()
print()
    

"""
por1= rabota(1, 'принести молоко', "купить молоко в магазине", "29.10", "29.12", "директор")
por2= rabota(2, 'принести ручку', "найти ее в кладовке и принести", "16.08", "16.08", "бухгалтер")
por3= rabota(3, 'купить авиабилет', "купить авиабилет Ростов-Шереметьево на 20 апреля", "11.04", "15.04", "директор")

por1.ra()
por2.ra()
por3.ra()
"""