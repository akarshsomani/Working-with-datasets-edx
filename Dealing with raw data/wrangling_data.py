import pandas as pd
import numpy as np
df=pd.read_csv("demo.csv",sep='\t')
print(df.dtypes)
df.Date=pd.to_datetime(df.Date, errors='raise')
print(df)
#if it gives error then use
df.Date=pd.to_datetime(df.Date, errors='coerce')