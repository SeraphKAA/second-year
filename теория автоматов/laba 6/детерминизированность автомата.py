
alphabet = {'a', 'b'}
vertices = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
nfa = {
    'q0': {'a': {'q1'}, 'b': {'q4'}},
    'q1': {'a': {'q2'}, 'b': {'q4'}},
    'q2': {'a': {'q5'}, 'b': {'q2'}},
    'q3': {'a': {'q7'}, 'b': {'q5'}},
    'q4': {'a': {'q2'}, 'b': {'q5'}},
    'q5': {'a': {'q6'}, 'b': {'q5'}},
    'q6': {'a': {'q7'}, 'b': {'q6'}},
    'q7': {'a': {'q7'}, 'b': {'q6'}}
}

initial_state = 'q0'
final_states = {'q3', 'q6', 'q7'}


def is_dfa(dfa):
    """
    Check if the given DFA is deterministic.
    """
    for state in dfa:
        for symbol in alphabet:
            if symbol not in dfa[state]:
                return False
            next_state = dfa[state][symbol]
            if isinstance(next_state, set) or isinstance(next_state, frozenset):
                return True
    return False

# Check if the resulting DFA is deterministic
if is_dfa(nfa):
    print("The DFA is deterministic.")
else:
    print("The DFA is not deterministic.")
    var = 1

