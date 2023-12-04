

Skip to main content

On this page

# neo4j-cypher-ft

This template allows you to interact with a Neo4j graph database using natural language, leveraging OpenAI's LLM.

Its main function is to convert natural language questions into Cypher queries (the language used to query Neo4j databases), execute these queries, and provide natural language responses based on the
query's results.

The package utilizes a full-text index for efficient mapping of text values to database entries, thereby enhancing the generation of accurate Cypher statements.

In the provided example, the full-text index is used to map names of people and movies from the user's query to corresponding database entries.

## Environment Setup​

The following environment variables need to be set:

[code]
```python




    OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>  
    NEO4J_URI=<YOUR_NEO4J_URI>  
    NEO4J_USERNAME=<YOUR_NEO4J_USERNAME>  
    NEO4J_PASSWORD=<YOUR_NEO4J_PASSWORD>  
    


```
[/code]


Additionally, if you wish to populate the DB with some example data, you can run `python ingest.py`. This script will populate the database with sample movie data and create a full-text index named
`entity`, which is used to map person and movies from user input to database values for precise Cypher statement generation.

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




    langchain app new my-app --package neo4j-cypher-ft  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add neo4j-cypher-ft  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from neo4j_cypher_ft import chain as neo4j_cypher_ft_chain  
      
    add_routes(app, neo4j_cypher_ft_chain, path="/neo4j-cypher-ft")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/neo4j-cypher-ft/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/neo4j-cypher-ft")  
    


```
[/code]


