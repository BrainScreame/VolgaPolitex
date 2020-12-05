import numpy as np

index_to_text = 'abcdef'


def check_position(battle_state, move):
    if battle_state[move[0]][move[1]] == 0:
        if move[0] - 1 >= 0 and battle_state[move[0] - 1][move[1]] == 2:
            return False
        elif move[0] + 1 < len(battle_state) and battle_state[move[0] + 1][move[1]] == 2:
            return False
        elif move[1] - 1 >= 0 and battle_state[move[0]][move[1] - 1] == 2:
            return False
        elif move[1] + 1 < len(battle_state) and battle_state[move[0]][move[1] + 1] == 2:
            return False
        else:
            return True
    else:
        return False


def kill_boat(battle_state, last_move):
    x = last_move[1] - 1
    y = index_to_text.index(last_move[0])

    shoot_poss = list()

    if x - 1 >= 0 and check_position(battle_state, (x - 1, y)):
        shoot_poss.append((x - 1, y))
    if x + 1 < len(battle_state) and check_position(battle_state, (x + 1, y)):
        shoot_poss.append((x + 1, y))
    if y - 1 >= 0 and check_position(battle_state, (x, y - 1)):
        shoot_poss.append((x, y - 1))
    if y + 1 < len(battle_state) and check_position(battle_state, (x, y + 1)):
        shoot_poss.append((x, y + 1))

    move = ("z", 0)  # пустой ход

    if len(shoot_poss) > 0:
        move = (index_to_text[shoot_poss[0][1]], shoot_poss[0][0] + 1)

    return move


def choose_act(battle_state, last_move, result):
    res = set()
    possible_move = list()
    move = ("z", 0)

    battle_find = np.zeros(shape=(len(battle_state), len(battle_state[0])))

    if result == 'injury':
        move = kill_boat(battle_state, last_move)
    else:
        for i in range(len(battle_state)):
            for j in range(len(battle_state[i])):
                if check_position(battle_state, (i, j)):
                    battle_find[i][j] = 1

        for i in range(len(battle_find)):
            for j in range(len(battle_find[i])):
                if battle_find[i][j] == 1:
                    possible_move.append((i, j))
                    if i + 1 < len(battle_find) and battle_find[i + 1][j] == 1:
                        res.add((i, j))
                        res.add((i + 1, j))
                    if j + 1 < len(battle_find[i]) and battle_find[i][j + 1] == 1:
                        res.add((i, j))
                        res.add((i, j + 1))

    if len(res) > 0:
        elem = res.pop()
        move = (index_to_text[elem[1]], elem[0] + 1)
    elif len(possible_move) > 0:
        move = (index_to_text[possible_move[0][1]], possible_move[0][0] + 1)

    return move
