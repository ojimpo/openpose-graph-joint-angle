import json
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

l_knee_joint_angle = []

def point_x(number):
        return number * 3 + 1

def point_y(number):
        return number * 3 + 2

for json_file in ['kazuma_{:012d}_keypoints.json'.format(i) for i in range(38)]:
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

plt.title('Angle of Left Knee Joint')
plt.xlabel('frame')
plt.ylabel('degrees')
plt.plot(l_knee_joint_angle)
plt.grid()
plt.show()