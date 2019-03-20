import numpy as np
from numpy import linalg as LA

u = np.array([3, 4])
v = np.array([-4, 3])

i = np.inner(u, v)
n = LA.norm(u) * LA.norm(v)

c = i / n
a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

print(a)

# 90.0