from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtGui import QPixmap
from jsonUtils.json_utils import ReadF, WriteS


class LibraryWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        library = ReadF()
        for manga in range(len(library)):
            pixmap = QPixmap(f"img/{library[manga]['img_path']}")
            
            label = QLabel()
            label.setPixmap(pixmap)
            label.setScaledContents(True)

            label.setMouseTracking(True)
            label.setCursor(Qt.PointingHandCursor)#change cursor to pointing hand cursor

            #connect the function to the manga object using lambda
            label.mousePressEvent = lambda event, idx=manga: self.selected(event, idx, library)

            #add to the grid
            layout.addWidget(label, manga // 2, manga % 2)

        self.setLayout(layout)

    def selected(self, event, index, library):
        manga = library[index]
        WriteS(manga)

