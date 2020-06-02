import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/test_data.csv')
colomns = ['price','mileage','hasAccidents','ownerCount','engineCylinders','carYear']
df = df[colomns]

# fill part of nan
# type_with_five_seats = ['Sedan','SUV / Crossover']
# type_with_four_seats = ['Coupe','Convertible']

# df.maxSeating=np.where(df.bodyType.isin(type_with_five_seats),df.maxSeating.fillna(5),df.maxSeating)
# df.maxSeating=np.where(df.bodyType.isin(type_with_four_seats),df.maxSeating.fillna(4),df.maxSeating)

# drop rows with nan
df = df.dropna()
df = df.drop('bodyType', 1)

# filter valid price
df = df.loc[(df['price'] >= 1000)]

# convert car year to car age
df['carAge'] = 2020-df['carYear']
df = df.drop('carYear', 1)

# convert isCPO and hasAccident to 0/1
df['hasAccidents'] = df['hasAccidents'].astype(int)

# Ordinal Encode for categorical variable engineCylinders
df['engineCylinders'] = df['engineCylinders'].astype('category')
df['engineCylinders'] = df['engineCylinders'].cat.reorder_categories(['I4', 'I6', 'V6','V8'], ordered=True)
df['engineCylinders'] = df['engineCylinders'].cat.codes

# check skewness and kurtosis
print("Skew ", df['price'].skew())
print("kurt ", df['price'].kurt())
print(df.shape)

# check distribution of price
plt.figure(figsize=(20,8))
plt.subplot(1,2,1)
sns.distplot(df['price'])

fig = plt.figure(figsize=(18,5))
fig.subplots_adjust(hspace=0.3, wspace=0.3)

ax1 = fig.add_subplot(1,2,1)
sns.scatterplot(x='price', y="carAge", data=df)
ax1.set_xlabel('Price')
ax1.set_ylabel('Car Age')
ax1.set_title('Car Age vs Price')

ax2 = fig.add_subplot(1,2,2)
sns.scatterplot(x='price', y='ownerCount', data=df)
ax2.set_ylabel('Number of Owners')
ax2.set_xlabel('Price')
ax2.set_title('Owner Count vs Price')
plt.show()


# Output to csv
df.to_csv('../data/test.csv')
