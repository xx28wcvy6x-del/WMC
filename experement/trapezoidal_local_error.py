#!/usr/bin/env python3
import numpy as np
# function to return exact result at x=4 for some dx
def exact(dx): 
    return 0.5*(dx + np.sin(4) - np.sin(4+dx))

# trapezoidal approximation at x=4 for some dx
def trapezoid(dx):
    return 0.5*dx*(np.sin(2)**2 + np.sin(2+0.5*dx)**2)

# calculate the local error for various dx
local_error= []
for dx in [0.001, 0.01, 0.1, 0.2, 0.5, 1]:
    local_error.append([dx, np.abs(trapezoid(dx) - exact(dx))])

print("dx\tlocal_error")
for dx, error in local_error:
    print(f"{dx}\t{error}")