# Face-Detection Using OpenCV

This project is a simple real-time face detection system using OpenCV and a pre-trained Haar Cascade classifier. The script captures video from a webcam, detects faces in real time, and highlights them with a bounding box.

Requirements:-
Python 3.x
OpenCV (cv2)

Installation:-
Install OpenCV 
Download the haarcascade_frontalface_default.xml file from OpenCV's GitHub repository source:
data/haarcascades/haarcascade_frontalface_default.xml
Save the file in an accessible location and update the script path accordingly.

Customization:-
To use a video file instead of a webcam, uncomment the line and write-
cap = cv2.VideoCapture('filename.mp4')
and replace 'filename.mp4' with your video file path.
