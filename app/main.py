import pandas as pd
import sys

input = pd.read_excel('data/input.xlsx', headers=True)
output = pd.DataFrame(columns = input.columns)

for index, row in input.iterrows():
    for elements in row:
        if(str(elements).lower().__contains__(str(sys.argv[1]).lower())):
            output = output.append(row)
            break

output.to_excel('data/output.xlsx')