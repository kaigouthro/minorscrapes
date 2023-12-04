

Skip to main content

On this page

# neo4j-generation

This template pairs LLM-based knowledge graph extraction with Neo4j AuraDB, a fully managed cloud graph database.

You can create a free instance on Neo4j Aura.

When you initiate a free database instance, you'll receive credentials to access the database.

This template is flexible and allows users to guide the extraction process by specifying a list of node labels and relationship types.

For more details on the functionality and capabilities of this package, please refer to this blog post.

## Environment Setup​

You need to set the following environment variables:

[code]
```python




    OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>  
    NEO4J_URI=<YOUR_NEO4J_URI>  
    NEO4J_USERNAME=<YOUR_NEO4J_USERNAME>  
    NEO4J_PASSWORD=<YOUR_NEO4J_PASSWORD>  
    


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




    langchain app new my-app --package neo4j-generation  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add neo4j-generation  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from neo4j_generation.chain import chain as neo4j_generation_chain  
      
    add_routes(app, neo4j_generation_chain, path="/neo4j-generation")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/neo4j-generation/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/neo4j-generation")  
    


```
[/code]


