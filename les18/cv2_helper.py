import cv2

cam = cv2.VideoCapture(0)


def cvtColor_helper_hls(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)


def cvtColor_helper_hsv(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

def cvtColor_helper_rgb(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def cvtColor_helper_gray(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
