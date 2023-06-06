from PyQt5.QtWidgets import QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
class FButton(QPushButton):
    def __init__(self,parent,text='SERCHE'):
        super().__init__(parent=parent)
        self.setText(text)
        self.setFixedHeight(200)
        self.setStyleSheet("""
        QPushButton{
            font:18px;
            color: rgb( 255, 255, 255);
            background-color:rgba(15,157,88,0.8);
            border:0px solid blue;
            border-radius: 12px;
            margin: 5px ;
            padding: 5px 10px 5px 10px;
            }
        QPushButton:hover {
            background-color:rgba(15,157,88,1);
            }""")
class Button(QPushButton):
    def __init__(self,parent,text='SERCHE'):
        super().__init__(parent=parent)
        self.setText(text)
        self.setStyleSheet("""
        QPushButton{
            font:18px;
            color: rgb( 255, 255, 255);
            background-color:rgba(15,157,88,0.8);
            border:0px solid blue;
            border-radius: 12px;
            margin: 10px ;
            padding: 10px 20px 10px 20px;
            }
        QPushButton:hover {
            background-color:rgba(15,157,88,1);
            }""")
