from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(669, 216)
        MainWindow.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cpf.setMinimumSize(QtCore.QSize(100, 25))
        self.lineEdit_cpf.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_cpf.setObjectName("lineEdit_cpf")
        self.gridLayout.addWidget(self.lineEdit_cpf, 0, 0, 1, 1)
        self.pushButton_cpf = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cpf.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_cpf.sizePolicy().hasHeightForWidth())
        self.pushButton_cpf.setSizePolicy(sizePolicy)
        self.pushButton_cpf.setMinimumSize(QtCore.QSize(50, 40))
        self.pushButton_cpf.setBaseSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.pushButton_cpf.setFont(font)
        self.pushButton_cpf.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_cpf.setObjectName("pushButton_cpf")
        self.gridLayout.addWidget(self.pushButton_cpf, 0, 1, 1, 1)
        self.lineEdit_cnpj = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cnpj.setMinimumSize(QtCore.QSize(100, 25))
        self.lineEdit_cnpj.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.lineEdit_cnpj.setObjectName("lineEdit_cnpj")
        self.gridLayout.addWidget(self.lineEdit_cnpj, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 2)
        self.pushButton_cnpj = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cnpj.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(12)
        self.pushButton_cnpj.setFont(font)
        self.pushButton_cnpj.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: black;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: black;")
        self.pushButton_cnpj.setObjectName("pushButton_cnpj")
        self.gridLayout.addWidget(self.pushButton_cnpj, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Validador de CPF- Lucas Reis"))
        self.pushButton_cpf.setText(_translate("MainWindow", "Validar CPF"))
        self.pushButton_cnpj.setText(_translate("MainWindow", "Validar CNPJ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
