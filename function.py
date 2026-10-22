import subprocess
from PySide6.QtWidgets import QMessageBox
proces = False

def kliknieto(wejscie, device):
    
    global proces

    try:
        sekundy = int(wejscie.text())
    except ValueError:
        QMessageBox.warning(None, "Błąd", "Proszę podać czas w liczbie")
        return

    if sekundy <= 0:
        QMessageBox.warning(None, "Błąd", "Czas musi być większy od 0")
        return

    proces = True

    glosnik = device.currentText()
    QMessageBox.information(None, "Timer",f"Wyłączenie za {sekundy} sekund przełączenie na {glosnik}")
    subprocess.run(["shutdown", "/s", "/t", str(sekundy)])

def anuluj():
    global proces
    if proces == True:
        subprocess.run(["shutdown", "/a"])
        proces = False
        QMessageBox.information(None, "Timer",f"Anulowano wyłączanie")
    else:
        QMessageBox.warning(None, "Timer", "Wyłączenie nie zostało jeszcze rozpoczęte")

def sprawdz_czas(wejscie, przycisk):
    try:
        sekundy = int(wejscie.text())
    except ValueError:
        przycisk.setEnabled(False)
        return

    if sekundy <= 0:
        przycisk.setEnabled(False)
        return  
    
    przycisk.setEnabled(True)