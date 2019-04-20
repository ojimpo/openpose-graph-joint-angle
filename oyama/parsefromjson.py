import json
import glob
from natsort import natsorted
import re
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

result = {}

def make_list(joint, point1, point2, point3):
        result[joint] = []

        def point_x(number):
                return number * 3

        def point_y(number):
                return (number * 3) + 1

        if json_object_length == 0:
                a = 0

        else:
                p1_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point1)]
                p1_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point1)]

                p2_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point2)]
                p2_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point2)]

                p3_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point3)]
                p3_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point3)]

                u = np.array([p1_x - p2_x, p1_y - p2_y])
                v = np.array([p3_x - p2_x, p3_y - p2_y])

                i = np.inner(u, v)
                n = LA.norm(u) * LA.norm(v)

                if n == 0:
                        a = 0
                else:
                        c = i / n
                        a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

        return ayyy
        

def joint_angle(point1, point2, point3):
        def point_x(number):
                return number * 3

        def point_y(number):
                return (number * 3) + 1

        if json_object_length == 0:
                a = 0

        else:
                p1_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point1)]
                p1_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point1)]

                p2_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point2)]
                p2_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point2)]

                p3_x = json_object['people'][0]['pose_keypoints_2d'][point_x(point3)]
                p3_y = json_object['people'][0]['pose_keypoints_2d'][point_y(point3)]

                u = np.array([p1_x - p2_x, p1_y - p2_y])
                v = np.array([p3_x - p2_x, p3_y - p2_y])

                i = np.inner(u, v)
                n = LA.norm(u) * LA.norm(v)

                if n == 0:
                        a = 0
                else:
                        c = i / n
                        a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

        return a

r_knee_joint_angle = []
l_knee_joint_angle = []

for json_file in natsorted(glob.glob('*_keypoints.json')):
    with open(json_file) as f:
        json_object = json.load(f)
        json_object_length = len(json_object['people'])

        r_knee_joint_angle.append(joint_angle(point1 = 9, point2 = 10, point3 = 11))
        l_knee_joint_angle.append(joint_angle(point1 = 12, point2 = 13, point3 = 14))

plt.title('Joint Angles')
plt.xlabel('frames')
plt.ylabel('degrees')
plt.plot(r_knee_joint_angle, label = 'R_Knee')
plt.plot(l_knee_joint_angle, label = 'L_Knee')
plt.grid()
plt.legend(loc = 'upper left')
plt.show()