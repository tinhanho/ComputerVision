import os
import cv2
import globals
from PyQt5.QtWidgets import QFileDialog
def LoadFolder():
#    folder = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q1_Image"

#    for filename in os.listdir(r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q1_Image"):
#        img = cv2.imread(os.path.join(folder, filename))
#        if img is not None:
#            globals.images.append(img)
    file_names, filetype = QFileDialog.getOpenFileNames(directory='/Users/hotin/Desktop/Dataset_CvDl_Hw1')
    if file_names:
        for file_name in file_names:
            img = cv2.imread(file_name)
            if img is not None:
                globals.images.append(img)
    print("read success")

def LoadImageL():
    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q3_Image\imL.png"
    img = cv2.imread(path)
    globals.images.append(img)
    print("read imL success")
def LoadImageR():
    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q3_Image\imR.png"
    img = cv2.imread(path)
    globals.images.append(img)
    print("read imR success")

def LoadImage1():
    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q4_Image\Left.jpg"
    img = cv2.imread(path)
    globals.images.append(img)
    print("read Load Image 1 success")

def LoadImage2():
    path = r"C:\Users\hotin\Desktop\Dataset_CvDl_Hw1\Q4_Image\Right.jpg"
    img = cv2.imread(path)
    globals.images.append(img)
    print("read Load Image 2 success")