def BFS(info, start):
    n = len(info)

    queue = [start]
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for i in adj_list[current]:
            if i not in queue and i not in result:
                queue.append(i)

    return result


adj_list = {
    0: [1, 3],
    1: [0, 2, 3],
    2: [1, 4],
    3: [0, 1, 4],
    4: [2, 3]
}

print(BFS(adj_list, 2))
