# Topic:- Matplotlib


# Matplotlib:- It is Python plotting library. It converts numberical data to visual form, making
# ----------   patterns and trends easy to understand. It is used for:

# - Data Visualization
# - Graphical representation of data.
# - Statistical analysis and reporting.

# Syntax:-

# import matplotlib.pyplot as plt

# plt.plot(x,y)
# plt.show()

# =================================================================================================

# Common Functions for Graph Colorful Representation:-
# ---------------------------------------------------

# For dots, colors & lines   -->  plt.plot(x, y, marker='o', linestyle='--', color='blue')

# For background grid lines  -->  plt.grid(True)

# For Fontsize increment     -->  plt.xlabel("Subjects", fontsize=10)

# For Label padding(space)   -->  plt.xlabel("Subjects", labelpad=10)

# For Font Bold              --> plt.xlabel("Subjects", fontweight='bold')

# =================================================================================================

# Basic Program to Create Graphical Data:-

# 1. Simple Line Plot(Up Trend):- A line plot shows data points connected by straight lines. It is
#    -------------------------    mainly used to show trend over time or sequence.

'''
import matplotlib.pyplot as plt

x = [5, 10, 15, 20, 25, 30]
y = [0, 5, 10, 20, 30, 40]

plt.plot(x,y, label="Line 1", color='b')
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Simple Line Plot")
plt.grid(True)
plt.legend()

plt.show()
'''

# 2. Scatter Plot:- A scatter plot displays data points with dots to show relationship between
#    ------------   two variables.

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 8, 7, 10]

# To Show Sactter Plot:-

plt.scatter(x,y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Scatter Line Plot")

plt.show()
'''

# 3. Density Plot:- A density plot shows the distribution of continuous data. It is smooth version 
#    ------------   of histogram. In Matplotlib, density is usually visualize using (histogram with
#                   density=True).

'''
import matplotlib.pyplot as plt

Data = [10, 20, 20, 30, 30, 30, 40, 50]

plt.hist(Data, density=True)
plt.title("Density Plot")

plt.show()
'''

# 4. Contour Plot(Visualizing Functions):- A contour plot represents a 3D surface in 2D using
#    -----------------------------------   contour lines. It is mainly used to visualize
#                                          mathematical functions.

'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

plt.contour(X,Y,Z)
plt.title("Contour Plot")

plt.show()
'''

# 5. Mutiple Subplots:- Subplots allow displaying graphs in a single figure.
#    ----------------

# Syntax:-
# ------

# plt.subplot(rows, columns, index)

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

plt.subplot(1, 2, 1)
plt.plot(x, [i*2 for i in x])
plt.title("Plot 1")

# --- Grid --- (It is use for background lines in graph.)

plt.grid(True)
 
plt.subplot(1, 2, 2)
plt.plot(x, [i*3 for i in x])
plt.title("Plot 2")
plt.grid(True)

plt.show()
'''

# 6. Histograms:- A histogram shows the frequency distribution of data.
#    ----------

# Syntax:-
# ------

# plt.hist(data, bins)

'''
import matplotlib.pyplot as plt


Marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

plt.hist(Marks, bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.show()
'''

# 7. Bar Charts:- A bar chart is used to compare categorical data.
#    ----------

# Syntax:-
# ------

# plt.bar(categories, values)

'''
import matplotlib.pyplot as plt

Subjects = ['English', 'Maths', 'Science', 'Hindi', 'Geography']

Marks = [87, 46, 51, 92, 75]

plt.bar(Subjects, Marks)
plt.xlabel("Subjects", fontsize=15, labelpad=15)
plt.ylabel("Marks", fontsize=15, labelpad=15)
plt.title("Bar Chart", fontsize=15)

plt.show()
'''

# ================================================================================================

# Plot Customization:-
# ------------------

# 1. Legend:- It is used to label and differentiate between multiple data series(Lines) in single 
#    ------   plot.

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]

y = [10, 20, 30, 40, 50]

z = [1, 2, 3, 4, 5]

q = [5, 10, 15, 20, 25]

plt.plot(x,y, label="Line 1", color="blue")
plt.plot(z,q, label="Line 2", color="red")
plt.legend()

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Line Plot")

# 2. Grid :- It is use for background lines in graph.
#    ----

plt.grid(True)

plt.show()
'''

# =================================================================================================

# Complete Graph Program:-
# ----------------------

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x,y, label="Sales")

plt.xlabel("Year")
plt.ylabel("Revenue")

plt.title("Sales Growth 2026")

plt.legend()

plt.show()
'''





