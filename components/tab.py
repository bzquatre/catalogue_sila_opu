from PyQt5.QtWidgets import QDialog,QApplication,QHBoxLayout,QTabBar,QTabWidget,QStylePainter,QStyleOptionTab,QStyle,QGraphicsDropShadowEffect
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect,QPoint,QSize
style="""
QTabWidget {
    background-color: rgb(255,255,255);
    border:0px;
    color:#0F9D58;
}
QTabBar{
    font-size:24px;
    font-family:Poppins;
    background-color:#0F9D58;
}
QTabBar::tab{
    height:250px;
    background-color:#0F9D58;
    color:rgb(255, 255, 255);
    padding: 15px 15px 15px 15px;
}
        
QTabBar::tab:selected{
    border:none;
    background-color:rgba(0,0,0,50);
}"""
class TabBar(QTabBar):
    def __init__(self,parent):
        super().__init__(parent=parent)
        x=QGraphicsDropShadowEffect()
        x.setBlurRadius(5)
        x.setXOffset(3)
        x.setYOffset(3)
    def tabSizeHint(self, index):
        s = QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s
    def paintEvent(self, event):
        painter = QStylePainter(self)
        opt = QStyleOptionTab()
        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QStyle.CE_TabBarTabShape, opt)
            painter.save()
            s = opt.rect.size()
            s.transpose()
            r = QRect(QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r
            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QStyle.CE_TabBarTabLabel, opt)
            painter.restore()
    

class TabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        x=TabBar(self)
        self.setTabBar(x)
        self.setTabPosition(QTabWidget.West)
        self.setStyleSheet(style)