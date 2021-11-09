from enum import Flag
import sys
import os
from PyQt6 import QtWidgets
from PyQt6 import QtGui
from PyQt6 import QtCore
from PyQt6.QtWidgets import (QWidget, QPushButton, 
    QApplication ,QLineEdit,QLabel, QVBoxLayout, )
from PyQt6.QtCore import QEvent
from PyQt6.QtCore import *
from functools import partial
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import *
from PyQt6.QtCore import QObject,QSize
import random

row =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
MINErow =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
MINErow2 =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
FLAGrow =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
ZEROrow =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],]
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

class application(QWidget):


    GO = False
    buttons = []
    minesForRow = []
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
        for i, x in enumerate(row):
            if v in x:
                #print(f"x = {i}")
                return i
        
    #find button y coord   
    def find_y(self,v):
        for i, x in enumerate(row):
            if v in x:
                #print(f"y = {x.index(v)}")
                return x.index(v)

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
    
    def gen_grid(self):
        global mines,width,height
        for i in range(0,width):
            for j in range(0,height):
                row[i].append(j+height*i)
                
        #make secondary identical row with all as False
        
        for i in range(0,width+1):
            for j in range(0,height+1):
                MINErow[i].append(False)
        
        #and third
        
        for i in range(0,height+1):
            for j in range(0,width+1):
                FLAGrow[j].append(False)
        
        #and fourth
        for i in range(0,width+1):
            for j in range(0,height+1):
                MINErow2[i].append(False)
        
        #and fifth
        for i in range(0,width):
            for j in range(0,height):
                ZEROrow[i].append(False)
        
        mines = int(round(float(width*height / 8),1))
        print(f"mines: {mines}")
        self.init_UI()


    def assign_ZEROrow(self,width,height):
        #print("inb4 ZERO row")
        for i in range(width+1):
            for j in range(height+1):
                try:
                    text = self.adjacent_mines(j+height*i)
                    if text == '0':
                        ZEROrow[i][j] = True
                except:
                    pass

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
        global row,MINErow,mines,MINErow2,FLAGrow,ZEROrow,usedSlots,notLost,mine,mines,test,rand,usedmines
        if self.reset:
            self.timer.stop()
            self.close()
            
            for y in range(width):
                for x in range(height):
                    self.buttons[int(row[y][x])].setStyleSheet("background-color: light gray")
                    self.buttons[int(row[y][x])].setEnabled(True)
            
            row[:][:] = []
            MINErow[:][:] = []
            MINErow2[:][:] = []
            FLAGrow[:][:] = []
            ZEROrow[:][:] = []
            usedSlots.clear()
            self.GO = False
            self.buttons.clear()
            self.minesForRow.clear()
            self.allign = None
            self.button = None
            self.flags = 0
            self.time = 0
            self.timer = None
            self.reset = False
            notLost = True
            mines = 0
            mine = 0
            usedmines = 0
            rand = 0
            test = 0
            
            self.gen_grid()
            self.assign_mines()
            
            self.timer = QTimer(self)
            self.timer.timeout.connect(lambda: self.clock())
            self.timer.start(1000)
            
    @pyqtSlot()
    def reset_clicked(self):
        self.reset = True
        self.reset_game()

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
        print(f"height: {height}, width: {width}")
        for i in range(height):
            if usedmines == 0:
                for i in range(len(self.minesForRow)):
                    for v in range(len(self.minesForRow)):
                        if self.minesForRow[v] < 0:
                            self.minesForRow[v] = 0
                    
                    if self.minesForRow[i] < 0:
                        self.minesForRow[i] = 0
                mine = int(round(mines/height,1) + random.randint(-1,int(round((width/4),1))))
                if mine < 0:
                    mine = 0
                #print(f"mine: {mine}")
                if mine < 0:
                    mine = 0
                    self.minesForRow.append(mine)
                if mine >= mines-usedmines:
                    mine = mines-usedmines
                    self.minesForRow.append(mine)
                    usedmines = usedmines + mine
                    mine = 0
                else:
                    usedmines = usedmines + mine
                    self.minesForRow.append(mine)
                    mine = 0
                if mine >= width or mine >= height:
                    mine = 0
            else:
                if mines == 0:
                    mine = 0
                    usedmines = usedmines + mine
                    self.minesForRow.append(mine)
                else: 
                    #print(f"mines-usedmines: {mines-usedmines}")
                    mine = int(round(mines-sum(self.minesForRow),1) / round(height - i,1) + random.randint(-3,3))
                    if mine >= mine-usedmines:
                        mine = mine-usedmines
                    usedmines = usedmines + mine
                    self.minesForRow.append(mine)
                    for i in range(0,len(self.minesForRow)):
                        if self.minesForRow[i] < 0:
                            self.minesForRow[i] = 0
                        if self.minesForRow[i] >= width or self.minesForRow[i] >= height:
                            self.minesForRow[i] = 0
                            
                    mine = 0
                    
        for i in range(len(self.minesForRow)):
            if self.minesForRow[i] < 0:
                self.minesForRow[i] = 0
            if self.minesForRow[i] >= width or self.minesForRow[i] >= height:
                self.minesForRow[i] = 0
        
        while sum(self.minesForRow) != mines:
            mine = mines- sum(self.minesForRow)
            rand = random.randint(0,height-1)
            if rand >= 0:
                self.minesForRow[rand] += mine
        
        rand = 0
        
        print(f"mines for row: {self.minesForRow}, sum: {sum(self.minesForRow)}")
        #print(MINErow)
    
        for i in range(height):
            for j in range(self.minesForRow[i]):
                test = 1
                while test == 1:
                    rand = random.randint(0,width-1)
                    #print(f"rand = {rand}, i = {i}")
                    if rand < 0:
                        rand = 0
                    if MINErow[rand][i]:
                        continue
                    else:
                        MINErow[rand][i] = True
                        test = 0
    
        self.assign_ZEROrow(width,height)
        
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

    def adjacent_mines(self,button):
        global width,height
        x = self.find_x(button)
        y = self.find_y(button)
        #print(f"type for x:{type(x)}, and y:{type(y)}")
        adj = 0
        if x != None and y != None:
            if MINErow[x][y]:
                return 10
            try:
                if MINErow[x][y-1]: #up
                    adj += 1
            except:
                adj += 0
            try:
                if MINErow[x][y+1]:  #down int(height) if y == int(height) else y+1
                    adj += 1
            except:
                adj += 0
            try:
                if MINErow[x-1][y]:     #left
                    adj += 1
            except:
                adj += 0
            try:
                if MINErow[x+1][y]:     #right
                    adj += 1
            except:
                adj += 0
            try:
                if MINErow[x-1][y-1]:#top left
                    adj += 1
            except:
                adj += 0
            try:
                if MINErow[x+1][y-1]:#top right
                    adj += 1
            except:
                adj += 0
            try:
                if MINErow[x-1][y+1]:#bottom left
                    adj += 1
            except:
                adj += 0
            try:
                if MINErow[x+1][y+1]:#bottom right
                    adj += 1
            except:
                adj += 0
            return str(adj)
        
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
            if FLAGrow[x][y]:
                self.flags -= 1
                one,two,three = self.bomb_calc(mines-self.flags)[0], self.bomb_calc(mines-self.flags)[1], self.bomb_calc(mines-self.flags)[2]
                self.counter(one,two,three)
                self.buttons[button].setIcon(QIcon())
                FLAGrow[x][y] = False
                if FLAGrow == MINErow:
                    print('You win')
                    pixmap4 = QIcon(path + os.sep + 'digit' + os.sep + 'win.png')
                    self.button.setIcon(pixmap4)

            elif FLAGrow[x][y] == False and MINErow2[x][y] == False and mines-self.flags != 0:
                self.flags += 1
                one,two,three = self.bomb_calc(mines-self.flags)[0], self.bomb_calc(mines-self.flags)[1], self.bomb_calc(mines-self.flags)[2]
                self.counter(one,two,three)
                FLAGrow[x][y] = True
                self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep +'flag.png'))
                self.buttons[button].setIconSize(QSize(100,100))
                if FLAGrow == MINErow:
                    print('You win')
                    pixmap4 = QIcon(path + os.sep + 'digit' + os.sep + 'win.png')
                    self.button.setIcon(pixmap4)
            else:
                pass

    def L_action(self, button):
        global width,usedSlots,notLost
        if notLost:
            x = self.find_x(button)
            y = self.find_y(button)
            MINErow2[x][y] = True
            text = self.adjacent_mines(button)
            if FLAGrow[x][y]:
                pass
            else:
                if text == 10:
                    self.timer.stop()
                    notLost = False
                    print("Game over, you lose!")
                    self.buttons[button].setStyleSheet("background-color: red")
                    self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep + 'mine.png'))
                    self.buttons[button].setIconSize(QSize(100,100))
                    pixmap4 = QIcon(path + os.sep + 'digit' + os.sep + 'bad.png')
                    self.button.setIcon(pixmap4)
                elif text == '0' and text not in usedSlots:
                    self.floodFill(ZEROrow,x,y)
                else:
                    self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep +f'{text}.png'))
                    self.buttons[button].setIconSize(QSize(100,100))

    def floodFillUtil(self,screen, x, y):
        # Base cases
        if (x < 0 or x >= width or y < 0 or
            y >= height or screen[x][y] != True or
            screen[x][y] == False or row[x][y] in usedSlots):
            try:
                button = row[x][y]
                text = self.adjacent_mines(button)
                self.buttons[button].setIcon(QIcon(path + os.sep + 'tiles' + os.sep + f'{text}.png'))
                self.buttons[button].setIconSize(QSize(100,100))
                return
            except:
                return
        
        button = row[x][y]
        usedSlots.append(row[x][y])
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
        prev = screen[x][y]
        if(prev==False):
            return
        self.floodFillUtil(screen, x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = application()
    #application.GO = True
    sys.exit(app.exec())