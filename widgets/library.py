from PySide6.QtWidgets import *
from PySide6.QtCore import Qt




class LibraryWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear los widgets para la pestaña de biblioteca
        layout = QVBoxLayout()
        self.setLayout(layout)