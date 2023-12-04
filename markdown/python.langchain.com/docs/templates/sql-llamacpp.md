

Skip to main content

On this page

# sql-llamacpp

This template enables a user to interact with a SQL database using natural language.

It uses Mistral-7b via llama.cpp to run inference locally on a Mac laptop.

## Environment Setup​

To set up the environment, use the following steps:

[code]
```python




    wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh  
    bash Miniforge3-MacOSX-arm64.sh  
    conda create -n llama python=3.9.16  
    conda activate /Users/rlm/miniforge3/envs/llama  
    CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 pip install -U llama-cpp-python --no-cache-dir  
    


```
[/code]


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




    langchain app new my-app --package sql-llamacpp  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add sql-llamacpp  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from sql_llamacpp import chain as sql_llamacpp_chain  
      
    add_routes(app, sql_llamacpp_chain, path="/sql-llamacpp")  
    


```
[/code]


The package will download the Mistral-7b model from here. You can select other files and specify their download path (browse here).

This package includes an example DB of 2023 NBA rosters. You can see instructions to build this DB here.

(Optional) Configure LangSmith for tracing, monitoring and debugging LangChain applications. LangSmith is currently in private beta, you can sign up here. If you don't have access, you can skip this
section

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


This will start the FastAPI app with a server running locally at http://localhost:8000

You can see all templates at http://127.0.0.1:8000/docs You can access the playground at http://127.0.0.1:8000/sql-llamacpp/playground

You can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/sql-llamacpp")  
    


```
[/code]


