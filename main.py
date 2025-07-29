import sys
import os
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QListWidgetItem, QAction
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from ui.main_window import Ui_MainWindow

TASKS_FILE = "tasks.json"

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set window title and icon
        self.setWindowTitle("PyQt5 To-Do List")
        if os.path.exists("assets/icon.png"):
            self.setWindowIcon(QIcon("assets/icon.png"))

        # Track dark mode
        self.dark_mode = False

        # Connect buttons
        self.addButton.clicked.connect(self.add_task)
        self.removeButton.clicked.connect(self.remove_task)
        self.clearButton.clicked.connect(self.clear_all_tasks)
        self.searchInput.textChanged.connect(self.filter_tasks)

        # Add menu bar
        self._create_menu_bar()

        # Load tasks from file
        self.load_tasks()

        # Update status bar
        self.update_status_bar()

    # ------------------- Task Management -------------------
    def add_task(self):
        task = self.taskInput.text().strip()
        if task:
            item = QListWidgetItem(task)
            item.setCheckState(Qt.Unchecked)
            self.taskList.addItem(item)
            self.taskInput.clear()
            self.save_tasks()
            self.update_status_bar()
        else:
            QMessageBox.warning(self, "Warning", "Task cannot be empty!")

    def remove_task(self):
        selected_items = self.taskList.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Warning", "No task selected!")
            return
        for item in selected_items:
            self.taskList.takeItem(self.taskList.row(item))
        self.save_tasks()
        self.update_status_bar()

    def clear_all_tasks(self):
        self.taskList.clear()
        self.save_tasks()
        self.update_status_bar()

    # ------------------- Save & Load -------------------
    def save_tasks(self):
        tasks = []
        for i in range(self.taskList.count()):
            item = self.taskList.item(i)
            tasks.append({"task": item.text(), "done": item.checkState() == Qt.Checked})
        with open(TASKS_FILE, "w") as f:
            json.dump(tasks, f)

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
                for task_data in tasks:
                    item = QListWidgetItem(task_data["task"])
                    item.setCheckState(Qt.Checked if task_data["done"] else Qt.Unchecked)
                    self.taskList.addItem(item)

    # ------------------- UI Enhancements -------------------
    def filter_tasks(self, text):
        for i in range(self.taskList.count()):
            item = self.taskList.item(i)
            item.setHidden(text.lower() not in item.text().lower())

    def update_status_bar(self):
        total = self.taskList.count()
        self.statusBar().showMessage(f"{total} task(s) in the list")

    def toggle_theme(self):
        if self.dark_mode:
            self.setStyleSheet("")  # Reset to default
            self.dark_mode = False
        else:
            self.setStyleSheet("""
                QWidget { background-color: #2e2e2e; color: white; }
                QPushButton { background-color: #444; color: white; border-radius: 5px; padding: 5px; }
                QLineEdit { background-color: #555; color: white; }
                QListWidget { background-color: #333; color: white; }
            """)
            self.dark_mode = True

    def _create_menu_bar(self):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("File")

        about_action = QAction("About", self)
        about_action.triggered.connect(
            lambda: QMessageBox.information(
                self, "About", "To-Do App v2.0 with PyQt5\nEnhanced GUI Features"
            )
        )

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        theme_action = QAction("Toggle Dark Mode", self)
        theme_action.triggered.connect(self.toggle_theme)

        file_menu.addAction(about_action)
        file_menu.addAction(theme_action)
        file_menu.addAction(exit_action)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
