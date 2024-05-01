def get_row(lst, x):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == x:
                result.append((i, j))
    return sorted(sorted(result, key=lambda x: x[1], reverse=True), key=lambda x: x[0])
