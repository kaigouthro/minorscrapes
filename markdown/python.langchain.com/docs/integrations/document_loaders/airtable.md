

Skip to main content

# Airtable

[code]
```python




    pip install pyairtable  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import AirtableLoader  
    


```
[/code]


  * Get your API key here.
  * Get ID of your base here.
  * Get your table ID from the table url as shown here.

[code]
```python




    api_key = "xxx"  
    base_id = "xxx"  
    table_id = "xxx"  
    


```
[/code]


[code]
```python




    loader = AirtableLoader(api_key, table_id, base_id)  
    docs = loader.load()  
    


```
[/code]


Returns each table row as `dict`.

[code]
```python




    len(docs)  
    


```
[/code]


[code]
```python




        3  
    


```
[/code]


[code]
```python




    eval(docs[0].page_content)  
    


```
[/code]


[code]
```python




        {'id': 'recF3GbGZCuh9sXIQ',  
         'createdTime': '2023-06-09T04:47:21.000Z',  
         'fields': {'Priority': 'High',  
          'Status': 'In progress',  
          'Name': 'Document Splitters'}}  
    


```
[/code]


