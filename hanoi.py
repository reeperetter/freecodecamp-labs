def hanoi_solver(discs: int) -> str:
    start_stack = [i for i in range(discs, 0, -1,)]
    cols = {
        'col1': start_stack.copy(),
        'col2': [],
        'col3': [],
    }
    moves = f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'

    # while cols['col3'] != start_stack:
        # cols['col3'].append(cols['col1'].pop())
        # moves += f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'
        # cols['col2'].append(cols['col1'].pop())
        # moves += f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'
        # cols['col2'].append(cols['col3'].pop())
        # moves += f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'
        # cols['col3'].append(cols['col1'].pop())
        # moves += f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'
        # cols['col1'].append(cols['col2'].pop())
        # moves += f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'
        # cols['col3'].append(cols['col2'].pop())
        # moves += f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'
        # cols['col3'].append(cols['col1'].pop())
        # moves += f'{cols["col1"]} {cols["col2"]} {cols["col3"]}\n'

    return moves


print(hanoi_solver(4))
