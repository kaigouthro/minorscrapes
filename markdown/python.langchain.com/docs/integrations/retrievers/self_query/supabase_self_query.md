

Skip to main content

On this page

# Supabase

> Supabase is an open-source `Firebase` alternative. `Supabase` is built on top of `PostgreSQL`, which offers strong `SQL` querying capabilities and enables a simple interface with already-existing
> tools and frameworks.

> PostgreSQL also known as `Postgres`, is a free and open-source relational database management system (RDBMS) emphasizing extensibility and `SQL` compliance.
>
> Supabase provides an open-source toolkit for developing AI applications using Postgres and pgvector. Use the Supabase client libraries to store, index, and query your vector embeddings at scale.

In the notebook, we'll demo the `SelfQueryRetriever` wrapped around a `Supabase` vector store.

Specifically, we will:

  1. Create a Supabase database
  2. Enable the `pgvector` extension
  3. Create a `documents` table and `match_documents` function that will be used by `SupabaseVectorStore`
  4. Load sample documents into the vector store (database table)
  5. Build and test a self-querying retriever

## Setup Supabase Database​

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
        embedding vector (1536) -- 1536 works for OpenAI embeddings, change if needed  
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


## Creating a Supabase vector store​

Next we'll want to create a Supabase vector store and seed it with some data. We've created a small demo set of documents that contain summaries of movies.

Be sure to install the latest version of `langchain` with `openai` support:

[code]
```python




    %pip install langchain openai tiktoken  
    


```
[/code]


The self-query retriever requires you to have `lark` installed:

[code]
```python




    %pip install lark  
    


```
[/code]


We also need the `supabase` package:

[code]
```python




    %pip install supabase  
    


```
[/code]


Since we are using `SupabaseVectorStore` and `OpenAIEmbeddings`, we have to load their API keys.

  * To find your `SUPABASE_URL` and `SUPABASE_SERVICE_KEY`, head to your Supabase project's API settings.

    * `SUPABASE_URL` corresponds to the Project URL
    * `SUPABASE_SERVICE_KEY` corresponds to the `service_role` API key
  * To get your `OPENAI_API_KEY`, navigate to API keys on your OpenAI account and create a new secret key.

[code]
```python




    import getpass  
    import os  
      
    os.environ["SUPABASE_URL"] = getpass.getpass("Supabase URL:")  
    os.environ["SUPABASE_SERVICE_KEY"] = getpass.getpass("Supabase Service Key:")  
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


 _Optional:_ If you're storing your Supabase and OpenAI API keys in a `.env` file, you can load them with `dotenv`.

[code]
```python




    %pip install python-dotenv  
    


```
[/code]


[code]
```python




    from dotenv import load_dotenv  
      
    load_dotenv()  
    


```
[/code]


First we'll create a Supabase client and instantiate a OpenAI embeddings class.

[code]
```python




    import os  
      
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.schema import Document  
    from langchain.vectorstores import SupabaseVectorStore  
    from supabase.client import Client, create_client  
      
    supabase_url = os.environ.get("SUPABASE_URL")  
    supabase_key = os.environ.get("SUPABASE_SERVICE_KEY")  
    supabase: Client = create_client(supabase_url, supabase_key)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


Next let's create our documents.

[code]
```python




    docs = [  
        Document(  
            page_content="A bunch of scientists bring back dinosaurs and mayhem breaks loose",  
            metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"},  
        ),  
        Document(  
            page_content="Leo DiCaprio gets lost in a dream within a dream within a dream within a ...",  
            metadata={"year": 2010, "director": "Christopher Nolan", "rating": 8.2},  
        ),  
        Document(  
            page_content="A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea",  
            metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6},  
        ),  
        Document(  
            page_content="A bunch of normal-sized women are supremely wholesome and some men pine after them",  
            metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},  
        ),  
        Document(  
            page_content="Toys come alive and have a blast doing so",  
            metadata={"year": 1995, "genre": "animated"},  
        ),  
        Document(  
            page_content="Three men walk into the Zone, three men walk out of the Zone",  
            metadata={  
                "year": 1979,  
                "director": "Andrei Tarkovsky",  
                "genre": "science fiction",  
                "rating": 9.9,  
            },  
        ),  
    ]  
      
    vectorstore = SupabaseVectorStore.from_documents(  
        docs,  
        embeddings,  
        client=supabase,  
        table_name="documents",  
        query_name="match_documents",  
    )  
    


```
[/code]


## Creating our self-querying retriever​

Now we can instantiate our retriever. To do this we'll need to provide some information upfront about the metadata fields that our documents support and a short description of the document contents.

