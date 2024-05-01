def fibfib(n: int):
    results = [0, 0, 1]
    if n < 3:
        return results[n]
    for _ in range(3, n + 1):
        results.append(results[-1] + results[-2] + results[-3])
        results.pop(0)
    return results[-1]

