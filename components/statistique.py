from PyQt5.QtWidgets import QFrame,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt   
style="""
QFrame {
    border:2px solid #0F9D58;
    border-radius: 5px;
}
QLabel {
    border:none;
    font-size: 15px;
}
#value{
    border:none;
    font-size: 30px;}
"""
class Statistique(QFrame):
    def __init__(self,parent,title):
        super().__init__(parent)
        self.setFixedHeight(100)
        self.setFixedWidth(180)
        self.setStyleSheet(style)
        self.title=QLabel(parent=self,text=title)
        self.value=QLabel(self)
        self.title.setAlignment(Qt.AlignCenter),self.value.setAlignment(Qt.AlignCenter)  
        self.value.setObjectName('value')
        self.setLayout()
    def setLayout(self ):
        a0=QVBoxLayout()
        a0.addWidget(self.title),a0.addWidget(self.value)
        return super().setLayout(a0)