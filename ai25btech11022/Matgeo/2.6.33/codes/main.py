import ctypes

# Load the shared library
lib = ctypes.CDLL("./libmain.so")   # use "main.dll" on Windows

# Declare the argument and return types
lib.triangle_area.argtypes = [ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double,
                              ctypes.c_double, ctypes.c_double]
lib.triangle_area.restype = ctypes.c_double

# Example points
points = [
    (1,0, 6,0, 4,3),
    (2,7, 1,1, 10,8),
    (-2,-3, 3,2, -1,8)
]

for p in points:
    area = lib.triangle_area(*p)
    print(f"Area of triangle with vertices {p} = {area}")

