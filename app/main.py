import pandas as pd
import sys
import re

input = pd.read_excel('data/input.xlsx', headers=True)
output = pd.DataFrame(columns = input.columns)

for index, row in input.iterrows():
    for elements in row:
        if( re.search(str(elements), (str(sys.argv[1])), re.IGNORECASE) ):
            output = output.append(row)
            break

output.to_excel('data/output.xlsx')