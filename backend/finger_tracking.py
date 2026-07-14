import cv2
import mediapipe as mp

print("Starting Finger Tracking...")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

mp_draw = mp.solutions.drawing_utils

while True:
    success, frame = cap.read()

    if not success:
        print("Failed to read frame")
        break

    # Flip image for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process hand
    results = hands.process(rgb_frame)

    # If hand detected
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw hand landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Index finger tip = landmark 8
            index_tip = hand_landmarks.landmark[8]

            h, w, c = frame.shape

            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            # Green circle on index finger
            cv2.circle(frame, (x, y), 15, (0, 255, 0), -1)

            # Display coordinates
            cv2.putText(
                frame,
                f"X:{x} Y:{y}",
                (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    cv2.imshow("Finger Tracking", frame)

    key = cv2.waitKey(1)

    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()