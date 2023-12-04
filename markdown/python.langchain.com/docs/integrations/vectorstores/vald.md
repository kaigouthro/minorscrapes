

Skip to main content

On this page

# Vald

> Vald is a highly scalable distributed fast approximate nearest neighbor (ANN) dense vector search engine.

This notebook shows how to use functionality related to the `Vald` database.

To run this notebook you need a running Vald cluster. Check Get Started for more information.

See the installation instructions.

[code]
```python




    pip install vald-client-python  
    


```
[/code]


## Basic Example​

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings import HuggingFaceEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Vald  
      
    raw_documents = TextLoader("state_of_the_union.txt").load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    documents = text_splitter.split_documents(raw_documents)  
    embeddings = HuggingFaceEmbeddings()  
    db = Vald.from_documents(documents, embeddings, host="localhost", port=8080)  
    


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


## Example of using secure connection​

In order to run this notebook, it is necessary to run a Vald cluster with secure connection.

Here is an example of a Vald cluster with the following configuration using Athenz authentication.

ingress(TLS) -> authorization-proxy(Check athenz-role-auth in grpc metadata) -> vald-lb-gateway

[code]
```python




    import grpc  
      
    with open("test_root_cacert.crt", "rb") as root:  
        credentials = grpc.ssl_channel_credentials(root_certificates=root.read())  
      
    # Refresh is required for server use  
    with open(".ztoken", "rb") as ztoken:  
        token = ztoken.read().strip()  
      
    metadata = [(b"athenz-role-auth", token)]  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings import HuggingFaceEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Vald  
      
    raw_documents = TextLoader("state_of_the_union.txt").load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    documents = text_splitter.split_documents(raw_documents)  
    embeddings = HuggingFaceEmbeddings()  
      
    db = Vald.from_documents(  
        documents,  
        embeddings,  
        host="localhost",  
        port=443,  
        grpc_use_secure=True,  
        grpc_credentials=credentials,  
        grpc_metadata=metadata,  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = db.similarity_search(query, grpc_metadata=metadata)  
    docs[0].page_content  
    


```
[/code]


### Similarity search by vector​

[code]
```python




    embedding_vector = embeddings.embed_query(query)  
    docs = db.similarity_search_by_vector(embedding_vector, grpc_metadata=metadata)  
    docs[0].page_content  
    


```
[/code]


### Similarity search with score​

[code]
```python




    docs_and_scores = db.similarity_search_with_score(query, grpc_metadata=metadata)  
    docs_and_scores[0]  
    


```
[/code]


### Maximal Marginal Relevance Search (MMR)​

[code]
```python




    retriever = db.as_retriever(  
        search_kwargs={"search_type": "mmr", "grpc_metadata": metadata}  
    )  
    retriever.get_relevant_documents(query, grpc_metadata=metadata)  
    


```
[/code]


Or:

[code]
```python




    db.max_marginal_relevance_search(query, k=2, fetch_k=10, grpc_metadata=metadata)  
    


```
[/code]


