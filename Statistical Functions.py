# Topic:- Statistical Functions
# -----

# Statistics:- Statistics in data science is the mathematical backbone for collecting, organizing,
# ----------   analysing, interpreting data and presenting results. Build predictive models and
#              make informed decisions.

# Why Statistics is important?
# ---------------------------

# - Convert raw data into meaningful information.
# - Helps in decision making.
# - Forms the foundation of machine learning.
# - Used fpr prediction and inference.

# Manipulating Statistical Data:- Manipulating statistical data means:
# ----------------------------- 

# - Cleaning data.
# - Organizing values.
# - Transforming datasets.
# - Preparing data for analysis.

# =================================================================================================

# Calculating Results of Statistical Operations:- Python allows calculation of various statistical
# ---------------------------------------------   measures such as:

# It Measures Central Tendency:-

# 1. Mean (Average):- Finding central tendency(middle value). It is used in Overall average.
#    --------------
'''
import statistics

Data = [10,20,30,40,50,50]
print("Original Data:", Data)

S1 = statistics.mean(Data)
print("\nMean:", S1)
'''

# 2. Median:- It finds middle value when data is sorted. It is used in income analysis.
#    ------

'''
S2 = statistics.median(Data)
print("Median:", S2)
'''

# 3. Mode:- The value that appears most frequently(repeating value). It is used popular choice
#    ----   analysis.
'''
S3 = statistics.mode(Data)
print("Mode:", S3)
'''
# =================================================================================================

# Measures of Dispersion:- These measures descibe spread or variability.
# ----------------------

# 1. Variance:- Average of squared deviation from the mean.
#    --------

'''
S4 = statistics.variance(Data)
print("Variance:",S4)
'''

# 2. Standard Deviation:- Square root of variance.
#    ------------------

'''
S5 = statistics.stdev(Data)
print("Standard Deviation:", S5)
'''

# =================================================================================================

# Correlation:- Correlation measures the strength and direction of relationship between two
# -----------   variables.

'''
import numpy as np

x = [1,2,3,4]

y = [2,4,6,8]

print(np.corrcoef(x,y))
'''
