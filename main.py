
import cv2
import mediapipe as eye
import pyautogui
cam= cv2.VideoCapture(0)
face_mesh= eye.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screem_h=pyautogui.size()
while True:
    _, frame = cam.read()
    frame= cv2.flip(frame,1)
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output= face_mesh.process(rgb_frame)
    landmark_points= output.multi_face_landmarks
    frame_height,frame_width, _ = frame.shape
    #print(landmark_points)
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            #print(len(landmarks))
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)

            cv2.circle(frame,(x,y),3,(0,255,0))
            if id==1:
                screen_x= 2*screen_w/frame_width * x
                screen_y= 2*screem_h/frame_height *y
                pyautogui.moveTo(screen_x,screen_y)

        left = [landmarks[145],landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        print(left[0].y-left[1].y)
        if (left[0].y-left[1].y) < 0.0079:
            print("click")
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow("Eye of Horus",frame)
    cv2.waitKey(1)