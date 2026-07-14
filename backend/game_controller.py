import cv2
import mediapipe as mp
import pydirectinput
import time

# -----------------------------
# Camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

# -----------------------------
# MediaPipe Hands
# -----------------------------
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

# -----------------------------
# Variables
# -----------------------------
prev_x = None
prev_y = None

THRESHOLD = 60
COOLDOWN = 0.8

last_action_time = 0

# -----------------------------
# Function to press keys
# -----------------------------
def press_key(key):

    pydirectinput.keyDown(key)
    time.sleep(0.05)
    pydirectinput.keyUp(key)

# -----------------------------
# Main Loop
# -----------------------------
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

            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

            current_time = time.time()

            if prev_x is not None:

                dx = x - prev_x
                dy = y - prev_y

                if current_time - last_action_time > COOLDOWN:

                    if dx > THRESHOLD:

                        print("➡ RIGHT")

                        press_key("right")

                        last_action_time = current_time

                    elif dx < -THRESHOLD:

                        print("⬅ LEFT")

                        press_key("left")

                        last_action_time = current_time

                    elif dy < -THRESHOLD:

                        print("⬆ JUMP")

                        press_key("up")

                        last_action_time = current_time

                    elif dy > THRESHOLD:

                        print("⬇ ROLL")

                        press_key("down")

                        last_action_time = current_time

            prev_x = x
            prev_y = y

    cv2.putText(
        frame,
        "ESC = Exit",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("Gesture Subway Controller", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()