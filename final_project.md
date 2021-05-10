### Final Project: Urban Change and Air Temperature in the Solomon Islands

##### Due May 12

###### Research Question

> What is the effect of urban sprawl on air temperature in the Solomon Islands?

> I chose the Solomon Islands because I wanted to examine a country that was urbanizing rapidly, but which was not too large and difficult to analyze.
Uganda has the fastest urbanization rate of any country currently, with an urbanization rate of 5.7% as of 2020.
However, Uganda is very large and populous, with 45 million people across 236,040 square kilometers.
The Solomon Islands have a much more managable geographic size and population, with just 652,857 people across 28,400 square kilometers.
However, it still has a very high urbanization rate and is in the top 30 fastest urbanizing countries, 
and its rising economic potential is often overlooked due to its small size. 

"Although 80% of the population live in rural areas, the Solomon Islands is considered to be one of the world’s fastest urbanizing countries, with an annual urban growth rate of 4.7 percent." - U.N Habitat for a Better Urban Future

> Understanding the effect of urban sprawl on temperatures is important for understanding the impact of human development on environmental factors. 
The Solomon Islands are urbanizing quickly but but their economy relies heavily on subsistence agriculture and their growing tourism industry. It is crucial to understand the consequences that urbanization may have, 
because increasing temperatures could hurt the natural environment and potentially harm both the agricultural and tourism sectors. By examining whether the urban change variable 
is having an effect on temperature, it can be determined whether the Solomon Islands needs to prepare for environmental consequences of urbanization in their key industries.


###### Data 

> The data I will be utilizing for this project is the Worldpop Urban Change dataset for the Solomon Islands, using the Estimated persons
per grid square feature as the independent variable, which is continuous geographic data from 2000 and 2010.
I will be using the World Bank air temperature data, using  air Temperature at 2 m above ground level in °C as the dependent variable,
which is also continuous geographic data. The urban change dataset was collected via land cover mapping. The air temperature data is modeled from 
metereological station measurements. I will be using the GeoBoundaries administrative boundaries shapefiles to split the geographic data 
based on ADM3 zones. 

Data sources:

