

Skip to main content

On this page

# Hybrid Search in Weaviate

This template shows you how to use the hybrid search feature in Weaviate. Hybrid search combines multiple search algorithms to improve the accuracy and relevance of search results.

Weaviate uses both sparse and dense vectors to represent the meaning and context of search queries and documents. The results use a combination of `bm25` and vector search ranking to return the top
results.

## Configurations​

Connect to your hosted Weaviate Vectorstore by setting a few env variables in `chain.py`:

  * `WEAVIATE_ENVIRONMENT`
  * `WEAVIATE_API_KEY`

You will also need to set your `OPENAI_API_KEY` to use the OpenAI models.

## Get Started​

To use this package, you should first have the LangChain CLI installed:

[code]
```python




    pip install -U langchain-cli  
    


```
[/code]


To create a new LangChain project and install this as the only package, you can do:

[code]
```python




    langchain app new my-app --package hybrid-search-weaviate  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add hybrid-search-weaviate  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from hybrid_search_weaviate import chain as hybrid_search_weaviate_chain  
      
    add_routes(app, hybrid_search_weaviate_chain, path="/hybrid-search-weaviate")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/hybrid-search-weaviate/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/hybrid-search-weaviate")  
    


```
[/code]


