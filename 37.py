def sort_even(l: list):
    evens = []
    odds = []
    for i in range(len(l)):
        if i % 2 == 0:
            evens.append(l[i])
        else:
            odds.append(l[i])
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans
