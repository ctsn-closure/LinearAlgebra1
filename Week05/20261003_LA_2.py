import numpy as np

A = np.array([
    [1, 0, 2],
    [2, -1, 3],
    [4, 1, 8]
])

B = np.array([
    [-11, 2, 2],
    [-4, 0, 1],
    [6, -1, -1]
])

I = np.eye(3, dtype=int)

AB = A @ B
BA = B @ A

print("A =\n{}".format(A))

print("\nB =\n{}".format(B))

print("\nAB =\n{}".format(AB))

print("\nBA =\n{}".format(BA))

print("\nAB = I : {}\nBA = I : {}".format(
    np.array_equal(AB, I),
    np.array_equal(BA, I)
))

if np.array_equal(AB, I) and np.array_equal(BA, I):
    print("\nA와 B는 서로 역행렬입니다.")
    print("즉, B = A^-1이고 A = B^-1입니다.")
else:
    print("\nA와 B는 서로 역행렬이 아닙니다.")
