
def main():
    final = input("Введите алфавит: ").split()
    # in_slov = ['a', 'b', 'c']
    in_slov = []
    for i in final:
        if i in final and i not in in_slov:
            in_slov.append(i)
    
    in_len = len(in_slov)
    print("алфавит- {}\nДлина алфавита- {}".format(in_slov, in_len))

## ====================================================================================================================== #
    
    # in_len1 = input("Введите кол-во уникальных значений: ")
    # if in_len != in_len1:
    #     return print("Вы ввели неправильное кол-во уникальных значений")

## ====================================================================================================================== #

    deist = input("Выбирете действие (1) или (2): ")
    # deist = '1'

# нахождение из слова число
    if deist == '1':
        deiss2 = input("Введите слово: ")
        # deiss2 = 'cbaac'
        
        k, a1 = len(deiss2), []

        [a1.append(in_slov.index(i) + 1) for i in deiss2]
        print(a1, k)
        b = 0
        
        for i in range(1, k+1):
            aa = in_len**(k-i) * a1[i - 1]
            b += aa
            print(b, in_len**(k-i), a1[i - 1])
        print(b)
        
# нахождение из числа слово
    elif deist == '2':          #+
        deiss1 = int(input("Введите число: "))
        if deiss1 == 0:
            return print('E = [ ]- т.е. пустое слово')
        deisss, lists = [], []
        deisss.append(deiss1)
        while deisss[len(deisss)-1] > 1 and deisss[len(deisss)-1] > in_len:  # and (deisss[len(deisss)-1] // in_len != in_len or (deisss[len(deisss)-1] - 1) // in_len != in_len)
            if deisss[len(deisss)-1] % in_len == 0:
                lists.append(in_len)
                deisss[len(deisss)-1] -= 1
                deisss1 = deisss[len(deisss)-1] // in_len
                deisss.append(deisss1)
                # print(deisss1, lists)
            else:
                for i in range(1, in_len):
                    if (deisss[len(deisss)-1] - i) % in_len == 0:
                        lists.append(i)
                        deisss1 = deisss[len(deisss)-1] // in_len
                        deisss.append(deisss1)
                        # print(deisss1, lists)

        if deisss[-1] == in_len:
            lists.append(in_len)
        
        # print(deisss, '\n', lists)

        ass = ''

        for i in range(len(lists)):
            print('{}: k = {}, r = {}'.format(i + 1, deisss[i], lists[i]))
        
        lists.reverse()
        
        for i in range(len(lists)):
            ass += in_slov[int(lists[i])-1]
        print('\n' + ass)
        
    else:
        print("вы ввели не 1 и 2")


if __name__ == "__main__":
    main()
    pass