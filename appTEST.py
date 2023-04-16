import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)
from ext_busqueda import library

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.edit = QLineEdit("Write the name of the manga ")
        self.button = QPushButton("Show list of manga")
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.button.clicked.connect(self.search)

    #
    def search(self):
        library(self.edit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.resize(300,300)
    form.show()
    sys.exit(app.exec())