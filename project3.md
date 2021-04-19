## Project 3, due April 18

##### Using two machine learning methods predict population values at 100 x 100 meter resolution throughout your selected country. Validate the two models using different methods presented in this class. Write a report assessing the two approaches and which of the two models was more accurate. Be sure to account for spatial variation throughout your selected location and provide substantive explanations for why those variations occurred

For this project, I chose to focus on the Philippines, specifically the regions of Davao del Norte, Davao del Sur, Davao Oriental, and Compostela Valley. 

#### Linear Regression Model:

Population sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155197-cea7e380-a04c-11eb-8b24-c37e7a64b830.png" width = 500>

Diff sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155316-60afec00-a04d-11eb-97cf-5b10c4151c9b.png" width = 500>

Mean Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155055-1c701c00-a04c-11eb-99fc-c0d1576f873c.png" width = 500>

Mean Absolute Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155083-3f9acb80-a04c-11eb-8bfd-40336b084a56.png" width = 500>

Root Mean Squared Error (3D):

<img src = "https://user-images.githubusercontent.com/54942759/115155124-796bd200-a04c-11eb-94a5-027219608881.png" width = 500>

Cell stats (diff sums): 6016931

#### Random Forest Model:

Population sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155496-31e64580-a04e-11eb-89a3-de98fce34500.png" width=500>

Diff sums plot:

<img src = "https://user-images.githubusercontent.com/54942759/115155510-432f5200-a04e-11eb-9b3b-a6a733cc3608.png" width = 500>

Variable importance plot:

<img src="https://user-images.githubusercontent.com/54942759/115155539-7540b400-a04e-11eb-9b06-1d8270068b9c.png" width = 500>

RF Mean Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155701-0adc4380-a04f-11eb-8f4c-ae66898fcf44.png" width = 500>

RF Mean Absolute Error:

<img src = "https://user-images.githubusercontent.com/54942759/115155716-1c255000-a04f-11eb-9d75-4515fd32569d.png" width = 500>

RF Root Mean Squared Error (3D):

<img src="https://user-images.githubusercontent.com/54942759/115155656-f0a26580-a04e-11eb-984f-360f04dcc80c.png" width=500>

#### Stretch goal: Support Vector Machine model

Source: https://www.kaggle.com/thapelomola/svm-with-caret

For this model, I attempted to examine the effect of dependent variables on sum.pop15. Obviously this is a different approach than the linear regression and random forest models above because it does not incorporate the geospatial element. The R-squared for this model is 0.5085856, which is not terrible but not very good either. The RMSE is  0.0791883 and the MAE is 0.03668218. 

```
library(caret)
library(MLmetrics)
data_split <- initial_split(data, prop = 4/5)
data_train <- training(data_split)
data_test <- testing(data_split)

TrainCtrl1 <- trainControl(method = "repeatedcv", number = 5,repeats=5,verbose = FALSE)
set.seed(512) 
SVMgrid <- expand.grid(sigma = c(0.025), C = c(2))

X <- data_train[,-10]
X_scaled <- (X-min(X))/(max(X)-min(X))
Y <- data_train$sum.pop15 
Y_scaled <- (Y-min(Y))/(max(Y)-min(Y))
x_test <- data_test[,-10]
x_test_scaled <-(x_test-min(x_test))/(max(x_test)-min(x_test))
y_test <- data_test$sum.pop15 
y_test_scaled <- (y_test-min(y_test))/(max(y_test)-min(y_test))

modelSvmRRB <- train(X_scaled, Y_scaled, method="svmRadial", trControl=TrainCtrl1,tuneGrid = SVMgrid,preProc = c("scale","YeoJohnson"), verbose=FALSE)
PredictedTest <- predict(modelSvmRRB,x_test_scaled)
Accuracy(PredictedTest, y_test_scaled)
```

Output: 

 ```
 >>>modelSvmRRB
Support Vector Machines with Radial Basis Function Kernel 

741 samples
 12 predictor

Pre-processing: scaled (12), Yeo-Johnson transformation (12) 
Resampling: Cross-Validated (5 fold, repeated 5 times) 
Summary of sample sizes: 593, 593, 593, 592, 593, 593, ... 
Resampling results:

  RMSE        Rsquared   MAE       
  0.07918833  0.5085856  0.03668218

Tuning parameter 'sigma' was held constant at a value of 0.025
Tuning parameter 'C' was held constant at a value of 2
```






