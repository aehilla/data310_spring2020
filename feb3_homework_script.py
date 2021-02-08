### Homework from class Feb 3

### home prices model 

# datapoints:
# # church: 399, 4 bd, 4 ba
# # hudgins: 97, 3 bd, 1 ba
# # mathews: 347.5, 5 bd, 2 ba
# # mobjack: 289, 4 bd, 2 ba
# # moon: 250, 2 bd, 1 ba
# # newptcomfort: 229, 3 bd, 2 ba

import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer = 'sgd',loss='mean_squared_error')

# number of bedrooms:
xs = np.array([4.0, 3.0, 5.0, 4.0, 2.0, 3.0], dtype = float)
# price:
ys = np.array([399.0, 97.0, 347.5, 289.0, 250.0, 229.0], dtype = float)

model.fit(xs, ys, epochs= 500)

print(model.predict([4.0]))
# output is approx. 299
print(model.predict([3.0]))
# output is approx. 235
print(model.predict([2.0]))
# output is approx. 169
print(model.predict([5.0]))
# output is approx. 365

### re-run model using number of bathrooms:

# number of bathrooms:
xs = np.array([4.0, 1.0, 2.0, 2.0, 1.0, 2.0], dtype = float)
# price:
ys = np.array([399.0, 97.0, 347.5, 289.0, 250.0, 229.0], dtype = float)

model.fit(xs, ys, epochs= 500)

print(model.predict([4.0]))
# output is approx. 426
print(model.predict([3.0]))
# output is approx. 346
print(model.predict([2.0]))
# output is approx. 266
print(model.predict([1.0]))
# output is approx. 186
