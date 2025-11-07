import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("Family must be list")
    if not all(isinstance(row, list)for row in family):
        raise TypeError("Family must be 2D array")
    if len(family) == 0:
        raise ValueError("family cannot be empty")
    
    first_row = len(family[0])
    
    if any(len(row) != first_row for row in family) :
        raise TypeError("family rows must have the same len")
    
    arr = np.array(family)
    
    print(f"My Shape is {arr.shape}")
    
    truncated = arr[start:end]
    print(f"My new shape is : {truncated.shape}")
    
    return truncated.tolist()