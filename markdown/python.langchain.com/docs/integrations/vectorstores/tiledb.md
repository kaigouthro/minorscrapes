

Skip to main content

On this page

# TileDB

> TileDB is a powerful engine for indexing and querying dense and sparse multi-dimensional arrays.

> TileDB offers ANN search capabilities using the TileDB-Vector-Search module. It provides serverless execution of ANN queries and storage of vector indexes both on local disk and cloud object stores
> (i.e. AWS S3).

More details in:

  * Why TileDB as a Vector Database
  * TileDB 101: Vector Search

This notebook shows how to use the `TileDB` vector database.

[code]
```python




    pip install tiledb-vector-search  
    


```
[/code]


## Basic Example​

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings import HuggingFaceEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import TileDB  
      
    raw_documents = TextLoader("../../modules/state_of_the_union.txt").load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    documents = text_splitter.split_documents(raw_documents)  
    embeddings = HuggingFaceEmbeddings()  
    db = TileDB.from_documents(  
        documents, embeddings, index_uri="/tmp/tiledb_index", index_type="FLAT"  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = db.similarity_search(query)  
    docs[0].page_content  
    


```
[/code]


### Similarity search by vector​

[code]
```python




    embedding_vector = embeddings.embed_query(query)  
    docs = db.similarity_search_by_vector(embedding_vector)  
    docs[0].page_content  
    


```
[/code]


### Similarity search with score​

[code]
```python




    docs_and_scores = db.similarity_search_with_score(query)  
    docs_and_scores[0]  
    


```
[/code]


## Maximal Marginal Relevance Search (MMR)​

In addition to using similarity search in the retriever object, you can also use `mmr` as retriever.

[code]
```python




    retriever = db.as_retriever(search_type="mmr")  
    retriever.get_relevant_documents(query)  
    


```
[/code]


Or use `max_marginal_relevance_search` directly:

[code]
```python




    db.max_marginal_relevance_search(query, k=2, fetch_k=10)  
    


```
[/code]


