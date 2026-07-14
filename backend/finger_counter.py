import cv2
import mediapipe as mp

# ---------------------------
# Initialize MediaPipe
# ---------------------------

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Finger tip landmarks
tip_ids = [4, 8, 12, 16, 20]

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    finger_count = 0
    gesture = "No Hand"

    if results.multi_hand_landmarks:

        hand_landmarks = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS
        )

        lm = hand_landmarks.landmark

        # ---------------------------
        # Thumb
        # ---------------------------
        if lm[tip_ids[0]].x < lm[tip_ids[0]-1].x:
            finger_count += 1

        # ---------------------------
        # Other four fingers
        # ---------------------------
        for id in range(1,5):

            if lm[tip_ids[id]].y < lm[tip_ids[id]-2].y:
                finger_count += 1

        # ---------------------------
        # Gesture Detection
        # ---------------------------

        if finger_count == 0:
            gesture = "ROLL"

        elif finger_count == 1:
            gesture = "LEFT"

        elif finger_count == 2:
            gesture = "RIGHT"

        elif finger_count == 5:
            gesture = "JUMP"

        else:
            gesture = "UNKNOWN"

    # ---------------------------
    # Display
    # ---------------------------

    cv2.rectangle(frame, (10,10), (320,130), (0,0,0), -1)

    cv2.putText(
        frame,
        f"Finger Count : {finger_count}",
        (20,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Gesture : {gesture}",
        (20,95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.imshow("Finger Counter", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()