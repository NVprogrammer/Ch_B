from bs4 import BeautifulSoup
from selenium import webdriver
import time
# from PyQt5.QtWidgets import QApplication, QWidget
# import chessbotFrame
#
# if __name__=="__main__":
#     import sys
#
#     app = QApplication(sys.argv)
#     Form = QWidget()
#     ui = chessbotFrame.Ui_MainWindow()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
import subprocess
from multiprocessing import Process
import time
s=time.time()
stockfish = subprocess.Popen(["stockfish_20011801_x64_modern"], stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                              universal_newlines=True)
# output=subprocess.check_output(["stockfish_20011801_x64_modern"],  stdin=subprocess.PIPE,
#                              universal_newlines=True,timeout=0.5)
stockfish.stdin.write("uci\n")
stockfish.stdin.flush()
stockfish.stdin.write("setoption name Contempt value 10\n")
stockfish.stdin.flush()
stockfish.stdin.write("setoption name Threads value 8\n")
stockfish.stdin.flush()
stockfish.stdin.write("setoption name UCI_AnalyseMode value true\n")
stockfish.stdin.flush()
stockfish.stdin.write("position startpos moves e2e4" + "\ngo infinite\n ")
stockfish.stdin.flush()
while True:
    line =  stockfish.stdout.readline()
    if(line.__contains__('depth')):
        if(line.split()[2]=='24'):
            break


stockfish.stdin.write("stop\n")
stockfish.stdin.flush()
stockfish.stdin.close()
lastLine_dep = ""
lastLine_move = ""
pos = ""
arr = []
for line in stockfish.stdout.readlines():
    lastLine_move = line
    if (line.__contains__('info')):
        lastLine_dep = line
    print(line)
print(time.time()-s)
    
