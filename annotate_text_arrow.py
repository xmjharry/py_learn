import numpy.random
import matplotlib.pyplot as plt

fig = plt.figure(1, figsize=(5, 5))
fig.clf()

ax = fig.add_subplot(111)
ax.set_aspect(1)

x1 = -1 + numpy.random.randn(100)
y1 = -1 + numpy.random.randn(100)
x2 = 1. + numpy.random.randn(100)
y2 = 1. + numpy.random.randn(100)

ax.scatter(x1, y1, color="r")
ax.scatter(x2, y2, color="g")

bbox_props = dict(boxstyle="round,pad=0.9,rounding_size=0.8", fc="w", ec="y", alpha=1)
t = ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("round", pad=0.6, rounding_size=0.4)

ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)

bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=-45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

plt.draw()
plt.show()
