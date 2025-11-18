# Imfusion

**An Open Source Image Fusion Desktop Application using Discrete Wavelet Transform (DWT)**

Imfusion is a Python-based desktop application that combines multiple images of the same scene to create a higher-quality, more detailed output by merging the best features from each source image.

---

## Table of Contents

- [Features](#features)
- [Use Cases](#use-cases)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technical Details](#technical-details)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

---

## Features

- **Three Operation Modes**: Image Mixing, Face Morphing, and Image Restoration
- **DWT-Based Fusion**: Uses Discrete Wavelet Transform for high-quality image fusion
- **User-Friendly GUI**: Built with PyQt5 for an intuitive desktop experience
- **Real-Time Preview**: See both input images and the fused result instantly
- **Auto-Save**: Automatically saves fused images to the `demo/` folder
- **Sample Images**: Includes demo images for immediate testing

---

## Use Cases

### Medical Imaging
Combine CT scans (bone structure) with MRI scans (soft tissues) to create comprehensive diagnostic images.

<table>
<tr>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/medical1.png" /><br /><center><b>CT Scan</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/medical2.png" /><br /><center><b>MRI Scan</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/out1956.jpg" /><br /><center><b>Fused Image</b></center></td>
</tr>
</table>

### Image Restoration
Fix faulty or incomplete images by combining multiple captures of the same scene.

### Image Mixing
Blend two different images to create artistic compositions.

### Face Morphing
Create smooth transitions between two face images.

---

## How It Works

### What is Image Fusion?

Image fusion combines information from two or more images of the same scene to generate a more detailed composite image than any individual source. This technique is widely used in:

- Medical imaging (combining CT and MRI scans)
- Remote sensing and satellite imagery
- Surveillance and security systems
- Photography and digital art

### Discrete Wavelet Transform (DWT)

The application uses DWT to decompose images into frequency components, allowing for intelligent fusion of image details.

<table>
<tr>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/fusionAlgo.png" /><br /><center><b>Fusion Workflow</b></center></td>
</tr>
</table>

### Algorithm Steps

1. **Load Images**: Read both input images in grayscale
2. **Resize**: Adjust second image to match the first image's dimensions
3. **Apply DWT**: Decompose each image using 2D Discrete Wavelet Transform (db5 wavelet)
   - Extract approximation coefficients (cA) - low-frequency content
   - Extract horizontal detail coefficients (cH)
   - Extract vertical detail coefficients (cV)
   - Extract diagonal detail coefficients (cD)
4. **Fuse Coefficients**: Combine coefficients using the mean method
   ```
   cA_fused = (cA1 + cA2) / 2
   cH_fused = (cH1 + cH2) / 2
   cV_fused = (cV1 + cV2) / 2
   cD_fused = (cD1 + cD2) / 2
   ```
5. **Inverse DWT**: Reconstruct the fused image from combined coefficients
6. **Normalize**: Scale pixel values to [0, 255] range
7. **Save**: Export the result as a JPEG file

---

## Screenshots

### Desktop Application

<table>
<tr>
    <td><img height="400" width="500" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/app.png" /><br /><center><b>Main Application Window</b></center></td>
</tr>
</table>

### Image Restoration Example

<table>
<tr>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/s2.png" /><br /><center><b>Faulty Image 1</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/s1.png" /><br /><center><b>Faulty Image 2</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/Screenshot%20from%202020-12-21%2002-23-39.png" /><br /><center><b>Restored Image</b></center></td>
</tr>
</table>

### Image Mixing Example

<table>
<tr>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/person1.png" /><br /><center><b>Image 1</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/person2.png" /><br /><center><b>Image 2</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/Screenshot%20from%202020-12-21%2002-15-37.png" /><br /><center><b>Mixed Image</b></center></td>
</tr>
</table>

### Face Morphing Example

<table>
<tr>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/Screenshot%20from%202020-12-22%2015-13-02.png" /><br /><center><b>Face 1</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/Screenshot%20from%202020-12-22%2015-13-10.png" /><br /><center><b>Face 2</b></center></td>
    <td><img height="250" src="https://github.com/robustTechie/Imfusion/blob/main/screenshots/out1371.jpg" /><br /><center><b>Morphed Face</b></center></td>
</tr>
</table>

---

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Display server (X11 on Linux, or native display on Windows/macOS)

### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/robustTechie/Imfusion.git
   cd Imfusion
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

### Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| PyQt5 | Latest | GUI framework |
| pywt | 1.1.1 | Discrete Wavelet Transform |
| numpy | 1.18.5 | Numerical computing |
| opencv-python | 4.3.0.36 | Image I/O and processing |
| matplotlib | 3.3.3 | Image visualization |

---

## Usage

### Running the Application

```bash
python3 imfusion_main.py
```

### Step-by-Step Guide

1. **Launch the application**
   - Run the command above to open the GUI window

2. **Select an operation mode**
   - Choose one of the three radio buttons:
     - **Image Mixing**: Blend two images together
     - **Face Morphing**: Morph between two faces
     - **Image Restoration**: Restore a faulty image using another capture

3. **Insert input images**
   - Click the **Insert** button to select the first image
   - Click **Insert** again to select the second image
   - Both images will appear in the preview panels

4. **Generate the fused image**
   - Click the **Generate Image** button
   - The fused result will display in the center panel
   - A preview window will also open

5. **View results**
   - The output is automatically saved to `demo/outXXXX.jpg`
   - Click **Exit** to close the application

### Testing with Demo Images

The `demo/` folder contains sample image pairs for testing:

| Image Pair | Description |
|------------|-------------|
| medical1.png, medical2.png | CT and MRI scans |
| face1.png, face2.png | Face images for morphing |
| landscape1.png, landscape2.png | Landscape scenes |
| book1.jpg, book2.jpg | Book images |
| clock1.jpg, clock2.jpg | Clock images |
| dol1.png, dol2.png | Object images |
| lab1.jpg, lab2.jpg | Laboratory images |

---

## Project Structure

```
Imfusion/
├── imfusion_main.py      # Application entry point
├── imfusion.py           # PyQt5 GUI components and event handlers
├── fusion_main.py        # Core DWT fusion algorithm
├── requirements.txt      # Python dependencies
├── README.md             # This documentation
├── demo/                 # Sample images and outputs
│   ├── medical1.png      # Sample CT scan
│   ├── medical2.png      # Sample MRI scan
│   ├── face1.png         # Sample face 1
│   ├── face2.png         # Sample face 2
│   ├── out*.jpg          # Generated fused images
│   └── ...
└── screenshots/          # Application screenshots
    ├── app.png           # Main window screenshot
    ├── fusionAlgo.png    # Algorithm diagram
    └── ...
```

### File Descriptions

| File | Lines | Description |
|------|-------|-------------|
| `imfusion_main.py` | 17 | Entry point that initializes and launches the PyQt5 application |
| `imfusion.py` | 209 | Defines the `Ui_Dialog` class with all GUI components and event handlers |
| `fusion_main.py` | 63 | Contains the core fusion algorithm using DWT |
| `requirements.txt` | 5 | Lists all Python package dependencies |

---

## Technical Details

### Wavelet Transform Parameters

- **Wavelet Family**: Daubechies 5 (`db5`)
- **Mode**: Periodization
- **Transform**: 2D DWT using `pywt.dwt2()` and `pywt.idwt2()`

### Image Processing

- **Input Formats**: Any format supported by OpenCV (jpg, png, bmp, etc.)
- **Color Space**: Images are converted to grayscale for processing
- **Output Format**: JPEG
- **Output Naming**: `demo/outXXXX.jpg` where XXXX is a random number (1000-2000)

### Fusion Methods

The `fuseCoeff()` function supports three fusion methods:

| Method | Description | Formula |
|--------|-------------|---------|
| `mean` | Average of coefficients (default) | `(coef1 + coef2) / 2` |
| `min` | Minimum of coefficients | `min(coef1, coef2)` |
| `max` | Maximum of coefficients | `max(coef1, coef2)` |

---

## API Reference

### fusion_main.py

#### `fuseCoeff(coef1, coef2, method)`

Fuses wavelet coefficients using the specified method.

**Parameters:**
- `coef1` (ndarray): Wavelet coefficients from first image
- `coef2` (ndarray): Wavelet coefficients from second image
- `method` (str): Fusion method - 'mean', 'min', or 'max'

**Returns:**
- `ndarray`: Fused coefficients

#### `fusion(img1, img2)`

Main fusion function that processes two images and returns the fused result.

**Parameters:**
- `img1` (str): Path to the first input image
- `img2` (str): Path to the second input image

**Returns:**
- `str`: Path to the generated fused image

**Example:**
```python
import fusion_main as fuse

result_path = fuse.fusion("demo/medical1.png", "demo/medical2.png")
print(f"Fused image saved to: {result_path}")
```

### imfusion.py

#### `class Ui_Dialog`

Main GUI class that handles the application interface.

**Key Methods:**
- `setupUi(Dialog)`: Initialize all GUI components
- `openFileNameDialog_1()`: Open file dialog for first image
- `openFileNameDialog_2()`: Open file dialog for second image
- `openGenImage()`: Generate the fused image
- `on_click()`: Exit the application

---

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test your changes**
5. **Commit your changes**
   ```bash
   git commit -m "Add: description of your feature"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

### Code Style

- Follow PEP 8 guidelines for Python code
- Add docstrings to new functions
- Include comments for complex logic

### Areas for Contribution

- Implement additional fusion algorithms (DCT, PCA)
- Add support for color image fusion
- Improve GUI design and responsiveness
- Add batch processing capabilities
- Write unit tests

---

## Roadmap

### Planned Features

- [ ] **Multiple Algorithm Support**: Add DCT (Discrete Cosine Transform) and PCA (Principal Component Analysis)
- [ ] **Color Image Fusion**: Support for RGB image processing
- [ ] **Batch Processing**: Process multiple image pairs at once
- [ ] **Custom Fusion Parameters**: Allow users to adjust wavelet type and fusion method
- [ ] **Image Format Options**: Support more output formats and quality settings
- [ ] **Undo/Redo**: Add operation history

---

## Troubleshooting

### Common Issues

**"No module named 'PyQt5'"**
```bash
pip3 install PyQt5
```

**"Cannot connect to X server"** (Linux)
- Ensure you have a display server running
- Try: `export DISPLAY=:0`

**"Image not loading"**
- Check if the image path contains special characters
- Ensure the image format is supported by OpenCV

---

## License

This project is open source and available under the MIT License.

---

## Acknowledgments

- [PyWavelets](https://pywavelets.readthedocs.io/) - Wavelet transform library
- [PyQt5](https://www.riverbankcomputing.com/software/pyqt/) - GUI framework
- [OpenCV](https://opencv.org/) - Computer vision library

---

## Contact

For questions, issues, or suggestions, please open an issue on GitHub.

**Repository**: [https://github.com/robustTechie/Imfusion](https://github.com/robustTechie/Imfusion)
