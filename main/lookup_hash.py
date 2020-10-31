

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lookup(object):
    def setupUi(self, lookup):
        lookup.setObjectName("lookup")
        lookup.resize(320, 240)
        lookup.setMinimumSize(QtCore.QSize(320, 240))
        lookup.setMaximumSize(QtCore.QSize(320, 240))
        lookup.setSizeIncrement(QtCore.QSize(1, 1))
        lookup.setBaseSize(QtCore.QSize(320, 240))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(13)
        font.setKerning(True)
        lookup.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/milk1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        lookup.setWindowIcon(icon)
        lookup.setWindowOpacity(7.0)
        lookup.setIconSize(QtCore.QSize(30, 21))
        self.centralwidget = QtWidgets.QWidget(lookup)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 171, 24))
        self.label.setStyleSheet("font: 75 20pt \"Ubuntu Mono\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 50, 91, 24))
        self.label_2.setStyleSheet("font: 75 13pt \"Ubuntu Mono\";")
        self.label_2.setObjectName("label_2")
        self.hashvalue_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.hashvalue_edit.setGeometry(QtCore.QRect(10, 80, 301, 51))
        self.hashvalue_edit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hashvalue_edit.setObjectName("hashvalue_edit")
        self.analyse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.analyse_btn.setGeometry(QtCore.QRect(100, 140, 111, 36))
        self.analyse_btn.setStyleSheet("font: 75 12pt \"Ubuntu Mono\";")
        self.analyse_btn.setObjectName("analyse_btn")
        lookup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lookup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 320, 24))
        self.menubar.setObjectName("menubar")
        lookup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lookup)
        self.statusbar.setObjectName("statusbar")
        lookup.setStatusBar(self.statusbar)

        self.retranslateUi(lookup)
        QtCore.QMetaObject.connectSlotsByName(lookup)

    def retranslateUi(self, lookup):
        _translate = QtCore.QCoreApplication.translate
        lookup.setWindowTitle(_translate("lookup", "Whiz Look Up"))
        self.label.setText(_translate("lookup", "Whiz Look Up"))
        self.label_2.setText(_translate("lookup", "Hash Value"))
        self.hashvalue_edit.setPlaceholderText(_translate("lookup", "Enter Hashed Value"))
        self.analyse_btn.setText(_translate("lookup", "Analyse Hash"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lookup = QtWidgets.QMainWindow()
    ui = Ui_lookup()
    ui.setupUi(lookup)
    lookup.show()
    sys.exit(app.exec_())
