def common(l1: list, l2: list):
    ret = []
    for e1 in l1:
        for e2 in l2:
            if e1 == e2:
                ret.append(e1)
    return sorted(list(set(ret)))
