

Skip to main content

On this page

# rag-singlestoredb

This template performs RAG using SingleStoreDB and OpenAI.

## Environment Setup​

This template uses SingleStoreDB as a vectorstore and requires that `SINGLESTOREDB_URL` is set. It should take the form `admin:password@svc-xxx.svc.singlestore.com:port/db_name`

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

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




    langchain app new my-app --package rag-singlestoredb  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-singlestoredb  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_singlestoredb import chain as rag_singlestoredb_chain  
      
    add_routes(app, rag_singlestoredb_chain, path="/rag-singlestoredb")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-singlestoredb/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-singlestoredb")  
    


```
[/code]


