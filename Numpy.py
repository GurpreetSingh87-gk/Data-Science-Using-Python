# Numpy :-

# Numpy:- It is a Numerical Pyhton. It is use to create array which is collection of elements of
#         similar data types. Numpy is use to handle matrix calculation. Numpy has pre-defined
#         functions to manipulate matrix.

# Syntax to create 1-D (One Dimensional) array:-

# array_name = np.array([element1, element2...])

# =================================================================================================

# Create One Dimensional (1-D) Array:-
'''
import numpy as np

d1=np.array([5,10,15,20,25])

print("One Dimensional Array:",d1)

# Create Two Dimensional (2-D) Array:-

d2=np.array([(5,10,15),(20,25,30)])

print("\nTow Dimensional Array:",d2)
'''
# ----------------------------------

# Process Array Element using For Loop:-
'''
import numpy as np

d1=np.array([5,10,15,20,25])
print("Array:",d1)

for i in d1:
    print(i)
    
# Process Array Element using Range Function:-

d1=np.array([0,5,10,15,20,25])

for i in range(0,5):
    print(d1[i])
'''
# =================================================================================================

# Questions:-
'''
# Q:-1. Display array element in reverse order.

import numpy as np

d1=np.array([1,2,3,4,5])

print("Original Array:",d1)

for i in range(5,0,-1):
    print("Reverse Order:",i)

# Q:-2. Input an array of Five elements from the user and display Even elements.

arr=[]

print("Enter 5 Elements:-")
    
for i in range(5):
    num=int(input(f"\nEnter Element {i+1}:"))
    arr.append(num)

print("\nEven Numbers are:")

for num in arr:
    if num%2==0:
        print(num, end=" ")

# Q:-3. Display the sum of given array elements.

arr=np.array([1,2,3,4,5])
print("Original Array:",arr)

print("\nSum of Elements is:",sum(arr))

# Q:-4. Display the maximum elements within array.

arr=np.array([5,10,15,20])
print("Original Array:",arr)

print("\nMaximum Elements is:",max(arr))

# Q:5. Input array of Five elements and search the given elements.

arr=[]

for i in range(5):
    num=int(input("Enter Element:"))
    arr.append(num)

search=int(input("\nEnter Element to search:"))

if num in arr:
    print("\nElement is Found:",{search})
else:
    print("Element is Not Found:",{search})
'''
# =================================================================================================

# Array creation using Numpy Methods:- (empty, zeros, ones)
# ----------------------------------

# 1. empty():- (The Empty method create an array that will generate garbage values.)
'''
import numpy as np

array=np.empty([1,2,3,4,5])

print("Empty:Garbage Values:-",array)
'''
# 2. zeros():- (The Zeros method creates an array filled with zero in the form of rows and columns.)
'''
array=np.zeros([1,2,3,4])

print("Zeros:",array)
'''
# 3. ones():- (The Ones method creates an array filled with ones. All values will ne one.)
'''
array=np.ones([1,2,3,4,5])

print("Ones:",array)
'''
# 4. full():- (The full method fills array with the number given by user.)
'''
array=np.full([1,2,3,4],52)

print("Full:",array)
'''
# =================================================================================================

# Array From Numerical Ranges:- (arange, linspace, random.random)
# ----------------------------

# 1. arange():- (The Arange function will generate list of numbers given by user.)
#

# Syntax:-
# ------

# array_name=np.arange(start,stop,step)

'''
import numpy as np

arr=np.arange(1,20,1)

print("Arange Function:",arr)
'''

# 2. linspace():- (The Linspace function will create space between numbers.)

'''
arr=np.linspace(1,2,3,4,5)

print("Linspace Function:",arr)
'''

# 3. random.random():- (This Function will generate random numbers in the form of rows and columns)
#

# Syntax:-
# ------

# array_name=np.random.random((rows,columns))

'''
arr=np.random.random((4,3))

print("Random.random Function:",arr)
'''
# =================================================================================================

# Array Creation From Existing Data:- (asarray, asmatrix)
# ---------------------------------

# 1. asarray():- (The Asarray Function will create an array using existing data like tuple or list.)

import numpy as np
'''
data=[1,2,3,4,5]
arr=np.asarray(data)

print("Asarray Function:",arr)
'''
# 2. asmatrix():- (The Asmatrix Function will interpret input as a matrix.)
'''
arr=np.asmatrix([[10,20],[30,40]])

print("Asmatrix Function:",arr)
'''
# =================================================================================================

# Array Attributes:- (shape, ndim, reshape, itemsize)
# ----------------

# 1. shape:- (This attibute will return a tuple containing number of rows and columns.)
#

# Syntax:-
# ------

# array_name=np.shape([rows,columns])
'''
import numpy as np

arr=np.shape([[10,20,30],[40,50,60]])

print("Shape:",arr)
'''

# 2. ndim:- The Ndim attribute will tell the dimension of array.)
'''
arr=np.ndim([[10,20,30],[40,50,60]])

print("Ndim:",arr)
'''

# 3. reshape:- (The Reshape attribute will reshape the array.)
'''
arr=np.array([[10,20,30],[40,50,60]])

print("Reshape:",arr.reshape(3,2))
'''
# 4. itemsize:- (This attribute will return length of each element of array in bytes
#                 dtype of array is int8 (1 byte).
'''
arr=np.array([1,2,3,4,5])

print("Itemsize:",arr.itemsize)
'''
# =================================================================================================

# Indexing and Slicing:-
# -------------------

# Indexing:-(Indexing means to accessing individual elements of a NumPy array using their position
# --------  (index).

# Syntax:-   array_name([Position])

# Indexing in 1-D Array:-
'''
import numpy as np

arr=np.array([10,20,30,40,50])
print("Original Array:",arr)

print("\nPositive Indexing:-")

print("\nElement 40 Position:",arr[3])
print("Element 50 Position:",arr[4])

print("\nNegative Indexing:-")

print("\nElement 40 Position:",arr[-2])
print("Element 50 Position:",arr[-1])

# Indexing in 2-D Array:-

arr=np.array([[10,20,30],[40,50,60]])
print("\nOriginal Array:",arr)

print("\nElement 40 Position:",arr[1][0])
'''

# Slicing:- (Slicing refers to extracting a range of elements from a NumPy array using their index
# -------    position.)

# Syntax:- array_name=np.([start,stop,step])

# Slicing in 1-D Array:-
'''
import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
print("\nOriginal Array:",arr)

# Positive Slicing:-

print("\nSlicing:",arr[2:7])
print("Slicing:",arr[:8])

# Negative Slicing:-

print("\nSlicing:",arr[:-2:-8])
print("Slicing:",arr[-2:])
'''
# Slicing in 2-D Array:-
'''
arr=np.array([[10,20,30],
             [40,50,60],
             [70,80,90],
             [100,110,120]])
print("Original Array:",arr)

# Positive Slicing:-

print("\nSlicing:",arr[1:4])
print("\nSlicing:",arr[:2])

# Negative Slicing:-

print("\nSlicing:",arr[-2:4])
print("\nSlicing:",arr[:-3])
'''
# =================================================================================================

# Median Function():- This will return the value in the middle of the array.
'''
import numpy as np

arr=np.median([1,2,3,4,5,6,7])
print("Median:",arr)
'''
# =================================================================================================

# Randint Function():- It will generate random numbers at every run.
#                      Syntax:-array_name=np.random.randint( 
'''
arr=np.random.randint([5,10,15,20,25,30])
print("Randint:",arr[4])
'''
