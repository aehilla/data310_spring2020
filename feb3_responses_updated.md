## Updated response using home prices model with three variables

The updated script I made to predict housing price predicts based on square footage, number of bedrooms, and number of bathrooms. 

This 3-variable model predicts prices (in 100k) of:

|Name | Actual      | Predicted | Deal|
|-----| ----------- | ----------- |----|
|Church| 3.99      | 3.96      | Fair deal|
|Hudgins| .97      | 1.649       | Good deal|
|Mathews| 3.475   | 3.076      | Bad deal |
|Mobjack| 2.890   | 3.092        | Good deal|
|Moon| 2.500  | 1.578        | Bad deal|
|New Pt. Comfort| 2.290   | 2.667        |Good deal|

To get these predictions, the model takes three input arrays:

<code>
  # number of bedrooms: /n
  x1 = np.array([4.0, 3.0, 5.0, 4.0, 2.0, 3.0], dtype = float)
  # square footage:
  x2 = np.array([3.680, 1.238, 3.051, 3.524, 1.479, 2.840], dtype = float)
  # number of bathrooms:
  x3 = np.array([4.0, 1.0, 2.0, 2.0, 1.0, 2.0], dtype = float)
  ## combine the arrays
  xs = np.stack([x1, x2, x3], axis = 1)
  # price:
  ys = np.array([3.990, .970, 3.475, 2.890, 2.500, 2.290], dtype = float)
