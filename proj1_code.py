## building model for predicting home prices from zillow jacksonville data

import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../jacksonville.csv")

# there are a few rows where the webscraper didn't work:
# drop any rows in the sqft column where the value is not a number
df['sqft'] = pd.to_numeric(df['sqft'], errors = 'coerce')
df.dropna(inplace = True)
print(df.shape)

## calculating descriptive statistics of input data:
df[['prices','no_beds','baths','sqft']].describe()

# input to the model = number of bedrooms, number of bathrooms, sq ft
# model will predict price

df['sqft'] = df['sqft']/1000

# number of bedrooms:
x1 = np.array(df['no_beds'], dtype = float)
# square footage (divided by 1000):
x2 = np.array(df['sqft'], dtype = float)
# number of bathrooms:
x3 = np.array(df['baths'], dtype = float)
## combine the arrays
xs = np.stack([x1, x2, x3], axis = 1)
# price:
ys = np.array(df['prices'], dtype = float)

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer = 'sgd',loss='mean_squared_error')
model.fit(xs, ys, epochs= 500)

# make a specific prediction for a 3 bedroom, 2144 sq ft, 2 bath home:
a = np.array([3.0], dtype = float)
b = np.array([2.144], dtype = float)
c = np.array([2.0], dtype = float)
d = np.stack([a,b,c], axis =1)
print(model.predict([d]))

# make predictions:

df['predictions'] = model.predict([df[['no_beds', 'sqft','baths']]])
