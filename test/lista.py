import sys
from PySide6.QtWidgets import *
from ext_busqueda import library

class ChatWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.messages = []

        # Crear los widgets
        self.input_field = QLineEdit()
        self.send_button = QPushButton("Buscar")
        self.message_list = QListWidget()

        # Crear el layout y añadir los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.message_list)
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        # Conectar los eventos a los métodos
        self.send_button.clicked.connect(self.send_message)
        self.input_field.returnPressed.connect(self.send_message)

    def send_message(self):
        # Obtener el texto del input field y añadirlo a la lista de mensajes
        message = self.input_field.text()
        self.input_field.clear()
        dic = library(message)
        for manga in dic:
            self.messages.append(manga)

        # Limitar la lista de mensajes a los últimos 5
        if len(self.messages) > 5:
            for i in range(0,5):
                self.messages.pop(0)

        # Actualizar la lista de mensajes en la interfaz
        self.message_list.clear()
        for message in self.messages:
            item = QListWidgetItem(message['title'])
            self.message_list.addItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = ChatWidget()
    widget.show()

    sys.exit(app.exec())
