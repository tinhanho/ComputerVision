import cv2
import globals
import time
import threading
def Keypoints():
    sift = cv2.SIFT.create()
    grayimg = cv2.cvtColor(globals.images[0], cv2.COLOR_BGR2GRAY)
    keypoint, des = sift.detectAndCompute(grayimg, None)
    img = cv2.drawKeypoints(grayimg, keypoint, None, color=(0, 255, 0))
    img = cv2.resize(img, (800, 800))
    cv2.imshow('img', img)

def running():
    while flag == 0:
        if int(time.time()) % 2 == 0:
            print("running..")
        else:
            print("running...")
        time.sleep(1)
def MatchedKeyPoints():
    sift = cv2.SIFT.create()
    grayimg1 = cv2.cvtColor(globals.images[0], cv2.COLOR_BGR2GRAY)
    grayimg2 = cv2.cvtColor(globals.images[1], cv2.COLOR_BGR2GRAY)
    keypoint1, des1 = sift.detectAndCompute(grayimg1, None)
    keypoint2, des2 = sift.detectAndCompute(grayimg2, None)
    bf = cv2.BFMatcher()
    print("matches start")
    thread = threading.Thread(target=running)
    global flag
    flag = 0
    thread.start()
    matches = bf.knnMatch(des1, des2, k=2)
    flag = 1
    print("matches end")
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])

    img = cv2.drawMatchesKnn(grayimg1, keypoint1, grayimg2, keypoint2, good, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    img = cv2.resize(img, (1600, 800))
    cv2.imshow('img', img)