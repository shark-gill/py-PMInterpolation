# import libraries
from scipy.interpolate import interpn
import numpy as np

# define a function to get the value
def v_function_3d(x, y, z):
    return 3 * x + 4 * y - z

# the np.linspace() function returns the interval between the given numbers.
x = np.linspace(0, 4, 5)
y = np.linspace(0, 5, 6)
z = np.linspace(0, 6, 7)

# in three dimensions, a point's coordinates are treated collectively as a single object.
points = (x, y, z)

# meshgrid, it changes NumPy arrays into coordinate matrices or grids of values
values = v_function_3d(*np.meshgrid(*points, indexing='ij'))

# coordinates to sample the gridded data are
point = np.array([2.21, 3.12, 1.15])

# evaluate the 3d interpolating function at a point
print(interpn(points, values, point))

# https://www.delftstack.com/howto/python/3d-interpolation-python/