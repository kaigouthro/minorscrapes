

Skip to main content

On this page

# rag-google-cloud-sensitive-data-protection

This template is an application that utilizes Google Vertex AI Search, a machine learning powered search service, and PaLM 2 for Chat (chat-bison). The application uses a Retrieval chain to answer
questions based on your documents.

This template is an application that utilizes Google Sensitive Data Protection, a service for detecting and redacting sensitive data in text, and PaLM 2 for Chat (chat-bison), although you can use any
model.

For more context on using Sensitive Data Protection, check here.

## Environment Setup​

Before using this template, please ensure that you enable the DLP API and Vertex AI API in your Google Cloud project.

For some common environment troubleshooting steps related to Google Cloud, see the bottom of this readme.

Set the following environment variables:

  * `GOOGLE_CLOUD_PROJECT_ID` \- Your Google Cloud project ID.
  * `MODEL_TYPE` \- The model type for Vertex AI Search (e.g. `chat-bison`)

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




    langchain app new my-app --package rag-google-cloud-sensitive-data-protection  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-google-cloud-sensitive-data-protection  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_google_cloud_sensitive_data_protection.chain import chain as rag_google_cloud_sensitive_data_protection_chain  
      
    add_routes(app, rag_google_cloud_sensitive_data_protection_chain, path="/rag-google-cloud-sensitive-data-protection")  
    


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


This will start the FastAPI app with a server running locally at http://localhost:8000

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-google-cloud-vertexai-search/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-google-cloud-sensitive-data-protection")  
    


```
[/code]


[code]
```python




      
    # Troubleshooting Google Cloud  
      
    You can set your `gcloud` credentials with their CLI using `gcloud auth application-default login`  
      
    You can set your `gcloud` project with the following commands  
    ```bash  
    gcloud config set project <your project>  
    gcloud auth application-default set-quota-project <your project>  
    export GOOGLE_CLOUD_PROJECT_ID=<your project>  
    


```
[/code]


