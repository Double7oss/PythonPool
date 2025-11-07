from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try :
        img = Image.open(path)
        if img.format not in ['JPG', 'JPEG']:
            raise ValueError("Image fromat should be JPG or JPEG")
        #convert image to RGB
        img = img.convert('RGB')
        arr = np.array(img)
        print(f"The shape of image is : {arr.shape}")
        return arr
    except FileExistsError :
        print("File not found")
    except ValueError as ve:
        print("Error : {ve}")
    except Exception as e:
        print(f"Unexpected error {e}")