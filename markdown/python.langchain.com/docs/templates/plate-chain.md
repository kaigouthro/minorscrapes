

Skip to main content

On this page

# plate-chain

This template enables parsing of data from laboratory plates.

In the context of biochemistry or molecular biology, laboratory plates are commonly used tools to hold samples in a grid-like format.

This can parse the resulting data into standardized (e.g., JSON) format for further processing.

## Environment Setup​

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

## Usage​

To utilize plate-chain, you must have the LangChain CLI installed:

[code]
```python




    pip install -U langchain-cli  
    


```
[/code]


Creating a new LangChain project and installing plate-chain as the only package can be done with:

[code]
```python




    langchain app new my-app --package plate-chain  
    


```
[/code]


If you wish to add this to an existing project, simply run:

[code]
```python




    langchain app add plate-chain  
    


```
[/code]


Then add the following code to your `server.py` file:

[code]
```python




    from plate_chain import chain as plate_chain  
      
    add_routes(app, plate_chain, path="/plate-chain")  
    


```
[/code]


(Optional) For configuring LangSmith, which helps trace, monitor and debug LangChain applications, use the following code:

[code]
```python




    export LANGCHAIN_TRACING_V2=true  
    export LANGCHAIN_API_KEY=<your-api-key>  
    export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"  
    


```
[/code]


If you're in this directory, you can start a LangServe instance directly by:

[code]
```python




    langchain serve  
    


```
[/code]


This starts the FastAPI app with a server running locally at http://localhost:8000

All templates can be viewed at http://127.0.0.1:8000/docs Access the playground at http://127.0.0.1:8000/plate-chain/playground

You can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/plate-chain")  
    


```
[/code]


