import cv2
import globals
import numpy as np

def FindCorners():
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    for img in globals.images:
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
        if ret:
            cv2.cornerSubPix(grayimg, corners, (5, 5), (-1, -1), criteria)
            cv2.drawChessboardCorners(img, (11, 8), corners, ret)
            img = cv2.resize(img, (800, 800))
            cv2.imshow('img', img)
            cv2.waitKey(0)


def FindIntrinsic():
    objectPoints = []
    imagePoints = []
    obj = np.zeros((11*8, 3), np.float32)
    obj[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
    for img in globals.images:
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
        if ret:
            objectPoints.append(obj)
            imagePoints.append(corners)
#            cv2.drawChessboardCorners(img, (11, 8), corners, ret)
            ret, mat, dis, rot, trans = cv2.calibrateCamera(objectPoints, imagePoints, grayimg.shape[::-1], None, None)
            print("Intrinsic:")
            print(mat, "\n")

def FindExtrinsic():
    num = int(globals.getint)
    objectPoints = []
    imagePoints = []
    obj = np.zeros((11*8, 3), np.float32)
    obj[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
    img = globals.images[num-1]
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
    if ret:
        objectPoints.append(obj)
        imagePoints.append(corners)
#        cv2.drawChessboardCorners(img, (11, 8), corners, ret)
        ret, mat, dis, rot, trans = cv2.calibrateCamera(objectPoints, imagePoints, grayimg.shape[::-1], None, None)
        R = cv2.Rodrigues(rot[0])
        ext = np.hstack((R[0], trans[0]))
        print("Extrinsic:")
        print(ext, "\n")

def FindDistortion():
    num = int(globals.getint)
    objectPoints = []
    imagePoints = []
    obj = np.zeros((11 * 8, 3), np.float32)
    obj[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
    img = globals.images[num - 1]
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
    for img in globals.images:
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(grayimg, (11, 8), None)
        if ret:
            objectPoints.append(obj)
            imagePoints.append(corners)
            #        cv2.drawChessboardCorners(img, (11, 8), corners, ret)
            ret, mat, dis, rot, trans = cv2.calibrateCamera(objectPoints, imagePoints, grayimg.shape[::-1], None, None)
            print("Distortion:")
            print(dis, "\n")

def ShowUndistorted():
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
            ret, mat, dis, rot, trans = cv2.calibrateCamera(objectPoints, imagePoints, grayimg.shape[::-1], None, None)
            h, w = img.shape[:2]
            newcameratx, roi = cv2.getOptimalNewCameraMatrix(mat, dis, (w, h), 1, (w, h))
            dst = cv2.undistort(img, mat, dis, None, newcameratx)
            x, y, w, h = roi
            dst = dst[y:y+h, x:x+w]
            dst = cv2.resize(dst, (800, 800))
            cv2.imshow('dst', dst)
            cv2.waitKey(0)