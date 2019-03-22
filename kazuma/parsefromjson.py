import json
import glob
import re
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

l_knee_joint_angle = []
# angle_results = []

# def joint_angle(a, b, c):
#         def point_x(number):
#                 return number * 3 + 1

#         def point_y(number):
#                 return number * 3 + 2

#         point_a_x = json_object['people'][0]['pose_keypoints_2d'][point_x(a)]
#         point_a_y = json_object['people'][0]['pose_keypoints_2d'][point_y(a)]

#         point_b_x = json_object['people'][0]['pose_keypoints_2d'][point_x(b)]
#         point_b_y = json_object['people'][0]['pose_keypoints_2d'][point_y(b)]

#         point_c_x = json_object['people'][0]['pose_keypoints_2d'][point_x(c)]
#         point_c_y = json_object['people'][0]['pose_keypoints_2d'][point_y(c)]

#         u = np.array([point_a_x - point_b_x, point_a_y - point_b_y])
#         v = np.array([point_c_x - point_b_x, point_c_y - point_b_y])

#         i = np.inner(u, v)
#         n = LA.norm(u) * LA.norm(v)

#         if n == 0:
#                 a = 0
#         else:
#                 c = i / n
#                 a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

def point_x(number):
        return number * 3 + 1

def point_y(number):
        return number * 3 + 2

for json_file in glob.glob('*.json'):
    with open(json_file) as f:
        json_object = json.load(f)
        json_object_length = len(json_object['people'])

        if json_object_length == 0:
                a = 0
        else:
                l_hip_x = json_object['people'][0]['pose_keypoints_2d'][point_x(12)]
                l_hip_y = json_object['people'][0]['pose_keypoints_2d'][point_y(12)]

                l_knee_x = json_object['people'][0]['pose_keypoints_2d'][point_x(13)]
                l_knee_y = json_object['people'][0]['pose_keypoints_2d'][point_y(13)]

                l_ankle_x = json_object['people'][0]['pose_keypoints_2d'][point_x(14)]
                l_ankle_y = json_object['people'][0]['pose_keypoints_2d'][point_y(13)]

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

# x_num = point_x(12)
# y_num = point_y(12)

# print(x_num)
# print(y_num)