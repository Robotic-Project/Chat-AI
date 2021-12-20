import cv2
import mediapipe as mp
from LocationCon import setLocation

class FaceDetector():
    tx = ty = 0

    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection  # 미디어 파이프 얼굴 감지 모듈
        self.mpDraw = mp.solutions.drawing_utils  # 미디어 파이프 특징 그리는 모듈
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)  # 얼굴 감지 객체

    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 이미지를 rgb로 변환
        self.results = self.faceDetection.process(imgRGB)   # 얼굴 감지 프로세스 결과
        bboxs = []  # 반환할 정보
        if self.results.detections:   # 점감지
            for id, detection in enumerate(self.results.detections):
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])

                if draw:
                    img, location = self.fancyDraw(img, bbox)

                    #cv2.rectangle(img, bbox, (0, 255, 0), 2)  # 경계 상자만 출력
                    cv2.putText(img, f'acc: {int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)  # 신뢰도 출력

        return img, bboxs, location  # 이미지 반환

    def fancyDraw(self, img, bbox, l = 30, t=5, rt = 1):  # 모서리에 강조주는 경계 박스
        x, y, w, h = bbox
        x1, y1 = int(w/2), int(h/4)

        cv2.rectangle(img, bbox, (0, 255, 0), rt)  # 경계 상자만 출력
        cv2.line(img, (x+x1, y+y1), (x+x1+1, y+y1+1), (0, 0, 255), 5)   # 비모의 추적점

        if abs(FaceDetector.tx-x)> 10 or abs(FaceDetector.ty-y) > 10:
            FaceDetector.tx = x
            FaceDetector.ty = y
            setLocation(x, y)

        return img, ((x+x1, y+y1), (x+x1+1, y+y1+1))