def count_distinct_characters(string: str) -> int:
    result = set()
    for c in string.lower():
        result.add(c)
    return len(result)
