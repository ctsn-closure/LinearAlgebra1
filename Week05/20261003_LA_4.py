from fractions import Fraction as F

def print_augmented(title, matrix):
    print("\n{}".format(title))

    for row in matrix:
        left = " ".join("{:>4}".format(str(x)) for x in row[:2])
        right = " ".join("{:>4}".format(str(x)) for x in row[2:])
        print("[ {} | {} ]".format(left, right))

augmented = [
    [F(3), F(4), F(1), F(0)],
    [F(2), F(3), F(0), F(1)]
]

print_augmented("초기 첨가행렬 [A | I]", augmented)

augmented[0] = [
    value / 3 for value in augmented[0]
]

print_augmented("1단계: (1/3)R1 → R1", augmented)

augmented[1] = [
    augmented[1][j] - 2 * augmented[0][j]
    for j in range(4)
]

print_augmented("2단계: R2 - 2R1 → R2", augmented)

augmented[1] = [
    3 * value for value in augmented[1]
]

print_augmented("3단계: 3R2 → R2", augmented)

augmented[0] = [
    augmented[0][j] - F(4, 3) * augmented[1][j]
    for j in range(4)
]

print_augmented("4단계: R1 - (4/3)R2 → R1", augmented)

A_inverse = [
    row[2:] for row in augmented
]

print("\nA의 역행렬:")
for row in A_inverse:
    print([str(value) for value in row])
