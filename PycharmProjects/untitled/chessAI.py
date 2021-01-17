#coding=utf8
import numpy as np
from PIL import Image
import random
import time
import mss
import cv2
import tkinter as tk
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow import keras
import os
import subprocess
from threading import Thread
import tensorflow as tf
import mouse
import sys
import imutils


import multiprocessing as mp
from concurrent import futures
from PyQt5.QtCore import QThread
from pynput import  keyboard

class Main(QThread):
    figures = ['bB_w.PNG', 'bK_w.PNG', 'bN_w.PNG', 'bp_w.PNG', 'bQ_w.PNG', 'bR_w.PNG', 'wB_w.PNG', 'wK_w.PNG',
               'wN_w.PNG', 'wp_w.PNG', 'wQ_w.PNG', 'wR_w.PNG', 'emp_w.PNG',
               'bB_b.PNG', 'bK_b.PNG', 'bN_b.PNG', 'bp_b.PNG', 'bQ_b.PNG', 'bR_b.PNG', 'wB_b.PNG', 'wK_b.PNG',
               'wN_b.PNG', 'wp_b.PNG', 'wQ_b.PNG', 'wR_b.PNG', 'emp_b.PNG'
               ]
    classes = [i.split('_')[0] for i in figures]
    classes = list(np.unique(classes))
    def reset(self):
        self.movenum = 0
        self.prev_fen = ''
        self.white_m = ''
        self.black_m = ''
        self.side = 'w'
        self.depth = ''
        self.est = ''
        self.autoMove = False
        self.timeThink = 0.30
        self.bestmoves = []
        self.move="w"

    def __init__(self,mainwindow,parent=None):
        super().__init__()
        self.mainwindow=mainwindow

        self.figures = ['bB_w.PNG', 'bK_w.PNG', 'bN_w.PNG', 'bp_w.PNG', 'bQ_w.PNG', 'bR_w.PNG', 'wB_w.PNG', 'wK_w.PNG',
               'wN_w.PNG', 'wp_w.PNG', 'wQ_w.PNG', 'wR_w.PNG', 'emp_w.PNG',
               'bB_b.PNG', 'bK_b.PNG', 'bN_b.PNG', 'bp_b.PNG', 'bQ_b.PNG', 'bR_b.PNG', 'wB_b.PNG', 'wK_b.PNG',
               'wN_b.PNG', 'wp_b.PNG', 'wQ_b.PNG', 'wR_b.PNG', 'emp_b.PNG'
               ]
        self.classes = [i.split('_')[0] for i in self.figures]
        self.classes = list(np.unique(self.classes))
        self.position = []
        self.boardXY=[]# для функции detectbyHand
        self.x_m = 0
        self.y_m = 0
        self.board_width = 0
        self.board_height = 0
        self.movenum = 0
        self.prev_fen = ''
        self.white_m = ''
        self.black_m = ''
        self.side = 'w'
        self.depth = ''
        self.est = ''
        self.autoMove = False
        self.timeThink = 0.30
        self.bestmoves=[]
        self.doNothing=False
        self.pause=False

    def createPicturesForHaar(self):
        dir = os.listdir('boardsForTrain')
        ind=1
        for i in dir:
            print(i)
            board=cv2.imread('boardsForTrain/'+i)
            board=cv2.resize(board,(800,800))
            h_step=100
            w_step=100

            bR_w = board[w_step * 0:w_step * 1, h_step * 0:h_step * 1]
            bR_b = board[w_step * 0:w_step * 1, h_step * 7:h_step * 8]
            bN_b = board[w_step * 0:w_step * 1, h_step * 1:h_step * 2]
            bN_w = board[w_step * 0:w_step * 1, h_step * 6:h_step * 7]
            bB_w = board[w_step * 0:w_step * 1, h_step * 2:h_step * 3]
            bB_b = board[w_step * 0:w_step * 1, h_step * 5:h_step * 6]
            bQ_b = board[w_step * 0:w_step * 1, h_step * 3:h_step * 4]
            bK_w = board[w_step * 0:w_step * 1, h_step * 4:h_step * 5]
            bK_b = board[w_step * 2:w_step * 3, h_step * 3:h_step * 4]
            bQ_w = board[w_step * 2:w_step * 3, h_step * 4:h_step * 5]
            bp_w = board[w_step * 1:w_step * 2, h_step * 3:h_step * 4]
            bp_b = board[w_step * 1:w_step * 2, h_step * 4:h_step * 5]

            emp_w = board[h_step * 3:h_step * 4, w_step * 3:w_step * 4, ]
            emp_b = board[h_step * 3:h_step * 4, w_step * 4:w_step * 5, ]

            wR_w = board[h_step * 7:h_step * 8, w_step * 7:w_step * 8]
            wR_b = board[h_step * 7:h_step * 8, w_step * 0:w_step * 1]
            wN_b = board[h_step * 7:h_step * 8, w_step * 6:w_step * 7]
            wN_w = board[h_step * 7:h_step * 8, w_step * 1:w_step * 2]
            wB_w = board[h_step * 7:h_step * 8, w_step * 5:w_step * 6]
            wB_b = board[h_step * 7:h_step * 8, w_step * 2:w_step * 3]
            wQ_w = board[h_step * 7:h_step * 8, w_step * 3:w_step * 4]
            wQ_b = board[h_step * 5:h_step * 6, w_step * 4:w_step * 5]
            wK_w = board[h_step * 5:h_step * 6, w_step * 3:w_step * 4]
            wK_b = board[h_step * 7:h_step * 8, w_step * 4:w_step * 5]
            wp_w = board[h_step * 6:h_step * 7, w_step * 4:w_step * 5]
            wp_b = board[h_step * 6:h_step * 7, w_step * 3:w_step * 4]
            whites=[bR_w,bN_w,bK_w,bQ_w,bp_w,wR_w,wN_w,wK_w,wQ_w,wp_w,wB_w,bB_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w,emp_w]
            blacks=[bR_b,bN_b,bK_b,bQ_b,bp_b,wR_b,wN_b,wK_b,wQ_b,wp_b,wB_b,bB_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b,emp_b]
            sizes=[(160,160,3),(240,240,3),(320,320,3),(400,400,3),(480,480,3),(560,560,3),(640,640,3)]
            for k in range(200):
                size=random.choice(sizes)

                newimage = np.zeros(size, np.uint8)
                h_step=int(size[0]/8)
                w_step=int(size[1]/8)
                for i in range(8):
                    for j in range(8):
                        print(h_step, w_step, len(newimage))
                        wh_in=cv2.resize(random.choice(whites),(h_step,w_step))
                        bl_in=cv2.resize(random.choice(blacks),(h_step,w_step))
                        if((i+j)%2==0):
                            newimage[h_step * i:h_step * (i + 1), w_step * j:w_step * (j + 1)]= wh_in
                        else:
                            newimage[h_step * i:h_step * (i + 1), w_step * j:w_step * (j + 1)] = bl_in

                newimage_blur=cv2.blur(newimage,(5,5))
                newimage = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
                newimage_blur= cv2.cvtColor(newimage_blur, cv2.COLOR_BGR2GRAY)

                cv2.imwrite("Good/"+str(ind)+str(k)+'.jpg',newimage)
                cv2.imwrite("Good/"+str(ind)+str(k)+'b.jpg',newimage_blur)
            ind+=1
        dir = os.listdir('add_figures')
        ind = 1
        for i in dir:
             newimage = cv2.imread('add_figures/' + i)
             newimage = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
             cv2.imwrite("Bad/a" + str(ind) + 'j.jpg', newimage)
             ind+=1

    def haarCascadeMakeFile(self):
        fileGood=open("Good.dat",'w')
        fileBad=open("Bad.dat",'w')
        dir=os.listdir('Good')
        for i in dir:
            img=cv2.imread('Good/'+i)
            h,w,s=img.shape
            fileGood.write("Good\\"+i+" 1 0 0 "+str(w)+' '+str(h)+'\n')
        dir = os.listdir('Bad')
        for i in dir:
            fileBad.write("Bad\\" + i +'\n')




    #Не работает
    def deterctBoardbyHaar(self,img):#not working
        image=img.copy()
        cascade=cv2.CascadeClassifier('cascade.xml')
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.namedWindow('i', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('i', 400, 400)
        cv2.imshow("i", image)

        boards=cascade.detectMultiScale(image,minNeighbors= 30,minSize=(100,100))
        print(len(boards))
        for (sx, sy, sw, sh) in boards:
            print(sx, sy, sw, sh)
            cv2.rectangle(img, (sx, sy), ((sx + sw), (sy + sh)), (0, 255, 0), 3)
        cv2.namedWindow('b', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('b', 400, 400)
        cv2.imshow("b", img)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()##


    def detectBoard(self,img):
        img2 = img.copy()

        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        у, img2 = cv2.threshold(img2, 200, 130, 40)
        template = cv2.imread('board.png', 0)
        w, h = template.shape[::-1]
        self.board_width = w
        self.board_height = h
        # cv2.namedWindow('board2', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('board2', 400, 400)
        # cv2.namedWindow('board3', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('board3', 400, 400)
        # cv2.imshow("board2", template)
        # cv2.imshow("board3", img2)

        # All the 6 methods for comparison in a list
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
        # Apply template Matching
        res = cv2.matchTemplate(img2, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        top_left = max_loc
        self.x_m, self.y_m = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        board = img[top_left[1]:top_left[1] + h, top_left[0]+1:top_left[0] + w]
        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        # cv2.namedWindow('board', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('board', 400, 400)
        # cv2.imshow("board", img)
        # cv2.namedWindow('c', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('c', 120, 120)
        # cv2.imshow('c',board)
        # cv2.waitKey(0)
        return board

    def getBoardbyHand(self):# ждём 2 координаты
        while len(self.boardXY)<2:
            pass


    def detectBoardbyHand(self,img):
        img2 = img.copy()
        print(self.boardXY)
        board=img2[self.boardXY[0].y:self.boardXY[1].y,self.boardXY[0].x:self.boardXY[1].x]
        self.board_width=abs(self.boardXY[0].x-self.boardXY[1].x)
        self.board_height=abs(self.boardXY[0].y-self.boardXY[1].y)
        self.x_m=self.boardXY[0].x
        self.y_m=self.boardXY[0].y
        # cv2.namedWindow('c', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('c', 240, 240)
        # cv2.imshow('c',board)
        # cv2.waitKey(0)
        return board


    def get_Pos(self,board):
        print()
        height, width, bb = board.shape[:]
        # cv2.imshow('b', board)
        # cv2.waitKey(0)
        w_step = int(width/8)
        h_step = int((height+1)/8)
        print("высота ширина board",height,width)
        board = cv2.cvtColor(board, 0)
        board = cv2.resize(board, (w_step * 8, h_step * 8))
        height, width, bb = board.shape[:]
        print("w h steps",w_step,h_step)
        fig = ''
        mas = []
        ts = time.time()
        for i in range(8):
            for j in range(8):
                d = []
                fig = board[h_step * i:h_step * (i + 1)-1, w_step * j+1:w_step * (j + 1)]
                # print(fig.shape)
                fig=cv2.cvtColor(fig,cv2.COLOR_BGR2GRAY)
                # cv2.namedWindow('fig', cv2.WINDOW_NORMAL)
                # cv2.resizeWindow('fig', 128, 128)
                # cv2.imshow('fig', fig)
                # cv2.waitKey(0)

                fig = cv2.resize(fig, (32, 32))# менять для разных нейросетей


                # predictFig(model,[t],onlycheck=True)
                mas.append(fig)
        # ind=0
        # for p in ph:
        #     cv2.imwrite("emptys/"+str(ind)+'.PNG',p)
        #     ind+=1
        # print(mas.__len__())
        # predictFig(model,mas
        print(len(mas))
        return np.array(mas,dtype="float").reshape(-1,32,32,1) / 255.0


    def toFen(self,pos):
        fen = ''
        for lines in range(8):
            pr_emp = False
            num = 0
            for i in pos[lines * 8:lines * 8 + 8]:
                if (i[0] == 'b'):
                    if (pr_emp):
                        fen += str(num)
                    pr_emp = False
                    fen += str(i[1]).lower()
                    num = 0
                elif (i[0] == 'w'):
                    if (pr_emp):
                        fen += str(num)
                    pr_emp = False
                    fen += str(i[1]).upper()
                    num = 0
                elif (i == 'emp'):
                    pr_emp = True
                    num += 1
            if (pr_emp == True):
                fen += str(num)

            fen += '/'

        print(fen[:len(fen) - 1])
        return fen[:len(fen) - 1]



    def getbestMove(self,fen, movenum=0):
            if(movenum%2==1):
                self.move='w'
            else:self.move='b'

            self.set_move()# Показываем чей ход по компу

            self.bestmoves=[]
            depth=self.depth=str(self.mainwindow.ui.spinBox.value())
            print(self.depth)
            stockfish = subprocess.Popen(["stockfish_20011801_x64_modern.exe"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                         universal_newlines=True)
            stockfish.stdin.write("uci\n")
            stockfish.stdin.flush()
            stockfish.stdin.write("setoption name Contempt value 100\n")
            stockfish.stdin.flush()
            stockfish.stdin.write("setoption name Threads value 4\n")
            stockfish.stdin.flush()
            stockfish.stdin.write("position fen " + fen + ' ' + self.move + ' -- - 0 1' + "\ngo infinite\n ")
            stockfish.stdin.flush()
            already_dep=False
            print('cycle')
            lines=[]
            wasUci=False
            for i in range(60):#Ограничение по выходу из цикла: 25 опций,1 лучший ход, остаётся 34 на глубину
                line = stockfish.stdout.readline()
                lines.append(line)
                # print(line)
                if(line=='uciok'):
                    wasUci=True
                if ((line.__len__() <=1) and wasUci):
                    print('exit')
                    break
                if (line.__contains__('depth')):
                    already_dep=True
                    if (line.split()[2] ==str(depth)):
                        break
            stockfish.stdin.write("stop\n")
            stockfish.stdin.flush()
            stockfish.stdin.close()
            for i in stockfish.stdout.readlines():
                print('in read')
                if(i.__contains__('bestmove')):
                    lines.append(i)
            lastLine_dep = ""
            lastLine = ""
            pos = ""
            mas = []
            use_lines=[]
            print("length",len(lines))
            for i in range(len(lines)):
                if(len(lines[i])>5):
                    use_lines.append(lines[i])

            for line in use_lines:
                lastLine=line
                if(line.__contains__('info')):
                    lastLine_dep=line
                print(line)
            if(lastLine_dep.__contains__('cp')):
                self.est = lastLine_dep.split(' ')[9]
                self.est = str(float(self.est) / 100)
            if (lastLine_dep.__contains__('mate')):
                self.est ='m '+ lastLine_dep.split(' ')[9]
            mas.append(lastLine.split(' ')[1])
            self.bestmoves.append(mas)


            print('est',self.est)
            print(self.bestmoves[0][0])
            self.mainwindow.ui.button_move1.setText(self.bestmoves[0][0])
            # self.mainwindow.ui.button_move2.setText(bestmoves[1])
            # self.mainwindow.ui.button_move3.setText(bestmoves[2])
            return self.bestmoves[0][0]


    def make_move(self,m):
        # self.getbestMove(self.prev_fen)
        try:
             print(self.board_height, self.board_width)
             wid_step = round(self.board_width / 8.0)
             hei_step = round(self.board_height / 8.0)
             dx_mouse = round(wid_step / 2)
             dy_mouse = round(hei_step / 2)
             print(m)
             f1,f2,f3,f4=m[0:4]
             print(self.board_height, self.board_width, wid_step, hei_step, dx_mouse, dy_mouse)

             print('white', self.white_m, self.movenum)
             if (self.side == 'w'):
                 wid_fr = (int(ord(f1)) - 97) * wid_step
                 hei_fr = (7 - (int(f2) - 1)) * hei_step
                 wid_to = (int(ord(f3)) - 97) * wid_step
                 hei_to = (7 - (int(f4) - 1)) * hei_step
             else:
                 print(m[0])
                 wid_fr = (7-(int(ord(f1)) - 97) )* wid_step
                 hei_fr = ((int(f2) - 1)) * hei_step
                 wid_to = (7-(int(ord(f3)) - 97)) * wid_step
                 hei_to = ((int(f4) - 1)) * hei_step
             xf = wid_fr + self.x_m + dx_mouse
             yf = hei_fr + self.y_m + dy_mouse
             xt = wid_to + self.x_m + dx_mouse
             yt = hei_to + self.y_m + dy_mouse
             print(m, self.x_m, self.y_m, wid_fr, hei_fr, wid_to, hei_to, xf, yf, xt, yt)
             pag.moveTo(xf, yf)
             pag.dragTo(xt, yt)
        except:
            print('ggg')

    def set_estimation(self):
        if (self.side == self.move and float(self.est) >= 0):
            self.mainwindow.ui.lineEdit_est.setStyleSheet("""
                                                font:bold 12px;
                                                background-color:rgba(0,255,0,0.8);
                                                """)
        else:
            self.mainwindow.ui.lineEdit_est.setStyleSheet("""
                                                font:bold 12px;
                                                background-color:rgba(255,0,0,0.9);""")
    def set_move(self):
        # self.mainwindow.ui.lineEdit_move.setStyleSheet("""
        #                                                 font:bold;
        #                                                 background-color:rgba(250,250,255,0.9);"""
        #                                                if self.move == 'w' else """
        #                                                     font:bold 12px;
        #                                                     background-color:rgba(0,0,0,0.8);"""
        #                                                )
        self.mainwindow.ui.lineEdit_move.setText('Move white' if self.move == 'w' else 'Move black')
        self.mainwindow.ui.lineEdit_est.setText(self.est)

    def run(self):
         listener= keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
         listener.start()
         self.mainwindow.ui.spinBox.setValue(16)
         # side=input("Сторона снизу")
         model = keras.models.load_model("chessFigConv.h5")
         width = pag.screenshot().width
         height = pag.screenshot().height
         print(width, height)
         self.getBoardbyHand()
         with mss.mss() as sct:
             # Part of the screen to capture
             monitor = {"top": 0, "left": 0, "width": width, "height": height}

             while "Screen capturing" :
               if(not self.pause):
                 last_time = time.time()
                 img = np.array(sct.grab(monitor))
                 # cv2.imshow("OpenCV/Numpy normal", img)

                 board = self.detectBoardbyHand(img)  # найти доску
                 mas = self.get_Pos(board)  # вычисляем позицию
                 position = []
                 ind=0
                 # нейросеть находит позицию

                 predictions=model.predict_classes(mas)
                 print(self.classes)
                 print(predictions)
                 for i in predictions:
                     position.append(self.classes[i])


                 print('position',position)
                 fen = self.toFen(position)  # преобразуем в fen

                 # timeThink=win.ui.ThinkdoubleSpinBox.value()
                 print('movenum ',self.movenum)
                 print('side ',self.side)
                 print('automove ',self.autoMove)
                 if(self.side=='b'):# движок не различает стороны поэтому переворачиваем если за черных
                     newfen=''
                     st=fen.split('/')
                     list.reverse(st)
                     for i in st:
                         newfen+=i[::-1]+'/'
                     newfen=newfen[0:len(newfen)-1]
                     fen=newfen

                 if (fen != self.prev_fen):
                    self.prev_fen = fen
                    self.movenum += 1

                 ts = time.time()
                 print('here')
                 try:
                    bestmove=self.getbestMove(fen,self.movenum)  # стокфишнаходит лучший ход и записывает его в глобальн
                 except:
                     print('mistake')
                 print("ааеук")
                 tf = time.time()
                 print("stockfish working time", tf - ts)
                 print('depth',self.depth,self.est,type(self.est))

                 self.set_estimation()# устанавливаем оценку

                 print("movenum",self.movenum)
                 if(self.side==self.move and self.autoMove):
                        self.make_move(bestmove)

                 print("fps: {}".format(1 / (time.time() - last_time)))




    def on_press(self,key):
        try:
            if key == keyboard.KeyCode.from_char('1'):
                self.mainwindow.make_move1()
            if  key == keyboard.KeyCode.from_char('+'):
                self.mainwindow.ui.spinBox.setValue(int(self.depth)+1)
            if  key == keyboard.KeyCode.from_char('-'):
                self.mainwindow.ui.spinBox.setValue(int(self.depth)-1)
            if key == keyboard.KeyCode.from_char('e'):
                self.boardXY.append(pag.position())
            if key == keyboard.KeyCode.from_char('w'):
                self.movenum+=1
            if key == keyboard.KeyCode.from_char('p'):
                if(self.pause==False):
                    self.pause=True
                else:self.pause=False
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(self,key):
        print('{0} released'.format(
            key))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    # Collect events until released







