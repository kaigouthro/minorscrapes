

Skip to main content

On this page

# ClickHouse

> ClickHouse is the fastest and most resource efficient open-source database for real-time apps and analytics with full SQL support and a wide range of functions to assist users in writing analytical
> queries. Lately added data structures and distance search functions (like `L2Distance`) as well as approximate nearest neighbor search indexes enable ClickHouse to be used as a high performance and
> scalable vector database to store and search vectors with SQL.

This notebook shows how to use functionality related to the `ClickHouse` vector search.

## Setting up environments​

Setting up local clickhouse server with docker (optional)

[code]
```python




    docker run -d -p 8123:8123 -p9000:9000 --name langchain-clickhouse-server --ulimit nofile=262144:262144 clickhouse/clickhouse-server:23.4.2.11  
    


```
[/code]


Setup up clickhouse client driver

[code]
```python




    pip install clickhouse-connect  
    


```
[/code]


We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.

[code]
```python




    import getpass  
    import os  
      
    if not os.environ["OPENAI_API_KEY"]:  
        os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Clickhouse, ClickhouseSettings  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    for d in docs:  
        d.metadata = {"some": "metadata"}  
    settings = ClickhouseSettings(table="clickhouse_vector_search_example")  
    docsearch = Clickhouse.from_documents(docs, embeddings, config=settings)  
      
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = docsearch.similarity_search(query)  
    


```
[/code]


[code]
```python




        Inserting data...: 100%|██████████| 42/42 [00:00<00:00, 2801.49it/s]  
    


```
[/code]


[code]
```python




    print(docs[0].page_content)  
    


```
[/code]


[code]
```python




        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   
          
        Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   
          
        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
    


```
[/code]


## Get connection info and data schema​

[code]
```python




    print(str(docsearch))  
    


```
[/code]


[code]
```python




        default.clickhouse_vector_search_example @ localhost:8123  
          
        username: None  
          
        Table Schema:  
        ---------------------------------------------------  
        |id                      |Nullable(String)        |  
        |document                |Nullable(String)        |  
        |embedding               |Array(Float32)          |  
        |metadata                |Object('json')          |  
        |uuid                    |UUID                    |  
        ---------------------------------------------------  
          
    


```
[/code]


### Clickhouse table schema​

> Clickhouse table will be automatically created if not exist by default. Advanced users could pre-create the table with optimized settings. For distributed Clickhouse cluster with sharding, table
> engine should be configured as `Distributed`.
[code]
```python




    print(f"Clickhouse Table DDL:\n\n{docsearch.schema}")  
    


```
[/code]


[code]
```python




        Clickhouse Table DDL:  
          
        CREATE TABLE IF NOT EXISTS default.clickhouse_vector_search_example(  
            id Nullable(String),  
            document Nullable(String),  
            embedding Array(Float32),  
            metadata JSON,  
            uuid UUID DEFAULT generateUUIDv4(),  
            CONSTRAINT cons_vec_len CHECK length(embedding) = 1536,  
            INDEX vec_idx embedding TYPE annoy(100,'L2Distance') GRANULARITY 1000  
        ) ENGINE = MergeTree ORDER BY uuid SETTINGS index_granularity = 8192  
    


```
[/code]


## Filtering​

You can have direct access to ClickHouse SQL where statement. You can write `WHERE` clause following standard SQL.

 **NOTE** : Please be aware of SQL injection, this interface must not be directly called by end-user.

If you custimized your `column_map` under your setting, you search with filter like this:

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.vectorstores import Clickhouse, ClickhouseSettings  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
      
    for i, d in enumerate(docs):  
        d.metadata = {"doc_id": i}  
      
    docsearch = Clickhouse.from_documents(docs, embeddings)  
    


```
[/code]


[code]
```python




        Inserting data...: 100%|██████████| 42/42 [00:00<00:00, 6939.56it/s]  
    


```
[/code]


[code]
```python




    meta = docsearch.metadata_column  
    output = docsearch.similarity_search_with_relevance_scores(  
        "What did the president say about Ketanji Brown Jackson?",  
        k=4,  
        where_str=f"{meta}.doc_id<10",  
    )  
    for d, dist in output:  
        print(dist, d.metadata, d.page_content[:20] + "...")  
    


```
[/code]


[code]
```python




        0.6779101415357189 {'doc_id': 0} Madam Speaker, Madam...  
        0.6997970363474885 {'doc_id': 8} And so many families...  
        0.7044504914336727 {'doc_id': 1} Groups of citizens b...  
        0.7053558702165094 {'doc_id': 6} And I’m taking robus...  
    


```
[/code]


## Deleting your data​

[code]
```python




    docsearch.drop()  
    


```
[/code]


