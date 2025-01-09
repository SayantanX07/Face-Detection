import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(r'C:\Users\SAYANTAN\Downloads\haarcascade_frontalface_default.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')
cv2.namedWindow('img', cv2.WND_PROP_FULLSCREEN)
# Set the window to full screen
cv2.setWindowProperty('img', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('FACE', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
        
# Release the VideoCapture object
cap.release()


#FULL SCREEN CODE---

# import cv2
# import win32api
# import win32con
# import win32gui

# face_cascade = cv2.CascadeClassifier(r'C:\Users\SAYANTAN\Downloads\haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# Create a named window
# cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# cv2.setWindowProperty('img', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# # Get screen resolution
# screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
# screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)

# # Get the window handle of the OpenCV window
# hwnd = win32gui.FindWindow(None, 'img')
# win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, screen_width, screen_height, win32con.SWP_SHOWWINDOW)

# while True:
#     # Read the frame
#     ret, img = cap.read()
#     if not ret:
#         break
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     cv2.imshow('img', img)
#     if cv2.waitKey(30) & 0xFF == 27:  # ESC key to exit
#         break
# cap.release()
# cv2.destroyAllWindows()
