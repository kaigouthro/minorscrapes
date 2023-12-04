

Skip to main content

On this page

# rag-timescale-conversation

This template is used for conversational retrieval, which is one of the most popular LLM use-cases.

It passes both a conversation history and retrieved documents into an LLM for synthesis.

## Environment Setup​

This template uses Timescale Vector as a vectorstore and requires that `TIMESCALES_SERVICE_URL`. Signup for a 90-day trial here if you don't yet have an account.

To load the sample dataset, set `LOAD_SAMPLE_DATA=1`. To load your own dataset see the section below.

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

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




    langchain app new my-app --package rag-timescale-conversation  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-timescale-conversation  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_timescale_conversation import chain as rag_timescale_conversation_chain  
      
    add_routes(app, rag_timescale_conversation_chain, path="/rag-timescale_conversation")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-timescale-conversation/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-timescale-conversation")  
    


```
[/code]


See the `rag_conversation.ipynb` notebook for example usage.

## Loading your own dataset​

To load your own dataset you will have to create a `load_dataset` function. You can see an example, in the `load_ts_git_dataset` function defined in the `load_sample_dataset.py` file. You can then run
this as a standalone function (e.g. in a bash script) or add it to chain.py (but then you should run it just once).

