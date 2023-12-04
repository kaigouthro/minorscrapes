

Skip to main content

On this page

# NucliaDB

You can use a local NucliaDB instance or use Nuclia Cloud.

When using a local instance, you need a Nuclia Understanding API key, so your texts are properly vectorized and indexed. You can get a key by creating a free account at https://nuclia.cloud, and then
create a NUA key.

[code]
```python




    #!pip install langchain nuclia  
    


```
[/code]


## Usage with nuclia.cloud​

[code]
```python




    from langchain.vectorstores.nucliadb import NucliaDB  
      
    API_KEY = "YOUR_API_KEY"  
      
    ndb = NucliaDB(knowledge_box="YOUR_KB_ID", local=False, api_key=API_KEY)  
    


```
[/code]


## Usage with a local instance​

Note: By default `backend` is set to `http://localhost:8080`.

[code]
```python




    from langchain.vectorstores.nucliadb import NucliaDB  
      
    ndb = NucliaDB(knowledge_box="YOUR_KB_ID", local=True, backend="http://my-local-server")  
    


```
[/code]


## Add and delete texts to your Knowledge Box​

[code]
```python




    ids = ndb.add_texts(["This is a new test", "This is a second test"])  
    


```
[/code]


[code]
```python




    ndb.delete(ids=ids)  
    


```
[/code]


## Search in your Knowledge Box​

[code]
```python




    results = ndb.similarity_search("Who was inspired by Ada Lovelace?")  
    print(res.page_content)  
    


```
[/code]


