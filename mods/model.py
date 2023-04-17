import tensorflow as tf
import numpy as np

from mods.config import model

print("Mouth model")
int_face = tf.lite.Interpreter(model["mouth"]["path"])
int_face.allocate_tensors()
print(int_face.get_signature_list())
face_judge = int_face.get_signature_runner("serving_default")

print("Eye model")
int_eye = tf.lite.Interpreter(model["eye"]["path"])
int_eye.allocate_tensors()
print(int_eye.get_signature_list())
eye_judge = int_eye.get_signature_runner("serving_default")


def predict_mouth(frame):
    tensor = tf.convert_to_tensor(frame/255, dtype=tf.float32)
    pframe = tf.expand_dims(tensor, 0)
    predict = face_judge(conv2d_1_input=pframe)
    return np.argmax(predict["dense_3"])


def predict_eye(frame):
    tensor = tf.convert_to_tensor(frame/255, dtype=tf.float32)
    pframe = tf.expand_dims(tensor, 0)
    predict = eye_judge(conv2d_input=pframe)
    return np.argmax(predict["dense_1"])
