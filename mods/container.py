from mods.config import model

class Face:
    def __init__(self, ft):
        # Frames
        self.mouth = None
        self.eye = None

        # States
        self.mouth_state = [0]*int(model["mouth"]["time"]*1000/ft)
        self.eye_state = [0]*int(model["eye"]["time"]*1000/ft)
        self.blink_count = 0

        # Warns
        self.warn = False
        self.score = 0

    def update_eye(self, n):
        self.eye_state.pop(0)
        self.eye_state.append(n)

    def update_mouth(self, n):
        self.mouth_state.pop(0)
        self.mouth_state.append(n)

    def reset(self):
        self.warn = False
        self.blink_count = 0
        self.score = 0

def get_feature(ft):
    return Face(ft)
