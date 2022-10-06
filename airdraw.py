from Hands import HandDetector
import cv2
import mediapipe as mp
import math


def DrawFromList(List, img, color, thickness):
    '''
    Takes a list and draws the coordinates loaded into that
    '''
    for i in range(0, len(List)-1):
        start_point = List[i]
        end_point = List[i+1]
        image = cv2.line(img, start_point, end_point, color, thickness)


cap = cv2.VideoCapture(0)
detector = HandDetector(mode=False, maxHands=1, detectionCon=1)


List = []
Curr = []
while True:
    # INITIALISE
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    # LMLIST HAS THE LOCATIONS FOR ALL THE POINTS ON THE HAND
    lmlist, bbox = detector.findPosition(img)

    if lmlist:  # ALL CODE SHOULD BE INSIDE THIS.... IT CHECKS IF A HAND HAS BEEN DETECTED
        # THIS BINARY ARRAY CONTAINS WHETHER A FINGER IS UP OR NOT
        fingers = detector.fingersUp()
        if fingers[0] and fingers[1]:
            Curr.append(lmlist[8])  # ADD THE CURRENT LOC OF INDEX FINGER
        else:
            List.append(Curr)
            Curr = []

    # ERASE THE BOARD IF PRESS A
    if cv2.waitKey(33) == ord('a'):
        List = []
        Curr = []

    # DRAWING THE BOARD

    for curr in List:
        DrawFromList(curr, img, (0, 0, 255), 7)
    DrawFromList(Curr, img, (0, 0, 255), 7)

    # DISPLAY THE PICTURE
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
