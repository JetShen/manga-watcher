from PySide6.QtWidgets import *
from PySide6.QtCore import Qt


class ConfigWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear los widgets para la pestaña de configuración
        self.config_label = QLabel("Pestaña de configuración")
        layout = QVBoxLayout()
        layout.addWidget(self.config_label)
        self.setLayout(layout)