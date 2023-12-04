

Skip to main content

On this page

# llama2-functions

This template performs extraction of structured data from unstructured data using a LLaMA2 model that supports a specified JSON output schema.

The extraction schema can be set in `chain.py`.

## Environment Setup​

This will use a LLaMA2-13b model hosted by Replicate.

Ensure that `REPLICATE_API_TOKEN` is set in your environment.

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




    langchain app new my-app --package llama2-functions  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add llama2-functions  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from llama2_functions import chain as llama2_functions_chain  
      
    add_routes(app, llama2_functions_chain, path="/llama2-functions")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/llama2-functions/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/llama2-functions")  
    


```
[/code]


