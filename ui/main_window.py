from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.searchInput = QtWidgets.QLineEdit()
        self.searchInput.setPlaceholderText("Search tasks...")
        self.verticalLayout.addWidget(self.searchInput)
        
        self.taskInput = QtWidgets.QLineEdit()
        self.taskInput.setPlaceholderText("Enter a new task...")
        self.verticalLayout.addWidget(self.taskInput)

        self.addButton = QtWidgets.QPushButton("Add Task")
        self.verticalLayout.addWidget(self.addButton)

        self.taskList = QtWidgets.QListWidget()
        self.verticalLayout.addWidget(self.taskList)

        self.removeButton = QtWidgets.QPushButton("Remove Selected Task")
        self.verticalLayout.addWidget(self.removeButton)

        self.clearButton = QtWidgets.QPushButton("Clear All Tasks")
        self.verticalLayout.addWidget(self.clearButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To-Do List App"))
