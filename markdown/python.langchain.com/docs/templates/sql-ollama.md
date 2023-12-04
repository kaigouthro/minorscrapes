

Skip to main content

On this page

# sql-ollama

This template enables a user to interact with a SQL database using natural language.

It uses Zephyr-7b via Ollama to run inference locally on a Mac laptop.

## Environment Setup​

Before using this template, you need to set up Ollama and SQL database.

  1. Follow instructions here to download Ollama.

  2. Download your LLM of interest:

    * This package uses `zephyr`: `ollama pull zephyr`
    * You can choose from many LLMs here
  3. This package includes an example DB of 2023 NBA rosters. You can see instructions to build this DB here.

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




    langchain app new my-app --package sql-ollama  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add sql-ollama  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from sql_ollama import chain as sql_ollama_chain  
      
    add_routes(app, sql_ollama_chain, path="/sql-ollama")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/sql-ollama/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/sql-ollama")  
    


```
[/code]


