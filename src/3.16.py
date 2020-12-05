def check(move, boats_position, shoots_map):
    res = 'miss'

    for boats in boats_position:
        for boat in boats:
            if move == boat:
                counter = 1
                for i in shoots_map:
                    for j in boats:
                        if i == j:
                            counter += 1
                if counter == len(boats):
                    res = 'killed'
                elif counter > len(boats):
                    break
                else:
                    res = 'injury'

    return res
