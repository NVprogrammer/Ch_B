from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow import keras
from threading import Thread
import tensorflow as tf
import cv2
import random
import numpy as np
import os
import pyautogui as pag
from PIL import Image



class AI():
    def __init__(self):
        self.figures = ['bB_w.PNG', 'bK_w.PNG', 'bN_w.PNG', 'bp_w.PNG', 'bQ_w.PNG', 'bR_w.PNG', 'wB_w.PNG', 'wK_w.PNG',
                   'wN_w.PNG', 'wp_w.PNG', 'wQ_w.PNG', 'wR_w.PNG', 'emp_w.PNG',
                   'bB_b.PNG', 'bK_b.PNG', 'bN_b.PNG', 'bp_b.PNG', 'bQ_b.PNG', 'bR_b.PNG', 'wB_b.PNG', 'wK_b.PNG',
                   'wN_b.PNG', 'wp_b.PNG', 'wQ_b.PNG', 'wR_b.PNG', 'emp_b.PNG'
                   ]
        self.classes = [i.split('_')[0] for i in self.figures]
        self.classes = list(np.unique(self.classes))
        self.data = []
        self.labels = []
        self.data2 = []

    def imagePre(self,dir):

        name = dir
        dir = os.listdir(dir)
        print(dir)
        for i in dir:
            img_w=32
            img_h=32
            print(name + '/' + i)
            image = cv2.imread(name + '/' + i,0)
            self.data2.append(image)
            image = cv2.resize(image, (img_h, img_w))
            # cv2.imshow('f', image)
            # cv2.waitKey(0)
            self.data.append(image)
            self.labels.append(i.split('_')[0])

            #Изображение с белым квадратом имитирует курсор
            image_w_w=image.copy()
            image_w_w[11:21,11:21]=255
            self.data.append(image_w_w)
            self.labels.append(i.split('_')[0])
            self.data2.append(image_w_w)

            #Разное положение фигуры
            for j in range(10):
                h=random.randint(1,5)
                w=random.randint(1,5)
                print(w,h)

                img_crop=image[0:img_h-h,0:img_w-w]
                img_crop=cv2.resize(img_crop,(32,32))
                self.data.append(img_crop)
                self.labels.append(i.split('_')[0])
                self.data2.append(img_crop)
                # cv2.imshow('f', img_crop)
                # cv2.waitKey(0)

                img_crop = image[0+h:img_h, 0+w:img_w ]
                img_crop = cv2.resize(img_crop, (32, 32))
                self.data.append(img_crop)
                self.labels.append(i.split('_')[0])
                self.data2.append(img_crop)


                img_crop = image[0:img_h, 0:img_w - w]
                img_crop = cv2.resize(img_crop, (32, 32))
                self.data.append(img_crop)
                self.labels.append(i.split('_')[0])
                self.data2.append(img_crop)


                img_crop = image[0:img_h - h, 0:img_w]
                img_crop = cv2.resize(img_crop, (32, 32))
                self.data.append(img_crop)
                self.labels.append(i.split('_')[0])
                self.data2.append(img_crop)


                img_crop = image[0 + h:img_h, 0:img_w]
                img_crop = cv2.resize(img_crop, (32, 32))
                self.data.append(img_crop)
                self.labels.append(i.split('_')[0])
                self.data2.append(img_crop)


                img_crop = image[0:img_h, 0 + w:img_w]
                img_crop = cv2.resize(img_crop, (32, 32))
                self.data.append(img_crop)
                self.labels.append(i.split('_')[0])
                self.data2.append(img_crop)




            # image = cv2.imread(name + '/' + i,0)
            # self.data2.append(image)
            # cv2.imshow('f', image)
            # cv2.waitKey(0)
            # image = cv2.blur(image, (3, 3))
            # image = cv2.resize(image, (32, 32))
            # self.data.append(image)
            # self.labels.append(i.split('_')[0])
            # for l in range(2):
            #
            #     image = cv2.imread(name + '/' + i)
            #     self.data2.append(image)
            #     height, width, bb = image.shape
            #     factor = random.randint(-(l + 2) * 5 - 3, (l + 2) * 5 + 3)
            #     for k in range(height):
            #         for j in range(width):
            #             a = image[k][j][0] + factor
            #             b = image[k][j][1] + factor
            #             c = image[k][j][2] + factor
            #             if (a < 0):
            #                 a = 0
            #             if (b < 0):
            #                 b = 0
            #             if (c < 0):
            #                 c = 0
            #             if (a > 255):
            #                 a = 255
            #             if (b > 255):
            #                 b = 255
            #             if (c > 255):
            #                 c = 255
            #             image[k][j] = (a, b, c)
            #     # cv2.imshow('f',image)
            #     # cv2.waitKey(0)
            #     image = cv2.resize(image, (16, 16))
            #     self.data.append(image)
            #     self.labels.append(i.split('_')[0])
            #
            #     image = cv2.imread(name + '/' + i)
            #     self.data2.append(image)
            #     height, width, bb = image.shape
            #     factor = random.randint(5 * (l) + 5, (l + 1) * 15)
            #     for k in range(height):
            #         for j in range(width):
            #             rand = random.randint(-factor, factor)
            #             a = image[k][j][0] + rand
            #             b = image[k][j][1] + rand
            #             c = image[k][j][2] + rand
            #             if (a < 0):
            #                 a = 0
            #             if (b < 0):
            #                 b = 0
            #             if (c < 0):
            #                 c = 0
            #             if (a > 255):
            #                 a = 255
            #             if (b > 255):
            #                 b = 255
            #             if (c > 255):
            #                 c = 255
            #             image[k][j] = (a, b, c)
            #     # cv2.imshow('f',image)
            #     # cv2.waitKey(0)
            #     image = cv2.resize(image, (16, 16))
            #     self.data.append(image)
            #     self.labels.append(i.split('_')[0])


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
        data *= 30
        labels *= 30
        data2 *= 30
        random.seed(30)
        a = data
        b = labels
        a2 = data2
        c = list(zip(a, b))
        c2 = list(zip(a2, b))
        random.shuffle(c)
        random.seed(30)
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
                                                          labels, test_size=0.1, random_state=30)
        lb = LabelBinarizer()
        EPOCHS = 200
        trainY_or = list.copy(list(trainY))
        trainY = lb.fit_transform(trainY)
        testY = lb.transform(testY)
        H = model.fit(trainX, trainY, validation_data=(testX, testY),
                      epochs=EPOCHS, batch_size=48)

        # оцениваем нейросеть
        print(" evaluating network...")
        predictions = model.predict(testX)
        print(classification_report(testY.argmax(axis=1),
                                    predictions.argmax(axis=1)))
        model.save("chessFigUltimate_2_modern.h5")


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

        self.data *= 1
        self.labels *= 1
        self.data2 *= 1

        # shake (data2 для проверки)
        random.seed(10)
        a = self.data
        b = self.labels
        a2 = self.data2
        c = list(zip(a, b))
        c2 = list(zip(a2, b))
        random.shuffle(c)
        random.seed(10)
        random.shuffle(c2)
        self.data, self.labels = zip(*c)
        self.data2, self.labels = zip(*c2)

        print(len(self.data))
        # for i in range(len(self.data)):
        #     print(self.labels[i])
        #     cv2.imshow("rt",self.data2[i])
        #     cv2.waitKey(0)
        data = np.array(self.data, dtype="float").reshape(-1,32,32,1) / 255.0
        print(data.shape)
        labels = np.array(self.labels)
        (trainX, testX, trainY, testY) = train_test_split(data,
                                                          labels, test_size=0.25, random_state=10)
        print(trainX.shape)
        lb = LabelBinarizer()
        trainY_or = list.copy(list(trainY))
        trainY = lb.fit_transform(trainY)
        testY = lb.transform(testY)

        model = keras.Sequential()
        # model.add(keras.layers.Dense(16, input_shape=(8 * 8 * 3,), activation="sigmoid", use_bias=True))
        # model.add(keras.layers.Dense(16, activation="sigmoid"))
        # model.add(keras.layers.Dense(len(self.classes), activation="sigmoid"))
        model.add(keras.layers.Conv2D(32,(3,3),activation='relu',input_shape=(32,32,1)))
        model.add(keras.layers.MaxPooling2D((2,2),strides=2))
        model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
        model.add(keras.layers.MaxPooling2D((2, 2), strides=2))
        model.add(keras.layers.Flatten())
        model.add(keras.layers.Dense(128,activation='relu'))
        model.add(keras.layers.Dense(len(self.classes), activation="softmax"))

        # инициализируем скорость обучения и общее число эпох
        INIT_LR = 0.001
        EPOCHS = 8

        # компилируем модель, используя SGD как оптимизатор и категориальную
        # кросс-энтропию в качестве функции потерь (для бинарной классификации
        # следует использовать binary_crossentropy)
        print(" training network...")
        opt = keras.optimizers.Adam(lr=INIT_LR)
        model.compile(loss='categorical_crossentropy', optimizer=opt,
                      metrics=['accuracy'])

        H = model.fit(trainX, trainY, validation_data=(testX, testY),
                      epochs=EPOCHS, batch_size=32)

        # оцениваем нейросеть
        print(" evaluating network...")
        predictions = model.predict(testX)
        print(classification_report(testY.argmax(axis=1),
                                    predictions.argmax(axis=1)))
        model.save("chessFigConv.h5")
        print(model.summary())



# model=keras.models.load_model('chessFigUltimate_2_modern.h5')
# ai=AI()
# ai.trainNet()
# ai.contTrainNet(model)


