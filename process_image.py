"""Script to process the image and generate grayscale matrix."""

import sys
import argparse
import numpy as np
from src.image_processor import process_image


def main():
    parser = argparse.ArgumentParser(
        description='Process image: crop and convert to grayscale'
    )
    parser.add_argument(
        'image_path',
        help='Path to the input image file'
    )
    parser.add_argument(
        '-o', '--output',
        default='output_grayscale.jpg',
        help='Path to save processed image (default: output_grayscale.jpg)'
    )
    parser.add_argument(
        '-c', '--csv',
        default='grayscale_matrix.csv',
        help='Path to save grayscale matrix as CSV (default: grayscale_matrix.csv)'
    )
    parser.add_argument(
        '-s', '--size',
        type=int,
        default=256,
        help='Crop size in pixels (default: 256)'
    )
    parser.add_argument(
        '-r', '--region',
        default='center',
        choices=[
            'center', 'top-center', 'top-left', 'top-right',
            'bottom-center', 'bottom-left', 'bottom-right',
            'center-left', 'center-right'
        ],
        help='Crop region (default: center)'
    )
    
    args = parser.parse_args()
    
    # Process the image
    image_path = args.image_path
    output_path = args.output
    csv_path = args.csv
    crop_size = args.size
    crop_region = args.region

    try:
        grayscale_img, matrix = process_image(
            image_path, 
            output_path,
            crop_size=crop_size,
            crop_region=crop_region
        )
        
        print("=" * 60)
        print("IMAGE PROCESSING COMPLETE")
        print("=" * 60)
        print(f"\nImage successfully processed:")
        print(f"  - Crop size: {crop_size}x{crop_size} pixels")
        print(f"  - Crop region: {crop_region}")
        print(f"  - Converted to: Grayscale")
        print(f"  - Output saved to: {output_path}")
        
        print(f"\nGrayscale Matrix Shape: {matrix.shape}")
        print(f"Data Type: {matrix.dtype}")
        print(f"Value Range: [{matrix.min()}, {matrix.max()}]")
        
        print(f"\nGrayscale Matrix (first 10x10):")
        print(matrix[:10, :10])
        
        print(f"\nMatrix Statistics:")
        print(f"  - Mean: {matrix.mean():.2f}")
        print(f"  - Std Dev: {matrix.std():.2f}")
        print(f"  - Min: {matrix.min()}")
        print(f"  - Max: {matrix.max()}")
        
        # Save matrix to NPY file for later use
        np.save("grayscale_matrix.npy", matrix)
        print(f"\nMatrix saved to: grayscale_matrix.npy")
        
        # Save matrix to CSV file for readability
        np.savetxt(csv_path, matrix, delimiter=',', fmt='%d')
        print(f"Matrix saved to: {csv_path} (readable CSV format)")
        
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
