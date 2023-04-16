import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from ext_busqueda import library


class LibraryWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear los widgets para la pestaña de biblioteca
        layout = QVBoxLayout()
        self.setLayout(layout)


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Crear los widgets para la pestaña de búsqueda
        layout = QVBoxLayout()
        self.input_field = QLineEdit()
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.input_field)

        self.send_button = QPushButton("Buscar manga")
        layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.buscar_manga)

        self.books = []
        self.books_list = QListWidget()
        layout.addWidget(self.books_list)
        self.books_list.clicked.connect(self.add_manga)

        self.setLayout(layout)
    
    def find_manga(self, title):
        for obj in self.books:
            if obj.get('title') == title:
                return obj
        return None


    def add_manga(self):
        item = self.books_list.currentItem()
        if item is not None:
            print("Clicked: ",item.text())
            manga = self.find_manga(item.text())
            print("Origin: ",manga)


    def buscar_manga(self):
        # Obtener el texto del input field y añadirlo a la lista de mensajes
        query = self.input_field.text()
        self.input_field.clear()
        dic = library(query)
        for manga in dic:
            self.books.append(manga)

        # Limitar la lista de mensajes a los últimos 5
        if len(self.books) > 5:
            for i in range(0,5):
                self.books.pop(0)

        # Actualizar la lista de mensajes en la interfaz
        self.books_list.clear()
        for books in self.books:
            manga = QListWidgetItem(books['title'])
            self.books_list.addItem(manga)
        
class ConfigWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Crear los widgets para la pestaña de configuración
        self.config_label = QLabel("Pestaña de configuración")
        layout = QVBoxLayout()
        layout.addWidget(self.config_label)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear un QTabWidget y agregar las pestañas
        tab_widget = QTabWidget()
        tab_widget.addTab(LibraryWidget(), "Biblioteca")
        tab_widget.addTab(SearchWidget(), "Buscar")
        tab_widget.addTab(ConfigWidget(), "Configuración")

        # Agregar el QTabWidget como widget central de la ventana principal
        self.setCentralWidget(tab_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 400)
    window.show()

    sys.exit(app.exec())
