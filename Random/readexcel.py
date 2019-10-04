import pandas as pd

# read 2nd sheet of an excel file
dataframe2 = pd.read_excel('excel.xlsx', sheet_name='Sheet1')
a = dataframe2.values.tolist()
print(len(a))
