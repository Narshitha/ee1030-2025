import ctypes

# Load the shared library compiled from main.c
lib = ctypes.CDLL("./libtriangle.so")

# Define the function signature
lib.compute_A.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Prepare output variables
Ax = ctypes.c_double()
Ay = ctypes.c_double()

# Call the C function
lib.compute_A(ctypes.byref(Ax), ctypes.byref(Ay))

print(f"Coordinates of A from C: ({Ax.value:.4f}, {Ay.value:.4f})")
