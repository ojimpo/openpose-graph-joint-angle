import numpy as np
from numpy import linalg as LA

l_hip_x = 90.656
l_hip_y = 273.001

l_knee_x = 134.778
l_knee_y = 337.153

l_ankle_x = 198.88
l_ankle_y = 387.174

u = np.array([3, 4])
v = np.array([-4, 3])

i = np.inner(u, v)
n = LA.norm(u) * LA.norm(v)

c = i / n
a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

print(a)

# 90.0