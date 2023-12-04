

Skip to main content

On this page

# rag-ollama-multi-query

This template performs RAG using Ollama and OpenAI with a multi-query retriever.

The multi-query retriever is an example of query transformation, generating multiple queries from different perspectives based on the user's input query.

For each query, it retrieves a set of relevant documents and takes the unique union across all queries for answer synthesis.

We use a private, local LLM for the narrow task of query generation to avoid excessive calls to a larger LLM API.

See an example trace for Ollama LLM performing the query expansion here.

But we use OpenAI for the more challenging task of answer syntesis (full trace example here).

## Environment Setup​

To set up the environment, you need to download Ollama.

Follow the instructions here.

You can choose the desired LLM with Ollama.

This template uses `zephyr`, which can be accessed using `ollama pull zephyr`.

There are many other options available here.

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




    langchain app new my-app --package rag-ollama-multi-query  
    


```
[/code]


To add this package to an existing project, run:

[code]
```python




    langchain app add rag-ollama-multi-query  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_ollama_multi_query import chain as rag_ollama_multi_query_chain  
      
    add_routes(app, rag_ollama_multi_query_chain, path="/rag-ollama-multi-query")  
    


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

You can see all templates at http://127.0.0.1:8000/docs You can access the playground at http://127.0.0.1:8000/rag-ollama-multi-query/playground

To access the template from code, use:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-ollama-multi-query")  
    


```
[/code]


