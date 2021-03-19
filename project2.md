## Project 2
### Due March 24

#### Model 1

Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce.
Which "top_model" performed the best (had the largest AUC)?

> This is the output produced by the top models:

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

> lr_best returns:

```
1 0.00108 roc_auc hand_till  0.611     1      NA Preprocessor1_Model11
```

> so this model was the "best"

> This is the output from the LR AUC plotting function:


<img src="https://user-images.githubusercontent.com/54942759/111728353-16b3ca80-8843-11eb-8f3c-37efb964a67b.png" width = 400/>


Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors?

> answer

Provide justification for your selected penalty value? 

> answer

Finally, provide your ROC plots and interpret them. 

> answer

How effective is your penalized logistic regression model at predicting each of the five wealth outcomes.

> answer

#### Model 2

Using the R script provided, set up your random forest model and 
produce the AUC - ROC values for the randomly selected predictors, 
and the minimal node size, again with wealth as the target. 

> answer

How did your random forest model fare when compared to the penalized logistic regression? 

> answer

Provide your ROC plots and interpret them. 

> answer

Are you able to provide a plot that supports the relative importance of each feature's contribution towards the predictive power of your random forest ensemble model?

> answer

#### Model 3

Using the python script provided, train a logistic regression model using the tensorflow estimator API and your DHS data, again with wealth as the target. 
Apply the linear classifier to the feature columns and determine the accuracy, AUC and other evaluative metrics towards each of the different wealth outcomes. 

> answer

Then continue with your linear classifier adding the derived feature columns you have selected in order to 
extend capturing combinations of correlations (instead of learning on single model weights for each outcome). 
Again produce your ROC curves and interpret the results.

> answer

#### Model 4

Using the python script provided, train a gradient boosting model using decision trees with the tensorflow estimator. 
Provide evaluative metrics including a measure of accuracy and AUC. 

> answer

Produce the predicted probabilities plot as well as the ROC curve for each wealth outcome and interpret these results.

> answer

#### Analyze all four models 

According to the evaluation metrics, which model produced the best results? 

> answer

Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?

> answer
