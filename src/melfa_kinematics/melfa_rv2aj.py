import numpy as np

from melfa_kinematics.transforms import fk_chain


DH_PARAMS = [
    (0, np.pi / 2, 300, 0),
    (250, 0, 0, 0),
    (160, 0, 0, 0),
]


def forward_kinematics(q):
    dh_params = [
        (a, alpha, d, theta + q_i)
        for (a, alpha, d, theta), q_i
        in zip(DH_PARAMS, q)
    ]

    return fk_chain(dh_params)