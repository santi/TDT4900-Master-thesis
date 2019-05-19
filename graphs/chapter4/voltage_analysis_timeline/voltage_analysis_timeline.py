import numpy as np
import matplotlib.pyplot as plt
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
np.random.seed(42)

t = np.linspace(0, 30, 600)
t1 = t[:201]
t2 = t[200:351]
t3 = t[350:401]
t4 = t[400:]

prediction_timeline = np.sin(t1)
classification_timeline = np.sin(t2 * 1.75) * 0.75 + np.random.normal(0, 0.3, len(t2))
stability_timeline1 = np.sin(t3) + np.random.normal(0, 0.1, len(t3)) * np.linspace(
    1.0, 0.1, len(t3)
)
stability_timeline2 = np.sin(t4) + np.random.normal(0, 0.01, len(t4)) * np.linspace(
    1.0, 0.1, len(t4)
)


plt.ylim([-2, 2])
plt.xlim([0, 30])

plt.xticks([])
plt.yticks([])

plt.ylabel(r"Voltage ($V$)")
plt.xlabel(r"Time ($t$)")


plt.plot(t1, prediction_timeline, color="black")
plt.plot(t2, classification_timeline, color="black")
plt.plot(t3, stability_timeline1, color="black")
plt.plot(t4, stability_timeline2, color="black")


# Add annotations
arrow_height = 1.5
text_height = arrow_height + 0.1

plt.annotate(
    "",
    xy=(0, arrow_height),
    xytext=(10, arrow_height),
    xycoords="data",
    textcoords="data",
    arrowprops={"arrowstyle": "|-|"},
)
plt.annotate("Fault prediction", xy=(5, text_height), ha="center", va="center")


plt.annotate(
    "",
    xy=(10, arrow_height),
    xytext=(17.5, arrow_height),
    xycoords="data",
    textcoords="data",
    arrowprops={"arrowstyle": "|-|"},
)
plt.annotate("Fault classification", xy=(13.75, text_height), ha="center", va="center")


plt.annotate(
    "",
    xy=(17.5, arrow_height),
    xytext=(30, arrow_height),
    xycoords="data",
    textcoords="data",
    arrowprops={"arrowstyle": "|-|"},
)
plt.annotate("Fault prediction", xy=(23.75, text_height), ha="center", va="center")


# plt.ylabel("Y")
# plt.xlabel("X")
# plt.legend()

fig = plt.gcf()
fig.set_size_inches(10, 5)

plt.savefig(os.path.join(dir_path, "voltage_analysis_timeline.eps"), format="eps")
plt.show()
