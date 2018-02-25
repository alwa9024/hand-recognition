#!usr/bin/env python3

# import the needed libraries
import sys
import cv2
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import queue

##############################
class mainWindow(QMainWindow):

    # initialize the main window
    def __init__(self):
        super().__init__()

        #self.noods = QWidget(webcam)
        self.woohoo = mainWidget()

##########################
class mainWidget(QWidget):


    # function for the controlling GUI
    def __init__(self):
        super().__init__()
        # define a custom signal to be sent from the stop function to start to kill the recording
        self.kill_rec = pyqtSignal()

        # set up the layout(s) and add to the main window
        hLayout1 = QHBoxLayout()

        start = QPushButton("Start Recording")
        start.clicked.connect(self.startAction)

        stop = QPushButton("Stop Recording")
        stop.clicked.connect(self.stopAction)

        write = QPushButton("Save file as: ")
        write.clicked.connect(self.writeAction)

        file_name = QLineEdit()


        hLayout1.addWidget(start)
        hLayout1.addWidget(stop)
        hLayout1.addWidget(write)
        hLayout1.addWidget(file_name)

        self.setLayout(hLayout1)
        self.show()

    # Start the video recording here
    def startAction(self):
        # set a flag
        self.play = True

        x1, y1, x2, y2 = 420, 200, 620, 400

        cap = cv2.VideoCapture(0)

        cap.set(3, 800)
        cap.set(4, 600)

        while (self.play):
            # capture frame-by-frame
            ret, image = cap.read()
            image = cv2.flip(image, 1)
            # Operate on the frame
            # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            image = cv2.rectangle(image, (x1, y1), (x2, y2), (255, 200, 0), 3)
            subIm = image[y1:y2, x1:x2]

            # display the result
            cv2.imshow('frame', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # kill the recording
        cv2.destroyAllWindows()


    # function to stop the recording
    def stopAction(self):
        self.play = False



    # function to write the words to a file with the specified file name
    def writeAction(self):
        print("hi bitch numero dos")


###########
def main():
    app = QApplication(sys.argv)
    start = mainWindow()

    ### This pops up a weird extra window. Avoid because life is hard
    ##start.show()

    sys.exit(app.exec_())


###########################
if(__name__ == "__main__"):
    main()





