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

> Its performance is very similar, and the mean ROC AUC values are quite similar (.613 as compared to .611 in the model I chose for logistic regression). The highest AUC value for Model 2 is slightly higher than the highest AUC value for Model 1, so Model 2 is slightly better. However, the difference are so small that I do think it's hard to make a case that this model is *significantly* better than model 1. 

Provide your ROC plots and interpret them. 
 
<img src="https://user-images.githubusercontent.com/54942759/111839014-86bc6200-88d0-11eb-8ef1-87d20a4c929f.png" width = 300/>

> these ROC plots are very similar to the plots produced by the penalized logistic regression. Although the evaluation metrics tell us that the AUC is slightly higher, it is very difficult to see that in the plots, because the AUC values are so close. In general, the main takeaway from these plots, as compared to the plots from model 1, is that both models performed similarly, especially in the fact that both models were relatively good at differentiating the poorest and the wealthiest (plots 1 and 5) from the general population, but were relatively bad at differentiating the middle income categories (plots 2, 3, and 4) from the general population. 

Are you able to provide a plot that supports the relative importance of each feature's contribution towards the predictive power of your random forest ensemble model?

<img src="https://user-images.githubusercontent.com/54942759/111839340-0813f480-88d1-11eb-9a32-61d9f618506c.png" width = 500/>


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

> Predicted probabilities plot for logistic regression

<img src="https://user-images.githubusercontent.com/54942759/111887689-19323380-89ad-11eb-8016-b51da6cd1bc8.png" width = 400/>

> These plots show that the predicted probabilities were mainly clustered at the lower end of the values. This suggests that the model may have over-predicted for the lower range of values, and under-predicted for higher values.
> The ROC plot shows that the model performed better than random chance. The evaluation metrics show that the model has an AUC of .74, which is not terrible, although it is closer to .50 than to 1, so in my opinion this model is not a lot better than random chance, but it is slightly better. 


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

> These plots show that this model also performed better than random chance. This ROC curve is extremely similar to model 3, although the slopes are slightly different, and the AUC of model 4 is slightly higher (.76 compared to .74). .76 is not a terrible AUC but it does seem like if the goal is to get as close to 1 as possible, then .76 is not *that* good.


#### Analyze all four models 

According to the evaluation metrics, which model produced the best results? 

> Model 4, the gradient boosting model using decision trees, performed the best, with an AUC of 0.760543. 

Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?

> It seems like each model consistently performed better at predicting the lowest and highest wealth outcomes, but performed worse at predicting the middle wealth outcomes. In other words, the models perfomed better at the extremes. If I had to guess, I would assume this might be because the characteristics that define the individuals in the lowest and highest wealth categories are probably more distinct than the characteristics of individuals who fall somewhere in the middle. This discrepancy in performance suggests that the Philippines may have very high income inequality, given that the lowest and highest income brackets seem to be so far from the middle brackets.
