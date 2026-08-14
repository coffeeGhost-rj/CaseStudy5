import pandas as pd
import numpy as np

# dataFile = f"Pandas\products-1000.csv" # type: ignore

# productdf = pd.read_csv(dataFile)

# print(

# # productdf.describe(),
 
# productdf.shape,
# productdf.columns,
# productdf.groupby("Color").count(),
# productdf.groupby("Category").count(),
# productdf.groupby( "Availability").count(),
 
# productdf["Availability"].skew)
# # print(round(productdf["Stock"].kurtosis(),3))
# # print(round(productdf["Price"].skew(),3))
 
# print("Mean: ", round(productdf["Stock"].mean(),3))
# print("Median: ", round(productdf["Stock"].median(),3))
# print("Mode: ", round(productdf["Stock"].mode(),3))
 
 
# dfagg = productdf.groupby("Availability").agg({"Price":"mean", "Stock":"sum"})
# print(dfagg)

# --------------------------------------------------------------------------------------

 
# # create a sample DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 35, 40],
#         'City': ['New York', 'London', 'Paris', 'Tokyo'],
#         'Height': ['165', '178', '185', '171'],
#         'Profession': ['Engineer', 'Entrepreneur', 'Unemployed', 'Actor'],
#         'Marital Status': ['Single', 'Married', 'Divorced', 'Engaged']}
# df = pd.DataFrame(data)
 
# # display the original DataFrame
# print("Original DataFrame:")
# print(df)
# print()
 
# # delete age column
# df.drop('Age', axis=1, inplace=True)
 
# # delete marital status column
# df.drop(columns='Marital Status', inplace=True)
 
# # delete height and profession columns
# df.drop(['Height', 'Profession'], axis=1, inplace=True)
 
# # display the modified DataFrame after deleting rows
# print("Modified DataFrame:")
# print(df)

# --------------------------------------------------------------------------

# df = pd.read_csv(f"Pandas\my_file.csv")
# df.fillna(np.nan)
 
# df["Actual gross"] = df["Actual gross"].str.replace("$","",regex=False).str.replace(",","",regex=False)
# # df["Actual gross"].replace(r"[\[.*]","", regex =True , inplace=True)
# df["Actual gross"] = df["Actual gross"].str.split("[").str[0]
 
# df["Actual gross(in 2022 dollars)"].replace(r"[\$,]","", regex =True , inplace=True)
 
 
# df["Average gross"].replace(r"[\$,]","", regex =True , inplace=True)
 
# df["Year(s)"].replace(r"\–.*", "", regex =True, inplace=True)
 
# # Splits at '-' and takes the first element (lower value)
# df["Year(s)"] = df["Year(s)"].str.split("–").str[0]
 
# df["Tour title"].replace(r"\†.*", "" , regex = True, inplace=True)
# df["Tour title"].replace(r"\‡.*", "", regex =True, inplace=True)
# df["Tour title"].replace(r"\*", "", regex =True, inplace=True)
 
# # df["Tour title"].str.replace(r"\†.*", "" , regex = False).str.replace(r"\‡.*", "", regex =False).str.replace(r"\*", "", regex =False)
 
# print(df)



# ------------------------------------------------------------------------------------------

ddsdf=pd.read_csv(f"Pandas\dirty_data_ship.csv")

print(ddsdf)

