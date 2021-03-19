## Informal responses from March 10

#### Import the households dataset for your selected country and create a data frame with a variable that describes each of the following: household ID, unit, weights, location, size, gender, age, education, wealth

output:

<img style="float: right;" src="march10hw_q1.png" width = 600/>

#### Pivot the persons columns within your households data to a long format in order to produce a similarly specified dataset that describes all persons residing within all households. Using this data frame describing all persons standardize, normalize and percentize your variables and visualize each post transformed dataset as a heatmap that illustrates the heterogeneity of the combination of patterns.

- pns dataframe:

<img style="float: right;" src="march10hw_q2.png" width = 300/>

- I scaled, normalized, and percentized the pns dataframe using the following code:
```
pnscopy = pns
pnscopy$size <- as.numeric(pnscopy$size)
pnscopy$gender <- as.numeric(pnscopy$gender)
pnscopy$age <- as.numeric(pnscopy$age)
pnscopy$edu <- as.numeric(pnscopy$edu)
pnscopy$wealth <- as.numeric(pnscopy$wealth)
pnscopy = scale(pnscopy)
pnscopy = normalize(pnscopy)
pnscopy = percentize(pnscopy)
```
which produced the following dataframe:

![image](https://user-images.githubusercontent.com/54942759/111726036-84112c80-883e-11eb-931f-ae4aa0f472c4.png)


- Heatmaps in progress, having issues with heatmaply
- Still can't get heatmaply to work, still getting the following error despite trying Caroline's workaround:

``` 
Error in hclustfun(dist) : must have n >= 2 objects to cluster
```
- I instead tried to create the heatmap of the raw data using the basic heatmap function in R:
``` 
pns_prep2 <- slice_sample(pnscopy, n = 1000, replace = FALSE)
pns_matrix2 <- data.matrix(pns_prep2)
pns_heatmap2 <- heatmap(pns_matrix2, Rowv=NA, Colv=NA,
                       col = cm.colors(256), scale="column", margins=c(5,10))
png(file = "./DHS/pns_heatmap2.png")
heatmap(pns_matrix2)  
dev.off() 
```
which produced the following plot:

![image](https://user-images.githubusercontent.com/54942759/111726158-c0dd2380-883e-11eb-8702-d2a65540ae82.png)

