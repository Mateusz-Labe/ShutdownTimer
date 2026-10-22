from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QHBoxLayout
from PySide6.QtGui import QIcon, QShortcut, QKeySequence
from PySide6.QtCore import Qt
from function import *
from ui import *
import sounddevice as sd



app = QApplication([])

with open("style.qss", "r") as file:
    app.setStyleSheet(file.read())

app.setWindowIcon(QIcon("assets/app.ico"))

window = QMainWindow()
window.setWindowTitle("Shutdown Timer")
window.resize(1000, 600)

# Creating widgets

label = create_label("Turn off device in (s):")
wejscie = create_text("ex: 3600")
select = create_select()
devices = sd.query_devices()

for device in devices:
    if device["max_output_channels"] > 0:
        select.addItem(device["name"])

#

# Creating inside layout

container = QWidget()

container_layout = QHBoxLayout()
container.setLayout(container_layout)

container_layout.addWidget(label)
container_layout.addWidget(wejscie)
container_layout.addWidget(select)

# Functionality

off = create_button("Turn off")
cancel = create_button("Cancel")

off.setFixedSize(150, 60)
cancel.setFixedSize(150, 60)

central_widget = QWidget()
window.setCentralWidget(central_widget)

layout = QVBoxLayout()

layout.addWidget(container)

layout.addStretch()
buttons = QHBoxLayout()
buttons.addWidget(off)
buttons.addWidget(cancel)

layout.addLayout(buttons)


central_widget.setLayout(layout)

# Functionality
wejscie.textChanged.connect(lambda: sprawdz_czas(wejscie, off))
off.clicked.connect(lambda: kliknieto(wejscie, select))


def uruchom_enter():
    if not off.isEnabled():
        return

    kliknieto(wejscie, select)
wejscie.returnPressed.connect(uruchom_enter)

cancel.clicked.connect(anuluj)
QShortcut(QKeySequence("Esc"), window, anuluj)

window.show()

app.exec()