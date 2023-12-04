

Skip to main content

On this page

# DashVector

> DashVector is a fully-managed vectorDB service that supports high-dimension dense and sparse vectors, real-time insertion and filtered search. It is built to scale automatically and can adapt to
> different application requirements.

This notebook shows how to use functionality related to the `DashVector` vector database.

To use DashVector, you must have an API key. Here are the installation instructions.

## Install​

[code]
```python




    pip install dashvector dashscope  
    


```
[/code]


We want to use `DashScopeEmbeddings` so we also have to get the Dashscope API Key.

[code]
```python




    import getpass  
    import os  
      
    os.environ["DASHVECTOR_API_KEY"] = getpass.getpass("DashVector API Key:")  
    os.environ["DASHSCOPE_API_KEY"] = getpass.getpass("DashScope API Key:")  
    


```
[/code]


## Example​

[code]
```python




    from langchain.embeddings.dashscope import DashScopeEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import DashVector  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = DashScopeEmbeddings()  
    


```
[/code]


We can create DashVector from documents.

[code]
```python




    dashvector = DashVector.from_documents(docs, embeddings)  
      
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = dashvector.similarity_search(query)  
    print(docs)  
    


```
[/code]


We can add texts with meta datas and ids, and search with meta filter.

[code]
```python




    texts = ["foo", "bar", "baz"]  
    metadatas = [{"key": i} for i in range(len(texts))]  
    ids = ["0", "1", "2"]  
      
    dashvector.add_texts(texts, metadatas=metadatas, ids=ids)  
      
    docs = dashvector.similarity_search("foo", filter="key = 2")  
    print(docs)  
    


```
[/code]


[code]
```python




        [Document(page_content='baz', metadata={'key': 2})]  
    


```
[/code]


