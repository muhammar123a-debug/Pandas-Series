import pandas as pd

#read datasets from CSV file in dataframe
df = pd.read_csv("sales_data_sample.csv",encoding="latin1")


#ROWS (head , tails)
# print("This is Head")
# print(df.head(3))
# print("This is Tail")
# print(df.tail(3))

print("Displaying the info of data sets")
print(df.info())