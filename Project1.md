## Project 1 write-up
### to be turned in March 3

Select a city and scrape as many observations as possible from zillow. Try to obtain at least 400 observations from your selected location.

* Selected location: Jacksonville, FL

Clean the housing data you obtained and create a number of usable features (independent variables) and targets (dependent variables). Set price as the response variable, and then set numbers of beds, number of bathrooms and total square footage as the predictors. Following the previous model you specified (6 houses in Mathews), import your new data set and train a new model on your target and features. Write a one and a half to two page report on your results and include the following:

A description of the housing data you scraped from zillow
* I initially scraped 400 observations, but 8 observations failed to scrape the square footage from the website and were dropped, so the data I used in the model ultimately contained 392 observations. 
* descriptive statistics:



|measure  |  prices | no_beds   |    baths    |     sqft |
|------|----------|-------------|-----------|
|count | 392    |    392 | 392 | 392 |
|mean |  $285,009    |      3.525  |  2.515 | 1988.882 |
|std  |  $242,487      |    0.848 |   0.718  | 693.0126 |
|min  |  $12,900      |     2  |  1 | 989.0 |
|25%  |  $178,675     |     3  |  2 | 1439.0 |
|50%  |   $249,100   |       4  |  2 | 1827.500000 |
|75%  |  $326,000    |      4  |  3 | 2440.0 |
|max  |  $3,692,000    |     5  |  5 | 3621.0 |

A description of your model architecture
* response
``` 
code
```

An analysis of your model output
* response

An analysis of the output that assesses and ranks all homes from best to worst deal
* response
* Graph showing all the homes' rankings 
* Table:

|Name | Actual      | Predicted | Deal|
|-----| ----------- | ----------- |----|
|Church| 3.99      | 3.96      | Fair deal|
|Hudgins| .97      | 1.649       | Good deal|
|Mathews| 3.475   | 3.076      | Bad deal |
|Mobjack| 2.890   | 3.092        | Good deal|
|Moon| 2.500  | 1.578        | Bad deal|
|New Pt. Comfort| 2.290   | 2.667   |Good deal|

Include at least three plots that support your project report

Stretch goal: add a spatial variable to your feature set and compare with the original model. Did this improve the predictive power of your model? If so, how?
* spatial variable could be zip code? 

