

Skip to main content

On this page

# RAG with Timescale Vector using hybrid search

This template shows how to use timescale-vector with the self-query retriver to perform hybrid search on similarity and time. This is useful any time your data has a strong time-based component. Some
examples of such data are:

  * News articles (politics, business, etc)
  * Blog posts, documentation or other published material (public or private).
  * Social media posts
  * Changelogs of any kind
  * Messages

Such items are often searched by both similarity and time. For example: Show me all news about Toyota trucks from 2022.

Timescale Vector provides superior performance when searching for embeddings within a particular timeframe by leveraging automatic table partitioning to isolate data for particular time-ranges.

Langchain's self-query retriever allows deducing time-ranges (as well as other search criteria) from the text of user queries.

## What is Timescale Vector?​

 **Timescale Vector is PostgreSQL++ for AI applications.**

Timescale Vector enables you to efficiently store and query billions of vector embeddings in `PostgreSQL`.

  * Enhances `pgvector` with faster and more accurate similarity search on 1B+ vectors via DiskANN inspired indexing algorithm.
  * Enables fast time-based vector search via automatic time-based partitioning and indexing.
  * Provides a familiar SQL interface for querying vector embeddings and relational data.

Timescale Vector is cloud PostgreSQL for AI that scales with you from POC to production:

  * Simplifies operations by enabling you to store relational metadata, vector embeddings, and time-series data in a single database.
  * Benefits from rock-solid PostgreSQL foundation with enterprise-grade feature liked streaming backups and replication, high-availability and row-level security.
  * Enables a worry-free experience with enterprise-grade security and compliance.

### How to access Timescale Vector​

Timescale Vector is available on Timescale, the cloud PostgreSQL platform. (There is no self-hosted version at this time.)

  * LangChain users get a 90-day free trial for Timescale Vector.
  * To get started, signup to Timescale, create a new database and follow this notebook!
  * See the installation instructions for more details on using Timescale Vector in python.

## Environment Setup​

This template uses Timescale Vector as a vectorstore and requires that `TIMESCALES_SERVICE_URL`. Signup for a 90-day trial here if you don't yet have an account.

To load the sample dataset, set `LOAD_SAMPLE_DATA=1`. To load your own dataset see the section below.

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




    langchain app new my-app --package rag-timescale-hybrid-search-time  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-timescale-hybrid-search-time  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_timescale_hybrid_search.chain import chain as rag_timescale_hybrid_search_chain  
      
    add_routes(app, rag_timescale_hybrid_search_chain, path="/rag-timescale-hybrid-search")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-timescale-hybrid-search/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-timescale-hybrid-search")  
    


```
[/code]


## Loading your own dataset​

To load your own dataset you will have to modify the code in the `DATASET SPECIFIC CODE` section of `chain.py`. This code defines the name of the collection, how to load the data, and the human-
language description of both the contents of the collection and all of the metadata. The human-language descriptions are used by the self-query retriever to help the LLM convert the question into
filters on the metadata when searching the data in Timescale-vector.

