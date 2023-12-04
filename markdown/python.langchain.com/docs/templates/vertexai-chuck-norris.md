

Skip to main content

On this page

# vertexai-chuck-norris

This template makes jokes about Chuck Norris using Vertex AI PaLM2.

## Environment Setup​

First, make sure you have a Google Cloud project with an active billing account, and have the gcloud CLI installed.

Configure application default credentials:

[code]
```python




    gcloud auth application-default login  
    


```
[/code]


To set a default Google Cloud project to use, run this command and set the project ID of the project you want to use:

[code]
```python




    gcloud config set project [PROJECT-ID]  
    


```
[/code]


Enable the Vertex AI API for the project:

[code]
```python




    gcloud services enable aiplatform.googleapis.com  
    


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




    langchain app new my-app --package pirate-speak  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add vertexai-chuck-norris  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from vertexai_chuck_norris.chain import chain as vertexai_chuck_norris_chain  
      
    add_routes(app, vertexai_chuck_norris_chain, path="/vertexai-chuck-norris")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/vertexai-chuck-norris/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/vertexai-chuck-norris")  
    


```
[/code]


