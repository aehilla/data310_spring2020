### Responses/ Notes using the script from class March 26 - April 9

LULC raster stacking:

```
names(lulc)[c(1,10:13)] <- c("water","topo","slope", "ntl", "pop19")

lulc_adm3 <- exact_extract(lulc, phlshp3, fun=c('sum', 'mean'))
```

successfully creates raster stack

#### April 2 script:

goal: creating "diamonds" model

notes:

diamonds model set up is successful

```
final_model <- fit(lr_workflow, data)  
# this throws the following error:

>Error in lm.fit(x, y, offset = offset, singular.ok = singular.ok, ...) : 
  NA/NaN/Inf in 'y'
>Timing stopped at: 0.06 0 0.07
```

Not sure why I can't fit the created model on the data

Workaround #1:

```
final_model <- fit(lr_workflow, na.omit(data))
```

The error from the original line of code suggests that there may be NA values present in the data, but na.omit does not resolve the error.
