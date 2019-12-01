# Whiz Quick Hash

__Dedicated__ = "LORD ALL POWERFUL"
__Author__ = "Primidac"
__Inc__ = "Cyber Xaviours"
__Date__ = "30/11/2019"


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    # fucntion to close app on click
    def exit(self):
        user_exit = QMessageBox()
        user_exit.setIcon(QMessageBox.Information)
        user_exit.setText("This is a message box")
        user_exit.setWindowTitle("MessageBox demo")
        user_exit.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        sys.exit(app.exec_()) if user_exit == QMessageBox.Yes else print("")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        MainWindow.setSizeIncrement(QtCore.QSize(1, 1))
        MainWindow.setBaseSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/milk.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plain_text = QtWidgets.QLabel(self.centralwidget)
        self.plain_text.setGeometry(QtCore.QRect(30, 190, 121, 24))
        self.plain_text.setStyleSheet("font: bold 12pt \"Ubuntu Mono\";")
        self.plain_text.setObjectName("plain_text")
        self.hash_algo = QtWidgets.QLabel(self.centralwidget)
        self.hash_algo.setGeometry(QtCore.QRect(30, 260, 121, 24))
        self.hash_algo.setStyleSheet("font: bold 12pt \"Ubuntu Mono\";")
        self.hash_algo.setObjectName("hash_algo")
        self.hash_value = QtWidgets.QLabel(self.centralwidget)
        self.hash_value.setGeometry(QtCore.QRect(280, 300, 81, 24))
        self.hash_value.setStyleSheet("font: bold 12pt \"Ubuntu Mono\";")
        self.hash_value.setObjectName("hash_value")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 491, 71))
        self.label_4.setStyleSheet("font: 75 italic 40pt \"DejaVu Sans Mono\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(483, 110, 81, 24))
        self.label_5.setStyleSheet("font: 17pt \"Karumbi\";\n"
"color:rgb(0, 42, 235)")
        self.label_5.setObjectName("label_5")
        self.plaintext_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.plaintext_edit.setGeometry(QtCore.QRect(150, 180, 441, 36))
        self.plaintext_edit.setAutoFillBackground(False)
        self.plaintext_edit.setText("")
        self.plaintext_edit.setMaxLength(999999999)
        self.plaintext_edit.setFrame(True)
        self.plaintext_edit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.plaintext_edit.setDragEnabled(False)
        self.plaintext_edit.setReadOnly(False)
        self.plaintext_edit.setClearButtonEnabled(True)
        self.plaintext_edit.setObjectName("plaintext_edit")
        self.hashalgo_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.hashalgo_edit.setGeometry(QtCore.QRect(150, 250, 441, 36))
        self.hashalgo_edit.setMaxLength(9)
        self.hashalgo_edit.setClearButtonEnabled(True)
        self.hashalgo_edit.setObjectName("hashalgo_edit")
        self.hash_button = QtWidgets.QPushButton(self.centralwidget)
        self.hash_button.setGeometry(QtCore.QRect(260, 380, 111, 36))
        self.hash_button.setObjectName("hash_button")
        self.Exit_app = QtWidgets.QLabel(self.centralwidget)
        self.Exit_app.setGeometry(QtCore.QRect(570, 390, 64, 24))
        self.Exit_app.setStyleSheet("font: bold 12pt \"Ubuntu Mono\";")
        self.Exit_app.setObjectName("Exit_app")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(80, 90, 118, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(410, 40, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.hashvalue_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.hashvalue_edit.setGeometry(QtCore.QRect(30, 330, 571, 31))
        self.hashvalue_edit.setStyleSheet("font: 12pt \"Ubuntu Mono\";")
        self.hashvalue_edit.setReadOnly(True)
        self.hashvalue_edit.setAcceptRichText(True)
        self.hashvalue_edit.setObjectName("hashvalue_edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 30))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuLookup_Hash = QtWidgets.QMenu(self.menuMenu)
        self.menuLookup_Hash.setObjectName("menuLookup_Hash")
        self.menuHash_Multiple_Text = QtWidgets.QMenu(self.menuMenu)
        self.menuHash_Multiple_Text.setObjectName("menuHash_Multiple_Text")
        self.menuHash_Algorithms = QtWidgets.QMenu(self.menubar)
        self.menuHash_Algorithms.setObjectName("menuHash_Algorithms")
        self.menuMD5 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuMD5.setObjectName("menuMD5")
        self.menuSHA256 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA256.setObjectName("menuSHA256")
        self.menuSHAKE_128 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHAKE_128.setObjectName("menuSHAKE_128")
        self.menuSHA3_256 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA3_256.setObjectName("menuSHA3_256")
        self.menuSHAKE_256 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHAKE_256.setObjectName("menuSHAKE_256")
        self.menuBLAKE2S = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuBLAKE2S.setObjectName("menuBLAKE2S")
        self.menuBLAKE2B = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuBLAKE2B.setObjectName("menuBLAKE2B")
        self.menuSHA3_224 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA3_224.setObjectName("menuSHA3_224")
        self.menuSHA3_384 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA3_384.setObjectName("menuSHA3_384")
        self.menuSHA512 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA512.setObjectName("menuSHA512")
        self.menuSHA224 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA224.setObjectName("menuSHA224")
        self.menuSHA3_512 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA3_512.setObjectName("menuSHA3_512")
        self.menuSHA384 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA384.setObjectName("menuSHA384")
        self.menuSHA1 = QtWidgets.QMenu(self.menuHash_Algorithms)
        self.menuSHA1.setObjectName("menuSHA1")
        self.menuEncryption = QtWidgets.QMenu(self.menubar)
        self.menuEncryption.setObjectName("menuEncryption")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuCredits = QtWidgets.QMenu(self.menuAbout)
        self.menuCredits.setObjectName("menuCredits")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Quick_Hash = QtWidgets.QAction(MainWindow)
        self.Quick_Hash.setObjectName("Quick_Hash")
        self.actionAbout_MD5 = QtWidgets.QAction(MainWindow)
        self.actionAbout_MD5.setObjectName("actionAbout_MD5")
        self.actionAbour_SHA256 = QtWidgets.QAction(MainWindow)
        self.actionAbour_SHA256.setObjectName("actionAbour_SHA256")
        self.actionHash_Details = QtWidgets.QAction(MainWindow)
        self.actionHash_Details.setObjectName("actionHash_Details")
        self.actionAbout_Hash = QtWidgets.QAction(MainWindow)
        self.actionAbout_Hash.setObjectName("actionAbout_Hash")
        self.actionSave_to_File = QtWidgets.QAction(MainWindow)
        self.actionSave_to_File.setObjectName("actionSave_to_File")
        self.actionSave_to_clipboard = QtWidgets.QAction(MainWindow)
        self.actionSave_to_clipboard.setObjectName("actionSave_to_clipboard")
        self.actionAbout_MD5_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_MD5_2.setObjectName("actionAbout_MD5_2")
        self.actionAbout_SHA256 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA256.setObjectName("actionAbout_SHA256")
        self.actionUse_SHAKE_128 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHAKE_128.setObjectName("actionUse_SHAKE_128")
        self.actionAbout_SHAKE_128 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHAKE_128.setObjectName("actionAbout_SHAKE_128")
        self.actionUse_SHA3_256 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA3_256.setObjectName("actionUse_SHA3_256")
        self.actionAbout_SHA3_256 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA3_256.setObjectName("actionAbout_SHA3_256")
        self.actionUse_SHAKE_256 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHAKE_256.setObjectName("actionUse_SHAKE_256")
        self.actionAbout_SHAKE_256 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHAKE_256.setObjectName("actionAbout_SHAKE_256")
        self.actionUse_BLAKE2S = QtWidgets.QAction(MainWindow)
        self.actionUse_BLAKE2S.setObjectName("actionUse_BLAKE2S")
        self.actionAbout_BLAKE2S = QtWidgets.QAction(MainWindow)
        self.actionAbout_BLAKE2S.setObjectName("actionAbout_BLAKE2S")
        self.actionUse_BLAKE2B = QtWidgets.QAction(MainWindow)
        self.actionUse_BLAKE2B.setObjectName("actionUse_BLAKE2B")
        self.actionAbout_BLAKE2B = QtWidgets.QAction(MainWindow)
        self.actionAbout_BLAKE2B.setObjectName("actionAbout_BLAKE2B")
        self.actionUse_SHA3_224 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA3_224.setObjectName("actionUse_SHA3_224")
        self.actionAbout_SHA3_224 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA3_224.setObjectName("actionAbout_SHA3_224")
        self.actionUse_SHA3_384 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA3_384.setObjectName("actionUse_SHA3_384")
        self.actionAbout_SHA3_384 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA3_384.setObjectName("actionAbout_SHA3_384")
        self.actionUse_SHA512 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA512.setObjectName("actionUse_SHA512")
        self.actionAbout_SHA512 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA512.setObjectName("actionAbout_SHA512")
        self.actionUse_SHA224 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA224.setObjectName("actionUse_SHA224")
        self.actionAbout_SHA224 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA224.setObjectName("actionAbout_SHA224")
        self.actionUse_SHA3_512 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA3_512.setObjectName("actionUse_SHA3_512")
        self.actionAbout_SHA3_512 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA3_512.setObjectName("actionAbout_SHA3_512")
        self.actionUse_SHA384 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA384.setObjectName("actionUse_SHA384")
        self.actionAbout_SHA384 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA384.setObjectName("actionAbout_SHA384")
        self.actionUse_SHA1 = QtWidgets.QAction(MainWindow)
        self.actionUse_SHA1.setObjectName("actionUse_SHA1")
        self.actionAbout_SHA1 = QtWidgets.QAction(MainWindow)
        self.actionAbout_SHA1.setObjectName("actionAbout_SHA1")
        self.actionHash_File = QtWidgets.QAction(MainWindow)
        self.actionHash_File.setObjectName("actionHash_File")
        self.actionAbout_Whiz = QtWidgets.QAction(MainWindow)
        self.actionAbout_Whiz.setObjectName("actionAbout_Whiz")
        self.actionAbout_CyberXaviours = QtWidgets.QAction(MainWindow)
        self.actionAbout_CyberXaviours.setObjectName("actionAbout_CyberXaviours")
        self.actionDevelopers = QtWidgets.QAction(MainWindow)
        self.actionDevelopers.setObjectName("actionDevelopers")
        self.actionMutate = QtWidgets.QAction(MainWindow)
        self.actionMutate.setObjectName("actionMutate")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDesigners = QtWidgets.QAction(MainWindow)
        self.actionDesigners.setObjectName("actionDesigners")
        self.actionUse_GUI = QtWidgets.QAction(MainWindow)
        self.actionUse_GUI.setObjectName("actionUse_GUI")
        self.actionUse_Shell = QtWidgets.QAction(MainWindow)
        self.actionUse_Shell.setObjectName("actionUse_Shell")
        self.menuLookup_Hash.addAction(self.actionHash_Details)
        self.menuLookup_Hash.addAction(self.actionAbout_Hash)
        self.menuHash_Multiple_Text.addAction(self.actionSave_to_File)
        self.menuHash_Multiple_Text.addAction(self.actionSave_to_clipboard)
        self.menuMenu.addAction(self.Quick_Hash)
        self.menuMenu.addAction(self.menuLookup_Hash.menuAction())
        self.menuMenu.addAction(self.menuHash_Multiple_Text.menuAction())
        self.menuMenu.addAction(self.actionHash_File)
        self.menuMenu.addAction(self.actionMutate)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuMD5.addAction(self.actionAbout_MD5)
        self.menuMD5.addAction(self.actionAbout_MD5_2)
        self.menuSHA256.addAction(self.actionAbour_SHA256)
        self.menuSHA256.addAction(self.actionAbout_SHA256)
        self.menuSHAKE_128.addAction(self.actionUse_SHAKE_128)
        self.menuSHAKE_128.addAction(self.actionAbout_SHAKE_128)
        self.menuSHA3_256.addAction(self.actionUse_SHA3_256)
        self.menuSHA3_256.addAction(self.actionAbout_SHA3_256)
        self.menuSHAKE_256.addAction(self.actionUse_SHAKE_256)
        self.menuSHAKE_256.addAction(self.actionAbout_SHAKE_256)
        self.menuBLAKE2S.addAction(self.actionUse_BLAKE2S)
        self.menuBLAKE2S.addAction(self.actionAbout_BLAKE2S)
        self.menuBLAKE2B.addAction(self.actionUse_BLAKE2B)
        self.menuBLAKE2B.addAction(self.actionAbout_BLAKE2B)
        self.menuSHA3_224.addAction(self.actionUse_SHA3_224)
        self.menuSHA3_224.addAction(self.actionAbout_SHA3_224)
        self.menuSHA3_384.addAction(self.actionUse_SHA3_384)
        self.menuSHA3_384.addAction(self.actionAbout_SHA3_384)
        self.menuSHA512.addAction(self.actionUse_SHA512)
        self.menuSHA512.addAction(self.actionAbout_SHA512)
        self.menuSHA224.addAction(self.actionUse_SHA224)
        self.menuSHA224.addAction(self.actionAbout_SHA224)
        self.menuSHA3_512.addAction(self.actionUse_SHA3_512)
        self.menuSHA3_512.addAction(self.actionAbout_SHA3_512)
        self.menuSHA384.addAction(self.actionUse_SHA384)
        self.menuSHA384.addAction(self.actionAbout_SHA384)
        self.menuSHA1.addAction(self.actionUse_SHA1)
        self.menuSHA1.addAction(self.actionAbout_SHA1)
        self.menuHash_Algorithms.addAction(self.menuMD5.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA256.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHAKE_128.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA3_256.menuAction())

        self.menuHash_Algorithms.addAction(self.menuSHAKE_256.menuAction())
        self.menuHash_Algorithms.addAction(self.menuBLAKE2S.menuAction())
        self.menuHash_Algorithms.addAction(self.menuBLAKE2B.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA3_224.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA3_384.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA512.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA224.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA3_512.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA384.menuAction())
        self.menuHash_Algorithms.addAction(self.menuSHA1.menuAction())
        self.menuEncryption.addAction(self.actionUse_GUI)
        self.menuEncryption.addAction(self.actionUse_Shell)
        self.menuCredits.addAction(self.actionDevelopers)
        self.menuCredits.addAction(self.actionDesigners)
        self.menuAbout.addAction(self.actionAbout_Whiz)
        self.menuAbout.addAction(self.actionAbout_CyberXaviours)
        self.menuAbout.addAction(self.menuCredits.menuAction())
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHash_Algorithms.menuAction())
        self.menubar.addAction(self.menuEncryption.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Whiz Quick Hash"))
        self.plain_text.setText(_translate("MainWindow", "Plain Text"))
        self.hash_algo.setText(_translate("MainWindow", "Hash Algorithm"))
        self.hash_value.setText(_translate("MainWindow", "Hash Value"))
        self.label_4.setText(_translate("MainWindow", "Whiz Quick Hash"))
        self.label_5.setText(_translate("MainWindow", "GUI Client"))
        self.plaintext_edit.setPlaceholderText(_translate("MainWindow", "Enter Plain Text to Hash"))
        self.hashalgo_edit.setPlaceholderText(_translate("MainWindow", "Enter Hashing Algorithm"))
        self.hash_button.setText(_translate("MainWindow", "Hash"))
        self.hashvalue_edit.setPlaceholderText(_translate("MainWindow", "                              Hash Result"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuLookup_Hash.setTitle(_translate("MainWindow", "Lookup Hash"))
        self.menuHash_Multiple_Text.setTitle(_translate("MainWindow", "Hash Multiple Text"))
        self.menuHash_Algorithms.setTitle(_translate("MainWindow", "Hash Algorithms"))
        self.menuMD5.setTitle(_translate("MainWindow", "MD5"))
        self.menuSHA256.setTitle(_translate("MainWindow", "SHA256"))
        self.menuSHAKE_128.setTitle(_translate("MainWindow", "SHAKE_128"))
        self.menuSHA3_256.setTitle(_translate("MainWindow", "SHA3_256"))
        self.menuSHAKE_256.setTitle(_translate("MainWindow", "SHAKE_256"))
        self.menuBLAKE2S.setTitle(_translate("MainWindow", "BLAKE2S"))
        self.menuBLAKE2B.setTitle(_translate("MainWindow", "BLAKE2B"))
        self.menuSHA3_224.setTitle(_translate("MainWindow", "SHA3_224"))
        self.menuSHA3_384.setTitle(_translate("MainWindow", "SHA3_384"))
        self.menuSHA512.setTitle(_translate("MainWindow", "SHA512"))
        self.menuSHA224.setTitle(_translate("MainWindow", "SHA224"))
        self.menuSHA3_512.setTitle(_translate("MainWindow", "SHA3_512"))
        self.menuSHA384.setTitle(_translate("MainWindow", "SHA384"))
        self.menuSHA1.setTitle(_translate("MainWindow", "SHA1"))
        self.menuEncryption.setTitle(_translate("MainWindow", "Encryption"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuCredits.setTitle(_translate("MainWindow", "Credits"))
        self.Quick_Hash.setText(_translate("MainWindow", "Quick Hash"))
        self.actionAbout_MD5.setText(_translate("MainWindow", "Use MD5"))
        self.actionAbour_SHA256.setText(_translate("MainWindow", "Use SHA256"))
        self.actionHash_Details.setText(_translate("MainWindow", "Hash Details"))
        self.actionAbout_Hash.setText(_translate("MainWindow", "About Hash"))
        self.actionSave_to_File.setText(_translate("MainWindow", "Save to File"))
        self.actionSave_to_clipboard.setText(_translate("MainWindow", "Save to clipboard"))
        self.actionAbout_MD5_2.setText(_translate("MainWindow", "About MD5"))
        self.actionAbout_SHA256.setText(_translate("MainWindow", "About SHA256"))
        self.actionUse_SHAKE_128.setText(_translate("MainWindow", "Use SHAKE_128"))
        self.actionAbout_SHAKE_128.setText(_translate("MainWindow", "About SHAKE_128"))
        self.actionUse_SHA3_256.setText(_translate("MainWindow", "Use SHA3_256"))
        self.actionAbout_SHA3_256.setText(_translate("MainWindow", "About SHA3_256"))
        self.actionUse_SHAKE_256.setText(_translate("MainWindow", "Use SHAKE_256"))
        self.actionAbout_SHAKE_256.setText(_translate("MainWindow", "About SHAKE_256"))
        self.actionUse_BLAKE2S.setText(_translate("MainWindow", "Use BLAKE2S"))
        self.actionAbout_BLAKE2S.setText(_translate("MainWindow", "About BLAKE2S"))
        self.actionUse_BLAKE2B.setText(_translate("MainWindow", "Use BLAKE2B"))
        self.actionAbout_BLAKE2B.setText(_translate("MainWindow", "About BLAKE2B"))
        self.actionUse_SHA3_224.setText(_translate("MainWindow", "Use SHA3_224"))
        self.actionAbout_SHA3_224.setText(_translate("MainWindow", "About SHA3_224"))
        self.actionUse_SHA3_384.setText(_translate("MainWindow", "Use SHA3_384"))
        self.actionAbout_SHA3_384.setText(_translate("MainWindow", "About SHA3_384"))
        self.actionUse_SHA512.setText(_translate("MainWindow", "Use SHA512"))
        self.actionAbout_SHA512.setText(_translate("MainWindow", "About SHA512"))
        self.actionUse_SHA224.setText(_translate("MainWindow", "Use SHA224"))
        self.actionAbout_SHA224.setText(_translate("MainWindow", "About SHA224"))
        self.actionUse_SHA3_512.setText(_translate("MainWindow", "Use SHA3_512"))
        self.actionAbout_SHA3_512.setText(_translate("MainWindow", "About SHA3_512"))
        self.actionUse_SHA384.setText(_translate("MainWindow", "Use SHA384"))
        self.actionAbout_SHA384.setText(_translate("MainWindow", "About SHA384"))
        self.actionUse_SHA1.setText(_translate("MainWindow", "Use SHA1"))
        self.actionAbout_SHA1.setText(_translate("MainWindow", "About SHA1"))
        self.actionHash_File.setText(_translate("MainWindow", "Hash File"))
        self.actionAbout_Whiz.setText(_translate("MainWindow", "About Whiz"))
        self.actionAbout_CyberXaviours.setText(_translate("MainWindow", "About Cyber Xaviours"))
        self.actionDevelopers.setText(_translate("MainWindow", "Developers"))
        self.actionMutate.setText(_translate("MainWindow", "Mutate"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.triggered.connect(self.exit)
        self.actionDesigners.setText(_translate("MainWindow", "Designers"))
        self.actionUse_GUI.setText(_translate("MainWindow", "Use GUI"))
        self.actionUse_Shell.setText(_translate("MainWindow", "Use Shell"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
