

Skip to main content

On this page

# sql-llama2

This template enables a user to interact with a SQL database using natural language.

It uses LLamA2-13b hosted by Replicate, but can be adapted to any API that supports LLaMA2 including Fireworks.

The template includes an example database of 2023 NBA rosters.

For more information on how to build this database, see here.

## Environment Setup​

Ensure the `REPLICATE_API_TOKEN` is set in your environment.

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




    langchain app new my-app --package sql-llama2  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add sql-llama2  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from sql_llama2 import chain as sql_llama2_chain  
      
    add_routes(app, sql_llama2_chain, path="/sql-llama2")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/sql-llama2/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/sql-llama2")  
    


```
[/code]


