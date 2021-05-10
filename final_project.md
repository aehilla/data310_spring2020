### Final Project: Urban Change and Air Temperature in the Solomon Islands

### Final Project Research Plan 

##### Due May 12

###### Research Question

> What is the effect of urban sprawl on air temperature in the Solomon Islands?

> I chose the Solomon Islands because I wanted to examine a country that was urbanizing rapidly, but which was not too large and difficult to analyze.
Uganda has the fastest urbanization rate of any country currently, with an urbanization rate of 5.7% as of 2020.
However, Uganda is very large and populous, with 45 million people across 236,040 square kilometers.
The Solomon Islands have a much more managable geographic size and population, with just 652,857 people across 28,400 square kilometers.
However, it still has a very high urbanization rate of 3.91%, putting it in the top 30 fastest urbanizing countries, 
and its rising economic potential is often overlooked due to its small size. 

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

> For my initial model, I used a simple Support Vector Machine model to assess the impact of the urban change data
on the air temperature measurements in each administrative zone. This was a very basic model and did not have a high level of 
accuracy:

<img src = "https://user-images.githubusercontent.com/54942759/117668652-24ffd200-b174-11eb-87ff-2d8048e84ce9.png" width = 500>

<img src = "https://user-images.githubusercontent.com/54942759/117668763-41037380-b174-11eb-8adc-f659354141df.png" width = 250>

> I tried to improve the model by 

###### Conclusion

Conclude with a section that preliminarily assesses model performance. 
If you have results from your implementation, you are welcome to add those in this section. 
Compare your preliminary results with those from the literature on your topic for a comparative assessment.
If you are not able to produce preliminary results, provide a cursory literature review that includes 2 sources that present and describes their validation.
With more time and project support, estimate what an ideal outcome looks like in terms of model validation.
