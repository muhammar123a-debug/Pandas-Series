import pandas as pd

data = {
    "Name":["Ammar","Anas","Qasim",],
    "city":["Karachi","lahore","Islamabad"],
    "age":[22,21,32]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv", index=False)