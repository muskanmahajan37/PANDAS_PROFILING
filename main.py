import pandas as pd
import os
from pandas_profiling import ProfileReport
path=os.path.dirname(__file__)
df=pd.read_excel(f'{path}/temp_1.xlsx')
# print(df)

profile=ProfileReport(df)
profile.to_file(output_file="temp_1.html")
