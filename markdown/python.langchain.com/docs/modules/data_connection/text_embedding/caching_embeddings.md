

Skip to main content

On this page

# Caching

Embeddings can be stored or temporarily cached to avoid needing to recompute them.

Caching embeddings can be done using a `CacheBackedEmbeddings`. The cache backed embedder is a wrapper around an embedder that caches embeddings in a key-value store. The text is hashed and the hash
is used as the key in the cache.

The main supported way to initialized a `CacheBackedEmbeddings` is `from_bytes_store`. This takes in the following parameters:

  * underlying_embedder: The embedder to use for embedding.
  * document_embedding_cache: The cache to use for storing document embeddings.
  * namespace: (optional, defaults to `""`) The namespace to use for document cache. This namespace is used to avoid collisions with other caches. For example, set it to the name of the embedding model used.

 **Attention** : Be sure to set the `namespace` parameter to avoid collisions of the same text embedded using different embeddings models.

[code]
```python




    from langchain.embeddings import CacheBackedEmbeddings, OpenAIEmbeddings  
    from langchain.storage import (  
        InMemoryStore,  
        LocalFileStore,  
        RedisStore,  
        UpstashRedisStore,  
    )  
    


```
[/code]


## Using with a vector store​

First, let's see an example that uses the local file system for storing embeddings and uses FAISS vector store for retrieval.

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    


```
[/code]


[code]
```python




    underlying_embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    fs = LocalFileStore("./cache/")  
      
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(  
        underlying_embeddings, fs, namespace=underlying_embeddings.model  
    )  
    


```
[/code]


The cache is empty prior to embedding:

[code]
```python




    list(fs.yield_keys())  
    


```
[/code]


[code]
```python




        []  
    


```
[/code]


Load the document, split it into chunks, embed each chunk and load it into the vector store.

[code]
```python




    raw_documents = TextLoader("../state_of_the_union.txt").load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    documents = text_splitter.split_documents(raw_documents)  
    


```
[/code]


Create the vector store:

[code]
```python




    db = FAISS.from_documents(documents, cached_embedder)  
    


```
[/code]


[code]
```python




        CPU times: user 608 ms, sys: 58.9 ms, total: 667 ms  
        Wall time: 1.3 s  
    


```
[/code]


If we try to create the vector store again, it'll be much faster since it does not need to re-compute any embeddings.

[code]
```python




    db2 = FAISS.from_documents(documents, cached_embedder)  
    


```
[/code]


[code]
```python




        CPU times: user 33.6 ms, sys: 3.96 ms, total: 37.6 ms  
        Wall time: 36.8 ms  
    


```
[/code]


And here are some of the embeddings that got created:

[code]
```python




    list(fs.yield_keys())[:5]  
    


```
[/code]


[code]
```python




        ['text-embedding-ada-002614d7cf6-46f1-52fa-9d3a-740c39e7a20e',  
         'text-embedding-ada-0020fc1ede2-407a-5e14-8f8f-5642214263f5',  
         'text-embedding-ada-002e4ad20ef-dfaa-5916-9459-f90c6d8e8159',  
         'text-embedding-ada-002a5ef11e4-0474-5725-8d80-81c91943b37f',  
         'text-embedding-ada-00281426526-23fe-58be-9e84-6c7c72c8ca9a']  
    


```
[/code]


## In Memory​

This section shows how to set up an in memory cache for embeddings. This type of cache is primarily useful for unit tests or prototyping. Do **not** use this cache if you need to actually store the
embeddings.

[code]
```python




    store = InMemoryStore()  
    


```
[/code]


[code]
```python




    underlying_embeddings = OpenAIEmbeddings()  
    embedder = CacheBackedEmbeddings.from_bytes_store(  
        underlying_embeddings, store, namespace=underlying_embeddings.model  
    )  
    


```
[/code]


[code]
```python




    embeddings = embedder.embed_documents(["hello", "goodbye"])  
    


```
[/code]


[code]
```python




        CPU times: user 10.9 ms, sys: 916 µs, total: 11.8 ms  
        Wall time: 159 ms  
    


```
[/code]


The second time we try to embed the embedding time is only 2 ms because the embeddings are looked up in the cache.

[code]
```python




    embeddings_from_cache = embedder.embed_documents(["hello", "goodbye"])  
    


```
[/code]


[code]
```python




        CPU times: user 1.67 ms, sys: 342 µs, total: 2.01 ms  
        Wall time: 2.01 ms  
    


