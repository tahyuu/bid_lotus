# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yong\fly_test\fly_test_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1042, 628)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 1021, 531))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listView = QtGui.QListView(self.horizontalLayoutWidget)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.horizontalLayout.addWidget(self.listView)
        self.transfer = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.transfer.setObjectName(_fromUtf8("transfer"))
        self.horizontalLayout.addWidget(self.transfer)
        self.listView_2 = QtGui.QListView(self.horizontalLayoutWidget)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.horizontalLayout.addWidget(self.listView_2)
        self.lineEdit = QtGui.QLabel(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 851, 31))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.checkBox_ca8 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_ca8.setGeometry(QtCore.QRect(26, 60, 50, 20))
        self.checkBox_ca8.setObjectName(_fromUtf8("checkBox_ca8"))
        self.checkBox_ca9 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_ca9.setGeometry(QtCore.QRect(83, 60, 50, 20))
        self.checkBox_ca9.setObjectName(_fromUtf8("checkBox_ca9"))
        self.checkBox_ta8 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_ta8.setGeometry(QtCore.QRect(140, 60, 49, 20))
        self.checkBox_ta8.setObjectName(_fromUtf8("checkBox_ta8"))
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.transfer.setText(_translate("MainWindow", "转换>>", None))
        self.checkBox_ca8.setText(_translate("MainWindow", "CA8", None))
        self.checkBox_ca9.setText(_translate("MainWindow", "CA9", None))
        self.checkBox_ta8.setText(_translate("MainWindow", "TA8", None))
        self.transfer.clicked.connect(self.getfiles)
        
    def getfile(self):
      fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
      self.le.setPixmap(QPixmap(fname))
    def getfiles(self):
      dlg = QtGui.QFileDialog()
      rootfolder=dlg.getExistingDirectory()
      if len(rootfolder)>0:
          self.lineEdit.setText(rootfolder)
          print(rootfolder)
      #dlg.setFileMode(QtGui.QFileDialog.AnyFile)
      #dlg.setFilter("Text files (*.txt)")
      #filenames = QStringList()
		
      #if dlg.exec_():
         #filenames = dlg.selectedFiles()
         #f = open(filenames[0], 'r')
			
         #with f:
            #data = f.read()
      #      print(data)
            #self.contents.setText(data)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

