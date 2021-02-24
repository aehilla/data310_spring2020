## Project 1 write-up
### to be turned in March 3

Select a city and scrape as many observations as possible from zillow. Try to obtain at least 400 observations from your selected location.

* Selected location: Jacksonville, FL

Clean the housing data you obtained and create a number of usable features (independent variables) and targets (dependent variables). Set price as the response variable, and then set numbers of beds, number of bathrooms and total square footage as the predictors. Following the previous model you specified (6 houses in Mathews), import your new data set and train a new model on your target and features. Write a one and a half to two page report on your results and include the following:

A description of the housing data you scraped from zillow
* I initially scraped 400 observations, but 8 observations failed to scrape the square footage from the website and were dropped, so the data I used in the model ultimately contained 392 observations. 
* descriptive statistics:
    * mean home price: $285,009
    * max home price: $3,692,000
    * min home price: $12,900
    * mean number of bathrooms: 2.5
    * mean number of bedrooms: 3.5
    * mean square footage: 1988 sq. ft.
    * max square footage: 3621 sq. ft.
    * min square footage: 989 sq. ft.

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

