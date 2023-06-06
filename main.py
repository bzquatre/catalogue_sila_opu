from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from components.tab import TabWidget
from components.catalogue import Catalogue
from config import Book,session
import pandas as pd
import sys,os,shutil
from components.web import Web
class MainWindo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("Icon.ico"))
        tabs=[[Catalogue(self),QIcon('images/catalogue.png') ,''],
            [Web(parent=self,url='https://www.opu.dz'),QIcon('images/site.png') , ''],
            [Web(parent=self,url='https://st.iqraa.opu.dz') ,QIcon('images/iqraa.png'), '']]
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
    def keyPressEvent(self, event):
        modifiers = QApplication.keyboardModifiers()
        if event.key() == Qt.Key_I and modifiers == Qt.ControlModifier:
            home_directory = os.getenv('HOME')
            fname, _ = QFileDialog.getOpenFileName(self, 'Open Books CSV File ', home_directory, 'XLSX files (*.xlsx)')
            if fname!='':
                data = pd.read_excel(fname)
                # Iterate over the rows and insert data into the database
                session.query(Book).delete()
                for _, row in data.iterrows():
                    book = Book(
                        isbn=row['ISBN'],
                        edition=row['Edition'],
                        title=row['Title'],
                        authors=row['Authors'],
                        category=row['Category'],
                        price=row['Price'],
                        cover='cover/' + str(row['Edition']) + '.jpg'
                    )
                    session.add(book)
                session.commit()
        elif event.key() == Qt.Key_U and modifiers == Qt.ControlModifier:
            file_dialog = QFileDialog()
            file_dialog.setWindowTitle("select Covers Books")
            file_dialog.setFileMode(QFileDialog.ExistingFiles)  # Allow selecting multiple files
            file_dialog.setNameFilter("Images (*.png *.jpg *.jpeg)")  # Set file filter to images

            if file_dialog.exec_():
                # Retrieve selected file paths
                selected_files = file_dialog.selectedFiles()
                
                # Move or copy the files to the desired folder
                destination_folder =os.getcwd()+"/cover/"
                os.makedirs(destination_folder, exist_ok=True)
                for file_path in selected_files:
                    # Copy the file
                    shutil.copy(file_path, destination_folder)
if __name__=="__main__":
    app=QApplication(sys.argv)
    app.setApplicationName('OPU')
    app.setApplicationVersion('1.0.1')
    windo=MainWindo()
    sys.exit(app.exec_())