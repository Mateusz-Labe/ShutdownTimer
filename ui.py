from PySide6.QtWidgets import QPushButton, QLabel, QLineEdit, QComboBox

def create_button(text):
    return QPushButton(text)

def create_label(text):
    return QLabel(text)

def create_text(placeholder):
    text = QLineEdit()
    text.setPlaceholderText(placeholder)
    return text

def create_select():
    return QComboBox()