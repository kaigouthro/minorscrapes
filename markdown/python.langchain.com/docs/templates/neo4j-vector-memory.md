

Skip to main content

On this page

# neo4j-vector-memory

This template allows you to integrate an LLM with a vector-based retrieval system using Neo4j as the vector store. Additionally, it uses the graph capabilities of the Neo4j database to store and
retrieve the dialogue history of a specific user's session. Having the dialogue history stored as a graph allows for seamless conversational flows but also gives you the ability to analyze user
behavior and text chunk retrieval through graph analytics.

## Environment Setup​

You need to define the following environment variables

[code]
```python




    OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>  
    NEO4J_URI=<YOUR_NEO4J_URI>  
    NEO4J_USERNAME=<YOUR_NEO4J_USERNAME>  
    NEO4J_PASSWORD=<YOUR_NEO4J_PASSWORD>  
    


```
[/code]


## Populating with data​

If you want to populate the DB with some example data, you can run `python ingest.py`. The script process and stores sections of the text from the file `dune.txt` into a Neo4j graph database.
Additionally, a vector index named `dune` is created for efficient querying of these embeddings.

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




    langchain app new my-app --package neo4j-vector-memory  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add neo4j-vector-memory  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from neo4j_vector_memory import chain as neo4j_vector_memory_chain  
      
    add_routes(app, neo4j_vector_memory_chain, path="/neo4j-vector-memory")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/neo4j-vector-memory/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/neo4j-vector-memory")  
    


```
[/code]


