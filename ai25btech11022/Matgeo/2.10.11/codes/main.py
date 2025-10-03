import ctypes
import numpy as np

# Load shared library
lib = ctypes.CDLL("./libmain.so")   # <-- use main.dll on Windows

# Define argument/return types
lib.plane_normal.argtypes = [ctypes.POINTER(ctypes.c_double),
                             ctypes.POINTER(ctypes.c_double),
                             ctypes.POINTER(ctypes.c_double)]

lib.vector_in_plane_perp.argtypes = [ctypes.POINTER(ctypes.c_double),
                                     ctypes.POINTER(ctypes.c_double),
                                     ctypes.POINTER(ctypes.c_double),
                                     ctypes.POINTER(ctypes.c_double)]

# Helper to convert numpy array -> ctypes
def to_c_array(vec):
    return (ctypes.c_double * 3)(*vec)

# Input vectors
u = np.array([1, 1, 2], dtype=np.float64)
v = np.array([1, 2, 1], dtype=np.float64)
w = np.array([1, 1, 1], dtype=np.float64)

# Buffers for results
normal = (ctypes.c_double * 3)()
result = (ctypes.c_double * 3)()

# Step 1: Find plane normal
lib.plane_normal(to_c_array(u), to_c_array(v), normal)
normal_vec = np.array([normal[i] for i in range(3)])
print("Plane normal:", normal_vec)

# Step 2: Find vector in plane perpendicular to w
lib.vector_in_plane_perp(to_c_array(u), to_c_array(v), to_c_array(w), result)
final_vec = np.array([result[i] for i in range(3)])
print("Final unit vector:", final_vec)
print("Magnitude check:", np.linalg.norm(final_vec))

