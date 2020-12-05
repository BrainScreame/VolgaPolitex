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
    index_to_text = 'abcdef'
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
