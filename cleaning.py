import pandas as pd
f = pd.read_csv("csv_data.txt",sep='\s+',skiprows=3,nrows=1317)
print(f.head(10))

print(f.dtypes)

f.describe()

%matplotlib inline
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

f.plot(kind='scatter', x='xl', y='sl', s=f["well_data"]/15)

