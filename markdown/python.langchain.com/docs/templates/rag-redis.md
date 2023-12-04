

Skip to main content

On this page

# rag-redis

This template performs RAG using Redis (vector database) and OpenAI (LLM) on financial 10k filings docs for Nike.

It relies on the sentence transformer `all-MiniLM-L6-v2` for embedding chunks of the pdf and user questions.

## Environment Setup​

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models:

[code]
```python




    export OPENAI_API_KEY= <YOUR OPENAI API KEY>  
    


```
[/code]


Set the following Redis environment variables:

[code]
```python




    export REDIS_HOST = <YOUR REDIS HOST>  
    export REDIS_PORT = <YOUR REDIS PORT>  
    export REDIS_USER = <YOUR REDIS USER NAME>  
    export REDIS_PASSWORD = <YOUR REDIS PASSWORD>  
    


```
[/code]


## Supported Settings​

We use a variety of environment variables to configure this application

Environment Variable| Description| Default Value  
---|---|---  
`DEBUG`| Enable or disable Langchain debugging logs| True  
`REDIS_HOST`| Hostname for the Redis server| "localhost"  
`REDIS_PORT`| Port for the Redis server| 6379  
`REDIS_USER`| User for the Redis server| ""  
`REDIS_PASSWORD`| Password for the Redis server| ""  
`REDIS_URL`| Full URL for connecting to Redis| `None`, Constructed from user, password, host, and port if not provided  
`INDEX_NAME`| Name of the vector index| "rag-redis"  
  
## Usage​

To use this package, you should first have the LangChain CLI and Pydantic installed in a Python virtual environment:

[code]
```python




    pip install -U langchain-cli pydantic==1.10.13  
    


```
[/code]


To create a new LangChain project and install this as the only package, you can do:

[code]
```python




    langchain app new my-app --package rag-redis  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-redis  
    


```
[/code]


And add the following code snippet to your `app/server.py` file:

[code]
```python




    from rag_redis.chain import chain as rag_redis_chain  
      
    add_routes(app, rag_redis_chain, path="/rag-redis")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-redis/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-redis")  
    


```
[/code]


