from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QVBoxLayout, QLabel
from PyQt5.QtGui import QPixmap, QFont


class TabProfile_OverView_View(QVBoxLayout):

    def __init__(self, qwidget):
        super().__init__()
        self.Profile_ImageLabel = QLabel(qwidget)
        self.User_Name_Label = QLabel("kiarash", qwidget)
        self.setupUi()

    def setupUi(self):
        self.Profile_ImageLabel. \
            setPixmap(QPixmap("/Users/Kia/Desktop/Cayload Desktop/Resourses/IMG_8613.JPG").
                      scaled(100, 100, Qt.IgnoreAspectRatio))
        self.Profile_ImageLabel.setMaximumSize(QSize(100, 100))
        self.User_Name_Label.setFont(QFont("Times", 17, QFont.Bold))
        self.User_Name_Label.setAlignment(Qt.AlignCenter)
        self.addWidget(self.Profile_ImageLabel)
        self.addWidget(self.User_Name_Label)
        self.addStretch(1)
        self.addSpacing(10)
        self.setAlignment(Qt.AlignCenter)


# from PyQt5.QtWidgets import *
# import sys
#
#
# class test1(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Music Player")
#         self.setGeometry(450, 150, 480, 700)
#         self.x = TabProfile_OverView_View(self)
#         self.setLayout(self.x)
#         self.show()
#
#
# def main():
#     App = QApplication(sys.argv)
#     window = test1()
#     sys.exit(App.exec_())
#
#
# if __name__ == '__main__':
#     main()
