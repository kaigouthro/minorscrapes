

Skip to main content

On this page

# rag-astradb

This template will perform RAG using Astra DB (`AstraDB` vector store class)

## Environment Setup​

An Astra DB database is required; free tier is fine.

  * You need the database **API endpoint** (such as `https://0123...-us-east1.apps.astra.datastax.com`) ...
  * ... and a **token** (`AstraCS:...`).

Also, an **OpenAI API Key** is required. _Note that out-of-the-box this demo supports OpenAI only, unless you tinker with the code._

Provide the connection parameters and secrets through environment variables. Please refer to `.env.template` for the variable names.

## Usage​

To use this package, you should first have the LangChain CLI installed:

[code]
```python




    pip install -U "langchain-cli[serve]"  
    


```
[/code]


To create a new LangChain project and install this as the only package, you can do:

[code]
```python




    langchain app new my-app --package rag-astradb  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-astradb  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from astradb_entomology_rag import chain as astradb_entomology_rag_chain  
      
    add_routes(app, astradb_entomology_rag_chain, path="/rag-astradb")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-astradb/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-astradb")  
    


```
[/code]


## Reference​

Stand-alone repo with LangServe chain: here.

