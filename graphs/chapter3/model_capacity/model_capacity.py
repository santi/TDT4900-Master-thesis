import numpy as np
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# y = -x^2  + 5

points = np.array(
    [
        (-3, -(-3) ** 2 + 5),
        (-2, -(-2) ** 2 + 5),
        (0, -(-0) ** 2 + 5),
        (1, -(-1) ** 2 + 5),
        (3, -(-3) ** 2 + 5),
        (3.5, -(-3.5) ** 2 + 5),
    ]
)

t = np.linspace(-5, 5, 1000)
linear = t - 5
poly2 = -(t ** 2) + 5
poly10 = np.poly1d(np.polyfit(points[:, 0], points[:, 1], 8))
poly10 = poly10(t)


fig, axs = plt.subplots(nrows=1, ncols=3, sharex=True, sharey=True)

ax = axs[0]


ax.plot(t, linear)
ax.scatter(points[:, 0], points[:, 1], color="black")
ax.set_yticks([])
ax.set_xlabel("Underfit")


ax = axs[1]
ax.plot(t, poly2)
ax.scatter(points[:, 0], points[:, 1], color="black")
ax.set_xlabel("Good capacity")


ax = axs[2]
ax.plot(t, poly10)
ax.scatter(points[:, 0], points[:, 1], color="black")
ax.set_xlabel("Overfit")


fig = plt.gcf()
fig.set_size_inches(7, 4)

plt.savefig(os.path.join(dir_path, "model_capacity.eps"), format="eps")
plt.show()
