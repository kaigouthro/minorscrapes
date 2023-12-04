

Skip to main content

# Tencent Cloud VectorDB

> Tencent Cloud VectorDB is a fully managed, self-developed, enterprise-level distributed database service designed for storing, retrieving, and analyzing multi-dimensional vector data. The database
> supports multiple index types and similarity calculation methods. A single index can support a vector scale of up to 1 billion and can support millions of QPS and millisecond-level query latency.
> Tencent Cloud Vector Database can not only provide an external knowledge base for large models to improve the accuracy of large model responses but can also be widely used in AI fields such as
> recommendation systems, NLP services, computer vision, and intelligent customer service.

This notebook shows how to use functionality related to the Tencent vector database.

To run, you should have a Database instance..

[code]
```python




    pip3 install tcvectordb  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.fake import FakeEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import TencentVectorDB  
    from langchain.vectorstores.tencentvectordb import ConnectionParams  
    


```
[/code]


[code]
```python




    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
    embeddings = FakeEmbeddings(size=128)  
    


```
[/code]


[code]
```python




    conn_params = ConnectionParams(  
        url="http://10.0.X.X",  
        key="eC4bLRy2va******************************",  
        username="root",  
        timeout=20,  
    )  
      
    vector_db = TencentVectorDB.from_documents(  
        docs,  
        embeddings,  
        connection_params=conn_params,  
        # drop_old=True,  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vector_db.similarity_search(query)  
    docs[0].page_content  
    


```
[/code]


[code]
```python




    vector_db = TencentVectorDB(embeddings, conn_params)  
      
    vector_db.add_texts(["Ankush went to Princeton"])  
    query = "Where did Ankush go to college?"  
    docs = vector_db.max_marginal_relevance_search(query)  
    docs[0].page_content  
    


```
[/code]


