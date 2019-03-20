import json
import numpy as np
import matplotlib.pyplot as plt

for json_file in ['kazuma_{:012}_keypoints.json'.format(i) for i in range(38)]:
    l_knee_joint_angle = []
    with open(json_file) as f:
        json_object = json.load(json_file)

        l_hip_x = json_object['people'][0]['pose_keypoints_2d'][36]
        l_hip_y = json_object['people'][0]['pose_keypoints_2d'][37]

        l_knee_x = json_object['people'][0]['pose_keypoints_2d'][39]
        l_knee_y = json_object['people'][0]['pose_keypoints_2d'][40]

        l_ankle_x = json_object['people'][0]['pose_keypoints_2d'][42]
        l_ankle_y = json_object['people'][0]['pose_keypoints_2d'][43]

json_file = open('sample.json', 'r')
json_object = json.load(json_file)

l_hip_x = json_object['people'][0]['pose_keypoints_2d'][36]
l_hip_y = json_object['people'][0]['pose_keypoints_2d'][37]

l_knee_x = json_object['people'][0]['pose_keypoints_2d'][39]
l_knee_y = json_object['people'][0]['pose_keypoints_2d'][40]

l_ankle_x = json_object['people'][0]['pose_keypoints_2d'][42]
l_ankle_y = json_object['people'][0]['pose_keypoints_2d'][43]

print(str(l_hip_x))
print(str(l_knee_x))
print(str(l_ankle_x))