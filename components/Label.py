from PyQt5.QtWidgets import QLabel,QPushButton
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import QSize,Qt 
class Label(QLabel):
    def __init__(self,text):
        super().__init__(text=text)
        self.setAlignment(Qt.AlignCenter)
        self.setWordWrap(True)
        self.setStyleSheet()
    def setStyleSheet(self):
        return super().setStyleSheet("""
        font-size: 16px;
        border: none;
        """)
class LabelNotification(QLabel):
    def __init__(self,parent=None,text=""):
        super().__init__(parent=parent,text=text)
        self.css()
    def css(self):
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
        margin-top: 0px ;
        margin-bottom:0px ;
        background-color:rgb(241,248,255);
        color:rgba(25, 24, 66, 1);
        font-size: 18px;
        border: none;
        padding-bottom:7px;
            """)
class HeaderLabel(QPushButton):
    def __init__(self,parent=None,text=""):
        super().__init__(parent=parent,text=text)
        self.css()
    def css(self):
        self.setIcon(QIcon('img/logo.png'))
        self.setIconSize(QSize(50,50))
        self.setFixedWidth(258)
        self.setStyleSheet("""
        border:0px solid blue;
        padding-top:10px;
        padding-bottom:10px;
        background-color:#1E81EA;
         color:rgb(255, 255, 255);
        font-size: 40px;""")
class HeaderTitel(QLabel):
    def __init__(self,parent=None,text=""):
        super().__init__()
        self.css()
    def css(self):
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
        background-color:rgb(241,248,255);
        color:rgba(25, 24, 66, 1);
        font-size: 34px;
        border: none;
        padding-bottom:7px;
            """)
    def settitle(self,title):
        self.setText(title)
class BLabel(QLabel):
    def __init__(self,parent,text):
        super().__init__(parent=parent,text=text)
        self.setStyleSheet(f"""
           background-color:rgba(255,255,255,255);
        color:rgba(25, 24, 66, 1);
        font-size: 22px;
        border: none;
        """)
class FooterLabel(QLabel):
    def __init__(self,parent=None,text=""):
        super().__init__(parent=parent,text=text)
        self.css()
    def css(self):
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
        background-color:rgba(255,255,255,255);
        color:rgba(25, 24, 66, 1);
        font-size: 34px;
        border: none;
        padding-bottom:7px;
            """)