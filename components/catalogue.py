from PyQt5.QtWidgets import QWidget,QVBoxLayout,QHBoxLayout,QFrame
from components.Entry import Combobox, Entry
from components.table import Table,Pagination
from components.Button import Button,FButton
from components.header import Header
from config import Book,Categories,session
from components.bookwidget import BookWidget
class Buttons(QFrame):
    def __init__(self) :
        super().__init__()
        self.buttons=[]
        self.vlayout=QHBoxLayout()
        self.setLayout(self.vlayout)
    def addItem(self,text):
        self.buttons.append(FButton(self,text))
        self.vlayout.addWidget(self.buttons[-1])
class Catalogue(QWidget):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.page=0
        self.category,self.text_research,self.table,self.button,self.reture=Combobox(self),Entry(self),Table(),Button(self,text='Research'),Button(self,text='<')
        self.text_research.setPlaceholderText('Research')
        self.text_research.setFixedWidth(500)
        self.header=Header()
        self.frame=Buttons()
        self.v=QVBoxLayout()
        self.pagination=Pagination(self)
        self.table.init_header(4)
        self.category.addItem('ALL Category')
        for item in [dis.description for dis in session.query(Categories).all()]:
            self.category.addItem(item)
            self.frame.addItem(item)
        self.setLayout()
        self.text_research.returnPressed.connect(self.showData)
        self.button.clicked.connect(self.showData)
        self.category.currentTextChanged.connect(self.showData) 
        for item in self.frame.buttons:    
            item.clicked.connect(self.buttonClicked)   
        self.pagination.btn_next.clicked.connect(self.next)
        self.pagination.btn_prev.clicked.connect(self.prev)
        self.reture.clicked.connect(self.back)
        self.data=session.query(Book,Categories).join(Categories,Book.category==Categories.code).all()
        self.text_research.set_autocomplite([livre[0].title for livre in self.data])
        self.showData()
        self.etat1()
    def getNmbrPage(self):
        try:
            return int(len(self.data)/20) if len(self.data)%20==0 else int(len(self.data)/20)+1
        except:
            return 0
    def next(self):
        if self.page+1 < self.getNmbrPage():
            self.page=self.page+1
            self.pagination.pagelabel.setText(f"{self.page+1} of {self.getNmbrPage()}")
            self.showData()
    def prev(self):
        if self.page-1 >=0 :
            self.page=self.page-1
            self.pagination.pagelabel.setText(f"{self.page+1} of {self.getNmbrPage()}")
            self.showData()
    def getData(self):
        self.data = session.query(Book, Categories)\
            .join(Categories, Book.category == Categories.code)\
            .filter(Categories.description == self.category.currentText(), Book.title.like(f"%{self.text_research.text()}%"))\
            .all() if self.category.currentText()!='ALL Category' else session.query(Book, Categories)\
            .join(Categories, Book.category == Categories.code)\
            .filter(Book.title.like(f"%{self.text_research.text()}%"))\
            .all()
    def showData(self):
        self.table.clear()
        self.table.init_header(4)
        self.getData()
        self.pagination.pagelabel.setText(f"{self.page+1} of {self.getNmbrPage()}")
        for j,article in  enumerate(self.data[self.page*20:self.page*20+20]):
            if j%4==0:
                self.table.setRowCount(self.table.rowCount()+1)
            self.table.setCellWidget(self.table.rowCount()-1,j%4,BookWidget(title=article[0].title, authors=article[0].authors, cover_path=article[0].cover, price=article[0].price))
    def back(self):
        self.text_research.setText('')
        self.etat1()
        self.text_research.setText('')
    def buttonClicked(self):
        button = self.sender()  # Get the reference to the clicked button
        self.category.setCurrentText(button.text())
        self.etat2()
        self.text_research.setText('')
    def etat2(self):
        self.frame.hide()
        [i.show() for i in [self.text_research,self.button,self.category,self.table,self.reture,self.pagination]]
    def etat1(self):
        self.frame.show()
        [i.hide() for i in [self.text_research,self.button,self.category,self.table,self.reture,self.pagination]]
    def setLayout(self):
        h=QHBoxLayout()
        h.addStretch(1),h.addWidget(self.reture),h.addWidget(self.text_research),h.addWidget(self.button),h.addStretch(1)
        self.v.setContentsMargins(0,0,0,0)
        self.v.setSpacing(0)
        self.v.addWidget(self.header)
        self.v.addLayout(h)
        self.v.addWidget(self.category)
        self.v.addWidget(self.pagination)
        self.v.addWidget(self.table)
        self.v.addWidget(self.frame)
        return super().setLayout(self.v)