- [Air temperature (from World Bank Group/ESMAP/Solargis)](https://www.kaggle.com/cathetorres/geospatial-environmental-and-socioeconomic-data)
    - Description: A GeoTIFF layer with the air Temperature at 2 m above ground level in °C (TEMP). Data layers are provided in a geographic spatial reference (EPSG:4326). The resolution (pixel size) of TEMP is 30 arcsec (nominally 1 km). 

- [Worldpop Urban Change 100m Resolution](https://www.worldpop.org/geodata/summary?id=1240)
    - Alpha version 2000 and 2010 estimates of numbers of people per grid square, with national totals adjusted to match UN population division estimates (http://esa.un.org/wpp/) and MODIS-derived urban extent change built in.
    
- [GeoBoundaries Subnational Administrative Boundaries](https://www.geoboundaries.org/data/geoBoundaries-3_0_0/SLB/)
    - ADM0 and ADM3 shapefiles

###### Machine Learning Model

Provide the specification for your applied machine learning method that presented the most promise in providing a solution to your problem.
Include the section from your python or R script that specifies your model architecture, layers, functional arguments and specifications for
compiling and fitting. Provide a brief description of how you implemented your code in practice.

> First I split the geospatial data into 183 observations, based on the ADM3 zones:
> <img src = "https://user-images.githubusercontent.com/54942759/117668139-a2771280-b173-11eb-9f09-19a566e03fc5.png" width = 500>

> Then I used a similar strategy from our DHS project, by stacking the urban change and air temperature rasters, cropping to the extent of the ADM0 boundary, and using exact_extract to obtain the sum in each ADM3 zone:

```
sol_adm0 <- read_sf("SLB_ADM0_fixedInternalTopology.shp")
sol_adm3 <- read_sf("SLB_ADM3_fixedInternalTopology.shp")

urbchg <- raster("./Solomon_Islands_100m_Urban_change/SLB10urbchg.tif") # 2010 urban change raster 
temp <- raster("temperature.tif")

temp_adm0 <- crop(temp, sol_adm0)
temp_adm0 <- mask(temp_adm0, sol_adm0)
urbchg_adm0 <- crop(urbchg, sol_adm0)
urbchg_adm0 <- mask(urbchg_adm0, sol_adm0)

urbchgResamp <- resample(urbchg_adm0, temp_adm0, resample='bilinear')

stacked <- stack(temp_adm0, urbchgResamp)

temp_adm3 <- exact_extract(temp, sol_adm3, fun=c('sum', 'mean'))
urbchg_adm3 <- exact_extract(urbchg, sol_adm3, fun=c('sum', 'mean'))

stackadm3 <- exact_extract(stacked, sol_adm3, fun=c('sum', 'mean'))
```

> For my initial model, I used a simple Support Vector Machine model to assess the impact of the urban change data (X)
on the air temperature measurements (Y) in each administrative zone. This was a very basic model and did not have a high level of 
accuracy:

```
> modelSvmRRB
Support Vector Machines with Radial Basis Function Kernel 

147 samples
  1 predictor

Pre-processing: scaled (1), Yeo-Johnson transformation (1) 
Resampling: Cross-Validated (5 fold, repeated 5 times) 
Summary of sample sizes: 118, 118, 117, 118, 117, 119, ... 
Resampling results:

  RMSE      Rsquared    MAE      
  0.220309  0.08397746  0.1664855

Tuning parameter 'sigma' was held constant at a value of
 0.025
Tuning parameter 'C' was held constant at a value of 2
```

SVM Radial Predicted Test plot:

<img src = "https://user-images.githubusercontent.com/54942759/117668763-41037380-b174-11eb-8adc-f659354141df.png" width = 250>

> I tried to improve the model by using a Linear kernel instead and using a tuning parameter of 1, which did slightly increase the R-squared and decreased the mean absolute error and RMSE:

```
> svm_Linear
Support Vector Machines with Linear Kernel 

147 samples
  1 predictor

Pre-processing: centered (1), scaled (1) 
Resampling: Cross-Validated (10 fold, repeated 3 times) 
Summary of sample sizes: 132, 132, 132, 132, 132, 133, ... 
Resampling results:

  RMSE       Rsquared   MAE      
  0.1434152  0.1057846  0.1065911

Tuning parameter 'C' was held constant at a value of 1
```

SVM Linear Predicted Test plot:

<img src = "https://user-images.githubusercontent.com/54942759/117677432-714f1000-b17c-11eb-96b3-96bb5586f94b.png" width = 250>




###### Conclusion

Conclude with a section that preliminarily assesses model performance. 
If you have results from your implementation, you are welcome to add those in this section. 
Compare your preliminary results with those from the literature on your topic for a comparative assessment.
If you are not able to produce preliminary results, provide a cursory literature review that includes 2 sources that present and describes their validation.
With more time and project support, estimate what an ideal outcome looks like in terms of model validation.

- My model is pretty weak and does not have much predictive power. The R-squared of the SVM linear model is only 0.10, suggesting that the correlation between the variables is weak. Prior literature on the relationship between urbanization and temperature suggests that there is a linear relationship between these variables. This is line with my models' performance showing that the Linear SVM model performs slightly better than the radial SVM model. I think my model could be improved by having a wider time frame of data - e.g. looking at the effects of urbanization over a span of several decades.

Literature on urbanization and surface temperature:

- Arulbajaji et al. (2020) find that increases in urbanization and urban land cover (and decreases in vegetation cover) correspond significantly with 
increases in land surface temperature. 
    - "The study revealed a marked decrease in vegetation cover (125–71 km2) and barren land (7–4 km2) in the area during 1988–2019. The built-up area showed a marked increase from 10 to 68 km2. It was noticed that the average LST has been increased from 26.5 °C to 28.1 °C during the study period."
    - Arulbalaji, P., Padmalal, D. & Maya, K. Impact of urbanization and land surface temperature changes in a coastal town in Kerala, India. Environ Earth Sci 79, 400 (2020). https://doi.org/10.1007/s12665-020-09120-1

- Yuan & Bauer (2007) similarly find that decreased vegetation and increased impervious surface cover (e.g. urban sprawl) linearly correlated with higher land surface temperature. 
    - "Our analysis indicates there is a strong linear relationship between LST (land surface temperature) and percent impervious surface for all seasons"
    - Yuan, Fei & Bauer, Marvin. Comparison of impervious surface area and normalized difference vegetation index as indicators of surface urban heat island effects in Landsat imagery. Remote Sensing of Environment, 106, 375-386 (2007). https://doi.org/10.1016/j.rse.2006.09.003. 

