import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from widgets.search import SearchWidget
from widgets.manga import About_manga
from widgets.library import LibraryWidget
from widgets.config import ConfigWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear un QTabWidget y agregar las pestañas
        tab_widget = QTabWidget()
        tab_widget.addTab(LibraryWidget(), "Library")
        tab_widget.addTab(SearchWidget(), "Search")
        tab_widget.addTab(About_manga(), "Manga")
        tab_widget.addTab(ConfigWidget(), "Config")

        # Agregar el QTabWidget como widget central de la ventana principal
        self.setCentralWidget(tab_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 620)
    window.show()

    sys.exit(app.exec())
