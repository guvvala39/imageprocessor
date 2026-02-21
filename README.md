# 📷 Image Processor

A beginner-friendly Python tool that crops images to 256×256 pixels and converts them to grayscale, then exports the data as a matrix (CSV and binary formats).

---

## 🎯 What Does This Project Do?

This tool takes an image file and:
1. **Crops** it to the top-center 256×256 pixel region
2. **Converts** it to grayscale (black & white)
3. **Exports** the data as:
   - A grayscale image (JPG)
   - A CSV file (human-readable spreadsheet)
   - A NumPy binary file (for Python analysis)

---

## ✅ Prerequisites

Before you start, make sure you have:
- **Python 3.8 or higher** ([Download Python](https://www.python.org/downloads/))
- **A terminal/command prompt** on your computer

Check if Python is installed:
```bash
python3 --version
```

---

## 🚀 Setup (First Time Only)

### Step 1: Navigate to the Project

```bash
cd /Users/abhinay/VsCodeProjects/imageprocessor
```

### Step 2: Create a Virtual Environment

A virtual environment is a isolated space where we install Python packages without affecting your system.

```bash
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You should see `(venv)` appear at the start of your terminal line.

### Step 4: Install Dependencies

This installs the libraries (Pillow for images, NumPy for data):

```bash
pip install -r requirements.txt
```

---

## 💻 How to Use

### Basic Usage

Process an image with default settings:

```bash
python process_image.py "path/to/your/image.jpg"
```

**This creates:**
- `output_grayscale.jpg` - The processed image
- `grayscale_matrix.csv` - The data in spreadsheet format
- `grayscale_matrix.npy` - The data in binary format (for Python)

### Custom Output Filenames

Save the processed image with a specific name:

```bash
python process_image.py "image.jpg" -o my_result.jpg
```

Save the matrix with a specific CSV name:

```bash
python process_image.py "image.jpg" -c my_data.csv
```

### Using Both Custom Names

```bash
python process_image.py "image.jpg" -o result.jpg -c data.csv
```

### View Available Options

```bash
python process_image.py --help
```

---

## 📚 Examples

### Example 1: Process a WhatsApp Photo

```bash
python process_image.py "WhatsApp Image 2026-02-21 at 08.15.22.jpeg"
```

Creates: `output_grayscale.jpg`, `grayscale_matrix.csv`

### Example 2: Process with Custom Names

```bash
python process_image.py "family_photo.jpg" -o family_gray.jpg -c family_data.csv
```

Creates: `family_gray.jpg`, `family_data.csv`

### Example 3: Process Multiple Images

```bash
python process_image.py "photo1.jpg" -o photo1_gray.jpg -c photo1_data.csv
python process_image.py "photo2.jpg" -o photo2_gray.jpg -c photo2_data.csv
```

---

## 📁 Project Structure

```
imageprocessor/
├── src/
│   ├── __init__.py
│   └── image_processor.py       # Core image processing functions
├── tests/
│   └── __init__.py              # For future tests
├── examples/                    # Sample outputs from processed images
│   ├── README.md
│   ├── output_grayscale.jpg
│   ├── grayscale_matrix.csv
│   └── grayscale_matrix.npy
├── venv/                        # Virtual environment (auto-created)
├── process_image.py             # Main script you run
├── requirements.txt             # List of required packages
├── .gitignore                   # Files to ignore in git
└── README.md                    # This file
```

### What Each File Does

| File/Folder | Purpose |
|------|---------|
| `process_image.py` | The main script - run this to process images |
| `src/image_processor.py` | The image processing functions (used by process_image.py) |
| `requirements.txt` | List of Python packages needed |
| `examples/` | Sample output files from running the processor |
| `venv/` | Virtual environment folder (created during setup) |

### Output Files (Created When You Run the Script)

When you run the script, it creates:
- `output_grayscale.jpg` (or custom name) - The processed grayscale image
- `grayscale_matrix.csv` (or custom name) - Matrix data in spreadsheet format
- `grayscale_matrix.npy` - Matrix data in binary format (for Python)

**Tip:** Save these files to the `examples/` folder to keep your repo organized!

---

## 📊 Understanding the CSV Output

When you export to CSV, each cell contains a number from **0 to 255**:
- **0** = Black
- **128** = Medium gray
- **255** = White

Example (first 5×5 pixels):
```
255,254,253,252,251
250,249,248,247,246
245,244,243,242,241
240,239,238,237,236
235,234,233,232,231
```

You can open this in:
- **Excel**
- **Google Sheets**
- **Any text editor**

See `examples/grayscale_matrix.csv` for a real example!

---

## 🔧 How It Works (Simple Explanation)

### Step 1: Crop
The image is cropped to the top-center region:
- Original image (e.g., 1000×800 pixels)
- Cropped to (256×256 pixels starting from the top)

### Step 2: Convert to Grayscale
Color pixels → Gray pixels:
- Red, Green, Blue values → Single gray value (0-255)

### Step 3: Export
The 256×256 matrix is saved in multiple formats:
- **JPG**: Visual image file
- **CSV**: Spreadsheet (easy to read/analyze)
- **NPY**: Binary (efficient for Python)

---

## 🐛 Troubleshooting

### Problem: "Command not found: python3"
**Solution:** Install Python from [python.org](https://www.python.org/downloads/)

### Problem: "No module named 'PIL'" or "No module named 'numpy'"
**Solution:** Activate the virtual environment and reinstall packages:
```bash
source venv/bin/activate  # or: venv\Scripts\activate (Windows)
pip install -r requirements.txt
```

### Problem: "No such file or directory: image.jpg"
**Solution:** Make sure the image file exists in the same folder as `process_image.py`, or provide the full path:
```bash
python process_image.py "/path/to/image.jpg"
```

### Problem: "permission denied"
**Solution:** On macOS/Linux, you may need to add execute permission:
```bash
chmod +x process_image.py
```

---

## 📖 Next Steps for Beginners

1. **Run your first image:**
   ```bash
   python process_image.py "WhatsApp Image 2026-02-21 at 08.15.22.jpeg"
   ```

2. **Open the CSV file** in Excel or Google Sheets to see the data

3. **Look at `src/image_processor.py`** to understand the code

4. **Modify the code** in `src/image_processor.py` to:
   - Change crop size (e.g., 512×512 instead of 256×256)
   - Crop from different position (left, center, bottom)
   - Add color channels instead of grayscale

---

## 💡 Tips

- **Batch processing:** Run the script multiple times with different images
- **File naming:** Use descriptive names like `photo_processed_2026.csv`
- **Analyze data:** Use Python/Excel to analyze the matrix values
- **Images supported:** JPG, PNG, BMP, GIF, TIFF, and more

---

## 📞 Getting Help

- Read the `--help` option: `python process_image.py --help`
- Check error messages carefully - they usually tell you what's wrong
- Make sure the image file path is correct
- See `examples/README.md` for sample runs and outputs

---

## 📜 License

Open source - feel free to use and modify!

---

**Happy image processing! 🎉**
