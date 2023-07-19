import math

def print_sin_values(u, h):
    x = 0.0
    i = 1
    while x <= u:
        x_radians = math.radians(x)
        sin_value = math.sin( x_radians)
        print(f" {i}\t {x}\t {sin_value:.4f}")
        x += h
        i += 1

# Get input from the user
u = float(input("Enter the value of u (in degrees): "))
h = float(input("Enter the value of h (in degrees): "))
print("\n")
print(" S.N\t x \t sinx  \n")
# Call the function to print sin(x) values
print_sin_values(u, h)

import numpy as np
import matplotlib.pyplot as plt

# Get user input for u and h
# u = float(input("Enter the value of u in degrees: "))
# h = float(input("Enter the value of h in degrees: "))

# Convert degrees to radians
u_rad = np.deg2rad(u)
h_rad = np.deg2rad(h)

# Generate x values from 0 to u at interval of h
x = np.arange(0, u_rad + h_rad, h_rad)

# Calculate corresponding y values using the sine function
y = np.sin(x)

# Convert x values back to degrees for plotting
x_deg = np.rad2deg(x)

# Plot the graph
plt.plot(x_deg, y)
plt.xlabel('x (degrees)')
plt.ylabel('sin(x)')
plt.title('Sine Graph')
plt.grid(True)
plt.show()