# Pandas:-

# Pandas:- It is open source python library which is used for data manipulation and analysis. It is
#          well suited for working with tabular data such as spreadsheet, sql tables. It contains
#          of data structure and s=functions to perform efficient operations on data.


# Various Task that we can do using Pandas:-
# ----------------------------------------

# - Data cleaning, merging and joining.
# - Handling missing data.
# - Group by operations which can be done using various group  functions like sum(), max(), min().
# - Data visualization using some libraries we can create plots, charts or graphs to visualise the
#   data.

# Benefits of Pandas:-
# ------------------

# 1. Representation of data:- It presents the data in manner that is appropriate for data analysis
#    ----------------------   and it is done with data frame and series.

# 2. Data Structure:- Pandas provides two important data structure for processing data that are 
#    --------------   series and data frame.

# 3. Series:- It is 1-D labelled array which can store different types of data. Series's size is 
#    ------   immutable and value is mutable. It means we can change elements of series but we
# cannot change the size of it. We can create a series by using series method of Pandas. It contains
# an index column and a data column.


# Syntax to create an empty series:-

# import pandas as pd

# object = pd.Series()
#           print(object)

# Note:- Difference between Attribute and Function

# Attribute:- An attribute represents data or a characteristic of an object. It's like a variable
#             that holds a value associated with that object.
#             for example:- (object.attribute_name)  print(S1.shape)

# Function:- A function (or method within a class) represents an action or behavior that an
#            object can perform. It's a block of code designed to do something.
#            for example:-(object.function_name())   print(S1.Sum())

# =================================================================================================
'''
# To Create an Empty Series:-

import pandas as pd

S3=pd.Series()
print(S3)

# To Create a Series with Names:-

S3=pd.Series(['Ethan','Roger','Sammy','Denny'])
print(S3)

# To Create a Series from Existing data:-

# List:-

Data=[35,'Michael','Los Angeles']
S2=pd.Series(Data)
print(S2)

# Tuple:-

Data=(12,'Auston','New York')
S1=pd.Series(Data)
print(S1)

# Dictionary:-

Data={"Age":35,"Name":"Elbert","City":"Las Vegas"}
S1=pd.Series(Data)
print(S1)

# Indexing on Series:-

Data=[14,"Sylvia",54,"Damascus"]
S3=pd.Series(Data)
print(S3)
print("\nAccess 2nd Element:",Data[1])
print("Access 3rd Element:",Data[3])

# To Change the Name of 2nd Position:-

S3[1]='Harry'
print(S3)
'''
# =================================================================================================

# Attribute of Series:-(size(), index(), values(), is_unique(), ndim(), length())
# -------------------
'''
# Size():- It will return the size of series that is the number of elements within series.

import pandas as pd

Data=(["Kavin",25,"London"])
S1=pd.Series(Data)

print(S1)

print("\nSize of Series:",S1.size)


# index():- It will return index values of series within a range index function.

Data=(["Fallcon","Andrew","Winter"])
S2=pd.Series(Data)
print(S2)

print("\nIndex of Series:",S2.index)

# values():- It will return all values of data column of series.

Data=(["Billi","Lerry","George"])
S3=pd.Series(Data)
print(S3)

print("\nValues of Series:",S3.values)


# is_unique():- This attribute returns the boolan value that is either True or False. If the series
#               contains unique values then it return True. If series contains duplicate entry it
#               will return False.

Data=(["Wilton","Talwer","Denny"])
S4=pd.Series(Data)

print(S4)

print("\nIs Unique:",S4.is_unique)


# ndim():- It will return the dimensions of the series or array.

Data=([[10,"Ethan"],[20,"Scott"],[30,"Jacob"]])
S5=pd.Series(Data)

print(S5)

print("\nDimension of Series:",S5.ndim)

# length(len):- It will return the number of elements within series.

Data=([23,"Qurtalib",54,"Simpson",43,"Elbert"])
S6=pd.Series(Data)

print(S6)

print("\nLength of Series:",len(S6))
'''
# =================================================================================================

