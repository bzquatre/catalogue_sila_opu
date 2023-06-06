from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os
class BookWidget(QWidget):
    def __init__(self, title, authors, cover_path, price, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()
        
        # Create QLabel for the book cover
        cover_label = QLabel(self)
        cover_label.setFixedHeight(300)
        cover_label.setScaledContents(True)  # Scale the image to fit the QLabel
        layout.addWidget(cover_label)
        
        # Create QLabel for the book title
        title_label = QLabel(title, self)
        title_label.setWordWrap(True)
        layout.addWidget(title_label)
        
        # Create QLabel for the book authors
        authors_label = QLabel(authors, self)
        layout.addWidget(authors_label)
        
        # Create QLabel for the book price
        price_label = QLabel(f"Price: {price}", self)
        layout.addWidget(price_label)
        
        self.setLayout(layout)
        
        # Load and set the cover image
        
        if os.path.exists(cover_path):
            self.set_cover(cover_path)
        else:
            self.set_cover("images\empty.jpg")
    
    def set_cover(self, cover_path):
        pixmap = QPixmap(cover_path)
        # Get the size of the cover label
        cover_size = self.layout().itemAt(0).widget().size()
        # Scale the pixmap to match the size of the cover label
        scaled_pixmap = pixmap.scaled(cover_size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
        self.layout().itemAt(0).widget().setPixmap(scaled_pixmap)
class BookWidget1(QWidget):
    def __init__(self, title, authors, cover_path, price, parent=None):
        super().__init__(parent)
        
        layout = QVBoxLayout()
        
        # Create QLabel for the book cover
        cover_label = QLabel(self)
        try:
            cover_label.setPixmap(QPixmap(cover_path))  # Assuming cover_path is the path to the book cover image
        except:
            cover_label.setPixmap(QPixmap("images\empty.jpg"))
        
        layout.addWidget(cover_label)
        
        # Create QLabel for the book title
        title_label = QLabel(title, self)
        layout.addWidget(title_label)
        
        # Create QLabel for the book authors
        authors_label = QLabel(authors, self)
        layout.addWidget(authors_label)
        
        # Create QLabel for the book price
        price_label = QLabel(f"Price: {price}", self)
        layout.addWidget(price_label)
        
        self.setLayout(layout)