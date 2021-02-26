## Informal responses from class on Feb 24

Convolutions:

Convolve the two 3x3 matrices that were assigned to you with your 9x9 matrix and calculate the resulting two matrices

* I tried to do this and get an output similar to what Natalie and Wayne got (since you said their answers were correct). I don't know what I'm doing wrong but I can only get output matrices that are 9x9. I don't understand what the issue is because I looked at Natalie's code on her github and it seems the same as mine, but when I run the convolution with the 3x3 filter on the 9x9 matrix it gives a 9x9 output, but I thought it was supposed to be 7x7. 
* I tried to google the issue and tried using `scipy.signal.convolve2d(A, b)` taken from [this stack overflow post](https://stackoverflow.com/questions/59878951/convolving-a-each-row-of-a-2d-matrix-with-a-vector) instead of the manual convolution code, but the scipy convolve function still gives a 9x9 output. 
* I can't figure out what I'm doing wrong, and I haven't taken linear algebra so I don't really understand matrices anyways, but here's my results:

```
filter1 = np.array([[1,0,0],[0,0,1],[1,1,0]])
filter2 = np.array([[1,1,1],[0,1,1],[1,1,0]]) 
matrix = np.array([
    [1,-1,0,2,0,0,1,1,1],
    [1,1,-1,2,0,-2,-1,0,0],
    [1,-1,-1,-2,0,2,0,0,-1],
    [1,0,0,-1,-1,2,-1,-1,-1],
    [-1,-1,1,-1,2,1,-1,-1,1],
    [-1,-1,-1,1,-2,-1,0,1,1],
    [-1,0,0,-1,1,-2,-1,1,-1],
    [0,1,0,-1,-1,-2,-1,0,-1],
    [1,1,-1,-1,1,1,0,-1,1]
])
```

```
output from filter 1:
>>> [[ 1 -1  0  2  0  0  1  1  1]
 [ 1  0  2  0  0  2  1  2  0]
 [ 1  0  1  0  1  1  0  0 -1]
 [ 1  0  0  0  4  0  0  0 -1]
 [-1  1  0  2  0  0  0  0  1]
 [-1  0  0  0  0  0  0  2  1]
 [-1  0  0  0  0  0  0  0 -1]
 [ 0  0  0  0  0  0  0  0 -1]
 [ 1  1 -1 -1  1  1  0 -1  1]]
```

```
output from filter 2:
 >>> [[ 1 -1  0  2  0  0  1  1  1]
 [ 1  2  1  0  0  0  0  1  0]
 [ 1  0  0  0  0  2  1  0 -1]
 [ 1  0  0  0  1  3  2  0 -1]
 [-1  0  0  1  2  0  0  0  1]
 [-1  0  0  0  0  0  0  2  1]
 [-1  0  0  0  0  0  0  0 -1]
 [ 0  2  0  0  0  0  0  0 -1]
 [ 1  1 -1 -1  1  1  0 -1  1]]
 ```

What is the purpose of using a 3x3 filter to convolve across a 2D image matrix?

* I think the purpose is to choose a filter that will highlight certain features, making the image matrix easier to feed into a ML model that might need to identify specific features but which doesn't need others (eg. vertical lines vs horizontal lines).

Why would we include more than one filter? 

* I think that including more than one filter could potentially allow you to emphasize different things in the image. Like if you had one filter that really emphasized sharp edges and another filter that really emphasized vertical lines, maybe by including both filters you can emphasize both kind of features in your image.

How many filters did you assign as part of your architecture when training a model to learn images of numbers from the mnist dataset?

* I just assigned one, because I didn't know I could include more than one filter. 

MSE: From your 400+ observations of homes for sale, calculate the MSE for the following:
* Overall MSE (for all observations) = 58,743,084,732
* The 10 biggest over-predictions
    * MSE = 64,017,901,166
* The 10 biggest under-predictions
    * MSE = 1,638,994,161,727
* The 10 most accurate results (use absolute value)
    * MSE = 6,332,792
    
In which percentile do the 10 most accurate predictions reside? 
* The homes for which the model predicted most accurately all had observed prices between $285,000 and $300,000, or between the 65th and 72nd percentiles:
```
prices = np.array(df['prices'])
print(np.percentile(prices, 65))
>>> 285000.0
print(np.percentile(prices, 72))
>>> 300000.0
```

Did your model trend towards over or under predicting home values?
* The average difference between the observed price and the predicted price was $11,970, so in that sense model trended towards over-predicting price. However, looking at the MSE for the 10 biggest under and over predictions, the MSE for the under-predictions is much higher, so I guess that means that the model made more over-predictions, but the under-predictions were off by a bigger margin. 

Which feature appears to be the most significant predictor in the above cases?
* Looking at the cases where the model over-predicted, it seems like the homes had a lot of square footage, but only an average number of bedrooms and/ or bathrooms. So I think it is likely that the model over-estimated how much the additional square footage would increase the value of the home, and guessed too high. For the under-predictions, there was not a clear pattern. I think it is possible that these homes are in very desirable areas, like being close to downtown or on the water, so they may be priced higher, but I did not include a geographic variable in my model, so it under-predicted in these cases.

Stretch goal: calculate the MAE and compare with your MSE results
* Mean Absolute Error for all observations = 126,914
* Mean Squared Error for all observations = 58,743,084,732
* obviously MSE is much larger because it is a squared value, but the square root of the MSE (RMSE) is 242,369, which is almost double the mean absolute error. I'm honestly not sure what that means or why the numbers would be so different. I tried to google this to understand why, and [this article](https://medium.com/human-in-a-machine-world/mae-and-rmse-which-metric-is-better-e60ac3bde13d) said that "Focusing on the upper bound, this means that RMSE has a tendency to be increasingly larger than MAE as the test sample size increases." So I think that might partly explain why the MSE is higher than MAE. 
