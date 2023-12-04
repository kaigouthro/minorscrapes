

Skip to main content

On this page

# neo4j-parent

This template allows you to balance precise embeddings and context retention by splitting documents into smaller chunks and retrieving their original or larger text information.

Using a Neo4j vector index, the package queries child nodes using vector similarity search and retrieves the corresponding parent's text by defining an appropriate `retrieval_query` parameter.

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

If you want to populate the DB with some example data, you can run `python ingest.py`. The script process and stores sections of the text from the file `dune.txt` into a Neo4j graph database. First,
the text is divided into larger chunks ("parents") and then further subdivided into smaller chunks ("children"), where both parent and child chunks overlap slightly to maintain context. After storing
these chunks in the database, embeddings for the child nodes are computed using OpenAI's embeddings and stored back in the graph for future retrieval or analysis. Additionally, a vector index named
`retrieval` is created for efficient querying of these embeddings.

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




    langchain app new my-app --package neo4j-parent  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add neo4j-parent  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from neo4j_parent import chain as neo4j_parent_chain  
      
    add_routes(app, neo4j_parent_chain, path="/neo4j-parent")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/neo4j-parent/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/neo4j-parent")  
    


```
[/code]


