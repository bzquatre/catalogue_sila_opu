from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem
style="""
QTableWidget{
        border:none;
    }
QHeaderView::section{
        Background-color: rgba(15,157,88,0.8);
        color:#000;
        border: 0.5px solid #707070;
        border-radius:0px;
        padding: 0px;
        margin: 0px;
    }
QHeaderView {padding:0px;
    background-color:#F0F7FE;
    font-size: 20px;
    color:rgba(25, 24, 66, 1);
    border-radius:0px;}
    QTableWidget::QLabel{
    border: none;
    padding: 0px;
    margin: 0px;
    }
"""
class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.objs=[]
        self.setStyleSheet(style)
        self.verticalHeader().hide()
        
    def add_obj(self,obj):
        self.objs.append(obj)
    def init_header(self,colum):
        self.setColumnCount(len(colum))
        self.setRowCount(0)
        for i,j in enumerate(colum):
            self.setHorizontalHeaderItem(i,QTableWidgetItem(j))
        
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

