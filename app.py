import PyQt5.QtWidgets as qtw
from MainWindow import *


def main():
    app = qtw.QApplication([])
    mainwindow = MainWindow()
    app.exec_()



if __name__ == '__main__':
    main()
