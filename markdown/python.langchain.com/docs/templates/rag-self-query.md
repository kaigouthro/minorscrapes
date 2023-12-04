

Skip to main content

On this page

# rag-self-query

This template performs RAG using the self-query retrieval technique. The main idea is to let an LLM convert unstructured queries into structured queries. See the docs for more on how this works.

## Environment Setup​

In this template we'll use OpenAI models and an Elasticsearch vector store, but the approach generalizes to all LLMs/ChatModels and a number of vector stores.

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

To connect to your Elasticsearch instance, use the following environment variables:

[code]
```python




    export ELASTIC_CLOUD_ID = <ClOUD_ID>  
    export ELASTIC_USERNAME = <ClOUD_USERNAME>  
    export ELASTIC_PASSWORD = <ClOUD_PASSWORD>  
    


```
[/code]


For local development with Docker, use:

[code]
```python




    export ES_URL = "http://localhost:9200"  
    docker run -p 9200:9200 -e "discovery.type=single-node" -e "xpack.security.enabled=false" -e "xpack.security.http.ssl.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:8.9.0  
    


```
[/code]


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




    langchain app new my-app --package rag-self-query  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-self-query  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_self_query import chain  
      
    add_routes(app, chain, path="/rag-elasticsearch")  
    


```
[/code]


To populate the vector store with the sample data, from the root of the directory run:

[code]
```python




    python ingest.py  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-elasticsearch/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-self-query")  
    


```
[/code]