[code]
```python




    from langchain.chains.query_constructor.base import AttributeInfo  
    from langchain.llms import OpenAI  
    from langchain.retrievers.self_query.base import SelfQueryRetriever  
      
    metadata_field_info = [  
        AttributeInfo(  
            name="genre",  
            description="The genre of the movie",  
            type="string or list[string]",  
        ),  
        AttributeInfo(  
            name="year",  
            description="The year the movie was released",  
            type="integer",  
        ),  
        AttributeInfo(  
            name="director",  
            description="The name of the movie director",  
            type="string",  
        ),  
        AttributeInfo(  
            name="rating", description="A 1-10 rating for the movie", type="float"  
        ),  
    ]  
    document_content_description = "Brief summary of a movie"  
    llm = OpenAI(temperature=0)  
    retriever = SelfQueryRetriever.from_llm(  
        llm, vectorstore, document_content_description, metadata_field_info, verbose=True  
    )  
    


```
[/code]


## Testing it out​

And now we can try actually using our retriever!

[code]
```python




    # This example only specifies a relevant query  
    retriever.get_relevant_documents("What are some movies about dinosaurs")  
    


```
[/code]


[code]
```python




        query='dinosaur' filter=None limit=None  
      
      
      
      
      
        [Document(page_content='A bunch of scientists bring back dinosaurs and mayhem breaks loose', metadata={'year': 1993, 'genre': 'science fiction', 'rating': 7.7}),  
         Document(page_content='Toys come alive and have a blast doing so', metadata={'year': 1995, 'genre': 'animated'}),  
         Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'year': 1979, 'genre': 'science fiction', 'rating': 9.9, 'director': 'Andrei Tarkovsky'}),  
         Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'year': 2006, 'rating': 8.6, 'director': 'Satoshi Kon'})]  
    


```
[/code]


[code]
```python




    # This example only specifies a filter  
    retriever.get_relevant_documents("I want to watch a movie rated higher than 8.5")  
    


```
[/code]


[code]
```python




        query=' ' filter=Comparison(comparator=<Comparator.GT: 'gt'>, attribute='rating', value=8.5) limit=None  
      
      
      
      
      
        [Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'year': 1979, 'genre': 'science fiction', 'rating': 9.9, 'director': 'Andrei Tarkovsky'}),  
         Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'year': 2006, 'rating': 8.6, 'director': 'Satoshi Kon'})]  
    


```
[/code]


[code]
```python




    # This example specifies a query and a filter  
    retriever.get_relevant_documents("Has Greta Gerwig directed any movies about women?")  
    


```
[/code]


[code]
```python




        query='women' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='director', value='Greta Gerwig') limit=None  
      
      
      
      
      
        [Document(page_content='A bunch of normal-sized women are supremely wholesome and some men pine after them', metadata={'year': 2019, 'rating': 8.3, 'director': 'Greta Gerwig'})]  
    


```
[/code]


[code]
```python




    # This example specifies a composite filter  
    retriever.get_relevant_documents(  
        "What's a highly rated (above 8.5) science fiction film?"  
    )  
    


```
[/code]


[code]
```python




        query=' ' filter=Operation(operator=<Operator.AND: 'and'>, arguments=[Comparison(comparator=<Comparator.GTE: 'gte'>, attribute='rating', value=8.5), Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='genre', value='science fiction')]) limit=None  
      
      
      
      
      
        [Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'year': 1979, 'genre': 'science fiction', 'rating': 9.9, 'director': 'Andrei Tarkovsky'})]  
    


```
[/code]


[code]
```python




    # This example specifies a query and composite filter  
    retriever.get_relevant_documents(  
        "What's a movie after 1990 but before (or on) 2005 that's all about toys, and preferably is animated"  
    )  
    


```
[/code]


[code]
```python




        query='toys' filter=Operation(operator=<Operator.AND: 'and'>, arguments=[Comparison(comparator=<Comparator.GT: 'gt'>, attribute='year', value=1990), Comparison(comparator=<Comparator.LTE: 'lte'>, attribute='year', value=2005), Comparison(comparator=<Comparator.LIKE: 'like'>, attribute='genre', value='animated')]) limit=None  
      
      
      
      
      
        [Document(page_content='Toys come alive and have a blast doing so', metadata={'year': 1995, 'genre': 'animated'})]  
    


```
[/code]


## Filter k​

We can also use the self query retriever to specify `k`: the number of documents to fetch.

We can do this by passing `enable_limit=True` to the constructor.

[code]
```python




    retriever = SelfQueryRetriever.from_llm(  
        llm,  
        vectorstore,  
        document_content_description,  
        metadata_field_info,  
        enable_limit=True,  
        verbose=True,  
    )  
    


```
[/code]


[code]
```python




    # This example only specifies a relevant query  
    retriever.get_relevant_documents("what are two movies about dinosaurs")  
    


```
[/code]


[code]
```python




        query='dinosaur' filter=None limit=2  
      
      
      
      
      
        [Document(page_content='A bunch of scientists bring back dinosaurs and mayhem breaks loose', metadata={'year': 1993, 'genre': 'science fiction', 'rating': 7.7}),  
         Document(page_content='Toys come alive and have a blast doing so', metadata={'year': 1995, 'genre': 'animated'})]  
    


```
[/code]


