# Detects landmarks on a face using the Google MediaPipe 

import cv2 
import mediapipe as mp 
from base import Base 

class FaceMesh(Base): 
    def __init__(self, staticMode = False, maxFaces = 1, minDetectConf = .5, minTrackConf = .5, dotSize = 1): 
        super().__init__()
        self.staticMode = staticMode 
        self.maxFaces = maxFaces
        self.minDetectConf = minDetectConf 
        self.minTrackConf = minTrackConf 

        self.mpDraw = mp.solutions.drawing_utils 
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.minDetectConf, self.minTrackConf)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=dotSize, circle_radius=dotSize)

    # Detects 468 landmarks on each of the faces within img 
    def findFacesMesh(self, img, shouldDraw = True): 
        imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRgb)
        faces = []
        if results.multi_face_landmarks: 
            for faceLms in results.multi_face_landmarks: 
                if shouldDraw: 
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACE_CONNECTIONS, self.drawSpec, self.drawSpec)
                face = []
                for lm in faceLms.landmark: 
                    ih, iw, _ = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih) 
                    face.append([x, y])
                faces.append(face) 
        return faces 

def main(): 
    cap = cv2.VideoCapture(0)
    detector = FaceMesh()

    while True: 
        _, img = cap.read()

        faces = detector.findFacesMesh(img)
        print (faces) 

        detector.fps(img)
        cv2.imshow(("Face mesh"), img)
        detector.tryDestruct(cap)

if __name__ == "__main__":
    main() 