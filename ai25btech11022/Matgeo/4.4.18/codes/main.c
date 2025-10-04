#include <stdio.h>

// Function to check if point (x, y) lies on line x - 3y + 15 = 0
int check_collinear(int x, int y) {
    if (x - 3*y + 15 == 0) {
        return 1;  // Collinear
    }
    return 0;  // Not collinear
}

int main() {
    // Test points
    int points[][2] = {
        {3, 6},   // B
        {-3, 4},  // C
        {0, 5},   // Example A
        {2, 1}    // Random
    };

    int n = sizeof(points) / sizeof(points[0]);

    for (int i = 0; i < n; i++) {
        int x = points[i][0];
        int y = points[i][1];
        if (check_collinear(x, y)) {
            printf("Point (%d, %d) lies on the line x - 3y + 15 = 0 (collinear)\n", x, y);
        } else {
            printf("Point (%d, %d) does NOT lie on the line\n", x, y);
        }
    }

    return 0;
}

