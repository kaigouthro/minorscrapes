

Skip to main content

On this page

# rag-opensearch

This Template performs RAG using OpenSearch.

## Environment Setup​

Set the following environment variables.

  * `OPENAI_API_KEY` \- To access OpenAI Embeddings and Models.

And optionally set the OpenSearch ones if not using defaults:

  * `OPENSEARCH_URL` \- URL of the hosted OpenSearch Instance
  * `OPENSEARCH_USERNAME` \- User name for the OpenSearch instance
  * `OPENSEARCH_PASSWORD` \- Password for the OpenSearch instance
  * `OPENSEARCH_INDEX_NAME` \- Name of the index 

To run the default OpenSeach instance in docker, you can use the command

[code]
```python




    docker run -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" --name opensearch-node -d opensearchproject/opensearch:latest  
    


```
[/code]


Note: To load dummy index named `langchain-test` with dummy documents, run `python dummy_index_setup.py` in the package

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




    langchain app new my-app --package rag-opensearch  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-opensearch  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_opensearch import chain as rag_opensearch_chain  
      
    add_routes(app, rag_opensearch_chain, path="/rag-opensearch")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-opensearch/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-opensearch")  
    


```
[/code]


