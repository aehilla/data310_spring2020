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
