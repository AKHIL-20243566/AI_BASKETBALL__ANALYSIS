import cv2
import sys
import numpy as np
sys.path.append("../")
from utils import get_center_of_bbox,get_bbox_width

def draw_triangle(frame, bbox, color):
    if bbox is None or len(bbox) < 4:
        return frame
    bbox = list(map(int, bbox))
    y = bbox[1]
    x, _ = get_center_of_bbox(bbox)
    triangle_points = np.array([[x, y], [x - 10, y - 20], [x + 10, y - 20]], np.int32)
    cv2.drawContours(frame, [triangle_points], 0, color, cv2.FILLED)
    cv2.drawContours(frame, [triangle_points], 0, (0,0,0), 2)
    return frame

def draw_ellipse(frame, bbox, color, track_id=None):
    x1, y1, x2, y2 = map(int, bbox)
    x_center = int((x1 + x2) / 2)
    width = int(x2 - x1)
    y_ellipse_center = y2 + 5  # move slightly below feet

    cv2.ellipse(
        frame,
        center=(x_center, y_ellipse_center),
        axes=(int(width * 0.8), int(0.35 * width)),
        angle=0,
        startAngle=-45,
        endAngle=235,
        color=color,
        thickness=3,
        lineType=cv2.LINE_AA
    )

    if track_id is not None:
        rectangle_width = 38
        rectangle_height = 20
        x1_rect = x_center - rectangle_width // 2
        y1_rect = y2 + 8
        x2_rect = x_center + rectangle_width // 2
        y2_rect = y1_rect + rectangle_height
        cv2.rectangle(frame, (x1_rect, y1_rect), (x2_rect, y2_rect), color, cv2.FILLED)
        text = str(track_id)
        text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 2)[0]
        text_x = x_center - text_size[0] // 2
        text_y = y1_rect + rectangle_height // 2 + text_size[1] // 2 - 2
        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 0), 2)

    return frame
