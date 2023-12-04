

Skip to main content

On this page

# Metal

> Metal is a managed service for ML Embeddings.

This notebook shows how to use Metal's retriever.

First, you will need to sign up for Metal and get an API key. You can do so here

[code]
```python




    # !pip install metal_sdk  
    


```
[/code]


[code]
```python




    from metal_sdk.metal import Metal  
      
    API_KEY = ""  
    CLIENT_ID = ""  
    INDEX_ID = ""  
      
    metal = Metal(API_KEY, CLIENT_ID, INDEX_ID)  
    


```
[/code]


## Ingest Documents​

You only need to do this if you haven't already set up an index

[code]
```python




    metal.index({"text": "foo1"})  
    metal.index({"text": "foo"})  
    


```
[/code]


[code]
```python




        {'data': {'id': '642739aa7559b026b4430e42',  
          'text': 'foo',  
          'createdAt': '2023-03-31T19:51:06.748Z'}}  
    


```
[/code]


## Query​

Now that our index is set up, we can set up a retriever and start querying it.

[code]
```python




    from langchain.retrievers import MetalRetriever  
    


```
[/code]


[code]
```python




    retriever = MetalRetriever(metal, params={"limit": 2})  
    


```
[/code]


[code]
```python




    retriever.get_relevant_documents("foo1")  
    


```
[/code]


[code]
```python




        [Document(page_content='foo1', metadata={'dist': '1.19209289551e-07', 'id': '642739a17559b026b4430e40', 'createdAt': '2023-03-31T19:50:57.853Z'}),  
         Document(page_content='foo1', metadata={'dist': '4.05311584473e-06', 'id': '642738f67559b026b4430e3c', 'createdAt': '2023-03-31T19:48:06.769Z'})]  
    


```
[/code]


