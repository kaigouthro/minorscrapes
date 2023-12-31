

Skip to main content

On this page

# elastic-query-generator

This template allows interacting with Elasticsearch analytics databases in natural language using LLMs.

It builds search queries via the Elasticsearch DSL API (filters and aggregations).

## Environment Setup​

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

### Installing Elasticsearch​

There are a number of ways to run Elasticsearch. However, one recommended way is through Elastic Cloud.

Create a free trial account on Elastic Cloud.

With a deployment, update the connection string.

Password and connection (elasticsearch url) can be found on the deployment console.

Note that the Elasticsearch client must have permissions for index listing, mapping description, and search queries.

### Populating with data​

If you want to populate the DB with some example info, you can run `python ingest.py`.

This will create a `customers` index. In this package, we specify indexes to generate queries against, and we specify `["customers"]`. This is specific to setting up your Elastic index.

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




    langchain app new my-app --package elastic-query-generator  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add elastic-query-generator  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from elastic_query_generator.chain import chain as elastic_query_generator_chain  
      
    add_routes(app, elastic_query_generator_chain, path="/elastic-query-generator")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/elastic-query-generator/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/elastic-query-generator")  
    


```
[/code]


