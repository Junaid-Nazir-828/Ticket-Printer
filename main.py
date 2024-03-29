# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from win32com import client
import time
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import PyPDF2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedWidth(1027)
        MainWindow.setFixedHeight(748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget, clicked = lambda : self.printTicket())
        self.pushButton.setGeometry(QtCore.QRect(350, 250, 271, 181))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def printTicket(self):
        
        try:
            # filename = os.path.abspath('ticket version 38.docx')
            # word = client.Dispatch("Word.Application")        

            # word.Documents.Open(filename)
            # word.ActiveDocument.PrintOut()
            # time.sleep(2)
            # word.ActiveDocument.Close()

            # word.Quit()

            # Specify the path to the PDF file you want to print

            # pdf_file_path = os.path.abspath('ticket version 1.pdf')

            # # Open the PDF file in read-binary mode
            # pdf_file = open(pdf_file_path, 'rb')

            # # Create a PDF reader object
            # pdf_reader = PyPDF2.PdfReader(pdf_file)

            # # Get the number of pages in the PDF
            # num_pages = len(pdf_reader.pages)

            # # Create a PDF printer object (you may need to change the printer_name)
            # printer_name = 'KONICA MINOLTA 4700P_4000P_3300P'
            # pdf_printer = PyPDF2.Printer(pdf_file_path, printer_name)
            
            # # Loop through each page and send it to the printer
            # for page_num in range(num_pages):
            #     pdf_printer.printPage(pdf_reader.getPage(page_num))

            # # Close the PDF file
            # pdf_file.close()

            os.startfile("ticket.jpeg", "print")
            time.sleep(5)

        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Print"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
