#!/usr/bin/env python3

import cv2
from operator import xor
import cv2
import numpy 

def callback(value):
    pass

def setup_trackbars(range_filter):
    cv2.namedWindow("Trackbars", 0)
    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)

def get_trackbar_values(range_filter):
    values = []
    for i in ["MIN", "MAX"]:
        for j in range_filter:
            v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
            values.append(v)
    return values

def main():
   
    image = cv2.imread('/home/asha/ball.png')
    range_filter = "HSV"
    setup_trackbars(range_filter)
    frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    while True:
        v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)
        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))
        print(v1_min, v2_min, v3_min, v1_max, v2_max, v3_max)
        preview = cv2.bitwise_and(image, image, mask=thresh)
        cv2.imshow("Preview", preview)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()