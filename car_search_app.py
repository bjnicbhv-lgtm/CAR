import sys
import os
import sqlite3
import json
import webbrowser
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QLineEdit, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox,
    QSizePolicy, QGridLayout, QScrollArea, QStackedWidget, QFrame,
    QCompleter, QToolTip
)
from PySide6.QtCore import Qt, QSize, QThread, Signal, QObject
from PySide6.QtGui import QFont, QPixmap, QIcon, QIntValidator, QCursor, QAction

# --- פונקציה לטיפול בנתיבי קבצים בתוך EXE ---
def resource_path(relative_path):
    """ מקבל נתיב יחסי ומחזיר נתיב מוחלט שמתאים גם ל-EXE וגם להרצה רגילה """
    try:
        # PyInstaller יוצר תיקייה זמנית ושומר את הנתיב שלה ב-sys._MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- הגדרות גלובליות ---
APP_VERSION = "1.3"
GITHUB_REPO = "cfopuser/car-finder"
CONFIG_FILE = "app_config.json"
HISTORY_LIMIT = 50 
HISTORY_DISPLAY_LIMIT = 4

# --- מחלקת האפליקציה הראשית ---
class CarSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("חיפוש רכב")
        self.resize(1000, 700)
        
        # טעינת אייקון החלון הראשי באמצעות resource_path
        self.setWindowIcon(QIcon(resource_path("my_icon.ico")))

        self.setup_ui()

    def setup_ui(self):
        # יצירת הווידג'ט המרכזי
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # דוגמה לטעינת אייקונים בכפתורים/פעולות
        search_btn = QPushButton("חפש")
        search_btn.setIcon(QIcon(resource_path("icon_search.ico")))
        
        delete_btn = QPushButton("מחק")
        delete_btn.setIcon(QIcon(resource_path("icon_delete.ico")))

        copy_btn = QPushButton("העתק")
        copy_btn.setIcon(QIcon(resource_path("icon_copy.ico")))

        self.main_layout.addWidget(search_btn)
        self.main_layout.addWidget(delete_btn)
        self.main_layout.addWidget(copy_btn)

        # כאן יבוא שאר הקוד של הממשק שלך...
        pass

# --- הפעלה ---
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setLayoutDirection(Qt.RightToLeft) # התאמה לעברית
    
    window = CarSearchApp()
    window.show()
    sys.exit(app.exec())
