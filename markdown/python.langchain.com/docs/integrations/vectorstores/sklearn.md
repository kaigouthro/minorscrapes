

Skip to main content

On this page

# scikit-learn

> scikit-learn is an open-source collection of machine learning algorithms, including some implementations of the k nearest neighbors. `SKLearnVectorStore` wraps this implementation and adds the
> possibility to persist the vector store in json, bson (binary json) or Apache Parquet format.

This notebook shows how to use the `SKLearnVectorStore` vector database.

[code]
```python




    # # if you plan to use bson serialization, install also:  
    # %pip install bson  
      
    # # if you plan to use parquet serialization, install also:  
    %pip install pandas pyarrow  
    


```
[/code]


To use OpenAI embeddings, you will need an OpenAI key. You can get one at https://platform.openai.com/account/api-keys or feel free to use any other embeddings.

[code]
```python




    import os  
    from getpass import getpass  
      
    os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI key:")  
    


```
[/code]


## Basic usage​

### Load a sample document corpus​

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import SKLearnVectorStore  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


### Create the SKLearnVectorStore, index the document corpus and run a sample query​

[code]
```python




    import tempfile  
      
    persist_path = os.path.join(tempfile.gettempdir(), "union.parquet")  
      
    vector_store = SKLearnVectorStore.from_documents(  
        documents=docs,  
        embedding=embeddings,  
        persist_path=persist_path,  # persist_path and serializer are optional  
        serializer="parquet",  
    )  
      
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vector_store.similarity_search(query)  
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


## Saving and loading a vector store​

[code]
```python




    vector_store.persist()  
    print("Vector store was persisted to", persist_path)  
    


```
[/code]


[code]
```python




        Vector store was persisted to /var/folders/6r/wc15p6m13nl_nl_n_xfqpc5c0000gp/T/union.parquet  
    


```
[/code]


[code]
```python




    vector_store2 = SKLearnVectorStore(  
        embedding=embeddings, persist_path=persist_path, serializer="parquet"  
    )  
    print("A new instance of vector store was loaded from", persist_path)  
    


```
[/code]


[code]
```python




        A new instance of vector store was loaded from /var/folders/6r/wc15p6m13nl_nl_n_xfqpc5c0000gp/T/union.parquet  
    


```
[/code]


[code]
```python




    docs = vector_store2.similarity_search(query)  
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


## Clean-up​

[code]
```python




    os.remove(persist_path)  
    


```
[/code]


