# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chessGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import chessAI
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.resize(421, 179)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(10, 20, 41, 16))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(True)
        self.move_line = QtWidgets.QLineEdit(self.centralwidget)
        self.move_line.setObjectName(u"move_line")
        self.move_line.setGeometry(QtCore.QRect(60, 20, 81, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.move_line.setFont(font)
        self.move_line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_moves = QtWidgets.QLabel(self.centralwidget)
        self.label_moves.setObjectName(u"label_moves")
        self.label_moves.setGeometry(QtCore.QRect(10, 50, 131, 31))
        self.label_moves.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.button_style = 'background-color: #ffffff;'
        self.button_move1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move1.setObjectName(u"button_move1")
        self.button_move1.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.button_move1.setFont(font1)
        self.button_move2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move2.setObjectName(u"button_move2")
        self.button_move2.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.button_move3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move3.setObjectName(u"button_move3")
        self.button_move3.setGeometry(QtCore.QRect(10, 140, 131, 31))
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QtCore.QRect(150, 80, 141, 61))
        self.checkBoxAutoMove = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAutoMove.setObjectName(u"checkBoxAutoMove")
        self.checkBoxAutoMove.setGeometry(QtCore.QRect(310, 10, 70, 17))
        self.checkBoxShowAddBoard = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxShowAddBoard.setObjectName(u"checkBoxShowAddBoard")
        self.checkBoxShowAddBoard.setGeometry(QtCore.QRect(310, 30, 101, 17))
        self.label_est = QtWidgets.QLabel(self.centralwidget)
        self.label_est.setObjectName(u"label_est")
        self.label_est.setGeometry(QtCore.QRect(146, 50, 81, 31))
        self.label_est.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lineEdit_est = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_est.setObjectName(u"lineEdit_est")
        self.lineEdit_est.setGeometry(QtCore.QRect(220, 60, 71, 16))
        self.label_depth = QtWidgets.QLabel(self.centralwidget)
        self.label_depth.setObjectName(u"label_depth")
        self.label_depth.setGeometry(QtCore.QRect(300, 150, 51, 16))
        self.label_depth.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pushButton_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change.setObjectName(u"pushButton_change")
        self.pushButton_change.setGeometry(QtCore.QRect(150, 140, 141, 31))
        self.working = QtWidgets.QPushButton(self.centralwidget)
        self.working.setObjectName(u"working")
        self.working.setGeometry(QtCore.QRect(150, 20, 141, 16))
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QtCore.QRect(351, 150, 51, 16))
        self.spinBox.setMinimum(1)
        self.radioButton_wK = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_wK.setObjectName(u"radioButton_wK")
        self.radioButton_wK.setGeometry(QtCore.QRect(310, 60, 91, 17))
        self.radioButton_wQ = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_wQ.setObjectName(u"radioButton_wQ")
        self.radioButton_wQ.setGeometry(QtCore.QRect(310, 80, 91, 17))
        self.radioButton_bK = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_bK.setObjectName(u"radioButton_bK")
        self.radioButton_bK.setGeometry(QtCore.QRect(310, 100, 91, 17))
        self.radioButton_bQ = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_bQ.setObjectName(u"radioButton_bQ")
        self.radioButton_bQ.setGeometry(QtCore.QRect(310, 120, 91, 17))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QtCore.QCoreApplication.translate("MainWindow", u"Move :", None))
        self.move_line.setText(QtCore.QCoreApplication.translate("MainWindow", u"white", None))
        self.label_moves.setText(QtCore.QCoreApplication.translate("MainWindow", u"         Engine moves:", None))
        self.button_move1.setText("")
        self.button_move2.setText("")
        self.button_move3.setText("")
        self.Start.setText(QtCore.QCoreApplication.translate("MainWindow", u"Start", None))
        self.checkBoxAutoMove.setText(QtCore.QCoreApplication.translate("MainWindow", u"AutoMove", None))
        self.checkBoxShowAddBoard.setText(QtCore.QCoreApplication.translate("MainWindow", u"ShowAddBoard", None))
        self.label_est.setText(QtCore.QCoreApplication.translate("MainWindow", u"  Estimation:", None))
        self.label_depth.setText(QtCore.QCoreApplication.translate("MainWindow", u"   Depth:", None))
        self.pushButton_change.setText(QtCore.QCoreApplication.translate("MainWindow", u"Change", None))
        self.working.setText("")
        self.radioButton_wK.setText(QtCore.QCoreApplication.translate("MainWindow", u"White 0-0", None))
        self.radioButton_wQ.setText(QtCore.QCoreApplication.translate("MainWindow", u"White 0-0-0", None))
        self.radioButton_bK.setText(QtCore.QCoreApplication.translate("MainWindow", u"Black 0-0", None))
        self.radioButton_bQ.setText(QtCore.QCoreApplication.translate("MainWindow", u"Black 0-0-0", None))


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Start.clicked.connect(self.btn_start)
        self.ui.pushButton_change.clicked.connect(self.changeSides)
        self.ui.checkBoxAutoMove.stateChanged.connect(self.auto_move)
        self.ui.spinBox.valueChanged.connect(self.depth)
        self.ui.button_move1.clicked.connect(self.make_move1)
        self.Main_instance=chessAI.Main(mainwindow=self)
    def make_move1(self):
        self.Main_instance.make_move(self.Main_instance.bestmoves[0][0])

    def depth(self):
        self.Main_instance.depth=self.ui.spinBox.value()
    def btn_start(self):
            if(self.ui.Start.text()=='Close'):sys.exit(0)
            self.Main_instance.start()
            self.ui.Start.setText('Close')
    def changeSides(self):
        self.Main_instance.movenum = 0
        self.Main_instance.prev_fen = ''
        if(self.Main_instance.side=='w'):
            self.Main_instance.side='b'
            self.ui.move_line.setText('black')
        elif (self.Main_instance.side == 'b'):
            self.Main_instance.side = 'w'
            self.ui.move_line.setText('white')

    def auto_move(self,checked):
        print('checkbox')
        self.Main_instance.movenum=0
        self.Main_instance.prev_fen=''
        if(checked):
            self.Main_instance.autoMove=True
        else:
            self.Main_instance.autoMove=False




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = mywindow()
    application.show()

    sys.exit(app.exec())

    # -*- coding: utf-8 -*-

    ################################################################################
    ## Form generated from reading UI file 'chessGUINbtHYF.ui'
    ##
    ## Created by: Qt User Interface Compiler version 5.14.1
    ##
    ## WARNING! All changes made in this file will be lost when recompiling UI file!
    ################################################################################



    class Ui_MainWindow(object):
        def setupUi(self, MainWindow):
            if MainWindow.objectName():
                MainWindow.setObjectName(u"MainWindow")


            self.retranslateUi(MainWindow)

            QMetaObject.connectSlotsByName(MainWindow)

        # setupUi

        def retranslateUi(self, MainWindow):
            MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
            self.label.setText(QCoreApplication.translate("MainWindow", u"Move :", None))
            self.move_line.setText(QCoreApplication.translate("MainWindow", u"white", None))
            self.label_moves.setText(QCoreApplication.translate("MainWindow", u"         Engine moves:", None))
            self.button_move1.setText("")
            self.button_move2.setText("")
            self.button_move3.setText("")
            self.Start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
            self.checkBoxAutoMove.setText(QCoreApplication.translate("MainWindow", u"AutoMove", None))
            self.checkBoxShowAddBoard.setText(QCoreApplication.translate("MainWindow", u"ShowAddBoard", None))
            self.label_est.setText(QCoreApplication.translate("MainWindow", u"  Estimation:", None))
            self.label_depth.setText(QCoreApplication.translate("MainWindow", u"   Depth:", None))
            self.pushButton_change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
            self.working.setText("")
            self.radioButton_wK.setText(QCoreApplication.translate("MainWindow", u"White 0-0", None))
            self.radioButton_wQ.setText(QCoreApplication.translate("MainWindow", u"White 0-0-0", None))
            self.radioButton_bK.setText(QCoreApplication.translate("MainWindow", u"Black 0-0", None))
            self.radioButton_bQ.setText(QCoreApplication.translate("MainWindow", u"Black 0-0-0", None))
        # retranslateUi

