def strange_sort_list(lst):
    res = []
    while lst:
        res.append(min(lst))
        lst.remove(res[-1])
        if lst:
            res.append(max(lst))
            lst.remove(res[-1])
    return res
