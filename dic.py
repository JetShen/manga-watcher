from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QHBoxLayout, QLabel, QPushButton

class BookWidget(QWidget):
    def __init__(self, title):
        super().__init__()

        # Crear los widgets para el libro
        self.title_label = QLabel(title)
        self.button = QPushButton('Botón')

        # Crear el layout horizontal y agregar los widgets
        layout = QHBoxLayout()
        layout.addWidget(self.title_label)
        layout.addWidget(self.button)
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Crear la lista y agregar algunos libros
        self.books = [{'title': 'Manga 1'}, {'title': 'Manga 2'}, {'title': 'Manga 3'}, {'title': 'Manga 4'}]
        self.books_list = QListWidget()

        for book in self.books:
            book_widget = BookWidget(book['title'])
            list_item = QListWidgetItem()
            list_item.setSizeHint(book_widget.sizeHint())
            self.books_list.addItem(list_item)
            self.books_list.setItemWidget(list_item, book_widget)

        # Crear el layout y agregar la lista
        layout = QVBoxLayout()
        layout.addWidget(self.books_list)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
