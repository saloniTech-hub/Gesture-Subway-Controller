import cv2
import mediapipe as mp
import pydirectinput
import time

# ------------------------------------
# MediaPipe Setup
# ------------------------------------

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

previous_gesture = ""
last_action_time = 0

COOLDOWN = 0.8


# ------------------------------------
# Function to Press Key
# ------------------------------------

def press_key(key):
    pydirectinput.keyDown(key)
    time.sleep(0.05)
    pydirectinput.keyUp(key)


# ------------------------------------
# Main Loop
# ------------------------------------

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    gesture = "NO HAND"

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        lm = hand.landmark

        fingers = []

        # Thumb
        if lm[4].x < lm[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

        # Index
        if lm[8].y < lm[6].y:
            fingers.append(1)
        else:
            fingers.append(0)

        # Middle
        if lm[12].y < lm[10].y:
            fingers.append(1)
        else:
            fingers.append(0)

        # Ring
        if lm[16].y < lm[14].y:
            fingers.append(1)
        else:
            fingers.append(0)

        # Pinky
        if lm[20].y < lm[18].y:
            fingers.append(1)
        else:
            fingers.append(0)

        # -------------------------------
        # Gesture Recognition
        # -------------------------------

        if fingers == [0,0,0,0,0]:
            gesture = "ROLL"

        elif fingers == [0,1,0,0,0]:
            gesture = "LEFT"

        elif fingers == [0,1,1,0,0]:
            gesture = "RIGHT"

        elif fingers == [1,1,1,1,1]:
            gesture = "JUMP"

        else:
            gesture = "UNKNOWN"

        # -------------------------------
        # Send Key Only When Gesture Changes
        # -------------------------------

        current_time = time.time()

        if gesture != previous_gesture and current_time-last_action_time > COOLDOWN:

            if gesture == "LEFT":
                press_key("left")

            elif gesture == "RIGHT":
                press_key("right")

            elif gesture == "JUMP":
                press_key("up")

            elif gesture == "ROLL":
                press_key("down")

            if gesture != "UNKNOWN":
                print("Gesture :", gesture)

            previous_gesture = gesture
            last_action_time = current_time

        cv2.putText(
            frame,
            f"Fingers : {sum(fingers)}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255,255,0),
            2
        )

    cv2.putText(
        frame,
        f"Gesture : {gesture}",
        (20,90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.imshow("Gesture Subway Controller", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()