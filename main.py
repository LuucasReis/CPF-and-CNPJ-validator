from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from validarcpf import validarcpf1
from valida_cnpj import valida
import sys
from design import *

class Teste(QMainWindow, Ui_MainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton_cpf.clicked.connect(self.val_cpf)
        self.pushButton_cnpj.clicked.connect(self.val_cnpj)

    
    def val_cpf(self):
        cpf= self.lineEdit_cpf.text()
        self.label.setText(
            validarcpf1(cpf)
        )
    def val_cnpj(self):
        cnpj= self.lineEdit_cnpj.text()
        self.label.setText(
            valida(cnpj)
        )
        

if __name__ =="__main__":
    qt= QApplication(sys.argv)
    t1= Teste()
    t1.show()
    qt.exec_()

