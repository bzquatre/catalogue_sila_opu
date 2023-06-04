from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from components.tab import TabWidget
from components.catalogue import Catalogue
import sys
from components.web import Web
class MainWindo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Icon.ico"))
        tabs=[[Catalogue(self),QIcon('images/catalogue.png') ,'Catalogue'],
                      [Web(parent=self,url='https://www.opu.dz'),QIcon('images/site.png') , 'Site Web'],
                      [Web(parent=self,url='https://st.iqraa.opu.dz') ,QIcon('images/iqraa.png'), 'Platforme']]
        self.tab=TabWidget()
        self.setObjectName('MainWindo')
        self.setGeometry(100,50,800,600)
        for i in tabs:
                    self.tab.addTab(i[0],i[1],i[2])
        self.setStyleSheet('#MainWindo{background-color: #0F9D58;}')
        self.setLayout()
        self.showFullScreen()
    def setLayout(self):
        v=QVBoxLayout()
        v.setContentsMargins(0,0,0,0)
        v.setSpacing(0)
        v.addWidget(self.tab)
        return super().setLayout(v)
    def resizeEvent(self, a0) :
        self.tab.setIconSize(QSize(100,int(self.height()/self.tab.count())-int(self.tab.count()*10)))
        return super().resizeEvent(a0)
if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setApplicationName('OPU')
    app.setApplicationVersion('1.0.1')
    windo=MainWindo()
    sys.exit(app.exec_())