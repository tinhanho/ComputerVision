import globals
from PyQt5.QtWidgets import QFileDialog
import cv2
def LoadVideo():
    file_name, filetype = QFileDialog.getOpenFileName(directory='/Users/hotin/Desktop/Dataset_CvDl_Hw2')
    cap = cv2.VideoCapture(file_name)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            globals.video.append(frame)
        else:
            break

def LoadImage():
    file_name, filetype = QFileDialog.getOpenFileName(directory='/Users/hotin/Desktop/Dataset_CvDl_Hw2')
    img = cv2.imread(file_name)
    globals.images.append(img)
    print("Read Success")

def LoadImages5():
    file_names, filetype = QFileDialog.getOpenFileNames(directory='/Users/hotin/Desktop/Dataset_CvDl_Hw2')
    if file_names:
        for file_name in file_names:
            img = cv2.imread(file_name)
            if img is not None:
                globals.images.append(img)
    print("LoadFolder success")
