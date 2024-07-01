import itertools
#from lab2 import vertices, alphabet, transitions, initial_state, final_states
vertices = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
alphabet = {'a', 'b'}
transitions = {
    'q0': {'a': 'q1', 'b': 'q4'},
    'q1': {'a': 'q2', 'b': 'q4'},
    'q2': {'a': 'q5', 'b': 'q2'},
    'q3': {'a': 'q7', 'b': 'q5'},
    'q4': {'a': 'q2', 'b': 'q5'},
    'q5': {'a': 'q6', 'b': 'q5'},
    'q6': {'a': 'q7', 'b': 'q6'},
    'q7': {'a': 'q7', 'b': 'q6'}
}
for i, j in transitions.items():
    print(i, j)
initial_state = 'q0'
final_states = {'q3', 'q6', 'q7'}

'''vertices = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9'}
alphabet = {0, 1}
transitions = {
    'q0': {0: 'q1', 1: 'q2'},
    'q1': {0: 'q3', 1: 'q4'},
    'q2': {0: 'q1', 1: 'q3'},
    'q3': {0: 'q5', 1: 'q6'},
    'q4': {0: 'q7', 1: 'q8'},
    'q5': {0: 'q6', 1: 'q9'},
    'q6': {0: 'q9', 1: 'q5'},
    'q7': {0: 'q9', 1: 'q8'},
    'q8': {0: 'q7', 1: 'q9'},
    'q9': {0: 'q9', 1: 'q9'}
}
initial_state = 'q0'
final_states = {'q4', 'q5', 'q6', 'q7', 'q8'}'''

# шаг 1: удалить недостижимые состояния
reachable_states = set()
queue = [initial_state]
while queue:
    state = queue.pop(0)
    reachable_states.add(state)
    transitions_from_state = transitions[state]
    for symbol in alphabet:
        next_state = transitions_from_state[symbol]
        if next_state not in reachable_states:
            queue.append(next_state)
# print(reachable_states)
# шаг 2: разбить состояния на эквивалентные классы
partition = [final_states, vertices - final_states]
# print(partition, '\n')
while True:
    new_partition = []
    for group in partition:
        # print(group)
        # проверяем, в какую группу попадает каждое состояние
        groups_for_states = {}
        for state in group:
            transitions_from_state = transitions[state]
            transitions_group = []
            for symbol in alphabet:
                next_state = transitions_from_state[symbol]
                for i, other_group in enumerate(partition):
                    if next_state in other_group:
                        transitions_group.append(i)
                        break
                else:
                    raise Exception("State {} has invalid transition for symbol {}".format(state, symbol))
            groups_for_states[state] = tuple(transitions_group)
        # разбиваем группу на подгруппы по переходам
        new_groups = []
        for sub_group in itertools.groupby(sorted(group, key=lambda s: groups_for_states[s]), key=lambda s: groups_for_states[s]):
            new_groups.append(set(sub_group[1]))
        # print(f"new group - {new_groups}")
        new_partition += new_groups
    if partition == new_partition: partition.pop(1); break
    partition = new_partition

# шаг 3: создать новый автомат на основе классов эквивалентности
print(partition)
new_vertices = []
new_transitions = {}
new_initial_state = None
new_final_states = set()
for i, group in enumerate(partition):
    # создаем новое состояние
    new_state = "q{}".format(i)
    new_vertices.append(new_state)
    # определяем, является ли группа начальным или конечным состоянием
    if initial_state in group:
        new_initial_state = new_state
    if group & final_states:
        new_final_states.add(new_state)
    # создаем переходы
    group_transitions = {}
    for symbol in alphabet:
        next_state = transitions[list(group)[0]][symbol]
        for j, new_group in enumerate(partition):
            if next_state in new_group:
                group_transitions[symbol] = "q{}".format(j)
                break
    new_transitions[new_state] = group_transitions

# выводим новый автомат
print("\nvertices = {}".format(new_vertices))
print("alphabet = {}".format(alphabet))
for state, transitions in new_transitions.items():
    for symbol, next_state in transitions.items():
        print(f'({state}, {symbol})--> {next_state}')
print("initial_state = {}".format(new_initial_state))
print("final_states = {}".format(new_final_states))
