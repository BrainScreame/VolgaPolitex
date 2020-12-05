import random
import numpy as np

size_area = 4  # размер поля
area = [[0] * size_area for i in range(size_area)]  # массив поля
index_to_text = 'abcdef'


def check_position_horizontal(size_ship):
    suitable_coordinates = list()
    for i in range(len(area)):
        for j in range(len(area[i])):
            state = True
            for k in range(j, j + size_ship):
                if k >= len(area[i]) or area[i][k] != 0:
                    state = False
                    break
            if state:
                temp_coord = (i, j)
                suitable_coordinates.append(temp_coord)
    return suitable_coordinates


def check_position_vertical(size_ship):
    suitable_coordinates = list()
    for i in range(len(area)):
        for j in range(len(area[i])):
            state = True
            for k in range(j, j + size_ship):
                if k >= len(area[i]) or area[k][i] != 0:
                    state = False
                    break
            if state:
                temp_coord = (j, i)
                suitable_coordinates.append(temp_coord)
    return suitable_coordinates


def put_sheep_horizontal(coord, ship_size):
    res = list()
    for j in range(coord[1], coord[1] + ship_size):
        area[coord[0]][j] = 1
        # res.append((coord[0], j))
        res.append((index_to_text[j], coord[0] + 1))
        if coord[0] - 1 >= 0:
            area[coord[0] - 1][j] = 2
        if coord[0] + 1 < size_area:
            area[coord[0] + 1][j] = 2

    if coord[1] - 1 >= 0:
        area[coord[0]][coord[1] - 1] = 2
        # if coord[0] - 1 >= 0:
        #     area[coord[0] - 1][coord[1] - 1] = 2
        # if coord[0] + 1 < size_area:
        #     area[coord[0] + 1][coord[1] - 1] = 2
    if coord[1] + ship_size < size_area:
        area[coord[0]][coord[1] + ship_size] = 2
        # if coord[0] - 1 >= 0:
        #     area[coord[0] - 1][coord[1] + ship_size] = 2
        # if coord[0] + 1 < size_area:
        #     area[coord[0] + 1][coord[1] + ship_size] = 2
    return res


def put_sheep_vertical(coord, ship_size):
    res = list()
    for i in range(coord[0], coord[0] + ship_size):
        area[i][coord[1]] = 1
        # res.append((i, coord[1]))
        res.append((index_to_text[coord[1]], i + 1))
        if coord[1] - 1 >= 0:
            area[i][coord[1] - 1] = 2
        if coord[1] + 1 < size_area:
            area[i][coord[1] + 1] = 2

    if coord[0] - 1 >= 0:
        area[coord[0] - 1][coord[1]] = 2
        # if coord[1] - 1 >= 0:
        #     area[coord[0] - 1][coord[1] - 1] = 2
        # if coord[1] + 1 < size_area:
        #     area[coord[0] - 1][coord[1] + 1] = 2
    if coord[0] + ship_size < size_area:
        area[coord[0] + ship_size][coord[1]] = 2
        # if coord[1] - 1 >= 0:
        #     area[coord[0] + ship_size][coord[1] - 1] = 2
        # if coord[1] + 1 < size_area:
        #     area[coord[0] + ship_size][coord[1] + 1] = 2
    return res


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


def start_boats_position(how_many_boats):
    boats_position = []

    cur_ship_size = len(how_many_boats)
    for boats in reversed(how_many_boats):
        for boat in range(0, boats):
            ship_orientation = random.randrange(0, 1)
            if ship_orientation == 0:
                coord = check_position_horizontal(cur_ship_size)
                # print(coord)
                cur_coord = random.randrange(0, len(coord))
                # print(coord[cur_coord])
                boats_position.append(put_sheep_horizontal(coord[cur_coord], cur_ship_size))
            else:
                coord = check_position_vertical(cur_ship_size)
                # print(coord)
                cur_coord = random.randrange(0, len(coord))
                # print(coord[cur_coord])
                boats_position.append(put_sheep_vertical(coord[cur_coord], cur_ship_size))
            # print_area()
        cur_ship_size -= 1

    return boats_position


def choose_act(battle_state, last_move, result):
    res = set()
    possible_move = list()
    move = ("z", 0)

    battle_find = np.zeros(shape=(len(battle_state), len(battle_state[0])))

    for i in range(len(battle_state)):
        for j in range(len(battle_state[i])):
            if battle_state[i][j] == 1:
                return kill_boat(battle_state, (index_to_text[j], i + 1))

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
        move_index = random.randrange(0, len(possible_move))
        move = (index_to_text[possible_move[move_index][1]], possible_move[move_index][0] + 1)

    return move
