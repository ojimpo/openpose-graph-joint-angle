import json
import glob
from natsort import natsorted
import re
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

angle_results = []

def joint_angle(point1, point2, point3):
        point1_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point1)]
        point1_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point1)]

        point2_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point2)]
        point2_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point2)]

        point3_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point3)]
        point3_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point3)]

        u = np.array([point1_x - point2_x, point1_y - point2_y])
        v = np.array([point3_x - point2_x, point3_y - point2_y])

        i = np.inner(u, v)
        n = LA.norm(u) * LA.norm(v)

        if n == 0:
                a = 0
        else:
                c = i / n
                a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

def point_x(number):
        return number * 3 + 1

def point_y(number):
        return number * 3 + 2

l_knee_joint_angle = []

for json_file in natsorted(glob.glob('*_keypoints.json')):
    with open(json_file) as f:
        json_object = json.load(f)
        json_object_length = len(json_object['people'])

        if json_object_length == 0:
                a = 0
        else:
                l_hip_x = json_object['people'][0]['pose_keypoints_2d'][36]
                l_hip_y = json_object['people'][0]['pose_keypoints_2d'][37]

                l_knee_x = json_object['people'][0]['pose_keypoints_2d'][39]
                l_knee_y = json_object['people'][0]['pose_keypoints_2d'][40]

                l_ankle_x = json_object['people'][0]['pose_keypoints_2d'][42]
                l_ankle_y = json_object['people'][0]['pose_keypoints_2d'][43]

                u = np.array([l_hip_x - l_knee_x, l_hip_y - l_knee_y])
                v = np.array([l_ankle_x - l_knee_x, l_ankle_y - l_knee_y])

                i = np.inner(u, v)
                n = LA.norm(u) * LA.norm(v)

                if n == 0:
                        a = 0
                else:
                        c = i / n
                        a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

        l_knee_joint_angle.append(a)

print(l_knee_joint_angle)

# plt.title('Angle of Left Knee Joint')
# plt.xlabel('frame')
# plt.ylabel('degrees')
# plt.plot(l_knee_joint_angle)
# plt.grid()
# plt.show()