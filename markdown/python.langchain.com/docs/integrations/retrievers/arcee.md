

Skip to main content

On this page

# Arcee Retriever

This notebook demonstrates how to use the `ArceeRetriever` class to retrieve relevant document(s) for Arcee's Domain Adapted Language Models (DALMs).

### Setup​

Before using `ArceeRetriever`, make sure the Arcee API key is set as `ARCEE_API_KEY` environment variable. You can also pass the api key as a named parameter.

[code]
```python




    from langchain.retrievers import ArceeRetriever  
      
    retriever = ArceeRetriever(  
        model="DALM-PubMed",  
        # arcee_api_key="ARCEE-API-KEY" # if not already set in the environment  
    )  
    


```
[/code]


### Additional Configuration​

You can also configure `ArceeRetriever`'s parameters such as `arcee_api_url`, `arcee_app_url`, and `model_kwargs` as needed. Setting the `model_kwargs` at the object initialization uses the filters
and size as default for all the subsequent retrievals.

[code]
```python




    retriever = ArceeRetriever(  
        model="DALM-PubMed",  
        # arcee_api_key="ARCEE-API-KEY", # if not already set in the environment  
        arcee_api_url="https://custom-api.arcee.ai",  # default is https://api.arcee.ai  
        arcee_app_url="https://custom-app.arcee.ai",  # default is https://app.arcee.ai  
        model_kwargs={  
            "size": 5,  
            "filters": [  
                {  
                    "field_name": "document",  
                    "filter_type": "fuzzy_search",  
                    "value": "Einstein",  
                }  
            ],  
        },  
    )  
    


```
[/code]


### Retrieving documents​

You can retrieve relevant documents from uploaded contexts by providing a query. Here's an example:

[code]
```python




    query = "Can AI-driven music therapy contribute to the rehabilitation of patients with disorders of consciousness?"  
    documents = retriever.get_relevant_documents(query=query)  
    


```
[/code]


### Additional parameters​

Arcee allows you to apply `filters` and set the `size` (in terms of count) of retrieved document(s). Filters help narrow down the results. Here's how to use these parameters:

[code]
```python




    # Define filters  
    filters = [  
        {"field_name": "document", "filter_type": "fuzzy_search", "value": "Music"},  
        {"field_name": "year", "filter_type": "strict_search", "value": "1905"},  
    ]  
      
    # Retrieve documents with filters and size params  
    documents = retriever.get_relevant_documents(query=query, size=5, filters=filters)  
    


```
[/code]


