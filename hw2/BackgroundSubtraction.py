import globals
import cv2
import numpy as np
def BackgroundSubtraction():
    subtractor = cv2.createBackgroundSubtractorKNN(history=500, detectShadows=True)
    videoframe = globals.video
    for i in range(0, len(videoframe)):
        frame = videoframe[i]
        blframe = cv2.GaussianBlur(videoframe[i], (5, 5), 0)
        mask = subtractor.apply(blframe)
        res_frame = cv2.bitwise_and(frame, frame, mask=mask)
#        cv2.imshow('RGB', frame)
#        cv2.imshow('M', mask)
#        cv2.imshow('R', res_frame)

        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) # This is important.
        img = np.hstack((frame, mask, res_frame))
        cv2.imshow('HelloWorlds', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break