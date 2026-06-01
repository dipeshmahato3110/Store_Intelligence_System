from send_dwell_event import (
    send_dwell_event
)
from send_dwell_event import send_dwell_event
from analytics import visitor_dwell
from conversion import (
    add_visitor,
    add_checkout,
    print_metrics
)
from journey import update_journey
from datetime import datetime
from dwell import zone_entry_time
from send_zone_event import send_zone_event
from zones import ZONES
from zones import get_zone
from send_event import send_entry_event
from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture("data/videos/CAM 2.mp4")

if not cap.isOpened():
    print("Cannot open video")
    exit()

# Entry line position
ENTRY_LINE_X = 800

# Store previous x positions of tracked persons
zone_history = {}
visitor_zones = {}
previous_positions = {}


while True:

    ret, frame = cap.read()

    if not ret:
        print("Video Finished")
        break

    print("Frame Shape:", frame.shape)

    # Run tracking
    results = model.track(
        frame,
        persist=True,
        classes=[0],  # person class only
        verbose=False
    )

    annotated_frame = results[0].plot()

    for zone_name, (x1, y1, x2, y2) in ZONES.items():

        cv2.rectangle(
            annotated_frame,
            (x1, y1),
            (x2, y2),
            (255, 255, 0),
            2
        )


    # Draw ENTRY line
    cv2.line(
        annotated_frame,
        (ENTRY_LINE_X, 0),
        (ENTRY_LINE_X, annotated_frame.shape[0]),
        (0, 255, 0),
        3
    )

    # Process tracked persons
    if results[0].boxes.id is not None:

        ids = results[0].boxes.id.cpu().numpy().astype(int)
        boxes = results[0].boxes.xyxy.cpu().numpy()

        for track_id, box in zip(ids, boxes):

            x1, y1, x2, y2 = box

           # Person center point
            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            print(
                f"Visitor {track_id} Center: "
                f"({center_x}, {center_y})"
            )

            cv2.putText(
                annotated_frame,
                f"({center_x},{center_y})",
                (center_x + 10, center_y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

            # Detect current zone
            zone = get_zone(center_x, center_y)

            update_journey(track_id, zone)

            previous_zone = zone_history.get(track_id)

            #Zone Event Block
            current_time = datetime.now()

            previous_zone = zone_history.get(track_id)

            if zone is not None and zone != previous_zone:

                if previous_zone is not None:

                    start_time = zone_entry_time.get(track_id)

                    if start_time:

                        dwell_seconds = (
                            current_time - start_time
                        ).total_seconds()

                        print(
                            f"DWELL -> Visitor {track_id} spent "
                            f"{dwell_seconds:.1f}s in {previous_zone}"
                        )

                        send_dwell_event(
                            track_id,
                            previous_zone,
                            dwell_seconds
                        )

                        send_dwell_event(
                            track_id,
                            previous_zone,
                            dwell_seconds
                        )

                        dwell_seconds = (
                            current_time - start_time
                        ).total_seconds()

                zone_entry_time[track_id] = current_time

                print(
                    f"ZONE EVENT -> Visitor {track_id} entered {zone}"
                )

                send_zone_event(track_id, zone)

                if zone == "CASH_COUNTER":

                    print(
                        f"CHECKOUT EVENT -> Visitor {track_id}"
                    )

                    add_checkout(track_id)

                    print_metrics()

                zone_history[track_id] = zone

            cv2.putText(
                annotated_frame,
                f"{zone}",
                (center_x, center_y - 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 255),
                2
            )
##
            print(
                f"Visitor {track_id} -> Zone: {zone}"
            )
##
            # Draw center point
            cv2.circle(
                annotated_frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Check if we have previous position
            if track_id in previous_positions:

                prev_x = previous_positions[track_id]

                # Crossing from left → right
                if prev_x < ENTRY_LINE_X and center_x >= ENTRY_LINE_X:

                    print(
                        f"ENTRY EVENT -> Visitor {track_id}"
                    )

                    add_visitor(track_id)

                    send_entry_event(track_id)

            # Update latest position
            previous_positions[track_id] = center_x

        print("Tracking IDs:", ids)

    # Show video
    cv2.imshow(
        "Store Intelligence - Tracking",
        annotated_frame
    )

    # ESC key to stop
    if cv2.waitKey(30) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()