import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy, QLabel
import re

class Comment_Remover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 900, 900)
        self.setWindowTitle("Comment Remover")

        # Create a vertical layout for the main window
        main_layout = QVBoxLayout()

        # Create a title label
        self.title_label = QLabel("Python Comment Remover", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        font = self.title_label.font()
        font.setBold(True)
        self.title_label.setFont(font)
        main_layout.addWidget(self.title_label)

        # Create a horizontal layout for the header
        header_layout = QHBoxLayout()
        self.header = QWidget(self)
        self.header.setFixedHeight(50)
        self.header.setLayout(header_layout)

        # Create the strip button and add it to the header layout
        self.strip_button = QPushButton("Strip", self)
        self.strip_button.clicked.connect(self.comment_remover)
        self.strip_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        header_layout.addWidget(self.strip_button)

        # Create a vertical layout for the text area
        text_layout = QVBoxLayout()

        self.text_area = QWidget(self)
        self.text_area.setLayout(text_layout)

        # Create the text box and add it to the text layout
        self.document = QTextEdit(self)
        self.document.setFixedSize(800, 800)
        text_layout.addWidget(self.document, alignment=Qt.AlignCenter)

        main_layout.addWidget(self.header)
        main_layout.addWidget(self.text_area)

        # Set the layout of the main window
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.show()

    def comment_remover(self):
        text = self.document.toPlainText()
        cleaned_text = re.sub(r"(\".*?\"|\'.*?\')|(#.*)", "", text)
        self.document.setPlainText(cleaned_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cr = Comment_Remover()
    sys.exit(app.exec_())
