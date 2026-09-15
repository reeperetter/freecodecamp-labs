def hanoi_solver(discs: int) -> str:
    cols = {
        'col1': [i for i in range(discs, 0, -1,)],
        'col2': [],
        'col3': [],
    }
    moves = ''


hanoi_solver(3)
