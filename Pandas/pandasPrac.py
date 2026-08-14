import pandas as pd
# import numpy as np

# # Panda series Attributes
# series = pd.Series([1,2,3,4])
 
# print(" Empty?:",series.empty)
# print("dimension: ",series.ndim)
# print("has NANs: ",series.hasnans)
# # print(series.list())
# print(series.first)
# print(series.axes)
# print("Flags: ",series.flags)
# print("Values:", series.values)
# print("Keys:", series.keys)
# print("Shape: ", series.shape)
# print("Index Values: ", series.index[3])
 
 
# s = pd.Series([1,2,3,4,5], dtype = int)
 
# # Display the original series
# print("Original Series:\n",s)
 
# # Modify the values of first two elements
# s[:2] = [100, 200] # type: ignore
 
# print("Series after modifying the first two elements:",s, sep ="\n")

# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
 
# print(s[3:])
 
# print(s[-3:])
 
# # Slice multiple elements
# print(s['a':'d'])
 
# print(s[:'c'])
 
 


# data = np.array(['a','b','c','d'])
 
# s = pd.Series(data)
 
# print(s[1])
 
# print("Original Series: \n",s, sep ="\n")
 
# result = s[1:3]
 
# print("values after slicing:\n", result, sep = "\n")
 
# result = s[0:4:2] #start,end,no.of steps
# print(result)

# data = {'a' : 0., 'b' : 1., 'c' : 2.}
# s = pd.Series(data,index=['b','c','x','a'])
# print(s)
 
# #dictionary keys are used to construct indexes
 

# data = {'a' : 0., 'b' : 1., 'c' : 2.}
 
# s = pd.Series(data)
 
# print(s)
 

# data = np.array(['a','b','c','d'])
 
 
# s = pd.Series(data, index  = [100,101,102,103])
 
# print(s)
 

# data = np.array(['a','b','c','d'])
 
# s = pd.Series(data)
# print(s)
 
# s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])# Display the Input Seriesprint('Input Series\n',s)# Apply all Arithmetic Operation and Display the Resultsprint('\nAddition:\n',s+2)print('\nSubtraction:\n', s-2)print('\nMultiplication:\n', s * 2)print('\nDivision:\n', s/2)print('\nExponentiation:\n', s**2)print('\nModulus:\n', s%2)print('\nFloor Division:\n', s//2)
 
 

# ----------------------------- DATAFRAMES -----------------------------------------------
# import pandas as pd
dataFile = "employees.csv"
empData = pd.read_csv(dataFile)
print(empData.describe())