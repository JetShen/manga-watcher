from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from jsonUtils.json_utils import ReadS, WriteF, ReadF
import requests

class About_manga(QWidget):
    
    def __init__(self):
        super().__init__()
        

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        self.title = QLabel("Manga Title:")
        layout.addWidget(self.title)

        self.img = QLabel(self)
        layout.addWidget(self.img)

        self.genders = QLabel("Tag, Tag")
        layout.addWidget(self.genders)

        self.chapters = QLabel("Chapters: ")
        layout.addWidget(self.chapters)
        
        self.btn_refresh = QPushButton("Refresh")
        layout.addWidget(self.btn_refresh)
        self.btn_refresh.clicked.connect(self.refresh)

        self.add_btn = QPushButton("Add Manga to Library")
        layout.addWidget(self.add_btn)
        self.add_btn.clicked.connect(self.add_manga)

        self.setLayout(layout)


    
    def refresh(self):
        try:
            manga = ReadS()
            
            #download the img of the manga
            response = requests.get(manga['img_link'], stream=True)
            response.raise_for_status()
            with open('img/'+str(manga['img_path']), "wb") as archivo:
                for chunk in response.iter_content(chunk_size=8192):
                    archivo.write(chunk)

            self.title.setText(f"Manga title: {manga['title']}")

            pixel = QPixmap("img/"+str(manga['img_path']))
            self.img.setPixmap(pixel)
            self.chapters.setText(f"Chapters: {manga['Chapters']}")
            self.genders.setText(f"Genders: {manga['Genders']}")
            self.btn_refresh.setText("Refresh")
            self.add_btn.setText("Add Manga to Library")    
        except Exception as e:
            print(e)
            self.btn_refresh.setText("Error loading")

        
    def add_manga(self):
        try:
            manga = ReadS()
            try:
                library = ReadF()
                library.append(manga)
                WriteF(library)
            except:
                WriteF([manga])
            self.add_btn.setText("manga added")
        except:
            self.add_btn.setText("Error adding manga")


        



