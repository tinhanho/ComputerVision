from PyQt5 import QtWidgets, QtCore
import sys
from CameraCalibration import FindCorners, FindIntrinsic, FindExtrinsic, FindDistortion, ShowUndistorted
import globals
from LoadFolder import LoadFolder, LoadImageL, LoadImageR, LoadImage1, LoadImage2, LoadImage5
from AugmentedReality import ShowWordsOnBoard, ShowWordsVertically
from StereoDisparityMap import StereoDisparityMap
from Keypoints import Keypoints, MatchedKeyPoints
from VGG19 import ShowAugmentedImages, ShowModelStructure, ShowAccAndLoss

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
def getcomboboxint():
    globals.getint = getint.currentText()

def LineEditGetStr():
    globals.getstr = getstr.text()

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
MainWindow.setObjectName("MainWindow")
MainWindow.setWindowTitle("cvdlhw1.ui")
MainWindow.resize(900, 800)
globals.initialize()

# Load Image
vbox = QtWidgets.QWidget(MainWindow)
text = QtWidgets.QLabel(vbox)
text.setAlignment(QtCore.Qt.AlignCenter)
text.setText("Load Image")
vbox.setGeometry(20, 20, 180, 240)
vbox.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox)
pushButton1_1 = QtWidgets.QPushButton(vbox)
pushButton1_1.setObjectName("Load folder")
pushButton1_1.setText("Load folder")
pushButton1_1.setStyleSheet(style_btn)
pushButton1_1.clicked.connect(LoadFolder)
v_layout.addWidget(pushButton1_1)

pushButton1_2 = QtWidgets.QPushButton(vbox)
pushButton1_2.setObjectName("Load folder_L")
pushButton1_2.setText("Load folder_L")
pushButton1_2.setStyleSheet(style_btn)
pushButton1_2.clicked.connect(LoadImageL)
v_layout.addWidget(pushButton1_2)

pushButton1_3 = QtWidgets.QPushButton(vbox)
pushButton1_3.setObjectName("Load folder_R")
pushButton1_3.setText("Load folder_R")
pushButton1_3.setStyleSheet(style_btn)
pushButton1_3.clicked.connect(LoadImageR)
v_layout.addWidget(pushButton1_3)

# Calibration
vbox2 = QtWidgets.QWidget(MainWindow)
vbox2.setGeometry(240, 20, 180, 360)
vbox2.setStyleSheet(style_box)
text2 = QtWidgets.QLabel(vbox2)
text2.setText("Calibration")
text2.setAlignment(QtCore.Qt.AlignCenter)
vbox2.setStyleSheet(style_box)

v_layout = QtWidgets.QVBoxLayout(vbox2)
pushButton2_1 = QtWidgets.QPushButton(vbox2)
pushButton2_1.setObjectName("1.1 Find Corners")
pushButton2_1.setText("1.1 Find Corners")
pushButton2_1.setStyleSheet(style_btn)
pushButton2_1.clicked.connect(FindCorners)
v_layout.addWidget(pushButton2_1)

pushButton2_2 = QtWidgets.QPushButton(vbox2)
pushButton2_2.setObjectName("1.2 Find intrinsic")
pushButton2_2.setText("1.2 Find intrinsic")
pushButton2_2.setStyleSheet(style_btn)
pushButton2_2.clicked.connect(FindIntrinsic)
v_layout.addWidget(pushButton2_2)

#####
getint = QtWidgets.QComboBox(vbox2)
getint.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'])
v_layout.addWidget(getint)

pushButton2_3 = QtWidgets.QPushButton(vbox2)
pushButton2_3.setObjectName("1.3 Find extrinsic")
pushButton2_3.setText("1.3 Find extrinsic")
pushButton2_3.setStyleSheet(style_btn)
pushButton2_3.clicked.connect(getcomboboxint)
pushButton2_3.clicked.connect(FindExtrinsic)
v_layout.addWidget(pushButton2_3)
#####

pushButton2_4 = QtWidgets.QPushButton(vbox2)
pushButton2_4.setObjectName("1.4 Find distortion")
pushButton2_4.setText("1.4 Find distortion")
pushButton2_4.setStyleSheet(style_btn)
pushButton2_4.clicked.connect(FindDistortion)
v_layout.addWidget(pushButton2_4)

pushButton2_5 = QtWidgets.QPushButton(vbox2)
pushButton2_5.setObjectName("1.5 show result")
pushButton2_5.setText("1.5 show result")
pushButton2_5.setStyleSheet(style_btn)
pushButton2_5.clicked.connect(ShowUndistorted)
v_layout.addWidget(pushButton2_5)

# SIFT
vbox3 = QtWidgets.QWidget(MainWindow)
vbox3.setGeometry(240, 400, 180, 350)
vbox3.setStyleSheet(style_box)
text3 = QtWidgets.QLabel(vbox3)
text3.setText("SIFT")
text3.setAlignment(QtCore.Qt.AlignCenter)
vbox3.setStyleSheet(style_box)
v_layout = QtWidgets.QVBoxLayout(vbox3)
pushButton3_1 = QtWidgets.QPushButton(vbox3)
pushButton3_1.setObjectName("Load Image1")
pushButton3_1.setText("Load Image1")
pushButton3_1.clicked.connect(LoadImage1)
pushButton3_1.setStyleSheet(style_btn)
v_layout.addWidget(pushButton3_1)

