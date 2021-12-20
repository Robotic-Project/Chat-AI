import cv2
import mediapipe as mp
import time
from tkinter import *
from LocationCon import setLocation
from FaceDetectionModule import FaceDetector

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    pTime = 0
    detector = FaceDetector()

    while True:
        success, img = cap.read()
        amg = cv2.imread("BMO.jpg", cv2.IMREAD_COLOR)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 이미지 색을 흑백으로 변경(계산 속도 향상을 위해)
        img, bboxs, location = detector.findFaces(img, amg)
        print(location)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.imshow('Image', amg)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()