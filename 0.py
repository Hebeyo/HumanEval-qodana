from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if i != j:
                if abs(numbers[i] - numbers[j]) < threshold:
                    return True
    return False
