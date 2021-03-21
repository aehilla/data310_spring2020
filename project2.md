## Project 2
### Due March 24

#### Model 1

Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce.

Which "top_model" performed the best (had the largest AUC)?

> This is the output produced by the top_models:

```     
    penalty .metric .estimator  mean     n   std_err .config              
      <dbl> <chr>   <chr>      <dbl> <int>   <dbl> <chr>                
 1 0.0001   roc_auc hand_till  0.611     1      NA Preprocessor1_Model01
 2 0.000127 roc_auc hand_till  0.611     1      NA Preprocessor1_Model02
 3 0.000161 roc_auc hand_till  0.611     1      NA Preprocessor1_Model03
 4 0.000204 roc_auc hand_till  0.611     1      NA Preprocessor1_Model04
 5 0.000259 roc_auc hand_till  0.611     1      NA Preprocessor1_Model05
 6 0.000329 roc_auc hand_till  0.611     1      NA Preprocessor1_Model06
 7 0.000418 roc_auc hand_till  0.611     1      NA Preprocessor1_Model07
 8 0.000530 roc_auc hand_till  0.611     1      NA Preprocessor1_Model08
 9 0.000672 roc_auc hand_till  0.611     1      NA Preprocessor1_Model09
10 0.000853 roc_auc hand_till  0.611     1      NA Preprocessor1_Model10
11 0.00108  roc_auc hand_till  0.611     1      NA Preprocessor1_Model11
12 0.00137  roc_auc hand_till  0.611     1      NA Preprocessor1_Model12
13 0.00174  roc_auc hand_till  0.611     1      NA Preprocessor1_Model13
14 0.00221  roc_auc hand_till  0.610     1      NA Preprocessor1_Model14
15 0.00281  roc_auc hand_till  0.609     1      NA Preprocessor1_Model15
```


Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors?

> Yes, I selected the penalty value from model 11, 0.00108, as the penalty. I think this did remove some irrelevant predictors. However, the AUC for model 11 was not significantly different from models 1 through 13, so I am unsure how much using the .00108 penalty improved the model as compared to the other options. 

Provide justification for your selected penalty value? 

> I selected the penalty value of 0.00108 because it fell in the middle of the range of penalty values in the 15 models created by the top_models. I ran all the different slices to look at the ROC plots and compare them. When n=15, there is not a huge difference between the models. However, I also tried running top_models with n= 30, and I then looked at the ROC plot for the 30th model (below). When I used slice(30), as you can see, the plots are all basically straight 45 degree lines. So in comparing the slices 1 through 15 to this plot, I found that slice 11 seemed like the plot had slightly bigger AUC than the other slices, although it is hard to be precise.

Finally, provide your ROC plots and interpret them. 

> The ROC plots created when n = 30 and I used the penalty from the 30th model:

<img src="https://user-images.githubusercontent.com/54942759/111836654-07795f00-88cd-11eb-960b-1458fbc75375.png" width = 400/>      

> This is the output from the LR AUC plotting function using 0.00108 (slice 11) as the penalty:

<img src="https://user-images.githubusercontent.com/54942759/111728353-16b3ca80-8843-11eb-8f3c-37efb964a67b.png" width = 400/>

> The difference between the penalty of slice 30 (first graph), where all the ROC plots are exactly 45 degree lines, and the output from slice 11 (second graph), shows that slice 11 is at least better at predicting the wealth outcomes than a model like model 30 where the predictions are essentially random. 

How effective is your penalized logistic regression model at predicting each of the five wealth outcomes.

> in this plot, it appears that the model is good at differentiating wealth categories 1 and 5 from the general population in the data, but the model is not good at all at differentiating 2 and 3. The performance for 4 is decent but not excellent. This suggests that the model could be significantly improved in terms of differentiating individuals in the middle wealth brackets.

#### Model 2

Using the R script provided, set up your random forest model and 
produce the AUC - ROC values for the randomly selected predictors, 
and the minimal node size, again with wealth as the target. 

