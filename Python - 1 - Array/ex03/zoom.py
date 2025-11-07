from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_zoom(path: str):
    try:
        img = Image.open(path)
        img = img.convert("RGB")
        arr = np.array(img)
        
        print(f"The shape of image is: {arr.shape}")
        print(arr)
        
        h, w, _ = arr.shape
        start_y = h // 2 - 200
        end_y = h   // 2 + 200
        start_x = w // 2 - 200
        end_x = w  // 2 + 200
        
        zoomed = arr[start_y:end_y, start_x:end_x, [1, 3]]
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        
        plt.imshow(zoomed.squeeze(), cmap="gray")
        plt.title("Zoomed Image (Green Channel)")
        plt.xlabel("X axis (pixels)")
        plt.ylabel("Y axis (pixels)")
        plt.show()

    except FileNotFoundError:
        print("Error: File not found. Please check the image path.")
    except Exception as e:
        print(f"Unexpected error: {e}")
        

if __name__ == "__main__":
    ft_zoom("blue_one.jpg")