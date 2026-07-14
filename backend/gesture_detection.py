import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils

prev_x = None
prev_y = None

THRESHOLD = 40

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            index_tip = hand_landmarks.landmark[8]

            h, w, _ = frame.shape

            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            cv2.circle(frame, (x, y), 15, (0, 255, 0), -1)

            if prev_x is not None:

                dx = x - prev_x
                dy = y - prev_y

                action = ""

                if dx > THRESHOLD:
                    action = "RIGHT"

                elif dx < -THRESHOLD:
                    action = "LEFT"

                elif dy < -THRESHOLD:
                    action = "JUMP"

                elif dy > THRESHOLD:
                    action = "ROLL"

                if action:
                    print(action)

                    cv2.putText(
                        frame,
                        action,
                        (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        2,
                        (0, 0, 255),
                        3
                    )

            prev_x = x
            prev_y = y

    cv2.imshow("Gesture Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()