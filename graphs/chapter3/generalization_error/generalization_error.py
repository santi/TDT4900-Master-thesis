import numpy as np
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

t = np.linspace(1, 20, 1000)
train_loss = np.exp(-t) * 100 - 0.2 * t + 30
val_loss = np.exp(-t) * 120 + np.exp(-0.6 * t) * 5 + 0.4 * t + 31

val_min = np.argmin(val_loss)


plt.plot(t, train_loss, label="Training loss")
plt.plot(t, val_loss, label="Validation loss")
plt.axvline(t[val_min], color="black", linestyle="--")

plt.ylabel("Loss")
plt.xlabel("Number of iterations over training dataset")
plt.legend()

plt.xticks([])
plt.yticks([])

annotation_index = 700

# Add arrow
plt.annotate(
    "",
    (t[annotation_index], train_loss[annotation_index]),  # from
    (t[annotation_index], val_loss[annotation_index]),  # to
    arrowprops=dict(facecolor="black", arrowstyle="<|-|>"),
)

# Add text
plt.annotate(
    "Generalization gap",
    (
        t[annotation_index],
        (train_loss[annotation_index] + val_loss[annotation_index]) / 2,
    ),  # from
    (
        t[annotation_index] + 0.2,
        (train_loss[annotation_index] + val_loss[annotation_index]) / 2 - 0.8,
    ),  # to
    # arrowprops=dict(facecolor="black", arrowstyle="-"),
)

fig = plt.gcf()
fig.set_size_inches(7, 4)

plt.savefig(os.path.join(dir_path, "generalization_error.eps"), format="eps")
plt.show()
