from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class VedicCharacterWindow(QWidget):
    def __init__(self, TextEdit, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Vedic Symbols")
        self.textedit = TextEdit
        layout = QGridLayout(self)
        special_chars = ['\u1CD0', '\u1CD1', '\u1CD2', '\u1CD3', '\u1CD4', '\u1CD5', '\u1CD6', '\u1CD7', '\u1CD8', '\u1CD9', '\u1CDA', '\u1CDB', '\u1CDC', '\u1CDD', '\u1CDE', '\u1CDF', '\u1CE0', '\u1CE1', '\u1CE2', '\u1CE3', '\u1CE4', '\u1CE5', '\u1CE6', '\u1CE7', '\u1CE8', '\u1CE9', '\u1CEA', '\u1CEB', '\u1CEC', '\u1CED', '\u1CEE', '\u1CEF', '\u1CF0', '\u1CF1', '\u1CF2', '\u1CF3', '\u1CF4', '\u1CF5', '\u1CF6', '\u1CF7', '\u1CF8', '\u1CF9']#]  # Add more special characters if needed
        _font = QFont("Shobhika", 18) 
        # Create buttons for special characters
        for i,char in enumerate(special_chars):
            button = QPushButton()
            # Define the font you want to usew
             # Change "Arial" to your desired font family and 12 to the font size
            # Set the font to the button
            button.setFont(_font)
            button.setText(char)
            button.clicked.connect(lambda checked, ch=char: self.insert_special_character(ch))
            layout.addWidget(button, i // 5, i % 5)

            # Increase button size
            button.setMinimumSize(50, 50)
            button.setMaximumSize(100, 100)

    def insert_special_character(self, char):
        cursor = self.textedit.textCursor()
        cursor.insertText(char)

class RareCharacterWindow(QWidget):
    def __init__(self, TextEdit, parent=None):
        super().__init__(parent)
        self.setWindowTitle("  Rare Symbols  ")
        self.textedit = TextEdit
        layout = QGridLayout(self)

        #Kashmiri and Bihari ऺ right alt

        special_chars = ['\u093A','\u093B','\u094E','\u0955','\u0956','\u0957','\u0973','\u0974','\u0976','\u0977','\u0970','\u0971','\u0900','\u0951','\u0952','\u094F']  # Add more special characters if needed
        _font = QFont("Shobhika", 18) 
        # Create buttons for special characters
        for i,char in enumerate(special_chars):
            button = QPushButton()
            # Define the font you want to use
             # Change "Arial" to your desired font family and 12 to the font size
            # Set the font to the button
            button.setFont(_font)
            button.setText(char)
            button.clicked.connect(lambda checked, ch=char: self.insert_special_character(ch))
            layout.addWidget(button, i // 5, i % 5)

            # Increase button size
            button.setMinimumSize(50, 50)
            button.setMaximumSize(100, 100)

    def insert_special_character(self, char):
        cursor = self.textedit.textCursor()
        cursor.insertText(char)