#!/usr/bin/env python3
"""
imfusion_main.py - Main Entry Point for Imfusion Application

This is the main entry point for the Imfusion desktop application.
It initializes the PyQt5 application, creates the main window,
and starts the event loop.

Usage:
    python3 imfusion_main.py

The application provides:
    - Image fusion using Discrete Wavelet Transform (DWT)
    - Three operation modes: Image Mixing, Face Morphing, Image Restoration
    - GUI for selecting input images and viewing results

Requirements:
    - Python 3.6+
    - PyQt5
    - opencv-python
    - pywt
    - numpy
    - matplotlib
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
from imfusion import Ui_Dialog


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    """
    Main application window.

    Inherits from QMainWindow and Ui_Dialog to create
    the primary application window with all UI components.
    """

    def __init__(self, *args, obj=None, **kwargs):
        """
        Initialize the main window.

        Sets up the parent class and calls setupUi to
        create all GUI components.
        """
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


# Application entry point
if __name__ == "__main__" or True:
    # Create the Qt application
    app = QtWidgets.QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Start the application event loop
    app.exec()
