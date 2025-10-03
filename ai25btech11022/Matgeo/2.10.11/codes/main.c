#include <stdio.h>
#include <math.h>

// Cross product
void cross_product(double a[3], double b[3], double result[3]) {
    result[0] = a[1]*b[2] - a[2]*b[1];
    result[1] = a[2]*b[0] - a[0]*b[2];
    result[2] = a[0]*b[1] - a[1]*b[0];
}

// Dot product
double dot_product(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Normalize vector to unit length
void normalize(double a[3]) {
    double norm = sqrt(dot_product(a, a));
    if (norm > 1e-9) {
        a[0] /= norm;
        a[1] /= norm;
        a[2] /= norm;
    }
}

// Function 1: Find normal to plane given two vectors u and v
void plane_normal(double u[3], double v[3], double normal[3]) {
    cross_product(u, v, normal);
    normalize(normal);
}

// Function 2: Find a unit vector in plane (spanned by u,v) and perpendicular to w
void vector_in_plane_perp(double u[3], double v[3], double w[3], double result[3]) {
    double n[3];
    plane_normal(u, v, n);  // normal to plane

    // Candidate vector = cross(n, w)  → this ensures perpendicular to w and lies in plane
    cross_product(n, w, result);
    normalize(result);
}

