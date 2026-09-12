import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-2, 3, 500)

x2_eq1 = 3 - 2 * x1
x2_eq2 = 2 * x1 - 1
x2_eq3 = (x1 + 1) / 2

plt.figure(figsize = (8, 7))

plt.plot(x1, x2_eq1, color = "deeppink", linewidth = 2.5, label = r"$2x_1+x_2=3$")
plt.plot(x1, x2_eq2, color = "dodgerblue", linewidth = 2.5, label = r"$2x_1+x_2=1$")
plt.plot(x1, x2_eq3, color = "seagreen", linewidth = 2.5, label = r"$x_1-2x_2=-1$")

sol_x1 = 1
sol_x2 = 1

plt.scatter(sol_x1, sol_x2, color = "black", s = 70, zorder = 5)
plt.annotate(r"%(1,1)", xy = (sol_x1, sol_x2), xytext = (1.15, 1.2), fontsize = 14)

plt.plot([sol_x1, sol_x1], [0, sol_x2], color = "deeppink", linestyle = "--", linewidth = 1)
plt.plot([0, sol_x1], [sol_x2, sol_x2], color= "deeppink", linestyle = "--", linewidth = 1)

plt.axhline(0, color = "black", linewidth = 1)
plt.axvline(0, color = "black", linewidth = 1)

plt.xlim(-2, 3)
plt.ylim(-3, 5)
plt.xlabel(r"$x_1", fontsize = 14)
plt.ylabel(r"$x_2", fontsize = 14, rotation = 0, labelpad = 15)
plt.title("Three Linear Equations", fontsize = 16)
plt.grid(alpha = 0.25)
plt.legend(fontsize = 12)
plt.gca().set_aspect("equal", adjustable = "box")

plt.tight_layout()
plt.show()
