from typing import List, Optional
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    result = strings[0]
    for s in strings:
        if len(s) > len(result):
            result = s
    return result
