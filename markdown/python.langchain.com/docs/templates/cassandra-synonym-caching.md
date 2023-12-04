

Skip to main content

On this page

# cassandra-synonym-caching

This template provides a simple chain template showcasing the usage of LLM Caching backed by Apache Cassandra® or Astra DB through CQL.

## Environment Setup​

To set up your environment, you will need the following:

  * an Astra Vector Database (free tier is fine!). **You need aDatabase Administrator token**, in particular the string starting with `AstraCS:...`;
  * likewise, get your Database ID ready, you will have to enter it below;
  * an **OpenAI API Key**. (More info here, note that out-of-the-box this demo supports OpenAI unless you tinker with the code.)

 _Note:_ you can alternatively use a regular Cassandra cluster: to do so, make sure you provide the `USE_CASSANDRA_CLUSTER` entry as shown in `.env.template` and the subsequent environment variables
to specify how to connect to it.

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




    langchain app new my-app --package cassandra-synonym-caching  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add cassandra-synonym-caching  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from cassandra_synonym_caching import chain as cassandra_synonym_caching_chain  
      
    add_routes(app, cassandra_synonym_caching_chain, path="/cassandra-synonym-caching")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/cassandra-synonym-caching/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/cassandra-synonym-caching")  
    


```
[/code]


## Reference​

Stand-alone LangServe template repo: here.

