import pandas as pd

data = pd.read_csv('avgIQpercountry.csv')

#print(data)

data.head(10)

first_rows = data.head(10)
print(first_rows)

last_rows = data.tail(10)
print(last_rows)