

Skip to main content

On this page

# SemaDB

> SemaDB from SemaFind is a no fuss vector similarity database for building AI applications. The hosted `SemaDB Cloud` offers a no fuss developer experience to get started.

The full documentation of the API along with examples and an interactive playground is available on RapidAPI.

This notebook demonstrates usage of the `SemaDB Cloud` vector store.

## Load document embeddings​

To run things locally, we are using Sentence Transformers which are commonly used for embedding sentences. You can use any embedding model LangChain offers.

[code]
```python




    pip install sentence_transformers  
    


```
[/code]


[code]
```python




    from langchain.embeddings import HuggingFaceEmbeddings  
      
    embeddings = HuggingFaceEmbeddings()  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.text_splitter import CharacterTextSplitter  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
    print(len(docs))  
    


```
[/code]


[code]
```python




        114  
    


```
[/code]


## Connect to SemaDB​

SemaDB Cloud uses RapidAPI keys to authenticate. You can obtain yours by creating a free RapidAPI account.

[code]
```python




    import getpass  
    import os  
      
    os.environ["SEMADB_API_KEY"] = getpass.getpass("SemaDB API Key:")  
    


```
[/code]


[code]
```python




        SemaDB API Key: ········  
    


```
[/code]


[code]
```python




    from langchain.vectorstores import SemaDB  
    from langchain.vectorstores.utils import DistanceStrategy  
    


```
[/code]


The parameters to the SemaDB vector store reflect the API directly:

  * "mycollection": is the collection name in which we will store these vectors.
  * 768: is dimensions of the vectors. In our case, the sentence transformer embeddings yield 768 dimensional vectors.
  * API_KEY: is your RapidAPI key.
  * embeddings: correspond to how the embeddings of documents, texts and queries will be generated.
  * DistanceStrategy: is the distance metric used. The wrapper automatically normalises vectors if COSINE is used.

[code]
```python




    db = SemaDB("mycollection", 768, embeddings, DistanceStrategy.COSINE)  
      
    # Create collection if running for the first time. If the collection  
    # already exists this will fail.  
    db.create_collection()  
    


```
[/code]


[code]
```python




        True  
    


```
[/code]


The SemaDB vector store wrapper adds the document text as point metadata to collect later. Storing large chunks of text is _not recommended_. If you are indexing a large collection, we instead
recommend storing references to the documents such as external Ids.

[code]
```python




    db.add_documents(docs)[:2]  
    


```
[/code]


[code]
```python




        ['813c7ef3-9797-466b-8afa-587115592c6c',  
         'fc392f7f-082b-4932-bfcc-06800db5e017']  
    


```
[/code]


## Similarity Search​

We use the default LangChain similarity search interface to search for the most similar sentences.

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = db.similarity_search(query)  
    print(docs[0].page_content)  
    


```
[/code]


[code]
```python




        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
    


```
[/code]


[code]
```python




    docs = db.similarity_search_with_score(query)  
    docs[0]  
    


```
[/code]


[code]
```python




        (Document(page_content='And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../modules/state_of_the_union.txt', 'text': 'And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.'}),  
         0.42369342)  
    


```
[/code]


## Clean up​

You can delete the collection to remove all data.

[code]
```python




    db.delete_collection()  
    


```
[/code]


[code]
```python




        True  
    


```
[/code]


