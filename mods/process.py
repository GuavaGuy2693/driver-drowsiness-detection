from typing import Tuple, Union
import cv2
import math


def crop(frame, dim):
    return frame[dim[0][0] : dim[0][1], dim[1][0] : dim[1][1]]


def no_color(frame, size):
    return cv2.resize(
        cv2.cvtColor(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2RGB),
        (size, size),
    )

def process_frame(frame, dim, size):
    return no_color(crop(frame, dim), size)


def draw_frame(frame, text, dim):
    frame = cv2.rectangle(
        frame, (dim[1][0], dim[0][0]), (dim[1][1], dim[0][1]), (36, 255, 12), 1
    )
    cv2.putText(
        frame,
        text,
        (dim[1][0], dim[0][1] + 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (36, 255, 12),
        1,
    )

def normalized_pixel(
    normalized_x: float, normalized_y: float, image_width: int, image_height: int
) -> Union[None, Tuple[int, int]]:
    def is_valid_normalized_value(value: float) -> bool:
        return (value > 0 or math.isclose(0, value)) and (
            value < 1 or math.isclose(1, value)
        )

    if not (
        is_valid_normalized_value(normalized_x)
        and is_valid_normalized_value(normalized_y)
    ):
        return None
    x_px = min(math.floor(normalized_x * image_width), image_width - 1)
    y_px = min(math.floor(normalized_y * image_height), image_height - 1)
    return x_px, y_px


def timeToFrame(time, ft):
    return int(time*1000*ft)