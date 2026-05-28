import sys
import numpy as np

sys.path.append("src")

from melfa_kinematics.transforms import Rx, Ry, Rz, Trans


I = np.eye(4)


assert np.allclose(Rx(0), I)
assert np.allclose(Ry(0), I)
assert np.allclose(Rz(0), I)
assert np.allclose(Trans(0, 0, 0), I)


T = Trans(1, 2, 3)

assert T[0, 3] == 1
assert T[1, 3] == 2
assert T[2, 3] == 3