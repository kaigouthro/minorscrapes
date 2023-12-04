

Skip to main content

On this page

# Google Vertex AI Search

Vertex AI Search (formerly known as Enterprise Search on Generative AI App Builder) is a part of the Vertex AI machine learning platform offered by Google Cloud.

Vertex AI Search lets organizations quickly build generative AI powered search engines for customers and employees. It's underpinned by a variety of Google Search technologies, including semantic
search, which helps deliver more relevant results than traditional keyword-based search techniques by using natural language processing and machine learning techniques to infer relationships within
the content and intent from the user’s query input. Vertex AI Search also benefits from Google’s expertise in understanding how users search and factors in content relevance to order displayed
results.

Vertex AI Search is available in the Google Cloud Console and via an API for enterprise workflow integration.

This notebook demonstrates how to configure Vertex AI Search and use the Vertex AI Search retriever. The Vertex AI Search retriever encapsulates the Python client library and uses it to access the
Search Service API.

## Install pre-requisites​

You need to install the `google-cloud-discoveryengine` package to use the Vertex AI Search retriever.

[code]
```python




    pip install google-cloud-discoveryengine  
    


```
[/code]


## Configure access to Google Cloud and Vertex AI Search​

Vertex AI Search is generally available without allowlist as of August 2023.

Before you can use the retriever, you need to complete the following steps:

### Create a search engine and populate an unstructured data store​

  * Follow the instructions in the Vertex AI Search Getting Started guide to set up a Google Cloud project and Vertex AI Search.
  * Use the Google Cloud Console to create an unstructured data store
    * Populate it with the example PDF documents from the `gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs` Cloud Storage folder.
    * Make sure to use the `Cloud Storage (without metadata)` option.

### Set credentials to access Vertex AI Search API​

The Vertex AI Search client libraries used by the Vertex AI Search retriever provide high-level language support for authenticating to Google Cloud programmatically. Client libraries support
Application Default Credentials (ADC); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make
credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code.

If running in Google Colab authenticate with `google.colab.google.auth` otherwise follow one of the supported methods to make sure that you Application Default Credentials are properly set.

[code]
```python




    import sys  
      
    if "google.colab" in sys.modules:  
        from google.colab import auth as google_auth  
      
        google_auth.authenticate_user()  
    


```
[/code]


## Configure and use the Vertex AI Search retriever​

The Vertex AI Search retriever is implemented in the `langchain.retriever.GoogleVertexAISearchRetriever` class. The `get_relevant_documents` method returns a list of `langchain.schema.Document`
documents where the `page_content` field of each document is populated the document content. Depending on the data type used in Vertex AI Search (website, structured or unstructured) the
`page_content` field is populated as follows:

  * Website with advanced indexing: an `extractive answer` that matches a query. The `metadata` field is populated with metadata (if any) of the document from which the segments or answers were extracted.
  * Unstructured data source: either an `extractive segment` or an `extractive answer` that matches a query. The `metadata` field is populated with metadata (if any) of the document from which the segments or answers were extracted.
  * Structured data source: a string json containing all the fields returned from the structured data source. The `metadata` field is populated with metadata (if any) of the document

### Extractive answers & extractive segments​

An extractive answer is verbatim text that is returned with each search result. It is extracted directly from the original document. Extractive answers are typically displayed near the top of web
pages to provide an end user with a brief answer that is contextually relevant to their query. Extractive answers are available for website and unstructured search.

An extractive segment is verbatim text that is returned with each search result. An extractive segment is usually more verbose than an extractive answer. Extractive segments can be displayed as an
answer to a query, and can be used to perform post-processing tasks and as input for large language models to generate answers or new text. Extractive segments are available for unstructured search.

For more information about extractive segments and extractive answers refer to product documentation.

NOTE: Extractive segments require the Enterprise edition features to be enabled.

When creating an instance of the retriever you can specify a number of parameters that control which data store to access and how a natural language query is processed, including configurations for
extractive answers and segments.

### The mandatory parameters are:​

  * `project_id` \- Your Google Cloud Project ID.
  * `location_id` \- The location of the data store.
    * `global` (default)
    * `us`
    * `eu`
  * `data_store_id` \- The ID of the data store you want to use.
    * Note: This was called `search_engine_id` in previous versions of the retriever.

The `project_id` and `data_store_id` parameters can be provided explicitly in the retriever's constructor or through the environment variables - `PROJECT_ID` and `DATA_STORE_ID`.

