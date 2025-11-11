import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def trim(
        image: np.ndarray, top: int, left: int,
        height: int, width: int, channels: int):
    """
        Trims the image by selecting a sub-region
        based on specified top, left, height, and width.
    """
    return image[top:top+height, left:left+width, :channels]


def zoom_image(pixel_data: np.ndarray):
    try:
        # Trim the image (hardcoded values: top=450, left=100,
        # height=400, width=400)
        image_trimmed = trim(pixel_data, 100, 400, 400, 400, 1)

        # Print new shape information after trimming
        print(f'New shape after slicing: {image_trimmed.shape} or '
            f'({image_trimmed.shape[0]}, {image_trimmed.shape[1]})')
        print(image_trimmed)

        # Display the trimmed image in grayscale
        # Remove the single channel dimension
        image_gray = np.squeeze(image_trimmed)
        plt.imshow(image_gray, cmap='gray')  # Show the image in grayscale
        plt.xlabel('')  # X-axis label
        plt.ylabel('')  # Y-axis label
        plt.title('Trimmed Grayscale Image')  # Title of the plot
        plt.show()

    except Exception as e:
        print(f"Error during zooming: {e}")


def main():
    try:
        # image path is : "../ex02/*.jpg"
        pixel_data = ft_load("animal.jpeg")
        if pixel_data is not None:
            zoom_image(pixel_data)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user (Ctrl+C). Exiting gracefully...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
