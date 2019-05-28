# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\yong\fly_test\fly_test_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#from PyQt4.QtCore import QStringListModel  

import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

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
        MainWindow.resize(1036, 628)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 3, 0, 1, 4)
        self.btn_LoadProgram = QtGui.QPushButton(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_LoadProgram.sizePolicy().hasHeightForWidth())
        self.btn_LoadProgram.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_LoadProgram.setFont(font)
        self.btn_LoadProgram.setObjectName(_fromUtf8("btn_LoadProgram"))
        self.gridLayout_2.addWidget(self.btn_LoadProgram, 0, 3, 1, 1)
        self.label_root = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_root.setFont(font)
        self.label_root.setObjectName(_fromUtf8("label_root"))
        self.gridLayout_2.addWidget(self.label_root, 0, 0, 1, 3)
        self.checkBox_ca8 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ca8.sizePolicy().hasHeightForWidth())
        self.checkBox_ca8.setSizePolicy(sizePolicy)
        self.checkBox_ca8.setTristate(False)
        self.checkBox_ca8.setObjectName(_fromUtf8("checkBox_ca8"))
        self.gridLayout_2.addWidget(self.checkBox_ca8, 1, 0, 1, 1)
        self.checkBox_ta8 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ta8.sizePolicy().hasHeightForWidth())
        self.checkBox_ta8.setSizePolicy(sizePolicy)
        self.checkBox_ta8.setObjectName(_fromUtf8("checkBox_ta8"))
        self.gridLayout_2.addWidget(self.checkBox_ta8, 1, 2, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listView_source = QtGui.QListView(self.centralWidget)
        self.listView_source.setObjectName(_fromUtf8("listView_source"))
        self.gridLayout.addWidget(self.listView_source, 0, 0, 1, 1)
        self.btn_transfer = QtGui.QPushButton(self.centralWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_transfer.setFont(font)
        self.btn_transfer.setObjectName(_fromUtf8("btn_transfer"))
        self.gridLayout.addWidget(self.btn_transfer, 0, 1, 1, 1)
        self.listView_object = QtGui.QListView(self.centralWidget)
        self.listView_object.setObjectName(_fromUtf8("listView_object"))
        self.gridLayout.addWidget(self.listView_object, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 4)
        self.checkBox_ca9 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_ca9.sizePolicy().hasHeightForWidth())
        self.checkBox_ca9.setSizePolicy(sizePolicy)
        self.checkBox_ca9.setObjectName(_fromUtf8("checkBox_ca9"))
        self.gridLayout_2.addWidget(self.checkBox_ca9, 1, 1, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_2.addWidget(self.textBrowser, 4, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.btn_LoadProgram.setText(_translate("MainWindow", "选择路径", None))
        self.label_root.setText(_translate("MainWindow", "<html><head/><body><p>C:\\Users\\yong\\Desktop\\7100 Platform\\7100 platform\\SHJC-Test System\\obj\\Debug\\TempPE</p></body></html>", None))
        self.checkBox_ca8.setText(_translate("MainWindow", "CA8", None))
        self.checkBox_ta8.setText(_translate("MainWindow", "TA8", None))
        self.btn_transfer.setText(_translate("MainWindow", "转换>>", None))
        self.checkBox_ca9.setText(_translate("MainWindow", "CA9", None))
        self.btn_LoadProgram.clicked.connect(self.getfiles)
        self.checkBox_ca8.setChecked(True)
        self.checkBox_ca9.setChecked(True)
        self.checkBox_ta8.setChecked(True)
        
    def getfiles(self):
        dlg = QtGui.QFileDialog()
        qlist = ['Item 1','Item 2','Item 3','Item 4' ]
        #rootfolder=dlg.getExistingDirectory()
        #strlist=QtCore.QStringList()
        #strlist.append('hello')
        strm=QtCore.QStringListModel(qlist)
        self.listView_source.setModel(strm)
        #for fil in os.listdir(rootfolder):
        #    self.listView_source.
        #    print fil
        #self.listView_source.Columns.Add("序号", 40, HorizontalAlignment.Center) 

        if len(rootfolder)>0:
            self.label_root.setText(rootfolder)
            print(rootfolder)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

