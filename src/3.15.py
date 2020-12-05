import random

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
