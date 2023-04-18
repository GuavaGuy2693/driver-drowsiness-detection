def blinkEval(roi, maxCount, track, ft):
    if (roi.blink_count >= maxCount):
        roi.blink_count = 0
        roi.score +=20
    else:
        if (track > 0):
            track -= 1
        elif (roi.eye_state[-1] == 1):
            track = 1000//ft # skip 1s worth of frames to give time for a blink to end
            roi.blink_count += 1

def basicEval(arr, model, feature, window, score):
    if infer(arr[-window:], model[feature]['faultRatio']):
        score += model[feature]['weight']

def infer(arr, factor):
    return True if (arr.count(1)/len(arr) >= factor) else False