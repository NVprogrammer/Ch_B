# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chessGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
import chessAI
class UI_NoHintWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.est = QtWidgets.QTextEdit(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        MainWindow.resize(421, 209)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet('background-color:silver')

        self.button_style = '''text-align:justify;
          font-family: times;
          font-weight: 700;
          margin:2px;
          font:12px;
          color: #101000;
          background-color:#ffffff;
          transition: .5s;
          border-radius: 0px;'''
        self.label_style = '''text-align:justify;
          font-family: times;
          font-weight: 600;
          font:11px;
          color: #101000;
          background-color:#ffffff;
          margin:2px;'''
        self.checkbox_style = '''
                font-family: times;
          font-weight: 600;
            color:white;
          display: inline-block;
          text-align: center;
          vertical-align: middle;
          transition: color ease .3s;'''


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QtCore.QRect(10, 18, 44, 18))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(True)
        self.label.setStyleSheet(self.label_style)
        self.move_line = QtWidgets.QLineEdit(self.centralwidget)
        self.move_line.setObjectName(u"move_line")
        self.move_line.setGeometry(QtCore.QRect(60, 18, 81, 18))
        self.move_line.setStyleSheet(self.label_style)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.move_line.setFont(font)
        self.move_line.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_moves = QtWidgets.QLabel(self.centralwidget)
        self.label_moves.setObjectName(u"label_moves")
        self.label_moves.setGeometry(QtCore.QRect(10, 50, 131, 31))
        self.label_moves.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_moves.setStyleSheet(self.label_style)


        self.button_move1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move1.setObjectName(u"button_move1")
        self.button_move1.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.button_move1.setFont(font1)
        self.button_move1.setStyleSheet(self.button_style)
        self.button_move2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move2.setObjectName(u"button_move2")
        self.button_move2.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.button_move2.setStyleSheet(self.button_style)
        self.button_move3 = QtWidgets.QPushButton(self.centralwidget)
        self.button_move3.setObjectName(u"button_move3")
        self.button_move3.setGeometry(QtCore.QRect(10, 140, 131, 31))
        self.button_move3.setStyleSheet(self.button_style)
        self.Start = QtWidgets.QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QtCore.QRect(150, 80, 141, 61))
        self.Start.setStyleSheet(self.button_style)
        self.NoHintMode = QtWidgets.QPushButton(self.centralwidget)
        self.NoHintMode.setObjectName(u"NoHintMode")
        self.NoHintMode.setGeometry(QtCore.QRect(150, 179, 141, 25))
        self.NoHintMode.setStyleSheet(self.button_style)


        self.checkBoxAutoMove = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxAutoMove.setObjectName(u"checkBoxAutoMove")
        self.checkBoxAutoMove.setGeometry(QtCore.QRect(310, 10, 80, 17))
        self.checkBoxAutoMove.setStyleSheet(self.checkbox_style)

        self.checkBoxShowAddBoard = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxShowAddBoard.setObjectName(u"checkBoxShowAddBoard")
        self.checkBoxShowAddBoard.setGeometry(QtCore.QRect(310, 30, 105, 17))
        self.checkBoxShowAddBoard.setStyleSheet(self.checkbox_style)

        self.checkBoxCastle = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxCastle.setObjectName(u"checkBoxCastle")
        self.checkBoxCastle.setGeometry(QtCore.QRect(310, 50, 105, 17))
        self.checkBoxCastle.setStyleSheet(self.checkbox_style)

        self.label_est = QtWidgets.QLabel(self.centralwidget)
        self.label_est.setObjectName(u"label_est")
        self.label_est.setGeometry(QtCore.QRect(150, 50, 70, 25))
        self.label_est.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_est.setStyleSheet(self.label_style)

        self.lineEdit_est = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_est.setObjectName(u"lineEdit_est")
        self.lineEdit_est.setGeometry(QtCore.QRect(220, 50, 70, 25))
        self.lineEdit_est.setStyleSheet(self.label_style)

        self.lineEdit_move = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_move.setObjectName(u"lineEdit_move")
        self.lineEdit_move.setGeometry(QtCore.QRect(10, 179, 131, 25))
        self.lineEdit_move.setStyleSheet(self.label_style)

        self.lineEdit_fps = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_fps.setObjectName(u"lineEdit_fps")
        self.lineEdit_fps.setGeometry(QtCore.QRect(351, 179, 50, 16))
        self.lineEdit_fps.setStyleSheet(self.label_style)

        self.label_thread = QtWidgets.QLabel(self.centralwidget)
        self.label_thread.setObjectName(u"label_depth")
        self.label_thread.setGeometry(QtCore.QRect(300, 124, 51, 16))
        self.label_thread.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_thread.setStyleSheet(self.label_style)

        self.label_depth = QtWidgets.QLabel(self.centralwidget)
        self.label_depth.setObjectName(u"label_depth")
        self.label_depth.setGeometry(QtCore.QRect(300, 150, 51, 16))
        self.label_depth.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_depth.setStyleSheet(self.label_style)

        self.label_fps = QtWidgets.QLabel(self.centralwidget)
        self.label_fps.setObjectName(u"label_fps")
        self.label_fps.setGeometry(QtCore.QRect(300, 179, 51, 16))
        self.label_fps.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_fps.setStyleSheet(self.label_style)

        self.pushButton_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_change.setObjectName(u"pushButton_change")
        self.pushButton_change.setGeometry(QtCore.QRect(150, 140, 141, 31))
        self.pushButton_change.setStyleSheet(self.button_style)
        self.working = QtWidgets.QPushButton(self.centralwidget)
        self.working.setObjectName(u"working")
        self.working.setGeometry(QtCore.QRect(150, 20, 141, 16))
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QtCore.QRect(351, 150, 51, 16))
        self.spinBox.setMinimum(8)
        # self.radioButton_wK = QtWidgets.QRadioButton(self.centralwidget)
        # self.radioButton_wK.setObjectName(u"radioButton_wK")
        # self.radioButton_wK.setGeometry(QtCore.QRect(310, 60, 91, 17))
        # self.radioButton_wQ = QtWidgets.QRadioButton(self.centralwidget)
        # self.radioButton_wQ.setObjectName(u"radioButton_wQ")
        # self.radioButton_wQ.setGeometry(QtCore.QRect(310, 80, 91, 17))
        # self.radioButton_bK = QtWidgets.QRadioButton(self.centralwidget)
        # self.radioButton_bK.setObjectName(u"radioButton_bK")
        # self.radioButton_bK.setGeometry(QtCore.QRect(310, 100, 91, 17))
        # self.radioButton_bQ = QtWidgets.QRadioButton(self.centralwidget)
        # self.radioButton_bQ.setObjectName(u"radioButton_bQ")
        # self.radioButton_bQ.setGeometry(QtCore.QRect(310, 120, 91, 17))

        self.spinBoxThread = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxThread.setObjectName(u"spinBoxThread")
        self.spinBoxThread.setGeometry(QtCore.QRect(351, 124, 51, 16))
        self.spinBoxThread.setMinimum(2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"ChessCheater", None))
        self.label.setText(QtCore.QCoreApplication.translate("ChessCheater", u"Side :", None))
        self.move_line.setText(QtCore.QCoreApplication.translate("MainWindow", u"white", None))
        self.label_moves.setText(QtCore.QCoreApplication.translate("MainWindow", u"Engine moves:", None))
        self.button_move1.setText("")
        self.button_move2.setText("")
        self.button_move3.setText("")
        self.NoHintMode.setText("Without hints")
        self.Start.setText(QtCore.QCoreApplication.translate("MainWindow", u"Start", None))
        self.checkBoxAutoMove.setText(QtCore.QCoreApplication.translate("MainWindow", u"AutoMove ", None))
        self.checkBoxShowAddBoard.setText(QtCore.QCoreApplication.translate("MainWindow", u"ShowAddBoard ", None))
        self.checkBoxCastle.setText(QtCore.QCoreApplication.translate("MainWindow", u"Without castle", None))
        self.checkBoxCastle.setCheckState(1)
        self.label_est.setText(QtCore.QCoreApplication.translate("MainWindow", u" Estimation:", None))
        self.label_depth.setText(QtCore.QCoreApplication.translate("MainWindow", u"Depth:", None))
        self.label_thread.setText(QtCore.QCoreApplication.translate("MainWindow", u"Threads:", None))
        self.label_fps.setText(QtCore.QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.pushButton_change.setText(QtCore.QCoreApplication.translate("MainWindow", u"Change", None))
        self.working.setText("")
        # self.radioButton_wK.setText(QtCore.QCoreApplication.translate("MainWindow", u"White 0-0", None))
        # self.radioButton_wQ.setText(QtCore.QCoreApplication.translate("MainWindow", u"White 0-0-0", None))
        # self.radioButton_bK.setText(QtCore.QCoreApplication.translate("MainWindow", u"Black 0-0", None))
        # self.radioButton_bQ.setText(QtCore.QCoreApplication.translate("MainWindow", u"Black 0-0-0", None))

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.w=[]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Start.clicked.connect(self.btn_start)
        self.ui.pushButton_change.clicked.connect(self.changeSides)
        self.ui.checkBoxAutoMove.stateChanged.connect(self.auto_move)
        self.ui.checkBoxCastle.stateChanged.connect(self.castled)
        self.ui.spinBox.valueChanged.connect(self.depth)
        self.ui.spinBoxThread.valueChanged.connect(self.threads)
        self.ui.button_move1.clicked.connect(self.make_move1)
        self.ui.NoHintMode.clicked.connect(self.to_NoHint)
        self.Main_instance=chessAI.Main(mainwindow=self)

    def to_NoHint(self):# Не доделано
        all = []
        all.append(self.ui.centralwidget.findChildren(QtWidgets.QCheckBox))
        all.append(self.ui.centralwidget.findChildren(QtWidgets.QLineEdit))
        all.append(self.ui.centralwidget.findChildren(QtWidgets.QLabel))
        all.append(self.ui.centralwidget.findChildren(QtWidgets.QPushButton))
        all.append(self.ui.centralwidget.findChildren(QtWidgets.QSpinBox))
        print(all)
        if(len(self.ui.NoHintMode.text())==13):
            for i in all:
                for j in i:
                    j.hide()
            self.ui.label_est.show()
            self.ui.lineEdit_est.show()
            self.ui.lineEdit_move.show()
            self.ui.move_line.show()
            self.ui.label.show()
            self.ui.NoHintMode.setText("With Hints")
            self.ui.NoHintMode.show()
        else:
            for i in all:
                for j in i:
                    j.show()
            self.ui.NoHintMode.setText("Without Hints")
    def make_move1(self):
        self.Main_instance.make_move(self.Main_instance.bestmoves[0][0])

    def depth(self):
        self.Main_instance.depth=self.ui.spinBox.value()
    def threads(self):
        self.Main_instance.thread_num=self.ui.spinBoxThread.value()
    def btn_start(self):
            if(self.ui.Start.text()=='Pause'):
                self.Main_instance.pause=False
                self.alreadyMate = False
            else:
                self.Main_instance.start()
                self.ui.Start.setText('Pause')
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

    def castled(self, checked):
        print('checkbox')
        self.Main_instance.movenum = 0
        self.Main_instance.prev_fen = ''
        if (checked):
            self.Main_instance.castled = True
        else:
            self.Main_instance.castled = False


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

