import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

def Volts(x, y):
    return (9 * 10**13) \
            * (((1) / (x**2 + (19 - y)**2)**0.5) \
            + ((2) / (x**2 + y**2)**0.5) \
            + ((3) / (y**2 + (23.6 - x)**2)**0.5))

def Height(V):
    return V / (8.5 * 10**12)

x = np.arange(-5, 30, 0.25)
y = np.arange(-5, 25, 0.25)
x, y = np.meshgrid(x, y)

z = np.minimum(15, Height(Volts(x, y)))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# note that the graph is scaled to centimeters, not meters
# i've already adjusted the value of k to account for this, no need to worry

surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)
xLabel = ax.set_xlabel("x coord (cm)")
yLabel = ax.set_ylabel("y coord (cm)")
zLabel = ax.set_zlabel("height (cm)")

point = Volts(10, 5)
print("%.2E" % point)
print("%.02f" % Height(point) + " cm")

plt.show()
