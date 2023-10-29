import cv2
import globals
import numpy as np

def ShowWordsOnBoard():
    fs = cv2.FileStorage('/Users/hotin/Desktop/Dataset_CvDl_Hw1/Q2_Image/Q2_lib/alphabet_lib_onboard.txt', cv2.FILE_STORAGE_READ)
    getglobalstr = globals.getstr
    getstrlen = len(getglobalstr)
    counter = 0
    while counter != getstrlen:
        getstr = getglobalstr[counter]
        ch = fs.getNode(getstr).mat()
        ch = np.float32(ch)
        objectPoints = []
        imagePoints = []
        obj = np.zeros((11 * 8, 3), np.float32)
        obj[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
        i = 0
        for img in globals.images:
            grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
            if ret:
                objectPoints.append(obj)
                imagePoints.append(corners)
                ret, mat, dis, rot, trans = cv2.calibrateCamera(objectPoints, imagePoints, grayimg.shape[::-1], None, None)
                chsize = np.size(ch, 0)
                if counter <= 2:
                    for j in range(chsize):
                        ch[j][0] += [7, 5, 0]
                        ch[j][0] -= [3*counter, 0, 0]
                        ch[j][1] += [7, 5, 0]
                        ch[j][1] -= [3*counter, 0, 0]
                        imgpts, jac = cv2.projectPoints(ch[j], rot[i], trans[i], mat, dis)
                        imgpts_int = np.int32(imgpts)
                        img = cv2.line(img, imgpts_int[0][0], imgpts_int[1][0], (0, 0, 255), 5)
                else:
                    for j in range(chsize):
                        ch[j][0] += [7, 2, 0]
                        ch[j][0] -= [3*(counter-3), 0, 0]
                        ch[j][1] += [7, 2, 0]
                        ch[j][1] -= [3*(counter-3), 0, 0]
                        imgpts, jac = cv2.projectPoints(ch[j], rot[i], trans[i], mat, dis)
                        imgpts_int = np.int32(imgpts)
                        img = cv2.line(img, imgpts_int[0][0], imgpts_int[1][0], (0, 0, 255), 5)
                i += 1
        counter += 1

    img = cv2.resize(img, (800, 800))
    cv2.imshow('img', img)
    cv2.waitKey(0)  # each for one sec, not done

def ShowWordsVertically():
    fs = cv2.FileStorage('/Users/hotin/Desktop/Dataset_CvDl_Hw1/Q2_Image/Q2_lib/alphabet_lib_vertical.txt', cv2.FILE_STORAGE_READ)
    getglobalstr = globals.getstr
    getstrlen = len(getglobalstr)
    counter = 0
    while counter != getstrlen:
        getstr = getglobalstr[counter]
        ch = fs.getNode(getstr).mat()
        ch = np.float32(ch)
        objectPoints = []
        imagePoints = []
        obj = np.zeros((11 * 8, 3), np.float32)
        obj[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
        i = 0
        for img in globals.images:
            grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
            if ret:
                objectPoints.append(obj)
                imagePoints.append(corners)
                ret, mat, dis, rot, trans = cv2.calibrateCamera(objectPoints, imagePoints, grayimg.shape[::-1], None, None)
                chsize = np.size(ch, 0)
                if counter <= 2:
                    for j in range(chsize):
                        ch[j][0] += [7, 5, 0]
                        ch[j][0] -= [3*counter, 0, 0]
                        ch[j][1] += [7, 5, 0]
                        ch[j][1] -= [3*counter, 0, 0]
                        imgpts, jac = cv2.projectPoints(ch[j], rot[i], trans[i], mat, dis)
                        imgpts_int = np.int32(imgpts)
                        img = cv2.line(img, imgpts_int[0][0], imgpts_int[1][0], (0, 0, 255), 5)
                else:
                    for j in range(chsize):
                        ch[j][0] += [7, 2, 0]
                        ch[j][0] -= [3*(counter-3), 0, 0]
                        ch[j][1] += [7, 2, 0]
                        ch[j][1] -= [3*(counter-3), 0, 0]
                        imgpts, jac = cv2.projectPoints(ch[j], rot[i], trans[i], mat, dis)
                        imgpts_int = np.int32(imgpts)
                        img = cv2.line(img, imgpts_int[0][0], imgpts_int[1][0], (0, 0, 255), 5)
                i += 1
        counter += 1

    img = cv2.resize(img, (800, 800))
    cv2.imshow('img', img)
    cv2.waitKey(0)  # each for one sec, not done