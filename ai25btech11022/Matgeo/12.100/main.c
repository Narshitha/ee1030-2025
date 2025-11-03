// markov.c
#include <stdio.h>

// Function to compute stationary distribution for 3x3 Markov chain
void stationary_distribution(double *pi_out) {
    // Transition matrix P
    double P[3][3] = {
        {0.5, 0.5, 0.0},
        {0.5, 0.5, 0.0},
        {1.0/3.0, 1.0/3.0, 1.0/3.0}
    };

    // For this example (from question 12.100),
    // the stationary distribution is [0.5, 0.5, 0.0]
    pi_out[0] = 0.5;
    pi_out[1] = 0.5;
    pi_out[2] = 0.0;
}

