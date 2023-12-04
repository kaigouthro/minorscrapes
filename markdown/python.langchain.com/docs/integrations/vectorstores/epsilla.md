

Skip to main content

# Epsilla

> Epsilla is an open-source vector database that leverages the advanced parallel graph traversal techniques for vector indexing. Epsilla is licensed under GPL-3.0.

This notebook shows how to use the functionalities related to the `Epsilla` vector database.

As a prerequisite, you need to have a running Epsilla vector database (for example, through our docker image), and install the `pyepsilla` package. View full docs at docs.

[code]
```python




    pip/pip3 install pyepsilla  
    


```
[/code]


We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.

[code]
```python




    import getpass  
    import os  
      
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


OpenAI API Key: ········

[code]
```python




    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.vectorstores import Epsilla  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.text_splitter import CharacterTextSplitter  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
      
    documents = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0).split_documents(  
        documents  
    )  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


Epsilla vectordb is running with default host "localhost" and port "8888". We have a custom db path, db name and collection name instead of the default ones.

[code]
```python




    from pyepsilla import vectordb  
      
    client = vectordb.Client()  
    vector_store = Epsilla.from_documents(  
        documents,  
        embeddings,  
        client,  
        db_path="/tmp/mypath",  
        db_name="MyDB",  
        collection_name="MyCollection",  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vector_store.similarity_search(query)  
    print(docs[0].page_content)  
    


```
[/code]


In state after state, new laws have been passed, not only to suppress the vote, but to subvert entire elections.

We cannot let this happen.

Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.

Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme
Court. Justice Breyer, thank you for your service.

One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.

And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.

