import numpy as np
import matplotlib.pyplot as plt


def plot_frame(ax, T, length=50, name=None):
    origin = T[:3, 3]

    x_axis = origin + T[:3, 0] * length
    y_axis = origin + T[:3, 1] * length
    z_axis = origin + T[:3, 2] * length

    ax.plot(
        [origin[0], x_axis[0]],
        [origin[1], x_axis[1]],
        [origin[2], x_axis[2]],
        color="r",
    )

    ax.plot(
        [origin[0], y_axis[0]],
        [origin[1], y_axis[1]],
        [origin[2], y_axis[2]],
        color="g",
    )

    ax.plot(
        [origin[0], z_axis[0]],
        [origin[1], z_axis[1]],
        [origin[2], z_axis[2]],
        color="b",
    )

    if name is not None:
        ax.text(origin[0], origin[1], origin[2], name)


def plot_chain(T_list):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    points = []

    for i, T in enumerate(T_list):
        plot_frame(ax, T, name=f"F{i}")

        p = T[:3, 3]
        points.append(p)

    points = np.array(points)

    ax.plot(
        points[:, 0],
        points[:, 1],
        points[:, 2],
        color="black",
        marker="o",
    )

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title("MELFA Kinematic Chain")

    ax.set_box_aspect([1, 1, 1])

    plt.show()