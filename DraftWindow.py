from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPlainTextEdit, QWidget
from PyQt6.QtCore import Qt

from .ui.ui_main import UiDraftWindow


class DraftWindow:
    def __init__(self):
        self.mainWindow = QWidget()
        self.mainWindow.setWindowTitle("Draft Window")
        self.mainWindow.setWindowFlags(Qt.WindowType.Window)
        self.mainWindow.resize(533, 380)
        
        # 设置UI
        self.draftWindow = UiDraftWindow()
        self.draftWindow.setupUi(self.mainWindow)
        
        # 获取UI组件
        self.draftTextEdit: QPlainTextEdit = self.draftWindow.draftTextEdit
        
        # 存储当前卡片ID，用于检测卡片切换
        self.current_card_id = None

    def show_window(self):
        """显示窗口"""
        if not self.mainWindow.isVisible():
            self.mainWindow.show()
        self.mainWindow.raise_()
        self.mainWindow.activateWindow()

    def keep_content(self):
        """保持内容不变，只确保窗口可见"""
        if not self.mainWindow.isVisible():
            self.mainWindow.show()

    def reset_content(self):
        """重置窗口内容"""
        self.draftTextEdit.setPlainText("")
        if not self.mainWindow.isVisible():
            self.mainWindow.show()

    def clear_and_show(self):
        """清除内容并显示窗口（兼容旧方法）"""
        self.reset_content()
