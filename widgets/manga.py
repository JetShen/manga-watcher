from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class About_manga(QWidget):
    def __init__(self):
        super().__init__()
        #about the manga selected
        self.manga_label = QLabel("Mnaga")
        layout = QVBoxLayout()
        layout.addWidget(self.manga_label)
        self.setLayout(layout)