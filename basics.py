import pandas as pd
import numpy as np

#read datasets from CSV file in dataframe
df = pd.read_csv("sales_data_sample.csv",encoding="latin1")


#ROWS (head , tails)
print("This is Head")
print(df.head(3))
print("This is Tail")
print(df.tail(3))

print("Displaying the info of data sets")
print(df.info())

print(df.describe())
row, col = np.shape(df)
print("Data Rows", row)
print("Data columns", col)

#none values in datasets
is_non = pd.isnull(df)
print(is_non)
print("Is non values is",pd.value_counts(is_non))

print(len(df))