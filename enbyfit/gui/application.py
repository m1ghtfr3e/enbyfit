import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QHBoxLayout


class FitGui(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUi()

        self.show()

    def initUi(self):
        pass


def main():
    app = QApplication(sys.argv)
    win = FitGui()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
