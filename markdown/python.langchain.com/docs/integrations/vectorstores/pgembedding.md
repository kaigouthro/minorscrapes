

Skip to main content

On this page

# Postgres Embedding

> Postgres Embedding is an open-source vector similarity search for `Postgres` that uses `Hierarchical Navigable Small Worlds (HNSW)` for approximate nearest neighbor search.

> It supports:
>
>   * exact and approximate nearest neighbor search using HNSW
>   * L2 distance
>

This notebook shows how to use the Postgres vector database (`PGEmbedding`).

> The PGEmbedding integration creates the pg_embedding extension for you, but you run the following Postgres query to add it:
[code]
```python




>     CREATE EXTENSION embedding;  
>     >


```
[/code]


[code]
```python




    # Pip install necessary package  
    pip install openai  
    pip install psycopg2-binary  
    pip install tiktoken  
    


```
[/code]


Add the OpenAI API Key to the environment variables to use `OpenAIEmbeddings`.

[code]
```python




    import getpass  
    import os  
      
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




        OpenAI API Key:········  
    


```
[/code]


[code]
```python




    ## Loading Environment Variables  
    from typing import List, Tuple  
    


```
[/code]


[code]
```python




    from langchain.docstore.document import Document  
    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import PGEmbedding  
    


```
[/code]


[code]
```python




    os.environ["DATABASE_URL"] = getpass.getpass("Database Url:")  
    


```
[/code]


[code]
```python




        Database Url:········  
    


```
[/code]


[code]
```python




    loader = TextLoader("state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    connection_string = os.environ.get("DATABASE_URL")  
    collection_name = "state_of_the_union"  
    


```
[/code]


[code]
```python




    db = PGEmbedding.from_documents(  
        embedding=embeddings,  
        documents=docs,  
        collection_name=collection_name,  
        connection_string=connection_string,  
    )  
      
    query = "What did the president say about Ketanji Brown Jackson"  
    docs_with_score: List[Tuple[Document, float]] = db.similarity_search_with_score(query)  
    


```
[/code]


[code]
```python




    for doc, score in docs_with_score:  
        print("-" * 80)  
        print("Score: ", score)  
        print(doc.page_content)  
        print("-" * 80)  
    


```
[/code]


## Working with vectorstore in Postgres​

### Uploading a vectorstore in PG​

[code]
```python




    db = PGEmbedding.from_documents(  
        embedding=embeddings,  
        documents=docs,  
        collection_name=collection_name,  
        connection_string=connection_string,  
        pre_delete_collection=False,  
    )  
    


```
[/code]


### Create HNSW Index​

By default, the extension performs a sequential scan search, with 100% recall. You might consider creating an HNSW index for approximate nearest neighbor (ANN) search to speed up
`similarity_search_with_score` execution time. To create the HNSW index on your vector column, use a `create_hnsw_index` function:

[code]
```python




    PGEmbedding.create_hnsw_index(  
        max_elements=10000, dims=1536, m=8, ef_construction=16, ef_search=16  
    )  
    


```
[/code]


The function above is equivalent to running the below SQL query:

[code]
```python




    CREATE INDEX ON vectors USING hnsw(vec) WITH (maxelements=10000, dims=1536, m=3, efconstruction=16, efsearch=16);  
    


```
[/code]


The HNSW index options used in the statement above include:

  * maxelements: Defines the maximum number of elements indexed. This is a required parameter. The example shown above has a value of 3. A real-world example would have a much large value, such as 1000000. An "element" refers to a data point (a vector) in the dataset, which is represented as a node in the HNSW graph. Typically, you would set this option to a value able to accommodate the number of rows in your in your dataset.

  * dims: Defines the number of dimensions in your vector data. This is a required parameter. A small value is used in the example above. If you are storing data generated using OpenAI's text-embedding-ada-002 model, which supports 1536 dimensions, you would define a value of 1536, for example.

  * m: Defines the maximum number of bi-directional links (also referred to as "edges") created for each node during graph construction. The following additional index options are supported:

  * efConstruction: Defines the number of nearest neighbors considered during index construction. The default value is 32.

  * efsearch: Defines the number of nearest neighbors considered during index search. The default value is 32. For information about how you can configure these options to influence the HNSW algorithm, refer to Tuning the HNSW algorithm.

### Retrieving a vectorstore in PG​

[code]
```python




    store = PGEmbedding(  
        connection_string=connection_string,  
        embedding_function=embeddings,  
        collection_name=collection_name,  
    )  
      
    retriever = store.as_retriever()  
    


```
[/code]


[code]
```python




    retriever  
    


```
[/code]


[code]
```python




        VectorStoreRetriever(vectorstore=<langchain.vectorstores.pghnsw.HNSWVectoreStore object at 0x121d3c8b0>, search_type='similarity', search_kwargs={})  
    


```
[/code]


[code]
```python




    db1 = PGEmbedding.from_existing_index(  
        embedding=embeddings,  
        collection_name=collection_name,  
        pre_delete_collection=False,  
        connection_string=connection_string,  
    )  
      
    query = "What did the president say about Ketanji Brown Jackson"  
    docs_with_score: List[Tuple[Document, float]] = db1.similarity_search_with_score(query)  
    


```
[/code]


[code]
```python




    for doc, score in docs_with_score:  
        print("-" * 80)  
        print("Score: ", score)  
        print(doc.page_content)  
        print("-" * 80)  
    


```
[/code]


