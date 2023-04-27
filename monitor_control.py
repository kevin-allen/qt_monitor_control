from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys



class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.

    This is use to create additional windows beside our main window
    """
    def __init__(self,index,window_width,window_height):
        super().__init__()

        self.setFixedSize(window_width, window_height)
        layout = QVBoxLayout()
        self.setWindowTitle("Monitor control {}".format(index))

        self.label = QLabel("")
        imageFileName="/home/kevin/Pictures/beaumont_rag_billy_lick.png"
        pixmap = QPixmap(imageFileName) # we create a pixmap that will go on the label
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio)) # scale the pixmax to the size of the label
        
        layout.addWidget(self.label)
        self.setLayout(layout)
        
        self.location_on_the_screen(index)
        
    def location_on_the_screen(self,index):
        """
        Set the location of the window
        """
        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()
        widget = self.geometry()
        xOffset = sg.width()-ag.width()
        self.move(widget.width()*index+xOffset, 0)

    def change_image(self,imageFileName=None):
        """
        Function to change the image on the label
        """
        if imageFileName is None: 
            imageFileName="/home/kevin/Pictures/bioRxiv.png"
            
        pixmap = QPixmap(imageFileName) # we create a pixmap that will go on the label
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio)) # scale the pixmax to the size of the label
        

class MainWindow(QMainWindow):
    """
    The main window of our application
    """

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)

        # this will set the window size
        self.window_width=640
        self.window_height=460

        
        self.setFixedSize(self.window_width, self.window_height)
        self.setWindowTitle("Monitor 0")


        self.layout = QVBoxLayout()
        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.on_button_press)

        # create a label and put an image file in it.
        self.label = QLabel("Amazing")
        imageFileName="beaumont_rag_billy_lick.png"
        pixmap = QPixmap(imageFileName) # we create a pixmap that will go on the label
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio)) # scale the pixmax to the size of the label
        self.label.setAlignment(Qt.AlignCenter)

        
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.container = QWidget()
        self.container.setLayout(self.layout)


        self.setCentralWidget(self.container)

        # set the location of the window
        self.location_on_the_screen(0)

        # we now create a list of additional windows that we store in a list.
        self.windowList=[]
        self.nWindows=2 # total number of windows that we want, including the main one
        for i in range(self.nWindows-1): # -1 because we already have the first one (main window)
            self.add_new_window(i+1)

    def change_image(self,imageFileName=None):
        """
        Function to change the image on the label
        """
        if imageFileName is None: 
            imageFileName="bioRxiv.png"
            
        pixmap = QPixmap(imageFileName) # we create a pixmap that will go on the label
        self.label.setPixmap(pixmap.scaled(self.label.size(), Qt.IgnoreAspectRatio)) # scale the pixmax to the size of the label
        
            
    def on_button_press(self):
        print("clicked")
        self.change_image()
        for w in self.windowList:
            w.change_image()


    def location_on_the_screen(self,index):
        ag = QDesktopWidget().availableGeometry() # available
        sg = QDesktopWidget().screenGeometry() # screen
        widget = self.geometry()
        #print("ag:",ag.width(), ag.height())
        #print("sg:",sg.width(), sg.height())
        xOffset = sg.width()-ag.width()
        #print("x_offset:", xOffset)
        #print("widget:",widget.width(),widget.height())
        #print("x:",widget.width()*index+xOffset, ", y:",0)
        self.move(widget.width()*index+xOffset, 0)

    def add_new_window(self,index):
        w = AnotherWindow(index,self.window_width,self.window_height)
        self.windowList.append(w) # add our new window to our list
        self.windowList[-1].show()


app = QApplication(sys.argv)


window = MainWindow()
window.show()


app.exec_()
