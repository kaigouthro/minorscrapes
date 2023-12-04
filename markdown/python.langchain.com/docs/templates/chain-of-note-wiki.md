

Skip to main content

On this page

# Chain-of-Note (Wikipedia)

Implements Chain-of-Note as described in https://arxiv.org/pdf/2311.09210.pdf by Yu, et al. Uses Wikipedia for retrieval.

Check out the prompt being used here https://smith.langchain.com/hub/bagatur/chain-of-note-wiki.

## Environment Setup​

Uses Anthropic claude-2 chat model. Set Anthropic API key:

[code]
```python




    export ANTHROPIC_API_KEY="..."  
    


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




    langchain app new my-app --package chain-of-note-wiki  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add chain-of-note-wiki  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from chain_of_note_wiki import chain as chain_of_note_wiki_chain  
      
    add_routes(app, chain_of_note_wiki_chain, path="/chain-of-note-wiki")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/chain-of-note-wiki/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/chain-of-note-wiki")  
    


```
[/code]


