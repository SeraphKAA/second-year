import pandas as pd
def main():
    global n, put, FSM, FSM_set
    
    main_dict = {}
    # n = int(input("Введите кол-во вершин: "))
    # put = list(input("Введите пути, кроме 'e', так как это эпсилонт: ").split())
    n = 3
    put = ["a", "b", "c"]

    # temp2 = list(input("Укажите какая вершина по счету конечная/конечные, например 'q1 q2': ").split())
    # FSM = list()
    # for i in temp2:
    #     if int(i[-1]) >= n:
    #         return print("Вы что-то не то написали")
    #     else:
    #         FSM.append(int(i[-1]))
    # FSM_set = set(FSM)
    FSM = [2]
    # FSM_set = set(2)

    main_dict.update({"вершины": ['q' + str(i) for i in range(n)]})
    for i in put:
        main_dict.update({i: [0 for k in range(n)]})
    main_dict.update({"e": [0 for k in range(n)]})

    temp3 = main_dict['вершины']
    for i in temp3:
        for z in FSM:
            if temp3.index(i) == z: temp3[z] = '<-' + i


    for i, j in main_dict.items():
        print(i + '\t', j)



    print('Сейчас будем вводить пути')
    while True:
        a = input("Укажите с какой вершины указываем путь: ")
        if not a: break
        b = list(input("Указываем по какому пути и в какую вершину идет путь: ").split())
        if not b: break
        temp1 = main_dict[b[0]]
        for i in range(n):
            if int(a[-1]) == i and temp1[i] == 0:
                temp1[i] = [b[1]]
            elif int(a[-1]) == i:
                temp1[i].append(b[1])

        main_dict.update({b[0]: temp1})
        # main_dict[b[0]][a[-1] - 1] = b[1]
        for i, j in main_dict.items():
            print(i + '\t', j)
    
    return main_dict


def matrix_s(dict, n, FSM):
    s = dict
    s.update({'вершины': ['s' + str(u) for u in range(n)]})
    temp1s = s['вершины']
    for i in temp1s:
        for z in FSM:
            if temp1s.index(i) == z: temp1s[z] = '<-' + i

    for i in s.keys():
        for j in s[i]:
            if type(j) == list:
                for z in range(len(j)):
                    t = j[z][-1]
                    j[z] = 's' + t


    for i, j in s.items():
        print(i + '\t', j)



    t1 = []; t2 = []; t3 = []
    temp = s['e']
    for i in temp:
        if i != 0:
            for z in i:
                for value in s['вершины']:
                    if z[-1] == value[-1]:
                        t1.append(i); t2.append(value); t3.append(temp.index(i))
                        print('в какую вершину:', t1, "вершина куда попало:", t2, "вершина из которой мы идем:", t3)


    for key in s.keys():
        if key != 'веришны':
            
            pass
    





def matrix_p(dict, n, FSM):
    p = dict
    p.update({'вершины': ['s' + str(u) for u in range(n)]})
    temp1s = p['вершины']
    for i in temp1s:
        for z in FSM:
            if temp1s.index(i) == z: temp1s[z] = '<-' + i

    for i, j in p.items():
        print(i + '\t', j)

    pass





if __name__ == '__main__':
    a = main()
    # a = {'вершины': ['q0', 'q1', '<- q2'], 'a': [0, ['q2'], 0], 'b': [['q2'], 0, 0], 'c': [0, ['q0'], ['q1']], 'e': [['q1'], ['q1'], 0]}
    b = matrix_s(a, 3, [2])




# class State:
#     def __init__(self, name):
#         self.name = name
#         self.transitions = {}
#         self.final = False

#     def add_transition(self, input_symbol, state):
#         self.transitions[input_symbol] = state

#     def set_final(self):
#         self.final = True

# # Функция для детерминизации автомата
#     def determinize(start_state):
#         new_start_state = State(frozenset([start_state]))
#         queue = [new_start_state]
#         table = {new_start_state.name: new_start_state}

#         while queue:
#             current_state = queue.pop(0)
#             for input_symbol in input_symbols:
#                 next_states = set()
#                 for state in current_state.name:
#                     next_state = state.transitions.get(input_symbol)
#                     if next_state:
#                         next_states.add(next_state)

#                     if not next_states:
#                         continue

#         next_states = frozenset(next_states)
#         if next_states not in table:
#         new_state = State(next_states)
#         table[next_states] = new_state
#         queue.append(new_state)
#         else:
#         new_state = table[next_states]

#         current_state.add_transition(input_symbol, new_state)

#         for state in table.values():
#         for inner_state in state.name:
#         if inner_state.final:
#         state.set_final()

#         return new_start_state

# # Пример конечного автомата
# input_symbols = ['a', 'b']
# q0 = State('q0')
# q1 = State('q1')
# q2 = State('q2')
# q3 = State('q3')
# q0.add_transition('a', q1)
# q0.add_transition('b', q2)
# q1.add_transition('a', q3)
# q1.add_transition('b', q2)
# q2.add_transition('a', q1)
# q2.add_transition('b', q3)
# q3.set_final()

# # Получаем детерминированный автомат
# dfa = determinize(q0)

# # Печатаем результат
# for state in dfa.transitions.keys():
# print(f'{state.name} -> {dfa.transitions[state].name}')