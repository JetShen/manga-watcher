from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from webScraping.ext_busqueda import library
from webScraping.ext_page import Manga
from jsonUtils.json_utils import WriteS


class SearchWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.input_field = QLineEdit()
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.input_field)

        self.send_button = QPushButton("Search Manga")
        layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.search_manga)

        self.books = []
        self.books_list = QListWidget()
        layout.addWidget(self.books_list)
        self.books_list.clicked.connect(self.add_manga)

        self.setLayout(layout)
    
    #help the funcion add_manga to find the object manga that the user selected then the function return the object to add_manga
    def find_manga(self, title):
        for obj in self.books:
            if obj.get('title') == title:
                return obj
        return None

    #add_manga add the manga to the json ./json/fav.json
    def add_manga(self):
        item = self.books_list.currentItem()
        if item is not None:
            manga = self.find_manga(item.text())
            new_manga = Manga(manga['link'])
            WriteS(new_manga)


    #search_manga look for the query the user is looking for in the web mangaupdates 
    def search_manga(self):
        query = self.input_field.text()
        self.input_field.clear()
        dic = library(query)
        for manga in dic:
            self.books.append(manga)

        #limit the number of manga to be returned to the user in 5
        if len(self.books) > 5:
            for i in range(0,5):
                self.books.pop(0)

        #add the list to books_list and refresh the display list
        self.books_list.clear()
        for books in self.books:
            manga = QListWidgetItem(books['title'])
            self.books_list.addItem(manga)