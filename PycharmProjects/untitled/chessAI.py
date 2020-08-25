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
import pyautogui as pag
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





    def deterctBoardbyHaar(self,img):
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
            cv2.destroyAllWindows()


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
        board = img[top_left[1]:top_left[1] + h, top_left[0]:top_left[0] + w]
        cv2.rectangle(img, top_left, bottom_right, 255, 2)
        # cv2.namedWindow('board', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('board', 400, 400)
        # cv2.imshow("board", img)
        # cv2.namedWindow('c', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('c', 120, 120)
        # cv2.imshow('c',board)
        # cv2.waitKey(0)
        return board





    def get_Pos(self,board):
        print()
        height, width, bb = board.shape[:]
        # cv2.imshow('b', board)
        # cv2.waitKey(0)
        w_step = 32
        h_step = 32
        board = cv2.cvtColor(board, cv2.COLOR_BGRA2BGR)
        board = cv2.resize(board, (w_step * 8, h_step * 8))
        fig = ''
        mas = []
        ts = time.time()
        for i in range(8):
            for j in range(8):
                d = []
                fig = board[h_step * i:h_step * (i + 1), w_step * j:w_step * (j + 1)]
                # cv2.imshow('fig', fig)
                # cv2.waitKey(0)

                fig = cv2.resize(fig, (w_step, h_step)).flatten()


                # predictFig(model,[t],onlycheck=True)
                mas.append(fig)
        # ind=0
        # for p in ph:
        #     cv2.imwrite("emptys/"+str(ind)+'.PNG',p)
        #     ind+=1
        # print(mas.__len__())
        # predictFig(model,mas
        return np.array(mas,dtype="float") / 255.0


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
            move=self.side
            self.bestmoves=[]
            depth=self.depth=str(self.mainwindow.ui.spinBox.value())
            print(self.depth)
            stockfish = subprocess.Popen(["stockfish_20011801_x64_modern"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                         universal_newlines=True)
            stockfish.stdin.write("uci\n")
            stockfish.stdin.flush()
            stockfish.stdin.write("setoption name Contempt value 100\n")
            stockfish.stdin.flush()
            stockfish.stdin.write("setoption name Threads value 4\n")
            stockfish.stdin.flush()
            stockfish.stdin.write("position fen " + fen + ' ' + move + ' -- - 0 1' + "\ngo infinite\n ")
            stockfish.stdin.flush()
            already_dep=False
            print('cycle')
            lines=[]
            wasUci=False
            while True:
                line = stockfish.stdout.readline()
                lines.append(line)
                print(line)
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


    def run(self):
         listener= keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
         listener.start()
         self.mainwindow.ui.spinBox.setValue(16)
         # side=input("Сторона снизу")
         model = keras.models.load_model("chessFigUltimate_2.h5")
         width = pag.screenshot().width
         height = pag.screenshot().height
         print(width, height)
         with mss.mss() as sct:
             # Part of the screen to capture
             monitor = {"top": 0, "left": 0, "width": width, "height": height}


             while "Screen capturing" :
                 last_time = time.time()
                 img = np.array(sct.grab(monitor))
                 # cv2.imshow("OpenCV/Numpy normal", img)

                 board = self.detectBoard(img)  # найти доску

                 mas = self.get_Pos(board)  # вычисляем позицию
                 position = []
                 ind=0
                 # нейросеть находит позицию

                 predictions=model.predict_classes(mas)
                 for i in predictions:
                     position.append(self.classes[i])


                 fen = self.toFen(position)  # преобразуем в fen

                 # timeThink=win.ui.ThinkdoubleSpinBox.value()
                 print('movenum ',self.movenum)
                 print('side ',self.side)
                 print('automove ',self.autoMove)
                 if(self.side=='b'):
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
                        if(self.movenum%2==1):
                            bestmove=self.getbestMove(fen,self.movenum)  # стокфишнаходит лучший ход и записывает его в глобальн
                     except:
                         print('mistake')
                     print("ааеук")
                     tf = time.time()
                     print("stockfish", tf - ts)
                     print('depth',self.depth,self.est)
                     self.mainwindow.ui.lineEdit_est.setText(self.est)


                     if(self.movenum%2==1 and self.autoMove):
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






class AI():
    figures = ['bB_w.PNG', 'bK_w.PNG', 'bN_w.PNG', 'bp_w.PNG', 'bQ_w.PNG', 'bR_w.PNG', 'wB_w.PNG', 'wK_w.PNG',
               'wN_w.PNG', 'wp_w.PNG', 'wQ_w.PNG', 'wR_w.PNG', 'emp_w.PNG',
               'bB_b.PNG', 'bK_b.PNG', 'bN_b.PNG', 'bp_b.PNG', 'bQ_b.PNG', 'bR_b.PNG', 'wB_b.PNG', 'wK_b.PNG',
               'wN_b.PNG', 'wp_b.PNG', 'wQ_b.PNG', 'wR_b.PNG', 'emp_b.PNG'
               ]
    classes = [i.split('_')[0] for i in figures]
    classes = list(np.unique(classes))

    def imagePre(self,dir):
        global data, labels, data2
        name = dir
        dir = os.listdir(dir)
        print(dir)
        for i in dir:
            print(name + '/' + i)
            image = cv2.imread(name + '/' + i)
            data2.append(image)
            # cv2.imshow('f', image)
            # cv2.waitKey(0)
            image = cv2.resize(image, (8, 8)).flatten()
            data.append(image)
            labels.append(i.split('_')[0])

            image = cv2.imread(name + '/' + i)
            data2.append(image)
            # cv2.imshow('f', image)
            # cv2.waitKey(0)
            image = cv2.blur(image, (3, 3))
            image = cv2.resize(image, (8, 8)).flatten()
            data.append(image)
            labels.append(i.split('_')[0])

            for l in range(2):

                image = cv2.imread(name + '/' + i)
                data2.append(image)
                height, width, bb = image.shape
                factor = random.randint(-(l + 2) * 5 - 3, (l + 2) * 5 + 3)
                for k in range(height):
                    for j in range(width):
                        a = image[k][j][0] + factor
                        b = image[k][j][1] + factor
                        c = image[k][j][2] + factor
                        if (a < 0):
                            a = 0
                        if (b < 0):
                            b = 0
                        if (c < 0):
                            c = 0
                        if (a > 255):
                            a = 255
                        if (b > 255):
                            b = 255
                        if (c > 255):
                            c = 255
                        image[k][j] = (a, b, c)
                # cv2.imshow('f',image)
                # cv2.waitKey(0)
                image = cv2.resize(image, (8, 8)).flatten()
                data.append(image)
                labels.append(i.split('_')[0])

                image = cv2.imread(name + '/' + i)
                data2.append(image)
                height, width, bb = image.shape
                factor = random.randint(5 * (l) + 5, (l + 1) * 15)
                for k in range(height):
                    for j in range(width):
                        rand = random.randint(-factor, factor)
                        a = image[k][j][0] + rand
                        b = image[k][j][1] + rand
                        c = image[k][j][2] + rand
                        if (a < 0):
                            a = 0
                        if (b < 0):
                            b = 0
                        if (c < 0):
                            c = 0
                        if (a > 255):
                            a = 255
                        if (b > 255):
                            b = 255
                        if (c > 255):
                            c = 255
                        image[k][j] = (a, b, c)
                # cv2.imshow('f',image)
                # cv2.waitKey(0)
                image = cv2.resize(image, (8, 8)).flatten()
                data.append(image)
                labels.append(i.split('_')[0])

    data = []
    labels = []
    data2 = []

    def getPicturesFromStartPosistion(self,board, num_of_Board):
        board = cv2.cvtColor(board, cv2.COLOR_BGRA2BGR)

        board = cv2.resize(board, (64 * 8, 64 * 8))
        w_step = 64
        h_step = 64
        mas = []

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

        cv2.imwrite('add_figures/bR_w' + str(num_of_Board) + '1' + '.PNG', bR_w)
        cv2.imwrite('add_figures/bR_b' + str(num_of_Board) + '2' + '.PNG', bR_b)
        cv2.imwrite('add_figures/bK_w' + str(num_of_Board) + '3' + '.PNG', bK_w)
        cv2.imwrite('add_figures/bK_b' + str(num_of_Board) + '4' + '.PNG', bK_b)

        cv2.imwrite('add_figures/bN_w' + str(num_of_Board) + '5' + '.PNG', bN_w)
        cv2.imwrite('add_figures/bN_b' + str(num_of_Board) + '6' + '.PNG', bN_b)
        cv2.imwrite('add_figures/bB_w' + str(num_of_Board) + '7' + '.PNG', bB_w)
        cv2.imwrite('add_figures/bB_b' + str(num_of_Board) + '8' + '.PNG', bB_b)

        cv2.imwrite('add_figures/bQ_w' + str(num_of_Board) + '9' + '.PNG', bQ_w)
        cv2.imwrite('add_figures/bQ_b' + str(num_of_Board) + '10' + '.PNG', bQ_b)
        cv2.imwrite('add_figures/bp_w' + str(num_of_Board) + '11' + '.PNG', bp_w)
        cv2.imwrite('add_figures/bp_b' + str(num_of_Board) + '12' + '.PNG', bp_b)

        cv2.imwrite('add_figures/wR_w' + str(num_of_Board) + '13' + '.PNG', wR_w)
        cv2.imwrite('add_figures/wR_b' + str(num_of_Board) + '14' + '.PNG', wR_b)
        cv2.imwrite('add_figures/wK_w' + str(num_of_Board) + '15' + '.PNG', wK_w)
        cv2.imwrite('add_figures/wK_b' + str(num_of_Board) + '16' + '.PNG', wK_b)

        cv2.imwrite('add_figures/wN_w' + str(num_of_Board) + '17' + '.PNG', wN_w)
        cv2.imwrite('add_figures/wN_b' + str(num_of_Board) + '18' + '.PNG', wN_b)
        cv2.imwrite('add_figures/wB_w' + str(num_of_Board) + '19' + '.PNG', wB_w)
        cv2.imwrite('add_figures/wB_b' + str(num_of_Board) + '20' + '.PNG', wB_b)

        cv2.imwrite('add_figures/wQ_w' + str(num_of_Board) + '21' + '.PNG', wQ_w)
        cv2.imwrite('add_figures/wQ_b' + str(num_of_Board) + '22' + '.PNG', wQ_b)
        cv2.imwrite('add_figures/wp_w' + str(num_of_Board) + '23' + '.PNG', wp_w)
        cv2.imwrite('add_figures/wp_b' + str(num_of_Board) + '24' + '.PNG', wp_b)

        cv2.imwrite('add_figures/emp_w' + str(num_of_Board) + '25' + '.PNG', emp_w)
        cv2.imwrite('add_figures/emp_b' + str(num_of_Board) + '26' + '.PNG', emp_b)

    def loadToDir_add_figures(self,nameDirFr='boardsForTrain'):
        dir = os.listdir(nameDirFr)
        ind = 1
        for i in dir:
            board = cv2.imread(nameDirFr + '/' + i)
            self.getPicturesFromStartPosistion(board, ind)
            ind += 1

    def contTrainNet(self,model, dir='add_figures'):
        data = []
        labels = []
        data2 = []
        name = dir
        dir = os.listdir(dir)
        print(dir)
        for i in dir:
            print(name + '/' + i)
            image = cv2.imread(name + '/' + i)
            data2.append(image)
            # cv2.imshow('f', image)
            # cv2.waitKey(0)
            image = cv2.resize(image, (32, 32)).flatten()
            data.append(image)
            labels.append(i.split('_')[0])
        data *= 40
        labels *= 40
        data2 *= 40
        random.seed(10)
        a = data
        b = labels
        a2 = data2
        c = list(zip(a, b))
        c2 = list(zip(a2, b))
        random.shuffle(c)
        random.seed(10)
        random.shuffle(c2)
        data, labels = zip(*c)
        data2, labels = zip(*c2)

        print(len(data))
        for i in range(len(data)):
            print(labels[i])
            # cv2.imshow("rt",data2[i])
            # cv2.waitKey(0)
        data = np.array(data, dtype="float") / 255.0
        labels = np.array(labels)
        (trainX, testX, trainY, testY) = train_test_split(data,
                                                          labels, test_size=0.25, random_state=10)
        lb = LabelBinarizer()
        EPOCHS = 50
        trainY_or = list.copy(list(trainY))
        trainY = lb.fit_transform(trainY)
        testY = lb.transform(testY)
        H = model.fit(trainX, trainY, validation_data=(testX, testY),
                      epochs=EPOCHS, batch_size=32)

        # оцениваем нейросеть
        print(" evaluating network...")
        predictions = model.predict(testX)
        print(classification_report(testY.argmax(axis=1),
                                    predictions.argmax(axis=1)))
        model.save("chessFigUltimate_2.h5")


    def trainNet(self):
        random.seed(10)
        global data, labels, data2
        self.imagePre('w_pawns')
        self.imagePre('w_Nights')
        self.imagePre('w_Rooks')
        self.imagePre('w_Queens')
        self.imagePre('w_Bishops')
        self.imagePre('w_Kings')
        self.imagePre('emp')
        self.imagePre('b_pawns')
        self.imagePre('b_Nights')
        self.imagePre('b_Rooks')
        self.imagePre('b_Queens')
        self.imagePre('b_Bishops')
        self.imagePre('b_Kings')
        self.imagePre("emptys")
        self.imagePre("add_figures")

        data *= 50
        labels *= 50
        data2 *= 50

        # shake (data2 для проверки)
        random.seed(10)
        a = data
        b = labels
        a2 = data2
        c = list(zip(a, b))
        c2 = list(zip(a2, b))
        random.shuffle(c)
        random.seed(10)
        random.shuffle(c2)
        data, labels = zip(*c)
        data2, labels = zip(*c2)

        print(len(data))
        # for i in range(len(data)):
        #     print(labels[i])
        #     cv2.imshow("rt",data2[i])
        #     cv2.waitKey(0)
        data = np.array(data, dtype="float") / 255.0
        labels = np.array(labels)
        (trainX, testX, trainY, testY) = train_test_split(data,
                                                          labels, test_size=0.25, random_state=10)
        lb = LabelBinarizer()
        trainY_or = list.copy(list(trainY))
        trainY = lb.fit_transform(trainY)
        testY = lb.transform(testY)

        model = keras.Sequential()
        model.add(keras.layers.Dense(16, input_shape=(8 * 8 * 3,), activation="sigmoid", use_bias=True))
        model.add(keras.layers.Dense(16, activation="sigmoid"))
        model.add(keras.layers.Dense(len(self.classes), activation="sigmoid"))

        # инициализируем скорость обучения и общее число эпох
        INIT_LR = 0.001
        EPOCHS = 400

        # компилируем модель, используя SGD как оптимизатор и категориальную
        # кросс-энтропию в качестве функции потерь (для бинарной классификации
        # следует использовать binary_crossentropy)
        print(" training network...")
        opt = keras.optimizers.SGD(lr=INIT_LR)
        model.compile(loss='categorical_crossentropy', optimizer=opt,
                      metrics=['accuracy'])

        H = model.fit(trainX, trainY, validation_data=(testX, testY),
                      epochs=EPOCHS, batch_size=32)

        # оцениваем нейросеть
        print(" evaluating network...")
        predictions = model.predict(testX)
        print(classification_report(testY.argmax(axis=1),
                                    predictions.argmax(axis=1)))
        model.save("chessFigUltimate_light.h5")
        print(model.summary())







class AI_findTable():

    def __init__(self):
        pass
    def createScreens(self):
        dir = os.listdir('boardsForTrain')
        ind = 1
        width = pag.screenshot().width
        height = pag.screenshot().height
        size = (height, width, 3)
        newimage = np.zeros(size, np.uint8)

        for i in range(height):
            for j in range(width):
                newimage[i][j] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.imwrite('Screenshots/sc.png',newimage)
        orimage=newimage.copy()
        for i in dir:
            print(i)
            board = cv2.imread('boardsForTrain/' + i)
            board = cv2.resize(board, (800, 800))
            h_step = 100
            w_step = 100

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
            whites = [bR_w, bN_w, bK_w, bQ_w, bp_w, wR_w, wN_w, wK_w, wQ_w, wp_w, wB_w, bB_w, emp_w, emp_w, emp_w,
                      emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w]
            blacks = [bR_b, bN_b, bK_b, bQ_b, bp_b, wR_b, wN_b, wK_b, wQ_b, wp_b, wB_b, bB_b, emp_b, emp_b, emp_b,
                      emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b]
            sizes_boards=[]
            scre=os.listdir('Screenshots')

            for i in range(95):
                sizes_boards.append((120+i*10,120+i*10,3))
            for sc in scre:
                width = pag.screenshot().width
                height = pag.screenshot().height
                size = (height, width, 3)
                newimage = cv2.imread('Screenshots/'+sc)
                orimage = newimage.copy()
                for k in range(20):
                    board_size=random.choice(sizes_boards)
                    print(width,board_size[1],height,board_size[0])
                    for m in range(10):
                        newimage=orimage.copy()
                        start_x = random.randint(1, width - board_size[1]-1)
                        start_y = random.randint(1, height-board_size[0] - 1)
                        h_step = int(board_size[0] / 8)
                        w_step = int(board_size[1] / 8)

                        for i in range(8):
                            for j in range(8):
                                print(h_step, w_step, len(newimage))
                                wh_in = cv2.resize(random.choice(whites), (h_step, w_step))
                                bl_in = cv2.resize(random.choice(blacks), (h_step, w_step))
                                if ((i + j) % 2 == 0):
                                    newimage[start_y+(h_step * i):start_y+(h_step * (i + 1)), start_x+(w_step * j):start_x+(w_step * (j + 1))] = wh_in
                                else:
                                    newimage[start_y+(h_step * i):start_y+(h_step * (i + 1)),start_x+(w_step * j):start_x+(w_step * (j + 1))] = bl_in

                        # cv2.imshow('g', newimage)
                        # cv2.waitKey(0)
                        n_w=32
                        n_h=32
                        k_w=1920/n_w
                        k_h=1080/n_h
                        newimage=cv2.resize(newimage,(n_h,n_w))
                        newimage=cv2.cvtColor(newimage,cv2.COLOR_BGRA2GRAY)
                        cv2.imwrite("Screens/" + str(ind) + str(k) + str(m)+'_'+str(int(start_y/k_h))+"_"+str(int(start_x/k_w))+"_"+str(int(board_size[0]/k_h))+"_"+str(int(board_size[1]/k_w))+"_"+'.PNG', newimage)
                        ind += 1
            break
    def train(self):
        random.seed(10)
        data=[]
        labels=[]
        data2=[]
        dir=os.listdir("Screens")
        ind=1
        for i in dir:
            # if(ind==100):break
            print(ind,i)
            img=cv2.imread('Screens/'+i,0)
            data.append(img)
            data2.append(img)
            labs=i.split('_')
            labels.append((int(labs[1])/32,int(labs[2])/32,(int(labs[1])+int(labs[3]))/32,(int(labs[2])+int(labs[4]))/32))
            ind+=1

        data *= 10
        labels *= 10
        data2 *= 10

        # shake (data2 для проверки)
        random.seed(10)
        a = data
        b = labels
        a2 = data2
        c = list(zip(a, b))
        c2 = list(zip(a2, b))
        random.shuffle(c)
        random.seed(10)
        random.shuffle(c2)
        data, labels = zip(*c)
        data2, labels = zip(*c2)

        print(len(data))
        # for i in range(len(data)):
        #     print(labels[i])
        #     cv2.imshow("rt",data2[i])
        #     cv2.waitKey(0)
        data = np.array(data, dtype="float")
        labels = np.around(np.array(labels),decimals=3)
        print(data.shape)
        data=data.reshape((len(data),32,32,1))
        print(data)
        print(labels)
        (trainX, testX, trainY, testY) = train_test_split(data,
                                                          labels, test_size=0.25, random_state=10)
        lb = LabelBinarizer()
        # trainY_or = list.copy(list(trainY))
        # trainY = lb.fit_transform(trainY)
        # testY = lb.transform(testY)
        print(keras.backend.epsilon())
        # keras.backend.set_epsilon(1e-3)
        print(keras.backend.epsilon())
        model = keras.Sequential()
        model.add(keras.layers.Conv2D(32,kernel_size=3,activation='relu',))
        model.add(keras.layers.Conv2D(32, kernel_size=3, activation='relu', ))
        model.add(keras.layers.MaxPooling2D())
        model.add(keras.layers.Conv2D(16, kernel_size=3, activation='relu', ))
        model.add(keras.layers.Conv2D(16, kernel_size=3, activation='relu', ))
        model.add(keras.layers.MaxPooling2D())
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(64, activation='softmax'))
        model.add(keras.layers.Dense(4,activation='softmax'))

        # инициализируем скорость обучения и общее число эпох
        INIT_LR = 0.001
        EPOCHS = 100

        # компилируем модель, используя SGD как оптимизатор и категориальную
        # кросс-энтропию в качестве функции потерь (для бинарной классификации
        # следует использовать binary_crossentropy)
        print(" training network...")
        opt = keras.optimizers.SGD(lr=INIT_LR)
        model.compile(loss='categorical_crossentropy', optimizer=opt,
                      metrics=['accuracy','mae'])

        history = model.fit(trainX, trainY, validation_data=(testX, testY),
                      epochs=EPOCHS, batch_size=16)

        # оцениваем нейросеть
        print(" evaluating network...")
        predictions = model.predict(testX)
        print(classification_report(testY.argmax(axis=1),
                                    predictions.argmax(axis=1)))
        model.save("board_rec.h5")
        print(model.summary())
        import matplotlib.pyplot as plt
        # Plot training & validation accuracy values
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()
        #
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('Model loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()




# screen_rec=AI_findTable()

#
# screen_rec.createScreens()
# screen_rec.train()
# model= keras.models.load_model('board_rec.h5')
# with mss.mss() as sct:
#     # Part of the screen to capture
#     monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}
#
#     while True:
#         img = np.array(sct.grab(monitor))
#         orimg=img.copy()
#         img=cv2.resize(img,(32,32))
#         img=cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
#         mas=[img]
#         mas=np.array([img/255.0])
#         print(mas)
#         pred=model.predict(mas)
#         print(pred)
#         y=int(pred[0][0]*1080)
#         x=int(pred[0][1]*1920)
#         y2=int(pred[0][2]*1080)
#         x2=int(pred[0][3]*1920)
#         print('y',y,'x',x,'sh',y2,'sw',x2)
#         cv2.rectangle(orimg, (x,y), (x2,y2), 255, 2)
#         cv2.namedWindow('s', cv2.WINDOW_NORMAL)
#         cv2.resizeWindow('s', 400, 400)
#         cv2.imshow("s", orimg)
#         cv2.waitKey(0)
#         print(pred)

