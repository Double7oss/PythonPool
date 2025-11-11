import pandas as pa
from typing import Optional


def load(path : str) -> Optional[pa.DataFrame]:
    try :
        dataset = pa.read_csv(path)
        
        print(f"Loading dataset of dimensions {dataset.shape}")
        
        return dataset
    except FileNotFoundError :
        return None
    except pa.errors.EmptyDataError:
        return None
    except pa.errors.ParserError:
        return None

def main() : 
    print(load("life_expectancy_years.csv"))
    

if __name__ == "__main__":
    main()