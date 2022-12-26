DIRECTIONS = [
    (['R'], (1, 0)),
    (['L'], (-1, 0)),
    (['U'], (0, 1)),
    (['D'], (0, -1))
]

DIRECTIONS_DICT = {key:value for key_list, value in DIRECTIONS for key in key_list}