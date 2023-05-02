from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from jsonUtils.json_utils import ReadF, WriteS

class LibraryWidget(QWidget):
    def __init__(self):
        super().__init__()

        #Add refresh button
        botonRefrescar = QPushButton("Refrescar")
        botonRefrescar.setStyleSheet("background-color: red; color: white;")
        botonRefrescar.clicked.connect(self.cLayout)
        layoutBoton = QHBoxLayout()
        layoutBoton.addStretch()
        layoutBoton.addWidget(botonRefrescar)
        layoutBoton.addStretch()

        
        layoutFrontal = QVBoxLayout()
        self.layoutCentral = QGridLayout()

        layoutFrontal.addLayout(layoutBoton)
        layoutFrontal.addLayout(self.layoutCentral)

        self.cLayout()

        self.setLayout(layoutFrontal)

    def selected(self, event, index, library):
        manga = library[index]
        WriteS(manga)

    
    def cLayout(self):

        library = ReadF()
        for manga in library:
            pass
            #add system to update


        for manga in range(len(library)):
            LyManga = QVBoxLayout()#Make the layout for the manga object

            #Add the title to the layout
            title = QLabel(str(library[manga]['title']))
            title.setStyleSheet("background-color: blue; color: white;")
            LyManga.addWidget(title)

            #Add the image to the layout
            pixmap = QPixmap(f"img/{library[manga]['img_path']}")
            img = QLabel()
            img.setStyleSheet("background-color: blue; color: white;")
            img.setPixmap(pixmap)
            img.setScaledContents(True)
            img.setMouseTracking(True)
            img.setCursor(Qt.PointingHandCursor)#change cursor to pointing hand cursor
            #connect the function to the manga object using lambda
            img.mousePressEvent = lambda event, idx=manga: self.selected(event, idx, library)
            LyManga.addWidget(img)

            #Add the chapters to the layout
            chapters = QLabel(f"Chapters: {library[manga]['Chapters']}")
            chapters.setStyleSheet("background-color: blue; color: white;")
            LyManga.addWidget(chapters)

            LyManga.setSpacing(0)

            #add to the grid int(rows) and int(columns) 
            self.layoutCentral.addLayout(LyManga, manga // 2, manga % 2)
        
        return self.layoutCentral

if __name__ == '__main__':
    pass
