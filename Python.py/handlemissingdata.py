import numpy as np
import pandas as pd
df= pd.DataFrame({'Name': ['A','B','C','D'],'Age':[25,np.nan,30,np.nan]})

#check missing values
print(df.isnull())

print(df.dropna())


print(df.fillna(0))
