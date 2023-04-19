from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from jsonUtils.json_utils import ReadS

class About_manga(QWidget):
    def __init__(self):
        super().__init__()
        #about the manga selected
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        try:
            self.manga = ReadS()
            
            
            title = "Title: " + self.manga['title']
            self.manga_title = QLabel()
            layout.addWidget(self.manga_title)

            chapters = "Chapters: " + self.manga['chapters']
            self.Chapthers = QLabel(str(chapters))
            layout.addWidget(self.Chapthers)

            self.prueba  = QPushButton("prueba")
            layout.addWidget(self.prueba)
            self.prueba.clicked.connect(self.test)

        except:
            self.selected = QLabel("No manga selected")
            layout.addWidget(self.selected)
            
        self.setLayout(layout)


    def test(self):
        print("object: ", self.manga)