def adj_list(mat):
    n = len(mat)
    result = {i:[] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if mat[i][j] > 0:
                result[i].append(j)

    return result


def adj_list_weighted(mat):
    n = len(mat)
    result = {i:[] for i in range(n)}

    for i in range(n):
        for j in range(n):
            if mat[i][j] > 0:
                result[i].append([j, mat[i][j]])

    return result


matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]


print(adj_list(matrix))
print(adj_list_weighted(matrix))
