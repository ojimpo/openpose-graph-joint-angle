import json
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

l_knee_joint_angle = []

with open('kazuma_000000000034_keypoints.json') as f:
        json_object = json.load(f)
        print(json_object['people'][0]['pose_keypoints_2d'][36])
        l_hip_x = json_object["people"][0]["pose_keypoints_2d"][36]
        l_hip_y = json_object["people"][0]["pose_keypoints_2d"][37]

        l_knee_x = json_object["people"][0]["pose_keypoints_2d"][39]
        l_knee_y = json_object["people"][0]["pose_keypoints_2d"][40]

        l_ankle_x = json_object["people"][0]["pose_keypoints_2d"][42]
        l_ankle_y = json_object["people"][0]["pose_keypoints_2d"][43]

        u = np.array([l_hip_x - l_knee_x, l_hip_y - l_knee_y])
        v = np.array([l_ankle_x - l_knee_x, l_ankle_y - l_knee_y])

        i = np.inner(u, v)
        n = LA.norm(u) * LA.norm(v)

        c = i / n
        a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

        l_knee_joint_angle.append(a)


print(l_knee_joint_angle)
