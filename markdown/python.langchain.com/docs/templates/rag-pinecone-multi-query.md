

Skip to main content

On this page

# rag-pinecone-multi-query

This template performs RAG using Pinecone and OpenAI with a multi-query retriever.

It uses an LLM to generate multiple queries from different perspectives based on the user's input query.

For each query, it retrieves a set of relevant documents and takes the unique union across all queries for answer synthesis.

## Environment Setup​

This template uses Pinecone as a vectorstore and requires that `PINECONE_API_KEY`, `PINECONE_ENVIRONMENT`, and `PINECONE_INDEX` are set.

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

## Usage​

To use this package, you should first install the LangChain CLI:

[code]
```python




    pip install -U langchain-cli  
    


```
[/code]


To create a new LangChain project and install this package, do:

[code]
```python




    langchain app new my-app --package rag-pinecone-multi-query  
    


```
[/code]


To add this package to an existing project, run:

[code]
```python




    langchain app add rag-pinecone-multi-query  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_pinecone_multi_query import chain as rag_pinecone_multi_query_chain  
      
    add_routes(app, rag_pinecone_multi_query_chain, path="/rag-pinecone-multi-query")  
    


```
[/code]


(Optional) Now, let's configure LangSmith. LangSmith will help us trace, monitor, and debug LangChain applications. LangSmith is currently in private beta, you can sign up here. If you don't have
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


This will start the FastAPI app with a server running locally at http://localhost:8000

You can see all templates at http://127.0.0.1:8000/docs You can access the playground at http://127.0.0.1:8000/rag-pinecone-multi-query/playground

To access the template from code, use:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-pinecone-multi-query")  
    


```
[/code]


