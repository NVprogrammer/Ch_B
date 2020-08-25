
import time
import subprocess
from threading import Thread
position=[
["a8","bR"], ["b8","bN"], ["c8","bB"], ["d8","bQ"], ["e8","bK"], ["f8","bB"] ,["g8","bN"] ,["h8","bR"],
["a7","bp"], ["b7","bp"], ["c7","bp"], ["d7","bp"], ["e7","bp"], ["f7","bp"] ,["g7","bp"] ,["h7","bp"],
["a6"," "],   ["b6"," "], ["c6"," "], ["d6"," "], ["e6"," "], ["f6"," "] ,["g6"," "] ,["h6"," "],
["a5"," "],  ["b5"," "], ["c5"," "], ["d5"," "], ["e5"," "], ["f5"," "] ,["g5"," "] ,["h5"," "],
["a4"," "],  ["b4"," "], ["c4"," "], ["d4"," "], ["e4"," "], ["f4"," "] ,["g4"," "] ,["h4"," "],
["a3"," "],  ["b3"," "], ["c3"," "], ["d3"," "], ["e3"," "], ["f3"," "] ,["g3"," "] ,["h3"," "],
["a2","wp"], ["b2","wp"], ["c2","wp"], ["d2","wp"], ["e2","wp"], ["f2","wp"] ,["g2","wp"] ,["h2","wp"],
["a1","wR"], ["b1","wN"], ["c1","wB"], ["d1","wQ"], ["e1","wK"], ["f1","wB"] ,["g1","wN"] ,["h1","wR"]
]


def showpos(position):
    for i in range(64):
        if(i%8==0):
            print()
        s=position[i][1];
        if(s==' '):s='  '
        print('|'+s+'|',end='')



def changePosition(old,new):
    global position
    indexOld=0
    indexNew=0
    for i in range(len(position)):
        if(position[i][0]==old):
            indexOld=i
        elif (position[i][0] == new):
            indexNew = i
    position[indexNew][1]=position[indexOld][1]
    position[indexOld][1]=" "
