"""
fusion_main.py - Core Image Fusion Algorithm

This module implements image fusion using Discrete Wavelet Transform (DWT).
It provides functions to fuse two images by decomposing them into wavelet
coefficients and combining them using various fusion methods.

The fusion algorithm:
1. Loads two input images in grayscale
2. Resizes the second image to match the first
3. Applies 2D DWT to decompose images into frequency components
4. Fuses the wavelet coefficients (approximation and detail)
5. Reconstructs the fused image using inverse DWT
6. Normalizes and saves the output

Example:
    import fusion_main as fuse
    result = fuse.fusion("image1.png", "image2.png")
    print(f"Fused image saved to: {result}")
"""

import pywt
import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image
from PIL import ImageFilter
import cv2


def fuseCoeff(coef1, coef2, method):
    """
    Fuse two sets of wavelet coefficients using the specified method.

    This function combines wavelet coefficients from two images using
    different fusion strategies. The choice of method affects the
    characteristics of the final fused image.

    Args:
        coef1 (numpy.ndarray): Wavelet coefficients from the first image.
        coef2 (numpy.ndarray): Wavelet coefficients from the second image.
        method (str): Fusion method to use. Options:
            - 'mean': Average of both coefficients (balanced fusion)
            - 'min': Minimum value (reduces noise, may lose detail)
            - 'max': Maximum value (preserves edges, may increase noise)

    Returns:
        numpy.ndarray: Fused coefficients, or empty list if invalid method.

    Example:
        >>> fused = fuseCoeff(cA1, cA2, 'mean')
    """
    if method == 'mean':
        coef = (coef1 + coef2) / 2
    elif method == 'min':
        coef = np.minimum(coef1, coef2)
    elif method == 'max':
        coef = np.maximum(coef1, coef2)
    else:
        coef = []

    return coef


def fusion(img1, img2):
    """
    Perform image fusion using Discrete Wavelet Transform (DWT).

    This function takes two input images and fuses them using the DWT
    algorithm. The images are decomposed into approximation and detail
    coefficients, which are then combined using the mean method and
    reconstructed into a single fused image.

    The fusion process:
    1. Load images in grayscale
    2. Resize image 2 to match image 1 dimensions
    3. Apply 2D DWT using Daubechies-5 wavelet
    4. Fuse coefficients: cA (approx), cH (horizontal), cV (vertical), cD (diagonal)
    5. Apply inverse DWT to reconstruct
    6. Normalize pixel values to [0, 255]
    7. Save result as JPEG

    Args:
        img1 (str): File path to the first input image.
        img2 (str): File path to the second input image.

    Returns:
        str: File path to the generated fused image (demo/outXXXX.jpg).

    Note:
        - Both images are converted to grayscale
        - Output is saved in the demo/ directory
        - File name includes a random number (1000-2000)

    Example:
        >>> result_path = fusion("demo/medical1.png", "demo/medical2.png")
        >>> print(f"Fused image saved to: {result_path}")
        Fused image saved to: demo/out1523.jpg
    """
    # Fusion method configuration
    # Options: 'mean', 'min', 'max'
    FUSION_METHOD = 'mean'

    # Load both images in grayscale (0 = grayscale flag)
    I1 = cv2.imread(img1, 0)
    I2 = cv2.imread(img2, 0)

    # Get dimensions of first image and resize second image to match
    # This ensures both images have the same size for coefficient fusion
    x = I1.shape
    invX = x[::-1]  # Reverse dimensions for cv2.resize (width, height)
    I2 = cv2.resize(I2, invX)

    # Apply 2D Discrete Wavelet Transform
    # Using Daubechies-5 wavelet with periodization mode
    wavelet = 'db5'
    cooef1 = pywt.dwt2(I1, wavelet, mode='periodization')
    cooef2 = pywt.dwt2(I2, wavelet, mode='periodization')

    # Unpack wavelet coefficients
    # cA: Approximation coefficients (low-frequency, overall structure)
    # cH: Horizontal detail coefficients (horizontal edges)
    # cV: Vertical detail coefficients (vertical edges)
    # cD: Diagonal detail coefficients (diagonal edges)
    cA1, (cH1, cV1, cD1) = cooef1
    cA2, (cH2, cV2, cD2) = cooef2

    # Fuse all coefficients using mean method
    # This creates a balanced combination of both images
    cA = (cA1 + cA2) / 2  # Fused approximation
    cH = (cH1 + cH2) / 2  # Fused horizontal details
    cV = (cV1 + cV2) / 2  # Fused vertical details
    cD = (cD1 + cD2) / 2  # Fused diagonal details

    # Pack fused coefficients for inverse transform
    finco = cA, (cH, cV, cD)

    # Reconstruct image using inverse DWT
    outImage = pywt.idwt2(finco, wavelet, mode='periodization')

    # Normalize pixel values to [0, 255] range
    # Min-max normalization: (value - min) / (max - min) * 255
    outImage = np.multiply(
        np.divide(outImage - np.min(outImage),
                  (np.max(outImage) - np.min(outImage))),
        255
    )

    # Convert to 8-bit unsigned integer for image saving
    outImage = outImage.astype(np.uint8)

    # Generate unique output filename with random number
    x = random.randint(1000, 2000)
    loc = 'demo/out' + str(x) + '.jpg'

    # Save the fused image
    cv2.imwrite(loc, outImage)

    return loc
