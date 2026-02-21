"""Image processing module for cropping and grayscale conversion."""

import numpy as np
from PIL import Image


def crop_center_256(image_path):
    """
    Crop image to top-center 256x256 region.
    
    Args:
        image_path (str): Path to the input image file
        
    Returns:
        PIL.Image: Cropped image (256x256)
    """
    img = Image.open(image_path)
    width, height = img.size
    
    # Calculate crop coordinates to top-center 256x256
    left = (width - 256) // 2
    top = 0  # Start from top
    right = left + 256
    bottom = top + 256
    
    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))
    return cropped_img


def to_grayscale(image):
    """
    Convert image to grayscale if not already.
    
    Args:
        image (PIL.Image): Input image
        
    Returns:
        PIL.Image: Grayscale image
    """
    if image.mode != 'L':
        return image.convert('L')
    return image


def image_to_matrix(image):
    """
    Convert grayscale image to numpy matrix.
    
    Args:
        image (PIL.Image): Grayscale image
        
    Returns:
        np.ndarray: 256x256 grayscale matrix
    """
    return np.array(image, dtype=np.uint8)


def process_image(image_path, output_path=None):
    """
    Main function to process image: crop center 256x256 and convert to grayscale.
    
    Args:
        image_path (str): Path to input image
        output_path (str, optional): Path to save processed image
        
    Returns:
        tuple: (grayscale_image, grayscale_matrix)
    """
    # Crop center 256x256
    cropped = crop_center_256(image_path)
    
    # Convert to grayscale
    grayscale_img = to_grayscale(cropped)
    
    # Convert to matrix
    matrix = image_to_matrix(grayscale_img)
    
    # Save if output path provided
    if output_path:
        grayscale_img.save(output_path)
        print(f"Processed image saved to: {output_path}")
    
    return grayscale_img, matrix
