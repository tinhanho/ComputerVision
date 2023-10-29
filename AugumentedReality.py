import cv2
import globals
import numpy as np

def ShowWordsOnBoard():
    fs = cv2.FileStorage('/Users/hotin/Desktop/Dataset_CvDl_Hw1/Q2_Image/Q2_lib/alphabet_lib_onboard.txt', cv2.FILE_STORAGE_READ)
    ch = fs.getNode('K').mat()
    print(ch)

'''
    objectPoints = []
    imagePoints = []
    obj = np.zeros((11 * 8, 3), np.float32)
    obj[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
    for img in globals.images:
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
        if ret:
            objectPoints.append(obj)
            imagePoints.append(corners)
            #            cv2.drawChessboardCorners(img, (11, 8), corners, ret)
            ret, mat, dis, rot, trans = cv2.calibrateCamera(objectPoints, imagePoints, grayimg.shape[::-1], None, None)
'''