def toUCI(str):

    try:
        global position,newstr
        position = [
            ["a8", "bR"], ["b8", "bN"], ["c8", "bB"], ["d8", "bQ"], ["e8", "bK"], ["f8", "bB"], ["g8", "bN"],["h8", "bR"],
            ["a7", "bp"], ["b7", "bp"], ["c7", "bp"], ["d7", "bp"], ["e7", "bp"], ["f7", "bp"], ["g7", "bp"],["h7", "bp"],
            ["a6", " "], ["b6", " "], ["c6", " "], ["d6", " "], ["e6", " "], ["f6", " "], ["g6", " "], ["h6", " "],
            ["a5", " "], ["b5", " "], ["c5", " "], ["d5", " "], ["e5", " "], ["f5", " "], ["g5", " "], ["h5", " "],
            ["a4", " "], ["b4", " "], ["c4", " "], ["d4", " "], ["e4", " "], ["f4", " "], ["g4", " "], ["h4", " "],
            ["a3", " "], ["b3", " "], ["c3", " "], ["d3", " "], ["e3", " "], ["f3", " "], ["g3", " "], ["h3", " "],
            ["a2", "wp"], ["b2", "wp"], ["c2", "wp"], ["d2", "wp"], ["e2", "wp"], ["f2", "wp"], ["g2", "wp"], ["h2", "wp"],
            ["a1", "wR"], ["b1", "wN"], ["c1", "wB"], ["d1", "wQ"], ["e1", "wK"], ["f1", "wB"], ["g1", "wN"],["h1", "wR"]
        ]
        str = str.replace("+","")
        str=str.strip()
        arr=str.split(" ")
        print(arr)
        newstr=""
        old=""
        new=""
        move=0
        for i in arr:
            if(i.__contains__("-") and len(i)==5):# рокировка в длинную
                if(move%2==0):
                    newstr+="e1c1"+" "
                    changePosition("e1","c1")
                    changePosition("a1","d1")
                else:
                    newstr += "e8c8"+" "
                    changePosition("e8", "c8")
                    changePosition("a8", "d8")

            elif(i.__contains__("-") and len(i)<5): #в короткую
                if (move % 2 == 0):
                    newstr += "e1g1"+" "
                    changePosition("e1", "g1")
                    changePosition("h1", "f1")
                else:
                    newstr += "e8g8"+" "
                    changePosition("e8", "g8")
                    changePosition("h8", "f8")
            elif(i.__contains__('=')):
                st=i.split('=')
                p=st[0]
                F=st[1]
                old,canproh=pawnUCI(p,move%2)
                new = p[len(p) - 2:]+F.lower()
                changePosition(old, new)
                ind=0
                for i in position:
                    if(i[0]==new[:len(new)-1]):
                        if(move%2==0):
                            position[ind][1]='w'+F
                        else:
                            position[ind][1]='b'+F
                    ind+=1
                newstr += old + new + " "

            elif(i[0] not in ["R","N","B","Q","K"]):# ход пешкой
                old,canproh=pawnUCI(i,move%2)
                new=i[len(i)-2:]
                #Взятие на проходе
                if(canproh):
                    for i in position:
                        if(i[0]==new and i[1]==' ' and old[0]!=new[0]):
                            if(move%2==0):
                                changePosition(new[0]+'5',new[0]+'5') # так как oldindex становится ' '. то это работает
                            else :
                                changePosition(new[0] + '4', new[0] + '4')
                changePosition(old,new)
                newstr+=old+new+" "
            elif(i[0]=="N"):
                old = KnightUCI(i, move % 2)
                new = i[len(i) - 2:]
                changePosition(old, new)
                newstr += old + new + " "
            elif (i[0] == "B"):
                old = BishopUCI(i, move % 2)
                new = i[len(i) - 2:]
                changePosition(old, new)
                newstr += old + new + " "
            elif (i[0] == "R"):
                old = RookUCI(i, move % 2)
                new = i[len(i) - 2:]
                changePosition(old, new)
                newstr += old + new + " "
            elif (i[0] == "Q"):
                old = QueenUCI(i, move % 2)
                new = i[len(i) - 2:]
                changePosition(old, new)
                newstr += old + new + " "
            elif (i[0] == "K"):
                old = KingUCI(i, move % 2)
                new = i[len(i) - 2:]
                changePosition(old, new)
                newstr += old + new + " "
            move+=1
        showpos(position)
        print()
    except Exception as e:
        pass
        #print(e)
    return newstr


def pawnUCI(s,move):
    # s- новая клетка, i- старая
    result="" # старая клетка
    canproh=False
    arr=findPawns(move)# находим все пешки одного цвета
    if(s[1]=="x"):
        canproh=True
        for i in arr:
            if(move==0):
                if(int(s[3])-int(i[1])==1 and s[0]==i[0]):
                    result=i
            elif(move==1):
                if (int(s[3]) - int(i[1]==-1) and s[0] == i[0]):
                    result = i
    else:
        for i in arr:
            if(move==0):
                if(int(s[1])-int(i[1])<=2 and s[0]==i[0]):#mistakes
                    result=i
            elif(move==1):
                if(int(s[1]) - int(i[1])>=-2 and s[0]==i[0]):
                    result=i
    return result,canproh

def KnightUCI(s,move):#not all
    result=""
    if(s[1]=="x"):
        arr=findKnights(move)
        for i in arr:
            if (abs(int(s[3]) - int(i[1])) == 1 and abs(ord(s[2]) - ord(i[0])) == 2 or abs(int(s[3]) - int(i[1])) == 2 and abs(ord(s[2]) - ord(i[0])) == 1):
                result = i
    elif(s[2]=="x"):
        arr = findKnights(move)
        for i in arr:
           if(s[1]==i[0] or s[2]==i[1]):
               result=i

    elif (len(s) == 4):
        arr = findKnights(move)
        for i in arr:
            if (s[1] == i[0] or s[1] == i[1]):
                result = i
    else:
        arr=findKnights(move)
        for i in arr:
            #print(int(s[2]),int(i[1]),ord(s[1]),ord(i[0]))
            if (abs(int(s[2]) - int(i[1])) == 1 and abs(ord(s[1]) - ord(i[0])) == 2 or abs(int(s[2]) - int(i[1])) == 2 and abs(ord(s[1]) - ord(i[0])) == 1
            ):
                result = i
    return result