You can also configure a number of optional parameters, including:

  * `max_documents` \- The maximum number of documents used to provide extractive segments or extractive answers
  * `get_extractive_answers` \- By default, the retriever is configured to return extractive segments.
    * Set this field to `True` to return extractive answers. This is used only when `engine_data_type` set to `0` (unstructured)
  * `max_extractive_answer_count` \- The maximum number of extractive answers returned in each search result.
    * At most 5 answers will be returned. This is used only when `engine_data_type` set to `0` (unstructured).
  * `max_extractive_segment_count` \- The maximum number of extractive segments returned in each search result.
    * Currently one segment will be returned. This is used only when `engine_data_type` set to `0` (unstructured).
  * `filter` \- The filter expression for the search results based on the metadata associated with the documents in the data store.
  * `query_expansion_condition` \- Specification to determine under which conditions query expansion should occur.
    * `0` \- Unspecified query expansion condition. In this case, server behavior defaults to disabled.
    * `1` \- Disabled query expansion. Only the exact search query is used, even if SearchResponse.total_size is zero.
    * `2` \- Automatic query expansion built by the Search API.
  * `engine_data_type` \- Defines the Vertex AI Search data type
    * `0` \- Unstructured data
    * `1` \- Structured data
    * `2` \- Website data with Advanced Website Indexing

### Migration guide for `GoogleCloudEnterpriseSearchRetriever`​

In previous versions, this retriever was called `GoogleCloudEnterpriseSearchRetriever`. Some backwards-incompatible changes had to be made to the retriever after the General Availability launch due to
changes in the product behavior.

To update to the new retriever, make the following changes:

  * Change the import from: `from langchain.retrievers import GoogleCloudEnterpriseSearchRetriever` -> `from langchain.retrievers import GoogleVertexAISearchRetriever`.
  * Change all class references from `GoogleCloudEnterpriseSearchRetriever` -> `GoogleVertexAISearchRetriever`.
  * Upon class initialization, change the `search_engine_id` parameter name to `data_store_id`.

### Configure and use the retriever for **unstructured** data with extractive segments​

[code]
```python




    from langchain.retrievers import (  
        GoogleVertexAIMultiTurnSearchRetriever,  
        GoogleVertexAISearchRetriever,  
    )  
      
    PROJECT_ID = "<YOUR PROJECT ID>"  # Set to your Project ID  
    LOCATION_ID = "<YOUR LOCATION>"  # Set to your data store location  
    DATA_STORE_ID = "<YOUR DATA STORE ID>"  # Set to your data store ID  
    


```
[/code]


[code]
```python




    retriever = GoogleVertexAISearchRetriever(  
        project_id=PROJECT_ID,  
        location_id=LOCATION_ID,  
        data_store_id=DATA_STORE_ID,  
        max_documents=3,  
    )  
    


```
[/code]


[code]
```python




    query = "What are Alphabet's Other Bets?"  
      
    result = retriever.get_relevant_documents(query)  
    for doc in result:  
        print(doc)  
    


```
[/code]


### Configure and use the retriever for **unstructured** data with extractive answers​

[code]
```python




    retriever = GoogleVertexAISearchRetriever(  
        project_id=PROJECT_ID,  
        location_id=LOCATION_ID,  
        data_store_id=DATA_STORE_ID,  
        max_documents=3,  
        max_extractive_answer_count=3,  
        get_extractive_answers=True,  
    )  
      
    result = retriever.get_relevant_documents(query)  
    for doc in result:  
        print(doc)  
    


```
[/code]


### Configure and use the retriever for **structured** data​

[code]
```python




    retriever = GoogleVertexAISearchRetriever(  
        project_id=PROJECT_ID,  
        location_id=LOCATION_ID,  
        data_store_id=DATA_STORE_ID,  
        max_documents=3,  
        engine_data_type=1,  
    )  
      
    result = retriever.get_relevant_documents(query)  
    for doc in result:  
        print(doc)  
    


```
[/code]


### Configure and use the retriever for **website** data with Advanced Website Indexing​

[code]
```python




    retriever = GoogleVertexAISearchRetriever(  
        project_id=PROJECT_ID,  
        location_id=LOCATION_ID,  
        data_store_id=DATA_STORE_ID,  
        max_documents=3,  
        max_extractive_answer_count=3,  
        get_extractive_answers=True,  
        engine_data_type=2,  
    )  
      
    result = retriever.get_relevant_documents(query)  
    for doc in result:  
        print(doc)  
    


```
[/code]


### Configure and use the retriever for multi-turn search​

Search with follow-ups is based on generative AI models and it is different from the regular unstructured data search.

[code]
```python




    retriever = GoogleVertexAIMultiTurnSearchRetriever(  
        project_id=PROJECT_ID, location_id=LOCATION_ID, data_store_id=DATA_STORE_ID  
    )  
      
    result = retriever.get_relevant_documents(query)  
    for doc in result:  
        print(doc)  
    


```
[/code]


