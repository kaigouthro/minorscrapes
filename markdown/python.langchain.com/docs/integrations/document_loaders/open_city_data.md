

Skip to main content

# Open City Data

Socrata provides an API for city open data.

For a dataset such as SF crime, to to the `API` tab on top right.

That provides you with the `dataset identifier`.

Use the dataset identifier to grab specific tables for a given city_id (`data.sfgov.org`) -

E.g., `vw6y-z8j6` for SF 311 data.

E.g., `tmnf-yvry` for SF Police data.

```python




    pip install sodapy



```


```python




    from langchain.document_loaders import OpenCityDataLoader



```


```python




    dataset = "vw6y-z8j6"  # 311 data
    dataset = "tmnf-yvry"  # crime data
    loader = OpenCityDataLoader(city_id="data.sfgov.org", dataset_id=dataset, limit=2000)



```


```python




    docs = loader.load()



```


```python




        WARNING:root:Requests made without an app_token will be subject to strict throttling limits.



```


```python




    eval(docs[0].page_content)



```


```python




        {'pdid': '4133422003074',
         'incidntnum': '041334220',
         'incident_code': '03074',
         'category': 'ROBBERY',
         'descript': 'ROBBERY, BODILY FORCE',
         'dayofweek': 'Monday',
         'date': '2004-11-22T00:00:00.000',
         'time': '17:50',
         'pddistrict': 'INGLESIDE',
         'resolution': 'NONE',
         'address': 'GENEVA AV / SANTOS ST',
         'x': '-122.420084075249',
         'y': '37.7083109744362',
         'location': {'type': 'Point',
          'coordinates': [-122.420084075249, 37.7083109744362]},
         ':@computed_region_26cr_cadq': '9',
         ':@computed_region_rxqg_mtj9': '8',
         ':@computed_region_bh8s_q3mv': '309'}



```
