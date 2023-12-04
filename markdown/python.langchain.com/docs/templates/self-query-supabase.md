

Skip to main content

On this page

# self-query-supabase

This templates allows natural language structured quering of Supabase.

Supabase is an open-source alternative to Firebase, built on top of PostgreSQL.

It uses pgvector to store embeddings within your tables.

## Environment Setup​

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

To get your `OPENAI_API_KEY`, navigate to API keys on your OpenAI account and create a new secret key.

To find your `SUPABASE_URL` and `SUPABASE_SERVICE_KEY`, head to your Supabase project's API settings.

  * `SUPABASE_URL` corresponds to the Project URL
  * `SUPABASE_SERVICE_KEY` corresponds to the `service_role` API key

[code]
```python




    export SUPABASE_URL=  
    export SUPABASE_SERVICE_KEY=  
    export OPENAI_API_KEY=  
    


```
[/code]


## Setup Supabase Database​

Use these steps to setup your Supabase database if you haven't already.

  1. Head over to https://database.new to provision your Supabase database.

  2. In the studio, jump to the SQL editor and run the following script to enable `pgvector` and setup your database as a vector store:
[code]
```python


    -- Enable the pgvector extension to work with embedding vectors  
    create extension if not exists vector;  
      
    -- Create a table to store your documents  
    create table  
      documents (  
        id uuid primary key,  
        content text, -- corresponds to Document.pageContent  
        metadata jsonb, -- corresponds to Document.metadata  
        embedding vector (1536) -- 1536 works for OpenAI embeddings, change as needed  
      );  
      
    -- Create a function to search for documents  
    create function match_documents (  
      query_embedding vector (1536),  
      filter jsonb default '{}'  
    ) returns table (  
      id uuid,  
      content text,  
      metadata jsonb,  
      similarity float  
    ) language plpgsql as $$  
    #variable_conflict use_column  
    begin  
      return query  
      select  
        id,  
        content,  
        metadata,  
        1 - (documents.embedding <=> query_embedding) as similarity  
      from documents  
      where metadata @> filter  
      order by documents.embedding <=> query_embedding;  
    end;  
    $$;  
    


```
[/code]


## Usage​

To use this package, install the LangChain CLI first:

[code]
```python




    pip install -U langchain-cli  
    


```
[/code]


Create a new LangChain project and install this package as the only one:

[code]
```python




    langchain app new my-app --package self-query-supabase  
    


```
[/code]


To add this to an existing project, run:

[code]
```python




    langchain app add self-query-supabase  
    


```
[/code]


Add the following code to your `server.py` file:

[code]
```python




    from self_query_supabase.chain import chain as self_query_supabase_chain  
      
    add_routes(app, self_query_supabase_chain, path="/self-query-supabase")  
    


```
[/code]


(Optional) If you have access to LangSmith, configure it to help trace, monitor and debug LangChain applications. If you don't have access, skip this section.

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

You can see all templates at http://127.0.0.1:8000/docs Access the playground at http://127.0.0.1:8000/self-query-supabase/playground

Access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/self-query-supabase")  
    


```
[/code]


TODO: Instructions to set up the Supabase database and install the package.

