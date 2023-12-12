import os
import cv2
import globals
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
def LoadFolder():
#    folder = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q2_Image"

#    for file_names in os.listdir(r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q2_Image"):
#            img = cv2.imread(os.path.join(folder, file_names))
#            if img is not None:
#                globals.images.append(img)

    file_names, filetype = QFileDialog.getOpenFileNames()
#    file_names, filetype = QFileDialog.getOpenFileNames(directory='/Users/hotin/Desktop/Dataset_CvDl_Hw1')
    if file_names:
        for file_name in file_names:
            img = cv2.imread(file_name)
            if img is not None:
                globals.images.append(img)
    print("LoadFolder success")

def LoadImageL():
#    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q3_Image\imL.png"
    file_names, filetype = QFileDialog.getOpenFileNames()
    img = cv2.imread(file_names[0])
    globals.images.append(img)
    print("LoadImageL success")
def LoadImageR():
#    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q3_Image\imR.png"
    file_names, filetype = QFileDialog.getOpenFileNames()
    img = cv2.imread(file_names[0])
    globals.images.append(img)
    print("LoadImageR success")

def LoadImage1():
#    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q4_Image\Left.jpg"
    file_names, filetype = QFileDialog.getOpenFileNames()
    img = cv2.imread(file_names[0])
    globals.images.append(img)
    print("LoadImage1 success")

def LoadImage2():
#    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q4_Image\Right.jpg"
    file_names, filetype = QFileDialog.getOpenFileNames()
    img = cv2.imread(file_names[0])
    globals.images.append(img)
    print("LoadImage2 success")

def LoadImage5():
    file_names, filetype = QFileDialog.getOpenFileNames()
    if file_names:
        for file_name in file_names:
            img = Image.open(file_name)
            if img is not None:
                globals.images.append(img)
    print("LoadImage5 success")
