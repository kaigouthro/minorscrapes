

Skip to main content

On this page

# rag-matching-engine

This template performs RAG using Google Cloud Platform's Vertex AI with the matching engine.

It will utilize a previously created index to retrieve relevant documents or contexts based on user-provided questions.

## Environment Setup​

An index should be created before running the code.

The process to create this index can be found here.

Environment variables for Vertex should be set:

[code]
```python




    PROJECT_ID  
    ME_REGION  
    GCS_BUCKET  
    ME_INDEX_ID  
    ME_ENDPOINT_ID  
    


```
[/code]


## Usage​

To use this package, you should first have the LangChain CLI installed:

[code]
```python




    pip install -U langchain-cli  
    


```
[/code]


To create a new LangChain project and install this as the only package, you can do:

[code]
```python




    langchain app new my-app --package rag-matching-engine  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-matching-engine  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_matching_engine import chain as rag_matching_engine_chain  
      
    add_routes(app, rag_matching_engine_chain, path="/rag-matching-engine")  
    


```
[/code]


(Optional) Let's now configure LangSmith. LangSmith will help us trace, monitor and debug LangChain applications. LangSmith is currently in private beta, you can sign up here. If you don't have
access, you can skip this section

[code]
```python




    export LANGCHAIN_TRACING_V2=true  
    export LANGCHAIN_API_KEY=<your-api-key>  
    export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"  
    


```
[/code]


If you are inside this directory, then you can spin up a LangServe instance directly by:

[code]
```python




    langchain serve  
    


```
[/code]


This will start the FastAPI app with a server is running locally at http://localhost:8000

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-matching-engine/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-matching-engine")  
    


```
[/code]


For more details on how to connect to the template, refer to the Jupyter notebook `rag_matching_engine`.

