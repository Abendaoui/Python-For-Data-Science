import numpy as np
import matplotlib.pyplot as plt

# Create an array of x-axis values
x = np.linspace(0, 10, 100)  # Creates 100 evenly spaced values from 0 to 10 (inclusive)

# Calculate the corresponding y-axis values (sine of x)
y = np.sin(x)  # Computes the sine of each element in the 'x' array

# Generate the line plot
plt.plot(x, y)  # Creates a line plot using 'x' and 'y' data arrays

# Generates a scatter plot representing data points.
plt.scatter(x, y,c='aqua')

# Set Title
plt.title('Data Points Visualization')

# Display the plot
plt.show()  # Displays the generated plot on the screen



