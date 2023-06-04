from PyQt5.QtWidgets import QFrame,QHBoxLayout,QVBoxLayout,QTableWidgetItem,QGraphicsDropShadowEffect
from components.Entry import Entry,NumEntrey,Code
from components.Button import Ajouter,NavButton
from components.Label import *
class NavBar(QFrame):
    def __init__(self, parent) :
        super().__init__(parent=parent)
        self.serche,self.refenc,self.ajouter=Entry(self),Entry(self),Ajouter(self)
        self.refenc.hide()
        self.setLayout()
    def setLayout(self):
        h=QHBoxLayout()
        h.addStretch()
        for i in [self.serche,self.ajouter]:
            h.addWidget(i) 
        return super().setLayout(h)
class NavBarVent(QFrame):
    def __init__(self, parent) :
        super().__init__(parent=parent)
        self.code,self.edition,self.qt,self.annuler,self.valider=Code(self),NumEntrey(self),NumEntrey(self),NavButton(self),NavButton(self)
        self.valider.icone('img/valider.svg')
        self.annuler.icone('img/annuler.svg')
        self.edition.setPlaceholderText("Edition ...1..2..3..16")
        self.setLayout(self.layout())
    def etat1(self,i):
        self.code.setDisabled(False)
        self.edition.setDisabled(True)
        self.qt.setDisabled(True)
        self.valider.setDisabled(i==0)
        self.code.setText("")
        self.edition.setText("")
        self.qt.setText("")
        self.code.setFocus()
    def etat2(self):
        self.code.setDisabled(True)
        self.edition.setDisabled(False)
        self.edition.setFocus()
    def etat3(self):
        self.edition.setDisabled(True)
        self.qt.setDisabled(False)
        self.qt.setFocus()
    def layout(self):
        h=QHBoxLayout()
        x=[self.code,self.edition,Label(parent=self,text='Qt'),self.qt],[self.annuler,self.valider]
        for i in x:
            for j in i:
                h.addWidget(j) 
            h.addStretch()
            h.addStretch()
       # map(h.addWidget,i)
        return h