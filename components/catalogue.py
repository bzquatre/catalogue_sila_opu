from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QFrame
from components.Entry import Combobox, Entry
from components.table import Table
from components.Button import Button,FButton
from components.header import Header
from config import Livre,Disciplins,session
from components.Label import Label

class Frame(QFrame):
    def __init__(self) :
        super().__init__()
        self.button1, self.button2, self.button3, self.button4=FButton(self,'Sciences Exactes, de la Terre et de la Nature'),FButton(self,'Technologie'),FButton(self,'Sciences Médicales'),FButton(self,'Sciences Sociales')
        self.setLayout()
    def setLayout(self):
        a0,h1,h2=QVBoxLayout(),QHBoxLayout(),QHBoxLayout()
        h1.addWidget(self.button1),h1.addWidget(self.button2)
        h2.addWidget(self.button3),h2.addWidget(self.button4)
        a0.addLayout(h1),a0.addLayout(h2)
        return super().setLayout(a0)

class Catalogue(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.desplin,self.text_serche,self.table,self.button,self.reture=Combobox(self),Entry(self),Table(),Button(self,text='Rechercher'),Button(self,text='<')
        self.text_serche.setPlaceholderText('Rechercher par titre,auteur et  edition')
        self.text_serche.setFixedWidth(500)
        self.header=Header()
        self.frame=Frame()
        self.v=QVBoxLayout()
        self.table.init_header(["Edition","Titre","Auteur","Discipline","Prix"])
        self.desplin.addItems(['Toutes les Disciplines']+[dis.desgination_disciplin for dis in session.query(Disciplins).all()])
        self.setLayout()
        self.text_serche.returnPressed.connect(self.remplire)
        self.button.clicked.connect(self.remplire)
        self.desplin.currentTextChanged.connect(self.remplire)     
        self.frame.button1.clicked.connect(self.click1)   
        self.frame.button2.clicked.connect(self.click2)   
        self.frame.button3.clicked.connect(self.click3)   
        self.frame.button4.clicked.connect(self.click4)   
        self.reture.clicked.connect(self.returee)
        self.liste_article()
        self.etat1()
    def liste_article(self):
        self.livres=session.query(Livre,Disciplins).join(Disciplins,Livre.disciplin==Disciplins.code_disciplin).all()
        self.text_serche.set_autocomplite([livre[0].titre_article for livre in self.livres])
        self.remplire()
    def returee(self):
        self.text_serche.setText('')
        self.etat1()
        self.text_serche.setText('')
    def click1(self):
        self.desplin.setCurrentIndex(2)
        self.etat2()
        self.text_serche.setText('')
    def click2(self):
        self.desplin.setCurrentIndex(3)
        self.etat2()
        self.text_serche.setText('')
    def click3(self):
        self.desplin.setCurrentIndex(4)
        self.etat2()
        self.text_serche.setText('')
    def click4(self):
        self.desplin.setCurrentIndex(5)
        self.etat2()
        self.text_serche.setText('')
    def remplire(self):
        self.table.clear()
        self.table.init_header(["Edition","Titre","Auteur","Discipline","Prix"])
        if self.text_serche.text()=="" and self.desplin.currentText()=="Toutes les Disciplines":
            for article in  self.livres:
                self.table.setRowCount(self.table.rowCount()+1)
                [self.table.setCellWidget(self.table.rowCount()-1,i,Label(str(item))) for i,item in enumerate([article[0].edition_article,article[0].titre_article,article[0].auteur_article,article[1].desgination_disciplin,article[0].prix_ttc])]
        elif self.text_serche.text()=="" and self.desplin.currentText()!="Toutes les Disciplines":
            for article in  self.livres:
                if self.desplin.currentText()== article[1].desgination_disciplin:
                        self.table.setRowCount(self.table.rowCount()+1)
                        [self.table.setCellWidget(self.table.rowCount()-1,i,Label(str(item))) for i,item in enumerate([article[0].edition_article,article[0].titre_article,article[0].auteur_article,article[1].desgination_disciplin,article[0].prix_ttc])]
        else:
            for article in  self.livres:
                if  (self.text_serche.text()=="" or self.text_serche.text().lower() in str(article[0].titre_article).lower() or self.text_serche.text() == str(article[0].edition_article)):
                    self.table.setRowCount(self.table.rowCount()+1)
                    [self.table.setCellWidget(self.table.rowCount()-1,i,Label(str(item))) for i,item in enumerate([article[0].edition_article,article[0].titre_article,article[0].auteur_article,article[1].desgination_disciplin,article[0].prix_ttc])]
        
    def etat2(self):
        self.frame.hide()
        self.text_serche.show(),self.button.show(),self.desplin.show(),self.table.show(),self.reture.show()
    def etat1(self):
        self.frame.show()
        self.text_serche.hide(),self.button.hide(),self.desplin.hide(),self.table.hide(),self.reture.hide()
    def setLayout(self):
        h=QHBoxLayout()
        h.addStretch(1),h.addWidget(self.reture),h.addWidget(self.text_serche),h.addWidget(self.button),h.addStretch(1)
        self.v.setContentsMargins(0,0,0,0)
        self.v.setSpacing(0)
        self.v.addWidget(self.header)
        self.v.addLayout(h)
        self.v.addWidget(self.desplin)
        self.v.addWidget(self.table)
        self.v.addWidget(self.frame)
        return super().setLayout(self.v)
    
    
    
    