def BishopUCI(s,move):
    result=""
    if(s[1]=="x"):
        arr=findBishops(move)
        for i in arr:
            if (abs(int(s[3]) - int(i[1]))  - abs(ord(s[2]) - ord(i[0])) ==0):
                result = i

    else:
        arr=findBishops(move)
        for i in arr:
            if (abs(int(s[2]) - int(i[1])) - abs(ord(s[1]) - ord(i[0])) == 0):
                result = i
    return result

def RookUCI(s,move):#not all
    result=""
    arr=findRooks(move)
    print('RookMove')
    if(s[1]=="x"):
        for i in arr:
            T = reachableForRook(s[3], i[1], s[2], i[0])
            if ((s[3]) == i[1] or ord(s[2])== ord(i[0]) and T):
                result = i
    elif(s[2]=="x"):
        for i in arr:
           if((s[4]==i[1] or s[3]==i[0]) and (s[1] == i[0] or s[1] == i[1])):
               result=i
    elif(len(s)==4):
        for i in arr:
            if (s[1] == i[0] or s[1] == i[1]):# ПО ВЕРТИКАЛИ И ПО ГОРИЗОНТАЛИ
                result = i
    else:
        print("Im",arr)

        for i in arr:
            T = reachableForRook(s[2], i[1], s[1], i[0])
            if((s[1]==i[0] or s[2]==i[1]) and T):
                result=i
    return result

def QueenUCI(s,move):
    result=""
    arr=findQueen(move)
    for i in arr:
        result = i
    return result
def KingUCI(s,move):
    result=""
    arr=findKing(move)
    for i in arr:
        result = i
    return result


def findPawns(move=0):
    global position
    arr=[]
    for i in position:
        if(move==0 and i[1].__contains__("wp")):
            arr.append(i[0])
        elif(move==1 and i[1].__contains__("bp")):
            arr.append(i[0])
    return arr
def findKnights(move=0):
    global position
    arr=[]
    for i in position:
        if(move==0 and i[1].__contains__("wN")):
            arr.append(i[0])
        elif(move==1 and i[1].__contains__("bN")):
            arr.append(i[0])
    return arr
def findBishops(move=0):
    global position
    arr=[]
    for i in position:
        if(move==0 and i[1].__contains__("wB")):
            arr.append(i[0])
        elif(move==1 and i[1].__contains__("bB")):
            arr.append(i[0])
    return arr
def findRooks(move=0):
    global position
    arr=[]
    for i in position:
        if(move==0 and i[1].__contains__("wR")):
            arr.append(i[0])
        elif(move==1 and i[1].__contains__("bR")):
            arr.append(i[0])
    return arr
def reachableForRook(s2,i2,s1,i1):
    global position
    print("in re")
    old=i1+i2
    newstr=s1+s2
    oldIndex=0
    newIndex=0
    for i in range(len(position)):
        if(position[i][0]==old):
            oldIndex=i
        if (position[i][0] == newstr):
            newIndex = i
    print(newstr, newIndex)
    isReachL=False
    isReachR=False
    isReachU=False
    isReachD=False
    try:
        for i in range(1,8):# right
            print(oldIndex + i, position[oldIndex + i][1])
            if (oldIndex + i == newIndex):
                isReachR = True
                break
            elif( position[oldIndex+i][1]!=" " and oldIndex+i!=newIndex ):
                break
    except Exception:
        isReachR = False
    try:
        for i in range(1, 8): #left
            print(oldIndex - i,position[oldIndex - i][1])
            if (oldIndex - i == newIndex):
                isReachL = True
                break
            elif (position[oldIndex - i][1] != " " and oldIndex - i != newIndex):
                break

    except Exception:
        isReachL = False
    try:
        for i in range(1, 8):#down
            print(oldIndex + i*8, position[oldIndex + i*8][1])
            if (oldIndex + i*8 == newIndex):
                isReachD = True
                break
            elif (position[oldIndex + i*8][1] != " " and oldIndex + i*8 != newIndex):
                break
    except Exception:
        isReachD = False
    try:
        for i in range(1, 8):
            if (oldIndex - i * 8 == newIndex):
                isReachU = True
                break
            if (position[oldIndex - i * 8][1] != " " and oldIndex - i*8 != newIndex):
                break
    except Exception as e:
        isReachU = False
    print(isReachR,isReachL,isReachD,isReachU)
    return isReachR or isReachL or isReachD or isReachU

