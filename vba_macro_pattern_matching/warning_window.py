import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import urllib.request

infinity_logo_url = "https://raw.githubusercontent.com/hgrgr/INFINITY_VBA/main/icon/infinity.png"
warning_logo_url = "https://raw.githubusercontent.com/hgrgr/INFINITY_VBA/main/icon/warning%20(1).png"


class MyApp(QWidget):

    def __init__(self, title, content):
        self.title = title
        self.content = content
        super().__init__()
        self.initUI()

    def initUI(self):
        # 상태표시줄
        self.setWindowTitle('Infinity')
        self.setWindowIcon(QIcon(load_img(infinity_logo_url, 50, 50)))
        self.setGeometry(500, 300, 1000, 400)
        self.show()

        # 알림창 TXET
        main_label = QLabel(self.title, self)
        main_label.setAlignment(Qt.AlignCenter)

        sub_label = QLabel(self.content, self)
        sub_label.setAlignment(Qt.AlignVCenter)
        sub_label.setAlignment(Qt.AlignCenter)

        main_label.setStyleSheet("color: red;")
        font1 = main_label.font()
        font1.setPointSize(20)
        font1.setBold(True)

        font2 = sub_label.font()
        font2.setFamily('Times New Roman')

        main_label.setFont(font1)
        sub_label.setFont(font2)

        # 경고 아이콘
        img_label = QLabel()
        img_label.setPixmap(load_img(warning_logo_url, 80, 80))

        # 위치설정
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(img_label)
        hbox.addWidget(main_label)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        vbox.addWidget(sub_label)
        vbox.addStretch(1)

        self.setLayout(vbox)


def load_img(url, width, height):
    img_url = url
    img = urllib.request.urlopen(img_url).read()
    img_obj = QPixmap()
    img_obj.loadFromData(img)
    img_obj = img_obj.scaled(width, height)
    return img_obj


def run(title, content):
    app = QApplication(sys.argv)
    ex = MyApp(title, content)
    sys.exit(app.exec_())
