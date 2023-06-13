# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QPushButton, QTableWidgetItem
import pyodbc


conn = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-AEEDTFK;Database=library;Trusted_Connection=yes;')
cursor = conn.cursor()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 130, 121, 61))
        self.pushButton.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(320, 140, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(320, 190, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 140, 221, 31))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 60, 231, 31))
        self.label_2.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 190, 221, 31))
        self.label_3.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 300, 841, 251))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.tableWidget.setHorizontalHeaderLabels(
                ["Название", "Автор"])
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 130, 121, 61))
        self.pushButton_2.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.delete)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(810, 130, 121, 61))
        self.pushButton_3.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.show)
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "добавить "))
        self.label.setText(_translate("MainWindow", "Название книги "))
        self.label_2.setText(_translate("MainWindow", "Библиотека "))
        self.label_3.setText(_translate("MainWindow", "Автор  книги "))
        self.pushButton_2.setText(_translate("MainWindow", "удалить"))
        self.pushButton_3.setText(_translate("MainWindow", "показать"))


    def add(self):
        try:
            name = self.lineEdit.text()
            author = self.lineEdit_2.text()
            cursor.execute(f"insert into dbo.bookss (bookname, author) values('{name}', '{author}')")
            conn.commit()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        except:
            pass


    def delete(self):
        try:
            name = self.lineEdit.text()
            author = self.lineEdit_2.text()
            cursor.execute("delete FROM dbo.bookss where bookname = '"+name+"' and  author = '" + author+"' ")
            conn.commit()
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
        except:
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            dlg = QMessageBox()
            dlg.setWindowTitle("Ошибка")
            dlg.setText('Вы удаляете то, чего нет в бд')
            dlg.exec()
            
                
                


    def show(self):
        cursor.execute('SELECT COUNT(*) FROM dbo.bookss')
        for rec in cursor:
            i = rec
        self.tableWidget.setRowCount(i[0])
        cursor.execute('SELECT bookname, author FROM dbo.bookss')
        i = 0
        while 1:
            row = cursor.fetchone()
            if not row:
                break
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row.bookname))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(row.author))
            i+=1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())