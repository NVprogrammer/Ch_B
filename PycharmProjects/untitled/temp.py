import subprocess
import multiprocessing
import time
import tempfile
from concurrent import futures
import os
def pr(s):
        print(s)
if __name__=='__main__':
    ts=time.time()
    out = tempfile.NamedTemporaryFile(delete=False)
    inp = tempfile.NamedTemporaryFile(delete=False)
    stockfish = subprocess.Popen(['stockfish_20011801_x64_modern',"uci","position starpos moves e2e4",'go'],stdout=subprocess.PIPE,universal_newlines=True,shell=True)
    print(stockfish.communicate()[0])
    # stockfish.stdin.write("setoption name Contempt value 100\n")
    # stockfish.stdin.flush()
    # stockfish.stdin.write("setoption name Threads value 7\n")
    # stockfish.stdin.flush()
    # stockfish.stdin.write("setoption name UCI_AnalyseMode value true\n")
    # stockfish.stdin.flush()
    # stockfish.stdin.write("position starpos moves e2e4\n")
    # stockfish.stdin.flush()
    # stockfish.stdin.write("go depth 25\n")
    # stockfish.stdin.flush()
    time.sleep(1)
    stockfish_out = subprocess.Popen(['stockfish_20011801_x64_modern'], stdin=subprocess.PIPE, stdout=stockfish.stdout)
    # stockfish.stdout.close()

    print(stockfish_out.communicate()[0])
    # executor=futures.ProcessPoolExecutor(1)
    # while True:
    #     executor.submit(pr,stockfish_out.communicate()[0])


    # print(stockfish.communicate()[0])
    print(time.time()-ts)