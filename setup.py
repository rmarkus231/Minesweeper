#from enum import Flag
import sys
import os
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QWidget, QPushButton, 
    QApplication ,QLineEdit,QLabel, QVBoxLayout, )
from PyQt6.QtCore import QEvent
from PyQt6.QtCore import *
from numpy import *
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import *
from PyQt6.QtCore import QObject,QSize
from reset import reset as reset
import random

row = None
MINErow = None
MINErow2 = None
FLAGrow = None
TEXTrow = None
usedSlots = []

path =os.getcwd() + os.sep + 'ressources'

width = 0
height = 0
mines = 0
mine = 0
usedmines = 0
rand = 0
test = 0
notLost = True
ex = None

class setup(QWidget):


    GO = False
    buttons = []
    allign = None
    button = None
    flags = 0
    time = 0
    timer = None
    reset = False

    def __init__(self):
        super().__init__()
        self.ask_dim()
        
        #time maybe?
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.clock())
        self.timer.start(1000)

    def clock(self):
        if self.GO:
            self.time = self.time +1
            one,two,three = self.bomb_calc(self.time)[0], self.bomb_calc(self.time)[1], self.bomb_calc(self.time)[2]
                                                                                         
        
            pixmap5 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{one}.png')
            self.label5.setPixmap(pixmap5)
            
            pixmap6 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{two}.png')
            self.label6.setPixmap(pixmap6)
                
            pixmap7 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{three}.png')
            self.label7.setPixmap(pixmap7)

    #find button x coord
    def find_x(self,v):
        i = where(row == v)
        #print(f"x = {int(i[0])}")
        return int(i[0])
        
    #find button y coord   
    def find_y(self,v):
        i = where(row == v)
        #print(f"y = {int(i[1])}")
        return int(i[1])

    def ask_dim(self):
        self.setWindowIcon(QIcon(path + os.sep + 'tiles' + os.sep + 'mine.png'))
        self.setGeometry(300, 300, 300, 205)
        self.setWindowTitle('Choose your grid size')
        self.layout = QVBoxLayout(self)
        self.layout.addStretch(1)
        self.layout.setSpacing(33)
        self.layout.setContentsMargins(10,10,10,110)
        print("Generated ask_dim window")
        
        # Create textbox and label
        self.textbox = QLineEdit(self)
        self.textbox.move(30, 20)
        self.textbox.resize(50,30)
        
        self.label = QLabel("X =  ",self.textbox)
        self.label.parent()
        self.label.move(0,0)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        
        # Create textbox2 and label
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(30, 70)
        self.textbox2.resize(50,30)
        
        self.labelY = QLabel("Y = ",self.textbox2)
        self.labelY.parent()
        self.labelY.move(0,0)
        self.layout.addWidget(self.labelY)
        self.setLayout(self.layout)
        print("Created textboxes and labels")
        

        # Create a button in the window
        self.button = QPushButton('Generate Grid\nsmall numbers may break', self)
        self.button.setGeometry(30,130,150,40)
        #print("Generated button for ask_dim")
        try:
            self.button.clicked.connect(self.sendToGrid)
            self.show()
        except:
            self.show()
        
    @pyqtSlot()
    def sendToGrid(self):
        global width,height
        height = int(self.textbox.text())
        width = int(self.textbox2.text())
        self.close()
        self.textbox.setParent(None)
        self.textbox2.setParent(None)
        self.label.setParent(None)
        self.labelY.setParent(None)
        self.button.setParent(None)
        
        self.gen_grid()
        self.assign_mines()
        self.TEXTrow_fill()
    
    def gen_grid(self):
        global mines,width,height,row,MINErow,FLAGrow,MINErow2,TEXTrow
        
        row = arange(width*height).reshape(width,height)
        #print(f"bool: {True if where(row > 0)[0].size == 0 else False}")
                
        #make secondary identical row with all as False, +4 to get rid of wraparound
        
        MINErow = full((width+4,height+4),False)
        
        #and third
        
        FLAGrow = full((width+4,height+4),False)
        
        #and fourth
        MINErow2 = full((width,height),False)
        
        #and fifth
        TEXTrow = full((width+4,height+4),'9')
        
        mines = int(round(float(width*height / 8),1))
        print(f"mines: {mines}")
        self.init_UI()


    def init_UI(self):     
        global width,height
        if height != 0 and width != 0:
            global row
            print("about to generate buttons")
            for y in range(width):
                for x in range(height):
                    self.buttons.append(QPushButton(str(row[y][x]), self))
                    #print(str(row[y][x]))
                    self.buttons[int(row[y][x])].setText(" ")
                    self.buttons[int(row[y][x])].setGeometry(10 + x * 40, 60 + y * 40,40,40)
                    self.buttons[int(row[y][x])].setObjectName(str(row[y][x]))
                    self.buttons[int(row[y][x])].installEventFilter(self)

            self.setGeometry(300, 300, 20 + 40 * height, 70 + 40 * width)
            self.setWindowTitle('Minesweeper')
            
            self.labels_at_start()
            self.clock_at_start()
            
            self.show()
            self.GO = True
            
    def labels_at_start(self):
        if mines < 10:
            one = 0
            two = 0
            three = mines 
        elif mines > 99:
            if mines > 999:
                one = 9
                two = 9
                three = 9
            else:
                one = str(mines)[0]
                two = str(mines)[1]
                three = str(mines)[2]
        else:
            one = 0
            two = str(mines)[0]
            three = str(mines)[1]
              
        self.label = QLabel(self)
        pixmap = QPixmap(path + os.sep + 'digit' + os.sep + f'C{one}.png')
        self.label.setPixmap(pixmap)
        self.label.setGeometry(12,8,26,46)
        
        self.label2 = QLabel(self)
        pixmap2 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{two}.png')
        self.label2.setPixmap(pixmap2)
        self.label2.setGeometry(38,8,26,46)
            
        self.label3 = QLabel(self)
        pixmap3 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{three}.png')
        self.label3.setPixmap(pixmap3)
        self.label3.setGeometry(64,8,26,46)
        
        #game condition indicator
        self.button = QPushButton('', self)
        self.button.setGeometry(int(round((22 + 40 * height)/2-19,1)),8,41 ,41)
        pixmap4 = QPixmap(path + os.sep + 'digit' + os.sep + 'good.png')
        self.button.setIcon(QIcon(pixmap4))
        self.button.setIconSize(QSize(100,100))
        self.button.setFlat(True)
        self.button.clicked.connect(self.reset_clicked)
        
    def reset_game(self):
        #global row,MINErow,mines,MINErow2,FLAGrow,usedSlots,notLost,mine,mines,test,rand,usedmines
        if self.reset:
            global ex
            #reset.width = width
            #reset.height = height
            #new = reset(width,height)
            #new.init_UI()
            ex = reset(width,height)
            QtCore.QCoreApplication.quit()
            status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
            print(status)
            
            
            
    
    @pyqtSlot()
    def reset_clicked(self):
        self.reset = True
        self.reset_game()
        sys.exit(app.exec())

    def clock_at_start(self):
        self.label5 = QLabel(self)
        pixmap5 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{0}.png')
        self.label5.setPixmap(pixmap5)
        self.label5.setGeometry(40 * height -69,8,26,46)
        
        self.label6 = QLabel(self)
        pixmap6 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{0}.png')
        self.label6.setPixmap(pixmap6)
        self.label6.setGeometry(40 * height -43,8,26,46)
            
        self.label7 = QLabel(self)
        pixmap7 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{0}.png')
        self.label7.setPixmap(pixmap7)
        self.label7.setGeometry(40 * height -17,8,26,46)

    def counter(self,one,two,three):
        
        #self.label = QLabel(self)
        pixmap = QPixmap(path + os.sep + 'digit' + os.sep + f'C{one}.png')
        self.label.setPixmap(pixmap)
        #self.label.setGeometry(12,8,26,46)
        
        #self.label2 = QLabel(self)
        pixmap2 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{two}.png')
        self.label2.setPixmap(pixmap2)
        #self.label2.setGeometry(38,8,26,46)
            
        #self.label3 = QLabel(self)
        pixmap3 = QPixmap(path + os.sep + 'digit' + os.sep + f'C{three}.png')
        self.label3.setPixmap(pixmap3)
        #self.label3.setGeometry(64,8,26,46)

    def assign_mines(self):
        global mines,mine,usedmines,width,height,MINErow,rand
        minesForRow = array(zeros(height,dtype=int8))
        print(f"height: {height}, width: {width}")
        for i in range(height):
            if usedmines == 0:
                for j in range(len(minesForRow)):
                    for v in range(len(minesForRow)):
                        if minesForRow[v] < 0:
                            minesForRow[v] = 0
                    
                    if minesForRow[i] < 0:
                        minesForRow[i] = 0
                mine = int(round(mines/height,1) + random.randint(-1,int(round((width/4),1))))
                if mine < 0:
                    mine = 0
                #print(f"mine: {mine}")
                if mine < 0:
                    mine = 0
                    minesForRow[i] = mine
                if mine >= mines-usedmines:
                    mine = mines-usedmines
                    minesForRow[i] = mine
                    usedmines = usedmines + mine
                    mine = 0
                else:
                    usedmines = usedmines + mine
                    minesForRow[i] = mine
                    mine = 0
                if mine >= width or mine >= height:
                    mine = 0
            else:
                if mines == 0:
                    mine = 0
                    usedmines = usedmines + mine
                    minesForRow[i] = mine
                else: 
                    #print(f"mines-usedmines: {mines-usedmines}")
                    mine = int(round(mines-sum(minesForRow),1) / round(height - i,1) + random.randint(-3,3))
                    if mine >= mine-usedmines:
                        mine = mine-usedmines
                    usedmines = usedmines + mine
                    minesForRow[i] = mine
                    for i in range(0,len(minesForRow)):
                        if minesForRow[i] < 0:
                            minesForRow[i] = 0
                        if minesForRow[i] >= width or minesForRow[i] >= height:
                            minesForRow[i] = 0
                            
                    mine = 0
        while True if where(row > 0)[0].size == 0 else False:
            print("Found value < 0")
            print(f"mines for row w/ <0: {minesForRow}, sum: {sum(minesForRow)}")
            for i in range(len(minesForRow)):
                if minesForRow[i] < 0:
                    minesForRow[i] = 0
                if minesForRow[i] >= width or minesForRow[i] >= height:
                    minesForRow[i] = 0
            
        while sum(minesForRow) != mines:
            if sum(minesForRow) < mines:
                mine = mines- sum(minesForRow)
                rand = random.randint(0,height-1)
                rand2 = random.randint(0,mine)
                if rand >= 0:
                    minesForRow[rand] += rand2
            else:
                rand = random.randint(0,height-1)
                if int(minesForRow[rand]) > 0:
                     minesForRow[rand] - 1
        
        rand = 0
        
        print(f"mines for row: {minesForRow}, sum: {sum(minesForRow)}")
        #print(MINErow)
    
        for i in range(height):
            for j in range(minesForRow[i]):
                test = 1
                while test == 1:
                    rand = random.randint(0,width-2)
                    #print(f"rand = {rand}, i = {i}")
                    if rand < 0:
                        rand = 0
                    if MINErow[rand+2][i+2]:
                        continue
                    else:
                        MINErow[rand+2][i+2] = True
                        test = 0
        #print(MINErow)
        
    def eventFilter(self, obj, event):
        button = obj.objectName()
        #print(x,y,button)
        if event.type() == QEvent.Type.MouseButtonPress:
            if event.button() == Qt.MouseButton.LeftButton:
                #print(button)
                self.L_action(int(button))
            elif event.button() == Qt.MouseButton.RightButton:
                self.R_action(int(button))
        return QObject.event(obj, event)       

    def TEXTrow_fill(self):
        for j in range(width):
            for i in range(height):
                adj = 0
                x = j +2
                y = i +2
                if MINErow[x][y]:
                    adj = 'b'
                    #print(f"x:{j},y:{i}, text:{adj}")
                    TEXTrow[x][y] = adj
                else:
                    adj = (adj + 1 * int(MINErow[x][y-1]))+(adj + 1* int(MINErow[x][y+1]))+(adj + 1* int(MINErow[x-1][y]))+(adj + 1* int(MINErow[x+1][y]))+(adj + 1* int(MINErow[x-1][y-1]))+(adj + 1* int(MINErow[x+1][y-1])) + (adj +1* int(MINErow[x-1][y+1])) + (adj + 1* int(MINErow[x+1][y+1]))

                #print(f"x:{j},y:{i}, text:{adj}")
                TEXTrow[x][y] = str(adj)
        #print(TEXTrow)
        
    def bomb_calc(self,rem):
        if rem < 1:
            one = 0
            two = 0
            three = 0
        elif rem < 10:
            one = 0
            two = 0
            three = rem 
        elif rem > 99:
            if rem > 999:
                one = 9
                two = 9
                three = 9
            else:
                one = str(rem)[0]
                two = str(rem)[1]
                three = str(rem)[2]
        else:
            one = 0
            two = str(rem)[0]
            three = str(rem)[1]
        return one,two,three
        
    def R_action(self,button):
        if notLost:
            x = self.find_x(button)
            y = self.find_y(button)
            if FLAGrow[x+2][y+2]:
                self.flags -= 1
                one,two,three = self.bomb_calc(mines-self.flags)[0], self.bomb_calc(mines-self.flags)[1], self.bomb_calc(mines-self.flags)[2]
                self.counter(one,two,three)
                self.buttons[button].setIcon(QIcon())
                FLAGrow[x+2][y+2] = False
                if array_equal(FLAGrow,MINErow):
                    print('You win')
                    pixmap4 = QIcon(path + os.sep + 'digit' + os.sep + 'win.png')
                    self.button.setIcon(pixmap4)

            elif FLAGrow[x+2][y+2] == False and MINErow2[x][y] == False and mines-self.flags != 0:
                self.flags += 1
                one,two,three = self.bomb_calc(mines-self.flags)[0], self.bomb_calc(mines-self.flags)[1], self.bomb_calc(mines-self.flags)[2]
                self.counter(one,two,three)
                FLAGrow[x+2][y+2] = True
                self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep +'flag.png'))
                self.buttons[button].setIconSize(QSize(100,100))
                if  array_equal(FLAGrow,MINErow):
                    print('You win')
                    pixmap4 = QIcon(path + os.sep + 'digit' + os.sep + 'win.png')
                    self.button.setIcon(pixmap4)
            else:
                pass

    def L_action(self, button):
        global width,usedSlots,notLost,TEXTrow
        if notLost:
            #print(button)
            x = self.find_x(button)
            y = self.find_y(button)
            MINErow2[x][y] = True
            text = TEXTrow[x+2][y+2]
            #print(text)
            if FLAGrow[x][y]:
                pass
            else:
                if text == 'b':
                    self.timer.stop()
                    notLost = False
                    print("Game over, you lose!")
                    self.buttons[button].setStyleSheet("background-color: red")
                    self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep + 'mine.png'))
                    self.buttons[button].setIconSize(QSize(100,100))
                    pixmap4 = QIcon(path + os.sep + 'digit' + os.sep + 'bad.png')
                    self.button.setIcon(pixmap4)
                elif text == '0' and text not in usedSlots:
                    #print(0)
                    self.floodFill(TEXTrow,x,y)
                else:
                    self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep +f'{text}.png'))
                    self.buttons[button].setIconSize(QSize(100,100))

    def floodFillUtil(self,screen, x, y):
        # Base cases
        if (x < 0 or x >= width or y < 0 or
            y >= height or screen[x+2][y+2] != '0' or row[x][y] in usedSlots or screen[x+2][y+2] == '9'):
            try:
                button = row[x][y]
                text = TEXTrow[x+2][y+2]
                usedSlots.append(row[x][y])
                self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep + f'{text}.png'))
                self.buttons[button].setIconSize(QSize(100,100))
                return
            except:
                return
        
        button = row[x][y]
        usedSlots.append(row[x][y])
        self.buttons[button].setText(" ")
        self.buttons[button].setEnabled(False)
        self.buttons[button].setText(" ")
        self.buttons[button].setEnabled(False)
    
        # Recur for north, east, south and west
        self.floodFillUtil(screen, x + 1, y)
        self.floodFillUtil(screen, x - 1, y)
        self.floodFillUtil(screen, x, y + 1)
        self.floodFillUtil(screen, x, y - 1)
        self.floodFillUtil(screen, x + 1, y-1)
        self.floodFillUtil(screen, x - 1, y-1)
        self.floodFillUtil(screen, x + 1, y+1)
        self.floodFillUtil(screen, x - 1, y+1)
 
    def floodFill(self,screen, x, y):
        prev = screen[x+2][y+2]
        if(prev != '0'):
            return
        self.floodFillUtil(screen, x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = setup()
    #setup.GO = True
    sys.exit(app.exec())