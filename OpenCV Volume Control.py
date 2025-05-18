import cv2
import pyautogui
import mediapipe as mp
# used python 3.11.8 version and install all this modules
# using 3.8 version matplot blib and numpy  and also jupyter is not working and working for mediapipe,cv2
# using 3.12.2 the tensorflow is not working and working cv2,mediapipe and jupyter is also working


cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=3,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils


while True:
    ret, frame = cap.read()
    if not ret:
        break

    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
            indexdip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
            middledip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
            ringdip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
            pinkydip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y
            thumbdip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
            print("thumbdip : ", thumbdip, "indexdip : ", indexdip, "middledip : ",
                  middledip, "ringdip : ", ringdip, "pinkydip : ", pinkydip)
            if abs(indexdip-thumbdip) < 0.1 and abs(indexdip-middledip) < 0.1 and abs(indexdip-ringdip) < 0.1 and abs(ringdip-middledip) < 0.1 and abs(pinkydip-middledip) < 0.1 and abs(pinkydip-ringdip) < 0.1:
                print("A")

            if abs(index_finger_y - thumb_y) <= abs(0.2):
                hand_gesture = 'pointing down'
            elif abs(index_finger_y - thumb_y) > abs(0.2):
                hand_gesture = 'pointing up'
            else:
                hand_gesture = 'other'

            if hand_gesture == 'pointing up':
                pyautogui.press('volumeup')
            elif hand_gesture == 'pointing down':
                pyautogui.press('volumedown')

    cv2.imshow('Hand Gesture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
