from mediapipe.python.solutions import face_detection
from mods.process import normalized_pixel

def find_features(frame, results):

    y, x, _ = frame.shape

    if not results.detections:
        return (None, None)

    for detection in results.detections:
        fbox = detection.location_data.relative_bounding_box

        fstart = normalized_pixel(fbox.xmin, fbox.ymin, x, y)
        fend = normalized_pixel(fbox.xmin + fbox.width, fbox.ymin + fbox.height, x, y)

        if fstart == None:
            fstart = (0, 0)
        if fend == None:
            fend = (x, y)

        s = int((fend[0] - fstart[0]) // 10)
        e, m = (s*2, s*3)

        epos = detection.location_data.relative_keypoints[0]
        epos = normalized_pixel(epos.x, epos.y, x, y)
        roi_eye = [[epos[1] - e, epos[1] + e], [epos[0] - e, epos[0] + e]]

        mpos = detection.location_data.relative_keypoints[3]
        mpos = normalized_pixel(mpos.x, mpos.y, x, y)
        roi_mouth = [[mpos[1] - m, mpos[1] + m], [mpos[0] - m, mpos[0] + m]]
    return (roi_mouth, roi_eye)
