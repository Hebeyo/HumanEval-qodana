from typing import List, Any
def filter_integers(values: List[Any]) -> List[int]:
    result = []
    for v in values:
        if isinstance(v, int):
            result.append(v)
    return result
