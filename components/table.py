from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QFrame,QPushButton,QHBoxLayout,QLabel
from PyQt5.QtCore import Qt
style="""
QTableWidget{
    border:none;
}
QHeaderView::section{
    Background-color: rgb(255, 255, 255);
    color:#000;
    border: 0px solid #ffffff;
    border-radius:0px;
    padding: 0px;
    margin: 0px;
}
QHeaderView {padding:0px;
background-color:#ffffff;
font-size: 20px;
color:rgba(25, 24, 66, 1);
border-radius:0px;}
"""
class Pagination(QFrame):
    def __init__(self,parent=None,page=None):
        super().__init__(parent)
        self.btn_prev,self.btn_next,self.pagelabel=QPushButton(self,text="<"),QPushButton(self,text=">"),QLabel(self,text='')
        self.pagelabel.setAlignment(Qt.AlignCenter)
        layoutpage=QHBoxLayout()
        layoutpage.setSpacing(0)
        [layoutpage.addWidget(i) for i in [self.btn_prev,self.pagelabel,self.btn_next]]
        self.setLayout(layoutpage)
class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.objs=[]
        self.setStyleSheet(style)
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.verticalHeader().setDefaultSectionSize(400)
        
    def add_obj(self,obj):
        self.objs.append(obj)
    def init_header(self,colum):
        self.setColumnCount(colum)
        self.setRowCount(0)
        for i in range(colum):
            self.setHorizontalHeaderItem(i,QTableWidgetItem(''))
        
    def clear(self):
        self.objs.clear()
        return super().clear()
    def resizeEvent(self, e):
        self.withe_column(self.columnCount(),self.columnCount())
        return super().resizeEvent(e)
    def withe_column(self,n,nbr):
        if n==-1:
            return None
        else :
            self.setColumnWidth(n,int(self.width()//nbr)-4)
            return self.withe_column(n-1,nbr)

