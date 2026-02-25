"""Image processing module for cropping and grayscale conversion."""

import numpy as np
from PIL import Image


def crop_image(image_path, crop_size=256, crop_region="center"):
    """
    Crop image to specified size from a specified region.
    
    Args:
        image_path (str): Path to the input image file
        crop_size (int): Size of the crop region (default: 256)
        crop_region (str): Region to crop from. Options:
                          'center', 'top-center', 'top-left', 'top-right',
                          'bottom-center', 'bottom-left', 'bottom-right',
                          'center-left', 'center-right' (default: 'center')
        
    Returns:
        PIL.Image: Cropped image
    """
    img = Image.open(image_path)
    width, height = img.size
    
    # Ensure crop size doesn't exceed image dimensions
    crop_size = min(crop_size, width, height)
    
    # Calculate crop coordinates based on region
    if crop_region == "center":
        left = (width - crop_size) // 2
        top = (height - crop_size) // 2
    elif crop_region == "top-center":
        left = (width - crop_size) // 2
        top = 0
    elif crop_region == "top-left":
        left = 0
        top = 0
    elif crop_region == "top-right":
        left = width - crop_size
        top = 0
    elif crop_region == "bottom-center":
        left = (width - crop_size) // 2
        top = height - crop_size
    elif crop_region == "bottom-left":
        left = 0
        top = height - crop_size
    elif crop_region == "bottom-right":
        left = width - crop_size
        top = height - crop_size
    elif crop_region == "center-left":
        left = 0
        top = (height - crop_size) // 2
    elif crop_region == "center-right":
        left = width - crop_size
        top = (height - crop_size) // 2
    else:
        raise ValueError(f"Unknown crop region: {crop_region}")
    
    right = left + crop_size
    bottom = top + crop_size
    
    # Crop the image
    cropped_img = img.crop((left, top, right, bottom))
    return cropped_img


def crop_center_256(image_path):
    """
    Crop image to center 256x256 region (backward compatibility).
    
    Args:
        image_path (str): Path to the input image file
        
    Returns:
        PIL.Image: Cropped image (256x256)
    """
    return crop_image(image_path, crop_size=256, crop_region="center")


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


def process_image(image_path, output_path=None, crop_size=256, crop_region="center", apply_crop=False):
    """
    Main function to process image: crop (optional) and convert to grayscale.
    
    Args:
        image_path (str): Path to input image
        output_path (str, optional): Path to save processed image
        crop_size (int): Size of the crop region (default: 256)
        crop_region (str): Region to crop from (default: 'center')
        apply_crop (bool): Whether to apply cropping (default: True)
        
    Returns:
        tuple: (grayscale_image, grayscale_matrix)
    """
    # Crop with specified parameters if enabled
    if apply_crop:
        cropped = crop_image(image_path, crop_size=crop_size, crop_region=crop_region)
    else:
        cropped = Image.open(image_path)
    
    # Convert to grayscale
    grayscale_img = to_grayscale(cropped)
    
    # Convert to matrix
    matrix = image_to_matrix(grayscale_img)
    
    # Save if output path provided
    if output_path:
        grayscale_img.save(output_path)
        print(f"Processed image saved to: {output_path}")
    
    return grayscale_img, matrix
