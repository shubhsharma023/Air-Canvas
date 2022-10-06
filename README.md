# Air-Canvas

## 1.	Introduction

### 1.1	Purpose
The purpose of this project is to build a canvas (Air Canvas) which uses your hand gestures to draw in the air. The project will use a camera to detect the fingertip and then we can draw the shape on the canvas.
1.2 PROJECT SCOPE
The purpose of the Air Canvas is to ease and create a convenient and easy-to-use application for teachers, students or artists. The project is based on a OpenCV which is a library of python. We will have a. Above all, we hope to provide a comfortable user experience.

### 1.2	REQUIREMENTS
The requirement to run this project is to use any compiler which can run python. You also need a system which contains webcam or any camera.

## 2.	DESCRIPTION

### 2.1 OVERALL DESCRIPTION
The project contains two files namely “airdraw.py” and “Hands.py” in which “airdraw.py” is the main file which inherits the “Hands.py” file to run the main program. “airdraw.py” contains all the command lines/rules on what to do in certain condition and how to process data and receives all the input from the user/camera and uses Hands.py to calculate and give the output to the screen.

“Hands.py” and “airdraw.py” calls all the important libraries which are required to implement the project such as:
- CV2 – This project is based on OpenCV so this library is must as it is used to invoke the camera and implement other important decision by the system.
- Math – to do basic calculation such as “sqrt” etc.
### 2.2 DESCRIBING “Hands.py”
After importing all the useful libraries in “Hands.py” we make a class named HandDetector which find hands using mediapipe library. Exports the landmarks in pixel format. Adds extra functionalities like finding how many fingers are up or the distance between two fingers. Also provides bounding box info of the hand found.
Then we define __init__ which will:
:param mode: In static mode, detection is done on each image: slower
:param maxHands: Maximum number of hands to detect
:param detectionCon: Minimum Detection Confidence Threshold
:param minTrackCon: Minimum Tracking Confidence Threshold

We will define findHands which will:
Finds hands in a BGR image.
:param img: Image to find the hands in.
:param draw: Flag to draw the output on the image.
:return: Image with or without drawings.

We will define findPosition which will:
Finds landmarks of a single hand and puts them in a list
in pixel format. Also finds the bounding box around the hand.
:param img: main image to find hand in
:param handNo: hand id if more than one hand detected
:param draw: Flag to draw the output on the image.
:return: list of landmarks in pixel format; bounding box.

We will define fingersUp which will:
Finds how many fingers are open and returns in a list.
Considers left and right hands separately
:return: List of which fingers are up.

We will define findDistance which will:
Find the distance between two landmarks based on their
index numbers.
:param p1: Point1 - Index of Landmark 1.
:param p2: Point2 - Index of Landmark 2.
:param img: Image to draw on.
:param draw: Flag to draw the output on the image.
:return: Distance between the points
Image with output drawn
Line information

After that we will define handType which will:
Checks if the hand is left or right
:return: "Right" or "Left".

**So basically we can say that the “Hands.py” can be defined as an asset to “AirDraw.py” which uses it to process the data.**


### 2.3 DESCRIBING “AirDraw.py”
Now we will describe the “AirDraw.py” which captures the data using camera and processes it with the help of “Hands.py” file. “DrawFromList” takes a list and draws the coordinates loaded into that.”lmlist” has the locations for all the points on the hand(21 in number).lmlist convert the input into the binary array and tells whether a finger is up or not. Finger 1 has been chosen for the input from the data has to be read. Finger 1 is the index finger of our hand. Finger 0 defined by the system as thumb and when it is found only then the input is taken.

## 3.	WORKING OF AIR CANVAS

-	Run “AirDraw.py” with any compiler supporting python.
-	The camera starts giving you output as a new window open of cv2
-	Put the hand you want to recognise up so that the camera recognises your hand and generate the 21 points on new window.
-	Start drawing on the window by moving your fingers in the air (in front of camera) by using your thumb (as the key to start to draw) and the index finger your   marker.
-	Use “a” letter key (small case) on your keyboard to clear the screen.
-	Use “q+ esc” (small case) to close the window and terminate the program.









