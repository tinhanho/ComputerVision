from PyQt5 import QtWidgets, QtCore
import sys
import globals
from Load import LoadVideo
from BackgroundSubtraction import BackgroundSubtraction
from OpticalFlow import Preprocessing, VideoTracking
# 設定放置 Layout 的 Widget 樣式
style_box = '''
    border:1px solid #bdbebd;
'''

# 設定按鈕樣式
style_btn = '''
    QPushButton{
        font-size:15px
    }
    QPushButton:pressed{
        background:#f90;
    }
'''

globals.initialize()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("cvdlhw1.ui")
MainWindow.resize(900, 800)

# Load Image & Video
vbox = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("Load Image")
vbox.setGeometry(20, 20, 180, 240)
vbox.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox)
pushButton1_1 = QtWidgets.QPushButton(vbox)
pushButton1_1.setObjectName("Load Image")
pushButton1_1.setText("Load Image")
pushButton1_1.setStyleSheet(style_btn)
# pushButton1_1.clicked.connect(LoadFolder)
v_layout.addWidget(pushButton1_1)

pushButton1_2 = QtWidgets.QPushButton(vbox)
pushButton1_2.setObjectName("Load Video")
pushButton1_2.setText("Load Video")
pushButton1_2.setStyleSheet(style_btn)
pushButton1_2.clicked.connect(LoadVideo)
v_layout.addWidget(pushButton1_2)

# Background Subtraction
vbox2 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox2)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("Background \n Subtraction")
vbox2.setGeometry(240, 20, 180, 100)
vbox2.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox2)
pushButton2_1 = QtWidgets.QPushButton(vbox2)
pushButton2_1.setObjectName("1. Background Subtraction")
pushButton2_1.setText("1. Background Subtraction")
pushButton2_1.setStyleSheet(style_btn)
pushButton2_1.clicked.connect(BackgroundSubtraction)
v_layout.addWidget(pushButton2_1)


# Optical Flow
vbox3 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox3)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("Optical Flow")
vbox3.setGeometry(240, 220, 180, 150)
vbox3.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox3)
pushButton3_1 = QtWidgets.QPushButton(vbox3)
pushButton3_1.setObjectName("2.1 Preprocessing")
pushButton3_1.setText("2.1 Preprocessing")
pushButton3_1.setStyleSheet(style_btn)
# pushButton2_1.clicked.connect(LoadFolder)
v_layout.addWidget(pushButton3_1)

pushButton3_2 = QtWidgets.QPushButton(vbox3)
pushButton3_2.setObjectName("2.2 Video tracking")
pushButton3_2.setText("2.2 Video tracking")
pushButton3_2.setStyleSheet(style_btn)
# pushButton2_1.clicked.connect(LoadFolder)
v_layout.addWidget(pushButton3_2)

# PCA
vbox4 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox4)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("PCA")
vbox4.setGeometry(240, 420, 180, 100)
vbox4.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox4)
pushButton2_1 = QtWidgets.QPushButton(vbox4)
pushButton2_1.setObjectName("3. Dimension Reduction")
pushButton2_1.setText("3. Dimension Reduction")
pushButton2_1.setStyleSheet(style_btn)
# pushButton2_1.clicked.connect(LoadFolder)
v_layout.addWidget(pushButton2_1)

# MNIST
vbox5 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox5)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("MNIST")
vbox5.setGeometry(440, 20, 360, 200)
vbox5.setStyleSheet(style_box)

#ResNet50
vbox6 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox6)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("ResNet50")
vbox6.setGeometry(440, 240, 360, 200)
vbox6.setStyleSheet(style_box)

if __name__ == '__main__':
    MainWindow.show()
    sys.exit(app.exec_())


