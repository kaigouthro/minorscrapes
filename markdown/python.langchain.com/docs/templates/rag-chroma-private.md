

Skip to main content

On this page

# rag-chroma-private

This template performs RAG with no reliance on external APIs.

It utilizes Ollama the LLM, GPT4All for embeddings, and Chroma for the vectorstore.

The vectorstore is created in `chain.py` and by default indexes a popular blog posts on Agents for question-answering.

## Environment Setup​

To set up the environment, you need to download Ollama.

Follow the instructions here.

You can choose the desired LLM with Ollama.

This template uses `llama2:7b-chat`, which can be accessed using `ollama pull llama2:7b-chat`.

There are many other options available here.

This package also uses GPT4All embeddings.

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




    langchain app new my-app --package rag-chroma-private  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-chroma-private  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_chroma_private import chain as rag_chroma_private_chain  
      
    add_routes(app, rag_chroma_private_chain, path="/rag-chroma-private")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-chroma-private/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-chroma-private")  
    


```
[/code]


The package will create and add documents to the vector database in `chain.py`. By default, it will load a popular blog post on agents. However, you can choose from a large number of document loaders
here.

