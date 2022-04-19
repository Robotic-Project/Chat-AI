import cv2
import mediapipe as mp
import time
from tkinter import *
from FaceDetectionModule import FaceDetector

def main():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    fname = "./source/unknown.png"
    pTime = 0
    detector = FaceDetector()

    while True:
        success, img = cap.read()
        #bmoBg = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        bmoBg = cv2.imread(fname, cv2.IMREAD_COLOR)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 이미지 색을 흑백으로 변경(계산 속도 향상을 위해)
        img = cv2.flip(img, 1) # 1은 좌우 반전, 0은 상하 반전입니다.
        img, bboxs = detector.findFaces(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.imshow('Image', img)

        cv2.namedWindow("BMO", cv2.WINDOW_NORMAL);
        cv2.setWindowProperty('BMO', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        if len(bboxs) != 0:
            bbox = bboxs[0][1]
            cv2.imshow('BMO', bmoBg)
            cv2.moveWindow('BMO', bbox[0], bbox[1])
        else: 
            cv2.imshow('BMO', bmoBg)
        cv2.resizeWindow('BMO', 1080, 136)

        cv2.waitKey(1)

if __name__ == '__main__':
    main()