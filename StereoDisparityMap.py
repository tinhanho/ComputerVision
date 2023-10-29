import cv2
import globals
import numpy as np

def StereoDisparityMap():
#    def show_xy(event, x, y, flags, userdata):
#        print(event,x, y, flags)
    def draw_match(event, x, y, flags, userdata):
        if event == cv2.EVENT_LBUTTONDOWN:
            point = int(disparity[y][x])
            img = cv2.circle(imgR, (x-point, y), 3, (0, 255, 0), 10)
            cv2.imshow('img', img)

    stereo = cv2.StereoBM.create(numDisparities=256, blockSize=25)
    grayimgL = cv2.cvtColor(globals.images[0], cv2.COLOR_BGR2GRAY)
    grayimgR = cv2.cvtColor(globals.images[1], cv2.COLOR_BGR2GRAY)
    imgL = globals.images[0]
    imgR = globals.images[1]
    disparity = stereo.compute(grayimgL, grayimgR)
    disparity = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
#    disparity = cv2.resize(disparity, (960, 540))
    cv2.imshow('disparity', disparity)
    cv2.imshow('imgL', imgL)
    cv2.setMouseCallback('imgL', draw_match)