# DataFrame:- The Data Frame is a 2 dimensional, tabular data structure like a Table or Spreadsheet
# ---------   It consists rows  and columns. Each column can have different data type (integer,flaot)
#             It is like a Table of Excel and SQL database.

# For Example:-
'''
import pandas as pd

Student={'Name':['Banton','Labron','Nathan'],'Class':['12th','10th','11th'],'Marks':[45,56,89]}
mydata=pd.DataFrame(Student)

print(mydata)

print("\nTo Access Name, Class & Marks of Students:-")

print("\nName:",mydata['Name'][1])
print("Class:",mydata['Class'][1])
print("Marks:",mydata['Marks'][1])
'''
# =================================================================================================

# Functions of DataFrame:-( head(), sort_values(), sort_index()
# ----------------------
'''
# head():- It is use to print starting elements given by the user.


import pandas as pd

Data={'Name':['Peter','Luke','Thomas'],'Department':['Sales','Computer','Health Care'],
      'City':['Las Vages','California','New York']}

S1=pd.DataFrame(Data)
print(S1)

# To Access First Two Elements:-

print("\n",S1.head(2))

# To Access Last Two Elements use:-

print("\n",S1.tail(2))

# sort_values():- It sorts the column data in ascending or descending order.

mydata={'SNO':[102,101,105,104,103],'Name':['Roger','Peter','Silvia','Lerry','Phillip']}
df=pd.DataFrame(mydata)
print("Original Data:","\n",df)

sorted_df=df.sort_values(by='SNO')

# To Sort Data in Ascending order it is by default turns into Ascend:-

print("\nAscending Order:","\n",sorted_df)

# To Sort Data in Descending Use this(ascending=False):-

sorted_df=df.sort_values(by='SNO',ascending=False)

print("\nDescending Order:","\n",sorted_df)

# sort_index():- It sorts index column data in into correct order.

mydata={'Items':['Saop','Facewash','Bodywash','Shampoo','Handwash'],'Quantity':[29,45,79,95,35],
         'Price':[149,250,110,369,456]}

df=pd.DataFrame(mydata, index=[4,2,5,1,3])

print("Original Data:","\n",df)

sorted_df=df.sort_index()

print("\nModified Data:","\n",sorted_df)
'''
# =================================================================================================

# Attributes of DataFrame:-( shape, axes )
# -----------------------
'''
# Shape:- It will return rows and columns in the DataFrame.

import pandas as pd

mydata={'Employee Id':[101,102,103,104,105],'Employee Name':['Arjan','Shoheb','Simran','Fardin',
        'Malika'],'Department':['Electronics','Sales','HealthCare','Finance','IT Management']}

df=pd.DataFrame(mydata)

print("\nOriginal Data:","\n",df)

print("\nShape of Data:",df.shape)


# Axes:- It will return range index values, in which there will be column name and datatype.

mydata={'Name':['Arjan','Shoheb','Simran','Kanika'],'Section':['A','C','B','D'],
        'Class':['12th','10th','9th','11th']}

df=pd.DataFrame(mydata)

print("Original Data:","\n",df)

print("\nAxes of Data:",df.axes)
'''
# =================================================================================================

# Data Indexing and Selection:-
# ----------------------------

'''
Student = {'Name':['Andrew','Philip','Jacob'],
           'Class':['12th','10th','11th'],
           'Marks':[40,98,58]}
mydata = pd.DataFrame(Student)

Column Based Selection:-

print(mydata['Name'])

# Row Based Selection:-

# - Label based Using Loc(Location):-

print(mydata.loc[2])

# - Index based Using iLoc:-

print(mydata.iloc[2])

# Multiple Selection:-

print(mydata.loc[1:2, ['Name','Class','Marks']])
'''

# ================================================================================================

# NaN Objects(Missing Data):-
# -------------------------

'''
import numpy as np

Data ={'Name':['Arjan','Shoheb','','Kanika','Shoheb'],
        'Section':['A','C','','D','E'],
        'Class':['12th','','9th','11th','9th']}
mydata = pd.DataFrame(Data)

mydata.replace('', np.nan, inplace=True)

# Dropna():- It will remove those recods that are missing in Dataframe.

#S1 = mydata.dropna()
#print(S1)

# Fillna():- It will fill missing records with "Unkown" or 0 as user gives anything.

# S1 = mydata.fillna('Unknown')
# print(S1)
'''

