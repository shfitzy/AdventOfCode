DIRECTIONS = [
    (['R', '>'], (1, 0)),
    (['L', '<'], (-1, 0)),
    (['U', '^'], (0, 1)),
    (['D', 'v'], (0, -1))
]

DIRECTIONS_DICT = {key:value for key_list, value in DIRECTIONS for key in key_list}

def get_dir_tuple(input, x_pos_right=True, y_pos_up=True):
    dir_tuple = DIRECTIONS_DICT[input]

    if not x_pos_right and dir_tuple[0] != 0: return (dir_tuple[0] * -1, 0)
    elif not y_pos_up and dir_tuple[1] != 0: return (0, dir_tuple[1] * -1)

    return dir_tuple

def move_in_dir(start_pos, input, x_pos_right=True, y_pos_up=True):
    dir_tuple = get_dir_tuple(input, x_pos_right, y_pos_up)
    return (start_pos[0] + dir_tuple[0], start_pos[1] + dir_tuple[1])