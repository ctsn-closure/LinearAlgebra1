import numpy as np

A = np.array([
    [1, 2],
    [1, 3]
], dtype=float)

B = np.array([
    [3, 2],
    [2, 2]
], dtype=float)

A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

AB = A @ B

left = np.linalg.inv(AB)

right = B_inv @ A_inv

np.set_printoptions(precision=3, suppress=True)

print("A^-1 =\n{}".format(A_inv))

print("\nB^-1 =\n{}".format(B_inv))

print("\nAB =\n{}".format(AB))

print("\n(AB)^-1 =\n{}".format(left))

print("\nB^-1 A^-1 =\n{}".format(right))

print("\n(AB)^-1 = B^-1 A^-1 인가?\n{}".format(
    np.allclose(left, right)
))