# ================================================================================================

# Manipulating DataFrames:-
# -----------------------

'''
Data ={'Name':['Arjan','Shoheb','Harry','Kanika','Shoheb'],
        'Section':['A','C','B','D','E'],
        'Class':['12th','10th','9th','11th','9th']}
mydata = pd.DataFrame(Data)

# Adding Column:-

S1 = mydata.insert(0, 'Roll NO', [101, 102, 103, 104, 105])
S2 = mydata['Grade']= ['A Grade','B Grade','C Grade','D Grade','E Grade']
print(S1)
print(S2)
print(mydata)

# Removing Column:-

print(mydata.drop('Grade', axis=1))

# Renaming Column:-

S1 = mydata.rename(columns={'Class':'Standard'})

print(S1)
'''
# =================================================================================================

# Grouping Data:-
# -------------

'''
Data = {'Department':['IT','HR','IT','HR'],
        'Salary':[50000, 40000, 55000, 45000]}

mydata = pd.DataFrame(Data)

print(mydata.groupby('Department').mean())

# Aggregate Functions:-

print(mydata)
print("\nTotal Salary:",mydata['Salary'].sum())
print("Maximum Salary:",mydata['Salary'].max())
print("Minimum Salary:",mydata['Salary'].min())
print("Count:")
print(mydata.count())
'''

# =================================================================================================

# Filtering Data:- It is the process of Selecting rows from a data frame based on specific
# --------------   conditions It is use with Arithmetic and Comparison operators.

'''
print(mydata[mydata['Salary']>45000])

# Multiple Conditions:-

print(mydata[(mydata['Salary'] > 45000) & (mydata['Department'] == 'IT')])


Data = {'Department':['IT','HR','IT','HR'],
        'Salary':[50000, 40000, 55000, 45000]}

mydata = pd.DataFrame(Data)

# Row Slicing:-

print(mydata[0:1])

# Column Slicing:-

S1 = mydata[['Department','Salary']]
print(S1)
'''
# =================================================================================================

# Combining Datasets: Merge and Join:-
# ----------------------------------

# Merge:-
# -----

'''
Data1 = {
    'EmpID':[101,102,103,104],
    'Dept':['IT','HR','IT','HR']}


Data2 = {
    'EmpID':[101,102,103,104],
    'Salary':[50000, 40000, 55000, 45000]}

mydata1 = pd.DataFrame(Data1)
mydata2 = pd.DataFrame(Data2)

s = mydata2.query("Salary > 45000")
print(s)

result = (pd.merge(mydata1, mydata2, on='EmpID'))
print(result)


# Types of Merge: Inner, Left, Right, Outer:-
# -------------

# Inner:-

result = (pd.merge(mydata1, mydata2, on='EmpID', how='inner'))
print(result)          

# Left:-

result = (pd.merge(mydata1, mydata2, on='EmpID', how='left'))
print(result)

# Right:-

result = (pd.merge(mydata1, mydata2, on='EmpID', how='right'))
print(result)

# Outer:-

result = (pd.merge(mydata1, mydata2, on='EmpID', how='outer'))
print(result)

# Join:-
# -----

print(mydata1.join(mydata2))
'''

# ================================================================================================

# Query DataFrame Structure:-
# -------------------------

'''
Data2 = {
    'EmpID':[101,102,103,104],
    'Salary':[50000, 40000, 55000, 45000]}

mydata2 = pd.DataFrame(Data2)

s = mydata2.query("Salary > 45000")
print(s)
'''

# =================================================================================================

# Information() Function:-
# ----------------------
'''
# Info():- This Attribute will give the details of column name and its datatype and memory using.

mydata={'Name':['Arjan','Shoheb','Simran','Kanika'],'Section':['A','C','B','D'],
        'Class':['12th','10th','9th','11th']}

df=pd.DataFrame(mydata)

print("\nInfo of Data:",df.info())
'''




