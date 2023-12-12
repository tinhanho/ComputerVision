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