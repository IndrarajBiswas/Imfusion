"""
imfusion.py - GUI Components for Imfusion Application

This module defines the PyQt5 user interface for the Imfusion desktop application.
It provides the main dialog window with controls for selecting operation modes,
loading input images, and generating fused images.

Classes:
    Ui_Dialog: Main UI class that sets up and manages all GUI components.

The GUI includes:
    - Welcome text and information
    - Radio buttons for operation mode selection
    - Insert button for loading images
    - Generate Image button to perform fusion
    - Preview panels for input and output images
    - Exit button to close the application

Usage:
    This module is imported by imfusion_main.py which creates the main window.
"""

import sys
import os
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QInputDialog,
    QLineEdit, QFileDialog, QHBoxLayout, QLabel, QTextEdit
)
from PyQt5.QtGui import QIcon, QPixmap
import webbrowser
import fusion_main as fuse
import cv2


class Ui_Dialog(object):
    """
    Main UI class for the Imfusion application.

    This class creates and manages all GUI components including:
    - Text browsers for information display
    - Radio buttons for operation selection
    - Buttons for image insertion and generation
    - Labels for image preview

    Attributes:
        fileName1 (str): Path to the first selected image.
        fileName2 (str): Path to the second selected image.
        generatedImage (str): Path to the generated fused image.
    """

    def setupUi(self, Dialog):
        """
        Initialize and set up all UI components.

        This method creates the entire GUI layout including:
        - Main window configuration
        - Text browsers for welcome message and status
        - Radio buttons for operation modes
        - Action buttons (Insert, Generate, Exit)
        - Image preview labels

        Args:
            Dialog: The parent dialog/window widget.
        """
        # Configure main dialog window
        Dialog.setObjectName("Dialog")
        Dialog.resize(958, 775)

        # Initialize file path storage
        self.fileName1 = ''
        self.fileName2 = ''

        # Create main vertical layout container
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 426, 354))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        # Set up vertical layout with padding and spacing
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        # Welcome message text browser
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        # Radio button 1: Image Mixing
        self.radioButton1 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton1.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton1)

        # Radio button 2: Face Morphing
        self.radioButton2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton2.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton2)

        # Radio button 3: Image Restoration
        self.radioButton3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton3)

        # Status text browser (shows selected operation)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser_2.setEnabled(True)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayout.addWidget(self.textBrowser_2)

        # Horizontal layout for action buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 6, 10, 6)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Insert button - for selecting input images
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)

        # Generate Image button - triggers fusion algorithm
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)

        # Exit button - closes the application
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Label for generated image title
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(460, 20, 151, 18))
        self.label.setObjectName("label")

        # Generated image preview panel (center)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(490, 60, 371, 271))
        self.label_2.setObjectName("label_2")

        # First input image preview panel (bottom left)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 480, 371, 271))
        self.label_3.setObjectName("label_3")

        # Label for Image 1 title
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 440, 151, 18))
        self.label_4.setObjectName("label_4")

        # Second input image preview panel (bottom right)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(530, 470, 371, 271))
        self.label_5.setObjectName("label_5")

        # Label for Image 2 title
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(500, 440, 151, 18))
        self.label_6.setObjectName("label_6")

        # Initialize generated image path storage
        self.generatedImage = ''

        # Set text content for all UI elements
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect signals to slots
        self.initUI()

    def initUI(self):
        """
        Initialize UI event connections.

        Connects button clicks and radio button selections to their
        respective handler methods.
        """
        # Connect Exit button
        self.pushButton.clicked.connect(self.on_click)

        # Connect Generate Image button
        self.pushButton_3.clicked.connect(self.openGenImage)

        # Connect radio buttons for operation selection
        self.radioButton1.clicked.connect(self.options_1)
        self.radioButton2.clicked.connect(self.options_2)
        self.radioButton3.clicked.connect(self.options_3)

        self.show()

    def options_1(self):
        """
        Handle Image Mixing option selection.

        Updates status text and connects Insert button to image dialogs.
        """
        self.textBrowser_2.setText("You selected Image Mixing")
        self.pushButton_2.clicked.connect(self.openFileNameDialog_1)
        self.pushButton_2.clicked.connect(self.openFileNameDialog_2)

    def options_2(self):
        """
        Handle Face Morphing option selection.

        Updates status text and connects Insert button to image dialogs.
        """
        self.textBrowser_2.setText("You selected Face Morphing ")
        self.pushButton_2.clicked.connect(self.openFileNameDialog_1)
        self.pushButton_2.clicked.connect(self.openFileNameDialog_2)

    def options_3(self):
        """
        Handle Image Restoration option selection.

        Updates status text and connects Insert button to image dialogs.
        """
        self.textBrowser_2.setText("You selected Image restoration")
        self.pushButton_2.clicked.connect(self.openFileNameDialog_1)
        self.pushButton_2.clicked.connect(self.openFileNameDialog_2)

    def showImg(self, img):
        """
        Display an image in a popup window.

        Creates a new window with the specified image displayed.

        Args:
            img (str): Path to the image file to display.
        """
        hbox = QHBoxLayout(self)
        pixmap = QPixmap(img)

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(300, 200)
        self.setWindowTitle('Image with PyQt')
        self.show()

    @pyqtSlot()
    def openFileNameDialog_1(self):
        """
        Open file dialog to select the first input image.

        Opens a file browser dialog for the user to select an image.
        The selected image is displayed in the first preview panel.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName1, _ = QFileDialog.getOpenFileName(
            self,
            "Select file to insert",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options
        )
        if self.fileName1:
            print(self.fileName1)
            self.label.setText("Attached image: " + self.fileName1)

            # Load and scale image for preview
            pixmap = QPixmap(self.fileName1)
            pixmap2 = pixmap.scaledToWidth(100)
            pixmap3 = pixmap.scaledToHeight(400)
            self.label_3.setPixmap(pixmap3)

            # Show in popup window
            self.showImg(self.fileName1)

    @pyqtSlot()
    def openFileNameDialog_2(self):
        """
        Open file dialog to select the second input image.

        Opens a file browser dialog for the user to select an image.
        The selected image is displayed in the second preview panel.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName2, _ = QFileDialog.getOpenFileName(
            self,
            "Select file to insert",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options
        )
        if self.fileName2:
            print(self.fileName2)
            self.label.setText("Attached image: " + self.fileName2)

            # Load and scale image for preview
            pixmap = QPixmap(self.fileName2)
            pixmap2 = pixmap.scaledToWidth(100)
            pixmap3 = pixmap.scaledToHeight(400)
            self.label_5.setPixmap(pixmap3)

            # Show in popup window
            self.showImg(self.fileName2)

    @pyqtSlot()
    def openFileNameDialog_3(self):
        """
        Alternative file dialog method (unused in current implementation).

        This is a duplicate of openFileNameDialog_1 for potential future use.
        """
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName1, _ = QFileDialog.getOpenFileName(
            self,
            "Select file to insert",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options
        )
        if self.fileName1:
            print(self.fileName1)
            self.label.setText("Attached image: " + self.fileName1)

            # Load and scale image for preview
            pixmap = QPixmap(self.fileName1)
            pixmap2 = pixmap.scaledToWidth(100)
            pixmap3 = pixmap.scaledToHeight(400)
            self.label_3.setPixmap(pixmap3)

            # Show in popup window
            self.showImg(self.fileName1)

    @pyqtSlot()
    def openGenImage(self):
        """
        Generate the fused image from the two selected input images.

        Calls the fusion algorithm with both selected images and displays
        the result in the generated image preview panel.
        """
        # Perform image fusion
        self.generatedImage = fuse.fusion(self.fileName1, self.fileName2)
        print(self.generatedImage)

        # Load and scale fused image for preview
        pixmap = QPixmap(self.generatedImage)
        pixmap2 = pixmap.scaledToWidth(100)
        pixmap3 = pixmap.scaledToHeight(400)
        self.label_2.setPixmap(pixmap3)

        # Show in popup window
        self.showImg(self.generatedImage)

    @pyqtSlot()
    def on_click(self):
        """
        Handle Exit button click.

        Closes the application.
        """
        sys.exit()

    def retranslateUi(self, Dialog):
        """
        Set text content for all UI elements.

        This method sets the display text for all labels, buttons,
        and text browsers in the interface.

        Args:
            Dialog: The parent dialog widget.
        """
        _translate = QtCore.QCoreApplication.translate

        # Window title
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        # Welcome message HTML content
        self.textBrowser.setHtml(_translate("Dialog",
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" />"
            "<style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'Ubuntu Medium Italic'; "
            "font-size:11pt; font-weight:400; font-style:normal;\">\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\"><span style=\" font-size:14pt;\">"
            "Welcome to Imfusion</span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\"><span style=\" font-size:10pt;\">"
            "An Open Source Imaging client of </span></p>\n"
            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
            "text-indent:0px;\"><span style=\" font-size:10pt;\">"
            "pyImageFusion library</span></p></body></html>"))

        # Radio button labels
        self.radioButton1.setText(_translate("Dialog", "Image Mixing"))
        self.radioButton2.setText(_translate("Dialog", "Face Morphing"))
        self.radioButton3.setText(_translate("Dialog", "Image Restoration"))

        # Button labels
        self.pushButton_2.setText(_translate("Dialog", "Insert"))
        self.pushButton_3.setText(_translate("Dialog", "Generate Image"))
        self.pushButton.setText(_translate("Dialog", "Exit"))

        # Image panel labels
        self.label.setText(_translate("Dialog", "Generated Image: "))
        self.label_2.setText(_translate("Dialog", "                               No Image"))
        self.label_3.setText(_translate("Dialog", "                               No Image"))
        self.label_4.setText(_translate("Dialog", "Image 1: "))
        self.label_5.setText(_translate("Dialog", "                               No Image"))
        self.label_6.setText(_translate("Dialog", "Image 2: "))
