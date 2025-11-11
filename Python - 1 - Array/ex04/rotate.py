import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    try:
        loaded_image = ft_load("animal.jpeg")
        image_trimmed = trim(loaded_image, 450, 100, 400, 400, 1)
        rotate_image(image_trimmed)

    except KeyboardInterrupt:
        print("\nProcess interrupted by user (Ctrl+C). Exiting gracefully...")
    except Exception as e:
        print(f"An error occurred: {e}")


def trim(array: np.array, x: int, y: int, width: int,
         height: int, depth: int = 3) -> np.array:
    return array[y: y + height, x: x + width, :depth]


def manual_transpose(image: np.ndarray) -> np.ndarray:
    """
    Manually transposes a 2D image array
    (swap rows and columns).
    For a 3D array (height, width, channels),
    we only transpose the first two dimensions.
    """
    height, width, channels = image.shape
    # Create an empty array for the transposed image
    transposed = np.zeros((width, height, channels), dtype=image.dtype)

    # Loop over the image array to swap rows and columns manually
    for i in range(height):
        for j in range(width):
            transposed[j, i] = image[i, j]

    return transposed


def rotate_image(pixel_data: np.ndarray):
    image_transposed = manual_transpose(pixel_data)
    print(f'Transposed image:\n{image_transposed}')

    # Remove the single channel dimension
    image_transposed_gray = np.squeeze(image_transposed)
    # Show the image in grayscale
    plt.imshow(image_transposed_gray, cmap='gray')
    # plt.colorbar()  # Adds a color scale to the right of the image
    plt.xlabel('')  # X-axis label
    plt.ylabel('')  # Y-axis label
    plt.title('Trimmed Grayscale Image')  # Title of the plot
    plt.show()


if __name__ == "__main__":
    main()