```
  `0.000000` .metric .estimator  mean     n std_err .config              
       <int> <chr>   <chr>      <dbl> <int>   <dbl> <chr>                
1         39 roc_auc hand_till  0.613     1      NA Preprocessor1_Model07
2         37 roc_auc hand_till  0.612     1      NA Preprocessor1_Model06
3         36 roc_auc hand_till  0.612     1      NA Preprocessor1_Model13
4         35 roc_auc hand_till  0.612     1      NA Preprocessor1_Model14
5         34 roc_auc hand_till  0.611     1      NA Preprocessor1_Model15
```

<img src="https://user-images.githubusercontent.com/54942759/111838314-8c657800-88cf-11eb-90fb-e4180dc57db8.png" width = 300/>

How did your random forest model fare when compared to the penalized logistic regression? 

> Its performance is very similar, and the mean ROC AUC values are quite similar (.613, .612, and .611 as compared to .611 in the model I chose for logistic regression). 

Provide your ROC plots and interpret them. 
 
<img src="https://user-images.githubusercontent.com/54942759/111839014-86bc6200-88d0-11eb-8ef1-87d20a4c929f.png" width = 300/>

> these ROC plots are very similar to the plots produced by the penalized logistic regression

Are you able to provide a plot that supports the relative importance of each feature's contribution towards the predictive power of your random forest ensemble model?

<img src="https://user-images.githubusercontent.com/54942759/111839340-0813f480-88d1-11eb-9a32-61d9f618506c.png" width = 300/>


#### Model 3

Using the python script provided, train a logistic regression model using the tensorflow estimator API and your DHS data, again with wealth as the target. 
Apply the linear classifier to the feature columns and determine the accuracy, AUC and other evaluative metrics towards each of the different wealth outcomes. 

> Logistic regression evaluation metrics:

| metric | score |
|----------|-------------|
|accuracy          |        0.858338 |
|accuracy_baseline    |     0.858338 |
|auc       |                0.748549 |
|auc_precision_recall  |    0.304784|
|average_loss      |        0.354891|
|label/mean       |         0.141662|
|loss               |       0.354891|
|precision      |           0.000000|
|prediction/mean      |    0.155981|
|recall            |        0.000000|
|global_step        |     100.000000|


Then continue with your linear classifier adding the derived feature columns you have selected in order to 
extend capturing combinations of correlations (instead of learning on single model weights for each outcome). 
Again produce your ROC curves and interpret the results.

> ROC:

<img src="https://user-images.githubusercontent.com/54942759/111887849-2996de00-89ae-11eb-9f7a-b4e68d1cef5f.png" width=400/>

<img src="https://user-images.githubusercontent.com/54942759/111921040-d3d33c00-8a68-11eb-800c-7006ae18a4b1.png" width=400/>


> Predicted probabilities plot for logistic regression

<img src="https://user-images.githubusercontent.com/54942759/111887689-19323380-89ad-11eb-8016-b51da6cd1bc8.png" width = 400/>

> These plots show how 


#### Model 4

Using the python script provided, train a gradient boosting model using decision trees with the tensorflow estimator. 
Provide evaluative metrics including a measure of accuracy and AUC. 

> 
| metric | score |
|----------|-------------|
|accuracy      |            0.858456|
|accuracy_baseline    |     0.858338|
|auc          |             0.760543|
|auc_precision_recall  |    0.331856|
|average_loss   |           0.338022|
|label/mean     |           0.141662|
|loss            |          0.338022|
|precision       |          0.523810|
|prediction/mean       |   0.146739|
|recall       |             0.009213|
|global_step    |         100.000000|

Produce the predicted probabilities plot as well as the ROC curve for each wealth outcome and interpret these results.

> ROC:

<img src="https://user-images.githubusercontent.com/54942759/111887811-f2283180-89ad-11eb-8f93-2980073a0f50.png" width=400/>

> predicted probabilities:

<img src="https://user-images.githubusercontent.com/54942759/111887768-b4c3a400-89ad-11eb-9846-b983717602d7.png" width = 400/>

> These plots show how..


#### Analyze all four models 

According to the evaluation metrics, which model produced the best results? 

> answer

Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?

> answer
