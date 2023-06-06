from PyQt5.QtWidgets import QLineEdit,QCompleter,QComboBox,QDateTimeEdit
from PyQt5.QtGui import QIcon,QDoubleValidator,QIntValidator
from PyQt5.QtCore import QSize,Qt
class Entry(QLineEdit):
    def __init__(self, parent) :
        super().__init__(parent=parent)
        self.setStyleSheet("""
        QLineEdit{
         font:24px;
            background-color: rgba(0,0,0,0);
            border:1px solid rgba(46, 82, 101,100) ;
            border-radius: 5px;
            padding:5px;
            margin: 10px ;
            color: rgba( 0, 0,0, 40);}
        QLineEdit:focus{
                 border:2px solid #0F9D58;
                 color: rgba( 0, 0,0, 255);
        }
        """)
    def is_float(self):
        self.setValidator(QDoubleValidator(self))
    def is_int(self):
        self.setValidator(QIntValidator(self))
    def set_autocomplite(self,liste):
        self.completer=QCompleter(liste)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.setCompleter(self.completer)
class Combobox(QComboBox):
    def __init__(self,parent=None,liste=[]):
        super().__init__(parent=parent)
        try:
            self.addItems(liste)
        except Exception as e :
            pass
        self.setStyleSheet("""
        QComboBox{
         font:24px;
            background-color: rgba(0,0,0,0);
            border:1px solid rgba(46, 82, 101,100) ;
            border-radius: 5px;
            padding:5px;
            margin: 10px ;
            color: rgba( 0, 0,0, 40);}
        QComboBox:focus{
                 border:2px solid #0F9D58;
                 color: rgba( 0, 0,0, 255);
        
        }
        """)
class Code(QLineEdit):
    def __init__(self, parent) :
        super().__init__(parent=parent)
        self.setValidator(QDoubleValidator(self))
        self.setPlaceholderText("N°ISBN Or Code")
        self.textChanged.connect(self.is_num)
        self.css()
    def is_num(self):
        x=""
        for i in self.text():
            if i not in ["E","e",",","-"]:
                x+=i
        self.setText(x)
    def css(self):
        self.setStyleSheet("""
        QLineEdit{
            font:24px;
            background-color: rgba(0,0,0,0);
            border:1px solid rgba(46, 82, 101,100) ;
            border-radius: 5px;
            padding:5px;
            color: rgba( 0, 0,0, 40);
            margin: 10px ;
        }
        QLineEdit:focus{
            border:2px solid rgba(79, 154, 254, 1);
            color: rgba( 0, 0,0, 255);
            margin: 10px ;
        }
        """)