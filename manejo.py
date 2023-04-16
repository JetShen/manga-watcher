import sys
from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear un label
        self.label = QLabel("Ejemplo de manejo de la zona de un widget", self)

        # Obtener la zona del label
        label_rect = self.label.geometry()
        print("Zona del label antes de cambiar su tamaño:", label_rect.x(), label_rect.y(), label_rect.width(), label_rect.height())

        # Cambiar el tamaño del label
        self.label.resize(200, 100)

        # Obtener la nueva zona del label
        label_rect = self.label.geometry()
        print("Zona del label después de cambiar su tamaño:", label_rect.x(), label_rect.y(), label_rect.width(), label_rect.height())

        # Crear un layout vertical y agregar el label
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    window.resize(400, 400)
    window.show()
    sys.exit(app.exec())
