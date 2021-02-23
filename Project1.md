## Project 1 write-up
### to be turned in March 3

Initial issues:

* In the original zillow_scrape.py file provided, everything runs up to and including line `df1.to_csv('out.csv', index=False)` 
The first line after that, `zillow_zestimate = []` will run, but the for loop does not:

```
for link in df1['links']:
    r = s.get(link, headers=req_headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    home_value = soup.select_one('h4:contains("Home value")')
    if not home_value:
        home_value = soup.select_one('.zestimate').text.split()[-1]
    else:
        home_value = home_value.find_next('p').get_text(strip=True)
    zillow_zestimate.append(home_value)
```

When I try running each line outside of a for loop, `s.get(link, headers=req_headers)` does not work because the links contain html still and therefore requests cannot access the info at the links' site. When I test on just the first link and fix it using 
```
link = df1['links'][0]
link = link.replace('<aclass="list-card-linklist-card-link-top-margin"href="','')
```
then  `s.get(link, headers=req_headers)` works. But when I try to fix all the links, using `df1['links'] = df1.links.replace('<aclass="list-card-linklist-card-link-top-margin"href="','')` it does not work, for some reason. 

* wait now if I use `df1['links'] = df1['links'].str.replace(replacement,'')` it does what I want it to


Select a city and scrape as many observations as possible from zillow. Try to obtain at least 400 observations from your selected location.

* Selected location: Asheville

Clean the housing data you obtained and create a number of usable features (independent variables) and targets (dependent variables). Set price as the response variable, and then set numbers of beds, number of bathrooms and total square footage as the predictors. Following the previous model you specified (6 houses in Mathews), import your new data set and train a new model on your target and features. Write a one and a half to two page report on your results and include the following:

A description of the housing data you scraped from zillow
* response
* descriptive statistics plot

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

