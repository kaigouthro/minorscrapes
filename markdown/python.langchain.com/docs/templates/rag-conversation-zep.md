

Skip to main content

On this page

# rag-conversation-zep

This template demonstrates building a RAG conversation app using Zep.

Included in this template:

  * Populating a Zep Document Collection with a set of documents (a Collection is analogous to an index in other Vector Databases).
  * Using Zep's integrated embedding functionality to embed the documents as vectors.
  * Configuring a LangChain ZepVectorStore Retriever to retrieve documents using Zep's built, hardware accelerated in Maximal Marginal Relevance (MMR) re-ranking.
  * Prompts, a simple chat history data structure, and other components required to build a RAG conversation app.
  * The RAG conversation chain.

## About Zep - Fast, scalable building blocks for LLM Apps​

Zep is an open source platform for productionizing LLM apps. Go from a prototype built in LangChain or LlamaIndex, or a custom app, to production in minutes without rewriting code.

Key Features:

  * Fast! Zep’s async extractors operate independently of the your chat loop, ensuring a snappy user experience.
  * Long-term memory persistence, with access to historical messages irrespective of your summarization strategy.
  * Auto-summarization of memory messages based on a configurable message window. A series of summaries are stored, providing flexibility for future summarization strategies.
  * Hybrid search over memories and metadata, with messages automatically embedded on creation.
  * Entity Extractor that automatically extracts named entities from messages and stores them in the message metadata.
  * Auto-token counting of memories and summaries, allowing finer-grained control over prompt assembly.
  * Python and JavaScript SDKs.

Zep project: https://github.com/getzep/zep | Docs: https://docs.getzep.com/

## Environment Setup​

Set up a Zep service by following the Quick Start Guide.

## Ingesting Documents into a Zep Collection​

Run `python ingest.py` to ingest the test documents into a Zep Collection. Review the file to modify the Collection name and document source.

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




    langchain app new my-app --package rag-conversation-zep  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-conversation-zep  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_conversation_zep import chain as rag_conversation_zep_chain  
      
    add_routes(app, rag_conversation_zep_chain, path="/rag-conversation-zep")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-conversation-zep/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-conversation-zep")  
    


```
[/code]