pushButton3_2 = QtWidgets.QPushButton(vbox3)
pushButton3_2.setObjectName("Load Image2")
pushButton3_2.setText("Load Image2")
pushButton3_2.clicked.connect(LoadImage2)
pushButton3_2.setStyleSheet(style_btn)
v_layout.addWidget(pushButton3_2)

pushButton3_3 = QtWidgets.QPushButton(vbox3)
pushButton3_3.setObjectName("4.1 Keypoints")
pushButton3_3.setText("4.1 Keypoints")
pushButton3_3.clicked.connect(Keypoints)
pushButton3_3.setStyleSheet(style_btn)
v_layout.addWidget(pushButton3_3)

pushButton3_4 = QtWidgets.QPushButton(vbox3)
pushButton3_4.setObjectName("4.2 Matched Keypoints")
pushButton3_4.setText("4.2 Matched Keypointss")
pushButton3_4.clicked.connect(MatchedKeyPoints)
pushButton3_4.setStyleSheet(style_btn)
v_layout.addWidget(pushButton3_4)


# Augmented Reality
vbox4 = QtWidgets.QWidget(MainWindow)
vbox4.setGeometry(460, 20, 180, 240)
vbox4.setStyleSheet(style_box)
text4 = QtWidgets.QLabel(vbox4)
text4.setText("SIFT")
text4.setAlignment(QtCore.Qt.AlignCenter)
vbox4.setStyleSheet(style_box)
v_layout = QtWidgets.QVBoxLayout(vbox4)

getstr = QtWidgets.QLineEdit(vbox4)
v_layout.addWidget(getstr)

pushButton4_1 = QtWidgets.QPushButton(vbox4)
pushButton4_1.setObjectName("2.1 show words on board")
pushButton4_1.setText("2.1 show words on board")
pushButton4_1.setStyleSheet(style_btn)
pushButton4_1.clicked.connect(LineEditGetStr)
pushButton4_1.clicked.connect(ShowWordsOnBoard)
v_layout.addWidget(pushButton4_1)

pushButton4_2 = QtWidgets.QPushButton(vbox4)
pushButton4_2.setObjectName("2.2 show words vertical")
pushButton4_2.setText("2.2 show words vertical")
pushButton4_2.clicked.connect(LineEditGetStr)
pushButton4_2.clicked.connect(ShowWordsVertically)
pushButton4_2.setStyleSheet(style_btn)
v_layout.addWidget(pushButton4_2)

# VGG19
vbox5 = QtWidgets.QWidget(MainWindow)
vbox5.setGeometry(460, 400, 180, 300)
vbox5.setStyleSheet(style_box)
text5 = QtWidgets.QLabel(vbox5)
text5.setText("VGG19")
text5.setAlignment(QtCore.Qt.AlignCenter)
vbox5.setStyleSheet(style_box)
v_layout = QtWidgets.QVBoxLayout(vbox5)
pushButton5_1 = QtWidgets.QPushButton(vbox5)
pushButton5_1.setObjectName("Load Image")
pushButton5_1.setText("Load Image")
pushButton5_1.clicked.connect(LoadImage5)
pushButton5_1.setStyleSheet(style_btn)
v_layout.addWidget(pushButton5_1)

pushButton5_2 = QtWidgets.QPushButton(vbox5)
pushButton5_2.setObjectName("5.1 Show Augmented \n Images")
pushButton5_2.setText("5.1 Show Augmented \n Images")
pushButton5_2.clicked.connect(ShowAugmentedImages)
pushButton5_2.setStyleSheet(style_btn)
v_layout.addWidget(pushButton5_2)

pushButton5_3 = QtWidgets.QPushButton(vbox5)
pushButton5_3.setObjectName("5.2 Show Model Structure")
pushButton5_3.setText("5.2 Show Model Structure")
pushButton5_3.clicked.connect(ShowModelStructure)
pushButton5_3.setStyleSheet(style_btn)
v_layout.addWidget(pushButton5_3)

pushButton5_4 = QtWidgets.QPushButton(vbox5)
pushButton5_4.setObjectName("5.3 Show Acc and Loss")
pushButton5_4.setText("5.3 Show Acc and Loss")
pushButton5_4.clicked.connect(ShowAccAndLoss)
pushButton5_4.setStyleSheet(style_btn)
v_layout.addWidget(pushButton5_4)

pushButton5_5 = QtWidgets.QPushButton(vbox5)
pushButton5_5.setObjectName("5.4 Inferences")
pushButton5_5.setText("5.4 Inference")
pushButton5_5.setStyleSheet(style_btn)
v_layout.addWidget(pushButton5_5)
# Lack Image

# Stereo disparity map
vbox6 = QtWidgets.QWidget(MainWindow)
vbox6.setGeometry(680, 20, 180, 240)
vbox6.setStyleSheet(style_box)
v_layout = QtWidgets.QVBoxLayout(vbox6)
text6 = QtWidgets.QLabel(vbox6)
text6.setText("3. Stereo \n disparity map")
text6.setAlignment(QtCore.Qt.AlignCenter)
vbox6.setStyleSheet(style_box)
pushButton6_5 = QtWidgets.QPushButton(vbox6)
pushButton6_5.setObjectName("3.1 stereo disparity map")
pushButton6_5.setText("3.1 stereo disparity map")
pushButton6_5.clicked.connect(StereoDisparityMap)
pushButton6_5.setStyleSheet(style_btn)
v_layout.addWidget(pushButton6_5)

if __name__ == '__main__':
    MainWindow.show()
    sys.exit(app.exec_())


