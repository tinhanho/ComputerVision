from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QImage
from PyQt5.QtCore import Qt, QBuffer, QByteArray, QIODevice
import sys
import globals
from Load import LoadVideo, LoadImage, LoadImages5
from BackgroundSubtraction import BackgroundSubtraction
from OpticalFlow import Preprocessing, VideoTracking
from PCA import DimensionReduction
from MNIST import ShowModelStructure, ShowAccuracyAndLoss, Predict
from ResNet50 import ShowModelStructureRN50, ShowImages
from io import BytesIO
import numpy as np
from PIL import Image
from torchvision import transforms,datasets

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
global drawing
global lastPoint
drawing = False
lastPoint = None
def Reset():
    pixmap = QPixmap(180, 200)
    pixmap.fill(QColor("black"))
    label.setPixmap(pixmap)

def qPixmapToImage():
    pixmap = label.pixmap()
    byte_array = QByteArray()
    buffer = QBuffer(byte_array)
    buffer.open(QIODevice.WriteOnly)
    pixmap.save(buffer, "PNG")
    image = Image.open(BytesIO(byte_array))
    image_np = np.array(image)
    transform = transforms.Compose([
        transforms.ToPILImage(),  # Convert NumPy array to PIL image
        transforms.Resize((32, 32)),
        transforms.Grayscale(),
        transforms.ToTensor()
    ])
    preprocessed_image = transform(image_np)
    globals.preimage = preprocessed_image


def mousePressEventHandler(event):
    global drawing
    global lastPoint
    if event.button() == Qt.LeftButton:
        drawing = True
        lastPoint = event.pos()

def mouseMoveEventHandler(event):
    global lastPoint
    if drawing:
        painter = QPainter(label.pixmap())
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.white)
        painter.setPen(pen)
        painter.drawLine(lastPoint, event.pos())
        lastPoint = event.pos()
        label.update()
def mouseReleaseEventHandler(event):
    global drawing
    global lastPoint
    if event.button() == Qt.LeftButton:
        drawing = False
        lastPoint = None

def setdtext():
    dtext.setText(globals.pdigit)

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
pushButton1_1.clicked.connect(LoadImage)
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
pushButton3_1.clicked.connect(Preprocessing)
v_layout.addWidget(pushButton3_1)

pushButton3_2 = QtWidgets.QPushButton(vbox3)
pushButton3_2.setObjectName("2.2 Video tracking")
pushButton3_2.setText("2.2 Video tracking")
pushButton3_2.setStyleSheet(style_btn)
pushButton3_2.clicked.connect(VideoTracking)
v_layout.addWidget(pushButton3_2)

# PCA
vbox4 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox4)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("PCA")
vbox4.setGeometry(240, 420, 180, 100)
vbox4.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox4)
pushButton4_1 = QtWidgets.QPushButton(vbox4)
pushButton4_1.setObjectName("3. Dimension Reduction")
pushButton4_1.setText("3. Dimension Reduction")
pushButton4_1.setStyleSheet(style_btn)
pushButton4_1.clicked.connect(DimensionReduction)
v_layout.addWidget(pushButton4_1)

# MNIST
vbox5 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox5)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("MNIST")
vbox5.setGeometry(440, 20, 180, 270)
vbox5.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox5)
pushButton5_1 = QtWidgets.QPushButton(vbox5)
pushButton5_1.setObjectName("1. Show Model Structure")
pushButton5_1.setText("1. Show Model Structure")
pushButton5_1.setStyleSheet(style_btn)
pushButton5_1.clicked.connect(ShowModelStructure)
v_layout.addWidget(pushButton5_1)

pushButton5_2 = QtWidgets.QPushButton(vbox5)
pushButton5_2.setObjectName("2. Show Accuracy and Loss")
pushButton5_2.setText("2. Show Accuracy and Loss")
pushButton5_2.setStyleSheet(style_btn)
pushButton5_2.clicked.connect(ShowAccuracyAndLoss)
v_layout.addWidget(pushButton5_2)

pushButton5_3 = QtWidgets.QPushButton(vbox5)
pushButton5_3.setObjectName("3. Predict")
pushButton5_3.setText("3. Predict")
pushButton5_3.setStyleSheet(style_btn)
pushButton5_3.clicked.connect(qPixmapToImage)
pushButton5_3.clicked.connect(Predict)
pushButton5_3.clicked.connect(setdtext)
v_layout.addWidget(pushButton5_3)

pushButton5_4 = QtWidgets.QPushButton(vbox5)
pushButton5_4.setObjectName("4. Reset")
pushButton5_4.setText("4. Reset")
pushButton5_4.setStyleSheet(style_btn)
pushButton5_4.clicked.connect(Reset)
v_layout.addWidget(pushButton5_4)

vbox5_3 = QtWidgets.QWidget(MainWindow)
dtext = QtWidgets.QLabel(vbox5_3)
dtext.setAlignment(QtCore.Qt.AlignCenter)

vbox5_3.setGeometry(510, 270, 50, 50)


vbox5_2 = QtWidgets.QWidget(MainWindow)
label = QtWidgets.QLabel(vbox5_2)
vbox5_2.setGeometry(640, 20, 180, 200)
vbox5_2.setStyleSheet(style_box)
pixmap = QPixmap(180, 200)
pixmap.fill(QColor("black"))
label.setPixmap(pixmap)
label.mousePressEvent = mousePressEventHandler
label.mouseMoveEvent = mouseMoveEventHandler
label.mouseReleaseEvent = mouseReleaseEventHandler




#ResNet50
vbox6 = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox6)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("ResNet50")
vbox6.setGeometry(440, 350, 180, 200)
vbox6.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox6)
pushButton6_1 = QtWidgets.QPushButton(vbox6)
pushButton6_1.setObjectName("Load images")
pushButton6_1.setText("Load images")
pushButton6_1.setStyleSheet(style_btn)
pushButton6_1.clicked.connect(LoadImages5)
v_layout.addWidget(pushButton6_1)

pushButton6_2 = QtWidgets.QPushButton(vbox6)
pushButton6_2.setObjectName("5.1 Show Images")
pushButton6_2.setText("5.1 Show Images")
pushButton6_2.setStyleSheet(style_btn)
pushButton6_2.clicked.connect(ShowImages)
v_layout.addWidget(pushButton6_2)

pushButton6_3 = QtWidgets.QPushButton(vbox6)
pushButton6_3.setObjectName("5.2 Show Model Structure")
pushButton6_3.setText("5.2 Show Model Structure")
pushButton6_3.setStyleSheet(style_btn)
pushButton6_3.clicked.connect(ShowModelStructureRN50)
v_layout.addWidget(pushButton6_3)


if __name__ == '__main__':
    MainWindow.show()
    sys.exit(app.exec_())