```
[/code]


[code]
```python




    embeddings == embeddings_from_cache  
    


```
[/code]


[code]
```python




        True  
    


```
[/code]


## File system​

This section covers how to use a file system store.

[code]
```python




    fs = LocalFileStore("./test_cache/")  
    


```
[/code]


[code]
```python




    embedder2 = CacheBackedEmbeddings.from_bytes_store(  
        underlying_embeddings, fs, namespace=underlying_embeddings.model  
    )  
    


```
[/code]


[code]
```python




    embeddings = embedder2.embed_documents(["hello", "goodbye"])  
    


```
[/code]


[code]
```python




        CPU times: user 6.89 ms, sys: 4.89 ms, total: 11.8 ms  
        Wall time: 184 ms  
    


```
[/code]


[code]
```python




    embeddings = embedder2.embed_documents(["hello", "goodbye"])  
    


```
[/code]


[code]
```python




        CPU times: user 0 ns, sys: 3.24 ms, total: 3.24 ms  
        Wall time: 2.84 ms  
    


```
[/code]


Here are the embeddings that have been persisted to the directory `./test_cache`.

Notice that the embedder takes a namespace parameter.

[code]
```python




    list(fs.yield_keys())  
    


```
[/code]


[code]
```python




        ['text-embedding-ada-002e885db5b-c0bd-5fbc-88b1-4d1da6020aa5',  
         'text-embedding-ada-0026ba52e44-59c9-5cc9-a084-284061b13c80']  
    


```
[/code]


## Upstash Redis Store​

[code]
```python




    from langchain.storage.upstash_redis import UpstashRedisStore  
    


```
[/code]


[code]
```python




    from upstash_redis import Redis  
      
    URL = "<UPSTASH_REDIS_REST_URL>"  
    TOKEN = "<UPSTASH_REDIS_REST_TOKEN>"  
      
    redis_client = Redis(url=URL, token=TOKEN)  
    store = UpstashRedisStore(client=redis_client, ttl=None, namespace="test-ns")  
      
    underlying_embeddings = OpenAIEmbeddings()  
    embedder = CacheBackedEmbeddings.from_bytes_store(  
        underlying_embeddings, store, namespace=underlying_embeddings.model  
    )  
    


```
[/code]


[code]
```python




    embeddings = embedder.embed_documents(["welcome", "goodbye"])  
    


```
[/code]


[code]
```python




    embeddings = embedder.embed_documents(["welcome", "goodbye"])  
    


```
[/code]


[code]
```python




    list(store.yield_keys())  
    


```
[/code]


[code]
```python




    list(store.client.scan(0))  
    


```
[/code]


## Redis Store​

[code]
```python




    from langchain.storage import RedisStore  
    


```
[/code]


[code]
```python




    # For cache isolation can use a separate DB  
    # Or additional namepace  
    store = RedisStore(  
        redis_url="redis://localhost:6379",  
        client_kwargs={"db": 2},  
        namespace="embedding_caches",  
    )  
      
    underlying_embeddings = OpenAIEmbeddings()  
    embedder = CacheBackedEmbeddings.from_bytes_store(  
        underlying_embeddings, store, namespace=underlying_embeddings.model  
    )  
    


```
[/code]


[code]
```python




    embeddings = embedder.embed_documents(["hello", "goodbye"])  
    


```
[/code]


[code]
```python




        CPU times: user 3.99 ms, sys: 0 ns, total: 3.99 ms  
        Wall time: 3.5 ms  
    


```
[/code]


[code]
```python




    embeddings = embedder.embed_documents(["hello", "goodbye"])  
    


```
[/code]


[code]
```python




        CPU times: user 2.47 ms, sys: 767 µs, total: 3.24 ms  
        Wall time: 2.75 ms  
    


```
[/code]


[code]
```python




    list(store.yield_keys())  
    


```
[/code]


[code]
```python




        ['text-embedding-ada-002e885db5b-c0bd-5fbc-88b1-4d1da6020aa5',  
         'text-embedding-ada-0026ba52e44-59c9-5cc9-a084-284061b13c80']  
    


```
[/code]


[code]
```python




    list(store.client.scan_iter())  
    


```
[/code]


[code]
```python




        [b'embedding_caches/text-embedding-ada-002e885db5b-c0bd-5fbc-88b1-4d1da6020aa5',  
         b'embedding_caches/text-embedding-ada-0026ba52e44-59c9-5cc9-a084-284061b13c80']  
    


```
[/code]


