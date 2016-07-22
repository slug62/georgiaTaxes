#!/usr/bin/python3
"""

"""

import numpy as np
import matplotlib.pyplot as plot

"""
Find annual population growth
"""


# Function that will plot graphs when provided a x and y vector
def drawPlot(x, y, ylimit=[0, 10000000]):
    plot.plot(x, y, marker='o', linestyle='-')
    axis = plot.gca()
    axis.set_xlim(x[0], x[len(x)-1])
    axis.set_ylim([ylimit[0], ylimit[1]])
    axis.get_yaxis().get_major_formatter().set_scientific(False)
    axis.get_xaxis().get_major_formatter().set_scientific(False)
    plot.autoscale(enable=False)
    plot.grid()
    plot.show()

# Historical Georgia Population
ga_census = [[1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900,
              1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
             [82548, 162686, 251407, 340989, 516823, 691392, 906185, 1057286, 1184109,
              1542181, 1837353, 2216331, 2609121, 2895832, 2908506, 3123723, 3444578,
              3943116, 4589575, 5463105, 6478216, 8186453, 9687653]]

# Show Current Population Growth Graph
# drawPlot(ga_census[0], ga_census[1])

# Population numpy array
population = np.array(ga_census[1])

# Creating a x vector to curve fit
xi = 0  # Starting x value
xf = len(population)  # Ending x value

# Degree of the polynomial we would like to end up with
deg = 6

# Create the x vector
x = np.linspace(xi, xf, len(population))

# Create Polynomial to predict growth up to the year 2020
poly = np.polyfit(x, population, deg)

# Output the polynomial
print(poly)

# Evaluate the Polynomial to compare to historical data
yc = np.polyval(poly, x)

# Plot our curve fitted polynomial
# drawPlot(ga_census[0], yc)

new_xf = len(population) + 1  # Plus one to predict population up to the year 2020
num_x = 220  # Number of years between 2010 and 1790
pop_years = ga_census[0]
pop_years.append(2020)  # Add the year 2020

new_x = np.linspace(xi, new_xf, num_x)
predict_pop = np.polyval(poly, new_x)

# Plot predicted annual population values to 2020
# drawPlot(new_x, predict_pop, ylimit=[0,14000000])


"""
Find Annual labor force
"""

# Historical Georgia WorkForce
ga_labor_force = [[2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015],
                  [4708085, 4815844, 4877838, 4798844, 4697608, 4746588, 4779937, 4749720, 4739843, 4758664]]

# Historical Georgia Unemployment rate
ga_unemployment_rate = np.array([4.717, 4.625, 6.475, 10.042, 10.392, 10.058, 9.017, 8.025,
                                 7.017, 5.825])

# Plot historical data
# drawPlot(ga_labor_force[0], ga_labor_force[1], ylimit=[4000000, 5500000])

# Attempt to find a polynomial through curvefitting
labor_x = np.linspace(xi, len(ga_labor_force[1]), len(ga_labor_force[1]))
poly = np.polyfit(labor_x, ga_labor_force[1], 3)
labor_y = np.polyval(poly, labor_x)

# Plot the curve fitted polynomial to see how close to historical data it is
# drawPlot(labor_x, labor_y, ylimit=[4000000, 5500000])

# Plot additinal data point to forecast labor force
labor_x_predict = np.linspace(xi, 15, 15)
predict_labor_y = np.polyval(poly, labor_x_predict)
# drawPlot(labor_x_predict, predict_labor_y)




# TESTING
amatrix = np.array([[1, 1, 1], [9, 4, 0]])
bmatrix = np.array([78.2, 62.56])
xmatrix = np.linalg.solve(amatrix, bmatrix)

print(xmatrix)
