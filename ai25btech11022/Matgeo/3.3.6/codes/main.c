#include <stdio.h>
#include <math.h>

// Function to compute coordinates of A
void compute_A(double *Ax, double *Ay) {
    double a = 6.0;  // side BC
    double angleB = M_PI/4.0;     // 45 degrees in radians
    double angleC = M_PI/6.0;     // 30 degrees in radians
    
    // c = side opposite to C (i.e., AB)
    double c = (6.0 * sqrt(2.0)) / (sqrt(3.0) + 1.0);
    
    // Coordinates of A
    *Ax = c * cos(angleB);
    *Ay = c * sin(angleB);
}

int main() {
    double Ax, Ay;
    compute_A(&Ax, &Ay);
    printf("Coordinates of A: (%.4f, %.4f)\n", Ax, Ay);
    return 0;
}
