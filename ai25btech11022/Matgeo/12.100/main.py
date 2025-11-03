import ctypes
import numpy as np

# Load the shared library
lib = ctypes.CDLL("./markov.so")

# Define function return type and argument
lib.stationary_distribution.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.stationary_distribution.restype = None

# Create space for result (array of 3 doubles)
pi = (ctypes.c_double * 3)()

# Call the C function
lib.stationary_distribution(pi)

# Convert to NumPy array for easy handling
pi_array = np.array([pi[0], pi[1], pi[2]])

print("Stationary distribution from C:", pi_array)

