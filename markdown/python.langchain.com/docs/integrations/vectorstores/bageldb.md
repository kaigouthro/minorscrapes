

Skip to main content

On this page

# BagelDB

> BagelDB (`Open Vector Database for AI`), is like GitHub for AI data. It is a collaborative platform where users can create, share, and manage vector datasets. It can support private projects for
> independent developers, internal collaborations for enterprises, and public contributions for data DAOs.

### Installation and Setup​

[code]
```python




    pip install betabageldb  
    


```
[/code]


## Create VectorStore from texts​

[code]
```python




    from langchain.vectorstores import Bagel  
      
    texts = ["hello bagel", "hello langchain", "I love salad", "my car", "a dog"]  
    # create cluster and add texts  
    cluster = Bagel.from_texts(cluster_name="testing", texts=texts)  
    


```
[/code]


[code]
```python




    # similarity search  
    cluster.similarity_search("bagel", k=3)  
    


```
[/code]


[code]
```python




        [Document(page_content='hello bagel', metadata={}),  
         Document(page_content='my car', metadata={}),  
         Document(page_content='I love salad', metadata={})]  
    


```
[/code]


[code]
```python




    # the score is a distance metric, so lower is better  
    cluster.similarity_search_with_score("bagel", k=3)  
    


```
[/code]


[code]
```python




        [(Document(page_content='hello bagel', metadata={}), 0.27392977476119995),  
         (Document(page_content='my car', metadata={}), 1.4783176183700562),  
         (Document(page_content='I love salad', metadata={}), 1.5342965126037598)]  
    


```
[/code]


[code]
```python




    # delete the cluster  
    cluster.delete_cluster()  
    


```
[/code]


## Create VectorStore from docs​

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.text_splitter import CharacterTextSplitter  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)[:10]  
    


```
[/code]


[code]
```python




    # create cluster with docs  
    cluster = Bagel.from_documents(cluster_name="testing_with_docs", documents=docs)  
    


```
[/code]


[code]
```python




    # similarity search  
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = cluster.similarity_search(query)  
    print(docs[0].page_content[:102])  
    


```
[/code]


[code]
```python




        Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the   
    


```
[/code]


## Get all text/doc from Cluster​

[code]
```python




    texts = ["hello bagel", "this is langchain"]  
    cluster = Bagel.from_texts(cluster_name="testing", texts=texts)  
    cluster_data = cluster.get()  
    


```
[/code]


[code]
```python




    # all keys  
    cluster_data.keys()  
    


```
[/code]


[code]
```python




        dict_keys(['ids', 'embeddings', 'metadatas', 'documents'])  
    


```
[/code]


[code]
```python




    # all values and keys  
    cluster_data  
    


```
[/code]


[code]
```python




        {'ids': ['578c6d24-3763-11ee-a8ab-b7b7b34f99ba',  
          '578c6d25-3763-11ee-a8ab-b7b7b34f99ba',  
          'fb2fc7d8-3762-11ee-a8ab-b7b7b34f99ba',  
          'fb2fc7d9-3762-11ee-a8ab-b7b7b34f99ba',  
          '6b40881a-3762-11ee-a8ab-b7b7b34f99ba',  
          '6b40881b-3762-11ee-a8ab-b7b7b34f99ba',  
          '581e691e-3762-11ee-a8ab-b7b7b34f99ba',  
          '581e691f-3762-11ee-a8ab-b7b7b34f99ba'],  
         'embeddings': None,  
         'metadatas': [{}, {}, {}, {}, {}, {}, {}, {}],  
         'documents': ['hello bagel',  
          'this is langchain',  
          'hello bagel',  
          'this is langchain',  
          'hello bagel',  
          'this is langchain',  
          'hello bagel',  
          'this is langchain']}  
    


```
[/code]


[code]
```python




    cluster.delete_cluster()  
    


```
[/code]


## Create cluster with metadata & filter using metadata​

[code]
```python




    texts = ["hello bagel", "this is langchain"]  
    metadatas = [{"source": "notion"}, {"source": "google"}]  
      
    cluster = Bagel.from_texts(cluster_name="testing", texts=texts, metadatas=metadatas)  
    cluster.similarity_search_with_score("hello bagel", where={"source": "notion"})  
    


```
[/code]


[code]
```python




        [(Document(page_content='hello bagel', metadata={'source': 'notion'}), 0.0)]  
    


```
[/code]


[code]
```python




    # delete the cluster  
    cluster.delete_cluster()  
    


```
[/code]


