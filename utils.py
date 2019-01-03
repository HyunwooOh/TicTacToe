def check_legal_actions(state):
    legal_move = []
    for i in range(len(state)):
        if type(state[i]) == int:
            legal_move.append(i)
    return legal_move
