

Skip to main content

On this page

# DocArray

> DocArray is a library for nested, unstructured, multimodal data in transit, including text, image, audio, video, 3D mesh, etc. It allows deep-learning engineers to efficiently process, embed,
> search, recommend, store, and transfer multimodal data with a Pythonic API.

## Installation and Setup​

We need to install `docarray` python package.

[code]
```python




    pip install docarray  
    


```
[/code]


## Vector Store​

LangChain provides an access to the `In-memory` and `HNSW` vector stores from the `DocArray` library.

See a usage example.

[code]
```python




    from langchain.vectorstores DocArrayHnswSearch  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.vectorstores DocArrayInMemorySearch  
    


```
[/code]


