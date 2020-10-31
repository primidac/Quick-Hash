# Whiz quick 

__Dedicated__ = "LORD ALL POWERFUL"
__Author__ = "Primidac"
__Inc__ = "Cyber Xaviours"
__Date__ = "30/11/2019"


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from hashlib import *
import random
import pyperclip
import pyautogui

class Ui_Quicklyhash(object):

    # random hash function
    def rand_hash(self):
        # plain_value = self.plaintext_edit.text()
        # available algorithms
        algos = [shake_128, sha3_256, shake_256, sha256, md5, blake2s, blake2b, sha3_384, sha512, sha3_224, sha3_512, sha224, sha384, sha1]
        rand_hashed = random.choice(algos)
        hash_result = rand_hashed(self.plaintext_edit.text().encode()).hexdigest()
        if self.plaintext_edit.text():
            pyperclip.copy(hash_result)
            self.hashresult_edit.clear()
            show_hash = self.hashresult_edit.insertPlainText(hash_result)
            return show_hash
        else:
            pass

    # fucntion to close app on click
    def exit(self):
        user_exit = QMessageBox()
        user_exit.setIcon(QMessageBox.Information)
        user_exit.setText("Exit Whiz Quick Hash?")
        user_exit.setWindowTitle("Exit")
        user_exit.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        user_exitexec = user_exit.exec()
        if user_exitexec == QMessageBox.Yes:
             pyautogui.hotkey('Alt', 'F4')
        else:
            pass



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 260)
        MainWindow.setMinimumSize(QtCore.QSize(400, 260))
        MainWindow.setMaximumSize(QtCore.QSize(400, 260))
        MainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        MainWindow.setBaseSize(QtCore.QSize(400, 260))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/milk1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 10, 171, 24))
        self.label.setStyleSheet("font: italic 20pt \"DejaVu Sans Mono\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 24))
        self.label_2.setStyleSheet("font: 75 12pt \"Ubuntu Mono\";")
        self.label_2.setObjectName("label_2")
        self.plaintext_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.plaintext_edit.setGeometry(QtCore.QRect(100, 60, 291, 36))
        self.plaintext_edit.setStyleSheet("font: 11pt \"Ubuntu Mono\";")
        self.plaintext_edit.setMaxLength(999999999)
        self.plaintext_edit.setClearButtonEnabled(True)
        self.plaintext_edit.setObjectName("plaintext_edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 91, 24))
        self.label_3.setStyleSheet("font: 75 11pt \"Ubuntu Mono\";")
        self.label_3.setObjectName("label_3")
        self.hashresult_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.hashresult_edit.setGeometry(QtCore.QRect(10, 130, 381, 30))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.hashresult_edit.setFont(font)
        self.hashresult_edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hashresult_edit.setReadOnly(True)
        self.hashresult_edit.setOverwriteMode(True)
        self.hashresult_edit.setObjectName("hashresult_edit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 94, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.rand_hash)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 30))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuAbout_Us = QtWidgets.QMenu(self.menuMenu)
        self.menuAbout_Us.setObjectName("menuAbout_Us")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exit)
        self.actionDevelpers = QtWidgets.QAction(MainWindow)
        self.actionDevelpers.setObjectName("actionDevelpers")
        self.actionDesigners = QtWidgets.QAction(MainWindow)
        self.actionDesigners.setObjectName("actionDesigners")
        self.actionInc = QtWidgets.QAction(MainWindow)
        self.actionInc.setObjectName("actionInc")
        self.menuAbout_Us.addAction(self.actionDevelpers)
        self.menuAbout_Us.addAction(self.actionDesigners)
        self.menuAbout_Us.addAction(self.actionInc)
        self.menuMenu.addAction(self.menuAbout_Us.menuAction())
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quick Hash"))
        self.label.setText(_translate("MainWindow", "Quick Hash"))
        self.label_2.setText(_translate("MainWindow", "Plain Text"))
        self.plaintext_edit.setPlaceholderText(_translate("MainWindow", "Enter Plain Text"))
        self.label_3.setText(_translate("MainWindow", "Hash Result"))
        self.hashresult_edit.setPlaceholderText(_translate("MainWindow", "                   Hash Result "))
        self.pushButton.setText(_translate("MainWindow", "Quick Hash"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuAbout_Us.setTitle(_translate("MainWindow", "About Us"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDevelpers.setText(_translate("MainWindow", "Developers"))
        self.actionDesigners.setText(_translate("MainWindow", "Designers"))
        self.actionInc.setText(_translate("MainWindow", "Inc."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Quicklyhash()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
