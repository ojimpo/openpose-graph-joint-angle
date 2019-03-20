import numpy as np
from numpy import linalg as LA

u = np.array([-44.122, -64.152])
v = np.array([64.102, 50.021])

i = np.inner(u, v)
n = LA.norm(u) * LA.norm(v)

c = i / n
a = np.rad2deg(np.arccos(np.clip(c, -1.0, 1.0)))

print(a)