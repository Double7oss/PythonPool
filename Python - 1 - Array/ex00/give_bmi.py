"""BMI = body mass index"""
import numpy as np

def give_bmi(height : list[int | float], weight: list[int | float]) -> list[int | float]:
    np_height = np.array(height)
    np_weight = np.array(weight)
    bmi = np_weight / (np_height ** 2)
    return bmi.tolist()
    
    
def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not isinstance(bmi, list):
        raise TypeError(f"bmi must be a list, got {type(bmi).__name__}")
    
    # Check if limit is an integer
    if not isinstance(limit, int):
        raise TypeError(f"limit must be an int, got {type(limit).__name__}")
    
    # Check if list is empty
    if len(bmi) == 0:
        raise ValueError("bmi list cannot be empty")
    
    # Check if all elements are int or float
    for i, value in enumerate(bmi):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Element at index {i} must be int or float, got {type(value).__name__}")
    
    # Convert to numpy array and apply limit
    bmi_arr = np.array(bmi)
    result_arr = bmi_arr > limit
    # Convert back to Python list of booleans
    return result_arr.tolist()



height = [2.71, 1.15]
weight = [168.5, 38.4]

bmi = give_bmi(height, weight)
print(bmi)
print(apply_limit(bmi, 31))
