import ctypes

# Load the shared library
lib = ctypes.CDLL("./libcollinear.so")

# Define argument and return types
lib.check_collinear.argtypes = [ctypes.c_int, ctypes.c_int]
lib.check_collinear.restype = ctypes.c_int

# Example points
points = [(3, 6), (-3, 4), (0, 5), (2, 1)]

for x, y in points:
    result = lib.check_collinear(x, y)
    if result == 1:
        print(f"Point ({x}, {y}) lies on the line x - 3y + 15 = 0 (collinear).")
    else:
        print(f"Point ({x}, {y}) does NOT lie on the line.")

