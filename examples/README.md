# Examples

This folder contains sample images and output files from running the image processor.

## Sample Images

| File | Description |
|------|-------------|
| `sample_image_001.jpg` | Example input image for processing |
| `sample_image_002.jpg` | Example input image for processing |

## Sample Output Files

### From sample_image_001.jpg

**Command:**
```bash
python ../process_image.py "examples/sample_image_001.jpg" -o "examples/output_grayscale.jpg" -c "examples/grayscale_matrix.csv"
```

**Generated Files:**
- `output_grayscale.jpg` - The processed grayscale image (256×256 pixels)
- `grayscale_matrix.csv` - The grayscale values in spreadsheet format
- `grayscale_matrix.npy` - The matrix in NumPy binary format

**Matrix Statistics:**
- Size: 256×256 pixels
- Data type: uint8 (values 0-255)
- Mean intensity: 95.72
- Standard deviation: 81.70
- Min value: 0
- Max value: 255

## How to Create Your Own Examples

1. Add your image file to this folder:
   ```bash
   cp your_image.jpg examples/
   ```

2. Run the processor:
   ```bash
   python process_image.py "examples/your_image.jpg" -o "examples/your_output.jpg" -c "examples/your_data.csv"
   ```

3. Update this README with your example details!

## Using Examples in Development

These example files are useful for:
- **Testing** - Verify the processor works correctly
- **Documentation** - Show sample input and output
- **Learning** - See what the output looks like
- **Benchmarking** - Test processing time and output quality

