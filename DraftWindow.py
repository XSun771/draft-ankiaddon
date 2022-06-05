from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton, QPlainTextEdit
from anki.cards import Card

from .ui.ui_main import UiDraftWindow


class DraftWindow:
    def __init__(self, card: Card):
        self.card = card
        self.mainWindow = QtWidgets.QWidget()
        self.draftWindow = UiDraftWindow();
        self.draftWindow.setupUi(self.mainWindow);

        self.historyButton: QPushButton = self.draftWindow.historyButton
        self.draftTextEdit: QPlainTextEdit = self.draftWindow.draftTextEdit

    def initClots(self):
        self.historyButton.clicked.connect(lambda x: print("Hello World"))

    def clearAndShow(self):
        if (not self.mainWindow.isVisible()):
            self.mainWindow.show()
        else:
            self.draftTextEdit.setPlainText("")

# app = QtWidgets.QApplication(sys.argv)
# window = DraftWindow()
# window.show()
# app.exec_()
