from mods.container import get_feature
from mods.process import process_frame, draw_frame
from mods.evaluate import update
from mods.features import find_features
from mods.model import predict_mouth, predict_eye

from mediapipe.python.solutions import face_detection

from mods.config import model, basic

import cv2

ft = 1000/basic["fps"]
reduceFrame = basic["reduceTime"]*1000//ft
print(reduceFrame)
track = 0

face_class = ["no_yawn", "yawn"]
eye_class = ["open", "closed"]
roi = get_feature(ft)

feed = cv2.VideoCapture(0)
feed.set(cv2.CAP_PROP_FPS, basic["fps"])

mp_face_detection = face_detection

with mp_face_detection.FaceDetection(
    min_detection_confidence=0.5, model_selection=0
) as face_detection:
    while True:

        ret, frame = feed.read()
        if not ret:
            break

        track += 1       

## Run inference
        results = face_detection.process(frame)
        mouthbox, eyebox = find_features(frame, results)

        if type(mouthbox) != type(None):
            roi.mouth = process_frame(frame, mouthbox, model["mouth"]["resolution"])
            roi.eye = process_frame(frame, eyebox, model["eye"]["resolution"])

            roi.update_mouth(predict_mouth(roi.mouth))
            roi.update_eye(predict_eye(roi.eye))
           
            draw_frame(frame, face_class[roi.mouth_state[-1]], mouthbox)
            draw_frame(frame, eye_class[roi.eye_state[-1]], eyebox)

## Evaluate results
        if not roi.warn:
            update(roi.eye_state, model["eye"]["faultTimeRatio"], model["eye"]["warn"])
            update(roi.mouth_state, model["mouth"]["faultTimeRatio"], model["mouth"]["warn"])

## Reduce warning level over time
            if (track > reduceFrame):
                if roi.eye_count:
                    roi.eye_count -= 1
                if roi.mouth_count:
                    roi.mouth_count -= 1

        if (roi.eye_count + roi.mouth_count > basic["maxWarn"]):
            roi.warn = True

## Warning alert
        if roi.warn:
            cv2.putText(
                frame,
                "!!XX!! DANGER !!XX!!",
                (20, 200),
                cv2.FONT_HERSHEY_DUPLEX,
                1.5,
                (120, 120, 220),
                2,
            )

## Key Inputs
        key = cv2.waitKey(1)
        if key & 0xFF == ord("q"):                  # Quit -> Q
            break
        if roi.warn and (key & 0xFF == ord(" ")):   # Reset warning state -> <Space>
            roi.reset()

        print((roi.eye_count, roi.mouth_count), roi.warn)

## Draw Frame
        cv2.imshow("feed", frame)

feed.release()
cv2.destroyAllWindows()
