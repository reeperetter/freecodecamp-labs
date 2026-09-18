def adjacency_list_to_matrix(dic) -> list[list[int]]:
    matrix = []

    for nodes in dic.values():
        row = [0] * len(dic)
        for node in nodes:
            row[node] = 1
        matrix.append(row)

    output = ''
    for row in matrix:
        output += str(row) + '\n'

    print(output)
    return matrix