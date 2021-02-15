### Extra Credit: Reflection on Slice of Data Science, Feb 11

Presentation by Caleb Robinson from Microsoft AI for Good Research Lab

Caleb began his talk by telling us about the AI for Good lab and what they work on. 
The lab has 5 pillars: Earth, Health, Accessibility, Humanitarian Action, and Cultural Heritage. 
Caleb's project is under the Earth pillar and focuses on land cover mapping. His team's goal 
was to classify land cover categories for high resolution satellite imagery at 1 meter 
resolution for the entire US. The high res satellite imagery existed but had not been 
classified. Semi-manual labeling would have been expensive, so doing the land cover mapping 
with ML is more affordable and scalable. Caleb's team trained a convolutional neural net 
to make predictions on the 1 meter imagery using a 1 meter resolution Chesapeake Bay manually labeled map plus 
lower resolution labeled imagery from the rest of the country. They successfully created the first US wide 
1m resolution land cover map. 

The process that Caleb's team used of training on the Chesapeake Bay land cover map 
and then training on the low res imagery to classify the high res input is called "transfer learning." 
He explained it as a workflow with the following steps: 

1. original model is trained on the rich dataset 
2. semantic segmentation 
3. pixel embedding 
4. linear model

The transfer step is to throw away 
the previous linear model, freeze the weights of the main network, and then retrain a new 
linear model for the new task (in this case, classifying land cover for the high res imagery). 

I was really interested in his explanation of transfer learning. In my opinion, this seems like 
a strategy that could have a lot of applications beyond land cover mapping. Being able to classify 
datasets based on more narrow labeled data sets plus broader unlabeled datasets would be 
useful in any case where highly granular, widespread data is newly available and needs to be classified. 
For example, I think this could be useful in applications such as mapping wildfires. Increasingly 
common wildfires in places like Australia and California have meant that more attention is being given 
to the issue and higher resolution imagery of the fires is being produced. Using the transfer 
learning process to help categorize what parts of the land area are burning at a higher resolution 
could be extremely important during future fire seasons. 
