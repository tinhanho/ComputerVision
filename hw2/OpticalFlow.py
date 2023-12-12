import cv2
import globals
import numpy as np
def Preprocessing():
    firstframe = globals.video[0]
    gryimg = cv2.cvtColor(firstframe, cv2.COLOR_BGR2GRAY)
    corners = cv2.goodFeaturesToTrack(gryimg, 1, 0.3, 7, blockSize=7)
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.drawMarker(firstframe, (x, y), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)
    firstframe = cv2.resize(firstframe,(960, 540))
    cv2.imshow('name', firstframe)

def VideoTracking():
    firstframe = globals.video[0]
    gryimg = cv2.cvtColor(firstframe, cv2.COLOR_BGR2GRAY)
    feature_par = dict(maxCorners = 1,qualityLevel = 0.3, minDistance = 7, blockSize = 7)
    lk_par = dict( winSize  = (15, 15),maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    p0 = cv2.goodFeaturesToTrack(gryimg, mask=None, **feature_par)
    color = np.full((100, 3), (0, 100, 255), dtype=np.uint8)
    mask = np.zeros_like(firstframe)
    for i in range(1, len(globals.video)):
        frame = globals.video[i]
        gryframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        p1, st, err = cv2.calcOpticalFlowPyrLK(gryimg, gryframe, p0, None, **lk_par)

        if p1 is not None:
            good_new = p1[st == 1]
            good_old = p0[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()

            mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2)
            frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
            img = cv2.add(frame, mask)
            gryimg = gryframe.copy()
            p0 = good_new.reshape(-1, 1, 2)

            img = cv2.resize(img, (960, 540))
            cv2.imshow('NiHao', img)
            cv2.waitKey(10)
