#include <stdio.h>
#include <math.h>

#define EPS 1e-9
#define ld double

int main() {
    ld A[3][2] = {
        {2.0, 1.0},
        {2.0, -1.0},
        {1.0, -2.0}
    };
    ld b[3] = {3.0, 1.0, -1.0};
    ld det, x1, x2;
    int commonsol;

    det = A[0][0] * A[1][1] - A[0][1] * A[1][0];
    if (fabs(det) < EPS) {
        printf("첫 번째와 두 번째 방정식만으로는\n유일한 해를 구할 수 없습니다.\n");
        return 1;
    }
    // 크래머
    x1 = (b[0] * A[1][1] - A[0][1] * b[1]) / det;
    x2 = (b[1] * A[0][0] - A[1][0] * b[0]) / det;

    printf("계산된 해\n");
    printf("x1 = %.6f\n", x1);
    printf("x2 = %.6f\n\n", x2);

    for (int i = 0; i < 3; i++) {
        ld leftside = A[i][0] * x1 + A[i][1] * x2;
        ld err = leftside - b[i];

        printf("%d번 방정식: 좌변 = %.6f, 우변 = %.6f\n", i + 1, leftside, b[i]);

        if (fabs(err) > EPS) {
            commonsol = 0;
        }
    }

    if (commonsol) {
        printf("\n세 방정식의 공통해가 존재합니다. \n");
        printf("공통해: (x1, x2) = (%.0f, %.0f)\n", x1, x2);
    } else {
        printf("\n세 방정식을 모두 만족하는 공통해가 없습니다,\n");
    }
    return 0;
}
