from PyQt5.QtWidgets import QLabel,QFrame,QHBoxLayout
from PyQt5.QtCore import Qt   
style="""
QLabel {
    background-color:rgb(241,248,255);
    color:#0F9D58;
    font-size: 34px;
    border: none;
    padding-bottom:7px;
}
QFrame{
    background-color:rgb(255,255,255);
    padding-top:0px;
}
""" 
class TitrePage(QFrame):
    def __init__(self,titre):
        super().__init__()
        self.title=QLabel(titre,self)
        self.title.setAlignment(Qt.AlignCenter)    
        self.setStyleSheet(style)
        self.setLayout()
    def setLayout(self):
        h=QHBoxLayout()
        h.setContentsMargins(0,0,0,0)
        h.setSpacing(0)
        h.addWidget(self.title)
        return super().setLayout(h)