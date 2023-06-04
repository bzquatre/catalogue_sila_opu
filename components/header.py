from PyQt5.QtWidgets import QLabel,QFrame,QPushButton
from PyQt5.QtCore import Qt,QTimer,QSize
from PyQt5.QtGui import QPixmap,QIcon

style="""
QPushButton {
    background-color:rgb(241,248,255);
    color:#000000;
    font-size: 34px;
    border: none;
    padding-bottom:7px;
}
QFrame{
    background-color:rgb(241,248,255);
    padding-top:0px;
}
""" 
class Header(QFrame):
    def __init__(self):
        super().__init__()
        self.title=QPushButton(parent=self,icon=QIcon('Icon.ico'))
        self.title.setIconSize(QSize(50,50))
        self.setFixedHeight(80)
        try:
            self.title.setText(open('header.txt','r',encoding="utf-8").read())
        except :
            pass
        self.setStyleSheet(style)
        self.p=0
        self.title.move(self.p,20)
        self.timer=QTimer()
        self.timer.start(20)
        self.timer.timeout.connect(self.move_label)
    def move_label(self):
        print()
        self.p=self.p-5 if self.p>-self.title.width() else self.width()
        self.title.move(self.p,20)
        self.timer.start(20)


