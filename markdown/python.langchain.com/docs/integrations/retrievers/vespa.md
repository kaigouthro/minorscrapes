

Skip to main content

# Vespa

> Vespa is a fully featured search engine and vector database. It supports vector search (ANN), lexical search, and search in structured data, all in the same query.

This notebook shows how to use `Vespa.ai` as a LangChain retriever.

In order to create a retriever, we use pyvespa to create a connection a `Vespa` service.

[code]
```python




    #!pip install pyvespa  
    


```
[/code]


[code]
```python




    from vespa.application import Vespa  
      
    vespa_app = Vespa(url="https://doc-search.vespa.oath.cloud")  
    


```
[/code]


This creates a connection to a `Vespa` service, here the Vespa documentation search service. Using `pyvespa` package, you can also connect to a Vespa Cloud instance or a local Docker instance.

After connecting to the service, you can set up the retriever:

[code]
```python




    from langchain.retrievers.vespa_retriever import VespaRetriever  
      
    vespa_query_body = {  
        "yql": "select content from paragraph where userQuery()",  
        "hits": 5,  
        "ranking": "documentation",  
        "locale": "en-us",  
    }  
    vespa_content_field = "content"  
    retriever = VespaRetriever(vespa_app, vespa_query_body, vespa_content_field)  
    


```
[/code]


This sets up a LangChain retriever that fetches documents from the Vespa application. Here, up to 5 results are retrieved from the `content` field in the `paragraph` document type, using
`doumentation` as the ranking method. The `userQuery()` is replaced with the actual query passed from LangChain.

Please refer to the pyvespa documentation for more information.

Now you can return the results and continue using the results in LangChain.

[code]
```python




    retriever.get_relevant_documents("what is vespa?")  
    


```
[/code]


