## after class Feb 3, refining code from homework 1:
# homework: add another variable, stack it, predict price for all the homes, and provide a new response on github,
# detailing which homes are good deals


import tensorflow as tf
import numpy as np
from tensorflow import keras
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer = 'sgd',loss='mean_squared_error')
# number of bedrooms:
x1 = np.array([4.0, 3.0, 5.0, 4.0, 2.0, 3.0], dtype = float)
# square footage:
x2 = np.array([3.680, 1.238, 3.051, 3.524, 1.479, 2.840], dtype = float)
# number of bathrooms:
x3 = np.array([4.0, 1.0, 2.0, 2.0, 1.0, 2.0], dtype = float)
## combine the arrays
xs = np.stack([x1, x2, x3], axis = 1)
# price:
ys = np.array([3.990, .970, 3.475, 2.890, 2.500, 2.290], dtype = float)
model.fit(xs, ys, epochs= 500)

a = np.array([4.0], dtype = float)
b = np.array([3.524], dtype = float)
c = np.array([2.0], dtype = float)
d = np.stack([a,b,c], axis =1)
print(model.predict([d]))
# the model predicts that for a 4 bedroom, 2 bathroom house with 3.524 sq ft,
# the price should be ~322K
