import cv2

def createPicturesForHaar(self):
    dir = os.listdir('boardsForTrain')
    ind = 1
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
        whites = [bR_w, bN_w, bK_w, bQ_w, bp_w, wR_w, wN_w, wK_w, wQ_w, wp_w, wB_w, bB_w, emp_w, emp_w, emp_w, emp_w,
                  emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w, emp_w]
        blacks = [bR_b, bN_b, bK_b, bQ_b, bp_b, wR_b, wN_b, wK_b, wQ_b, wp_b, wB_b, bB_b, emp_b, emp_b, emp_b, emp_b,
                  emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b, emp_b]
        sizes = [(160, 160, 3), (240, 240, 3), (320, 320, 3), (400, 400, 3), (480, 480, 3), (560, 560, 3),
                 (640, 640, 3)]
        for k in range(200):
            size = random.choice(sizes)

            newimage = np.zeros(size, np.uint8)
            h_step = int(size[0] / 8)
            w_step = int(size[1] / 8)
            for i in range(8):
                for j in range(8):
                    print(h_step, w_step, len(newimage))
                    wh_in = cv2.resize(random.choice(whites), (h_step, w_step))
                    bl_in = cv2.resize(random.choice(blacks), (h_step, w_step))
                    if ((i + j) % 2 == 0):
                        newimage[h_step * i:h_step * (i + 1), w_step * j:w_step * (j + 1)] = wh_in
                    else:
                        newimage[h_step * i:h_step * (i + 1), w_step * j:w_step * (j + 1)] = bl_in

            newimage_blur = cv2.blur(newimage, (5, 5))
            newimage = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
            newimage_blur = cv2.cvtColor(newimage_blur, cv2.COLOR_BGR2GRAY)

            cv2.imwrite("Good/" + str(ind) + str(k) + '.jpg', newimage)
            cv2.imwrite("Good/" + str(ind) + str(k) + 'b.jpg', newimage_blur)
        ind += 1
    dir = os.listdir('add_figures')
    ind = 1
    for i in dir:
        newimage = cv2.imread('add_figures/' + i)
        newimage = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("Bad/a" + str(ind) + 'j.jpg', newimage)
        ind += 1


def haarCascadeMakeFile(self):
    fileGood = open("Good.dat", 'w')
    fileBad = open("Bad.dat", 'w')
    dir = os.listdir('Good')
    for i in dir:
        img = cv2.imread('Good/' + i)
        h, w, s = img.shape
        fileGood.write("Good\\" + i + " 1 0 0 " + str(w) + ' ' + str(h) + '\n')
    dir = os.listdir('Bad')
    for i in dir:
        fileBad.write("Bad\\" + i + '\n')


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