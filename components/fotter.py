from PyQt5.QtWidgets import  QWidget,QVBoxLayout,QTableWidgetItem,QFrame,QHBoxLayout
from components.Entry import *
from components.Label import *
class FooterVent(QFrame):
    def __init__(self, parent) :
        super().__init__(parent=parent)
        self.total,self.rende,self.verse=FooterLabel(parent=self,text='0'),FooterLabel(parent=self,text='0'),NumEntrey(self)
        self.rende.setStyleSheet("font-size: 24px;")
        self.setLayout(self.layout())
        self.verse.returnPressed.connect(self.rend)
    def rend(self):
        if float(self.total.text())<int(self.verse.text()):
            self.rende.setText(str(int(self.verse.text())-float(self.total.text())))
    def layout(self):
        v,h=QVBoxLayout(),QHBoxLayout()
        v.addWidget(self.verse)
        v.addWidget(self.rende)
        h.addStretch()
        h.addWidget(FooterLabel(parent=self,text='TOTAL :'))
        h.addStretch()
        h.addWidget(self.total)
        h.addLayout(v)
        return h