import cv2
import mediapipe as mp
import time

class FaceDetector():
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
                    img = self.fancyDraw(img, bbox)

                    #cv2.rectangle(img, bbox, (0, 255, 0), 2)  # 경계 상자만 출력
                    cv2.putText(img, f'FPS: {int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)  # 신뢰도 출력

        return img, bboxs  # 이미지 반환

    def fancyDraw(self, img, bbox, l = 30, t=5, rt = 1):  # 모서리에 강조주는 경계 박스
        x, y, w, h = bbox
        x1, y1 = x+w, y+h

        cv2.rectangle(img, bbox, (0, 255, 0), rt)  # 경계 상자만 출력
        # Top Left
        cv2.line(img, (x, y), (x+l, y), (0, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (0, 0, 255), t)
        # Top Right
        cv2.line(img, (x1, y), (x1 - l, y), (0, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y + l), (0, 0, 255), t)
        # Bottom Left
        cv2.line(img, (x, y1), (x + l, y1), (0, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (0, 0, 255), t)
        # Bottom Right
        cv2.line(img, (x1, y1), (x1 - l, y1), (0, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (0, 0, 255), t)

        return img


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = FaceDetector()

    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        cv2.imshow('Image', img)
        cv2.waitKey(1)



if __name__ == '__main__':
    main()