def findQueen(move=0):
    global position
    arr=[]
    for i in position:
        if(move==0 and i[1].__contains__("wQ")):
            arr.append(i[0])
        elif(move==1 and i[1].__contains__("bQ")):
            arr.append(i[0])
    return arr
def findKing(move=0):
    global position
    arr=[]
    for i in position:
        if(move==0 and i[1].__contains__("wK")):
            arr.append(i[0])
        elif(move==1 and i[1].__contains__("bK")):
            arr.append(i[0])
    return arr

stockfish=""
def getMove(str):
    global stockfish
    depth='16'
    stockfish = subprocess.Popen(["stockfish_20011801_x64_modern"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                 universal_newlines=True)
    stockfish.stdin.write("setoption name Contempt value 100")
    stockfish.stdin.flush()
    stockfish.stdin.write("setoption name Threads value 8")
    stockfish.stdin.flush()
    stockfish.stdin.write("uci\n")
    stockfish.stdin.flush()
    stockfish.stdin.write("position startpos moves " + str + "\ngo depth="+depth+"\n")
    stockfish.stdin.flush()
    time.sleep(1)
    stockfish.stdin.write("stop\n")
    stockfish.stdin.flush()
    stockfish.stdin.close()
    move=""
    pos=""
    print(str)
    arr=[]
    for line in stockfish.stdout.readlines():
        move=line
        if(line.__contains__("cp")):
            pos=line
    print(move)

    return pos[pos.find("cp")+2:pos.find("cp")+6],move.split(" ")[1]

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
def addToClipBoard(text):
    command = 'echo ' + text+ '| clip'
    os.system(command)

def toPGN(bestmove):
    global position
    try:
        old=bestmove[0:2]
        new=bestmove[2:4]

        fig=""
        for i in position:
            if(i[0]==old):
                fig=i[1][1]
                if(fig=="p"):
                    fig=""
                    ind=0
                    for j in position:
                        if(j[0]==new):
                            if(position[ind][1]!=' ' and old[0]!=new[0]):
                                new=old[0]+'x'+bestmove[2:4]
                        ind += 1
                if (fig == "K"):
                    if(old=='e1' and new=='g1'):
                        fig=''
                        new="0-0"
                    if (old == 'e1' and new == 'c1'):
                        fig = ''
                        new = "0-0-0"
                    if (old == 'e8' and new == 'g8'):
                        fig = ''
                        new = "0-0"
                    if (old == 'e8' and new == 'c8'):
                        fig = ''
                        new = "0-0-0"
                if(fig=='R' or fig=='N'):
                    fig+=old[0]
                break
    except :pass
    return fig+new

clipText=''
from pynput.keyboard import Key, Listener
def on_press(key):
    global clipText
    if key==Key.shift:
        print("HRE")
        print(clipText)
        clipText=clipText[0]+clipText[2:]
        addToClipBoard(clipText)
    if key==Key.insert:
        start()
def on_release(key):
    if key == Key.esc:
       pass

# Collect events until released
def clip():
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


def start():
    global stockfish,clipText
    print("Старт")
    var = Thread(target=clip)
    var.start()
    html = input()
    prevstr = "1"
    while True:
        r = urlopen(html).read()
        soup = BeautifulSoup(r, 'html.parser')
        table = soup.findAll("div", class_="pgn")
        strMoves = ""
        for i in table:
            strMoves = str(i.text)
        ind = strMoves.find("1.")
        strMoves = strMoves[ind:len(strMoves) - 1]
        strarr = strMoves.split(" ")
        strMoves = ""
        for i in strarr:
            if (not i.__contains__(".")):
                strMoves += i + " "

        strMoves = strMoves.lstrip()
        if (len(strMoves) > len(prevstr)):
            # strmoves=input()
            oc, bestmove = getMove(toUCI(strMoves))
            print(strMoves)
            # print(showpos(position))
            print(bestmove, oc)
            clipText = toPGN(bestmove)
            print(toPGN(bestmove))
            addToClipBoard(clipText)
            prevstr = strMoves
if __name__=="__main__":
    start()
