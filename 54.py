def same_chars(s0: str, s1: str):
    for c in s0:
        if c not in s1:
            return False
    for c in s1:
        if c not in s0:
            return False
    return True

