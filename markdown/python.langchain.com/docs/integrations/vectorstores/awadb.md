

Skip to main content

On this page

# AwaDB

> AwaDB is an AI Native database for the search and storage of embedding vectors used by LLM Applications.

This notebook shows how to use functionality related to the `AwaDB`.

[code]
```python




    pip install awadb  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import AwaDB  
    


```
[/code]


[code]
```python




    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
    


```
[/code]


[code]
```python




    db = AwaDB.from_documents(docs)  
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = db.similarity_search(query)  
    


```
[/code]


[code]
```python




    print(docs[0].page_content)  
    


```
[/code]


[code]
```python




        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
    


```
[/code]


## Similarity search with score​

The returned distance score is between 0-1. 0 is dissimilar, 1 is the most similar

[code]
```python




    docs = db.similarity_search_with_score(query)  
    


```
[/code]


[code]
```python




    print(docs[0])  
    


```
[/code]


[code]
```python




        (Document(page_content='And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../modules/state_of_the_union.txt'}), 0.561813814013747)  
    


```
[/code]


## Restore the table created and added data before​

AwaDB automatically persists added document data.

If you can restore the table you created and added before, you can just do this as below:

[code]
```python




    awadb_client = awadb.Client()  
    ret = awadb_client.Load("langchain_awadb")  
    if ret:  
        print("awadb load table success")  
    else:  
        print("awadb load table failed")  
    


```
[/code]


awadb load table success

