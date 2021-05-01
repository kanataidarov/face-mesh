# Base class for OpenCV projects 

import cv2 
import time 

class Base(): 
    def __init__(self): 
        self.color = {'BLUE': [255,0,0], 
                 'GREEN': [0,255,0], 
                 'RED': [0,0,255]}
        self.pTime = 0
        
    def fps(self, img): 
        cTime = time.time() 
        fps = 1/(cTime-self.pTime)
        self.pTime = cTime 
        cv2.putText(img, f'{int(fps)}', (15,40), cv2.FONT_HERSHEY_PLAIN, 2, self.color['BLUE'], 2)

    def tryDestruct(self, cap): 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()

def main(): 
    cap = cv2.VideoCapture(0)
    base = Base()

    while True: 
        _, img = cap.read()
        base.fps(img)
        cv2.imshow(("Base frame"), img)
        base.tryDestruct(cap)
        

if __name__ == "__main__":
    main() 