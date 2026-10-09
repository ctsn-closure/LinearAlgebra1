import math

def determinant_2x2(matrix):
    return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])

angle_25 = math.radians(25)
angle_15 = math.radians(15)

A = [[math.cos(angle_25), -math.cos(angle_15)], [math.sin(angle_25), math.sin(angle_15)]]
b = [0, 30]

A1 = [
    [b[0], A[0][1]],
    [b[1], A[1][1]]
]

A2 = [
    [A[0][0], b[0]],
    [A[1][0], b[1]]
]

D = determinant_2x2(A)
D1 = determinant_2x2(A1)
D2 = determinant_2x2(A2)

print("계수행렬 A")
for row in A:
    print(row)
print("\nA1: 첫 번째 열을 b로 교체")
for row in A1:
    print(row)
print("\nA2: 두 번째 열을 b로 교체")
for row in A2:
    print(row)
print('\nD  = det(A)  = {:.6f}'.format(D))
print('D1 = det(A1) = {:.6f}'.format(D1))
print('D2 = det(A2) = {:.6f}'.format(D2))

if math.isclose(D, 0.0, abs_tol=1e-12):
    print("\ndet(A)가 0이므로 유일한 해가 없습니다.")
else:
    T1 = D1 / D
    T2 = D2 / D
    print("\n크래머의 규칙 계산")
    print('T1 = D1 / D = {:.6f} / {:.6f}'.format(D1, D))
    print('T1 = {:.4f}'.format(T1))
    print('\nT2 = D2 / D = {:.6f} / {:.6f}'.format(D2, D))
    print('T2 = {:.4f}'.format(T2))

    equation1 = (math.cos(angle_25) * T1 - math.cos(angle_15) * T2)
    equation2 = (math.sin(angle_25) * T1 + math.sin(angle_15) * T2)
    print("\n검산")
    print('수평 방향 합 = {:.6f}'.format(equation1))
    print('수직 방향 합 = {:.6f}'.format(equation2))
