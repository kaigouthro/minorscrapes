

Skip to main content

# SingleStoreDB

> SingleStoreDB is a high-performance distributed SQL database that supports deployment both in the cloud and on-premises. It provides vector storage, and vector functions including dot_product and
> euclidean_distance, thereby supporting AI applications that require text similarity matching.

This tutorial illustrates how to work with vector data in SingleStoreDB.

[code]
```python




    # Establishing a connection to the database is facilitated through the singlestoredb Python connector.  
    # Please ensure that this connector is installed in your working environment.  
    pip install singlestoredb  
    


```
[/code]


[code]
```python




    import getpass  
    import os  
      
    # We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.  
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import SingleStoreDB  
    


```
[/code]


[code]
```python




    # Load text samples  
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


There are several ways to establish a connection to the database. You can either set up environment variables or pass named parameters to the `SingleStoreDB constructor`. Alternatively, you may
provide these parameters to the `from_documents` and `from_texts` methods.

[code]
```python




    # Setup connection url as environment variable  
    os.environ["SINGLESTOREDB_URL"] = "root:pass@localhost:3306/db"  
      
    # Load documents to the store  
    docsearch = SingleStoreDB.from_documents(  
        docs,  
        embeddings,  
        table_name="notebook",  # use table with a custom name  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = docsearch.similarity_search(query)  # Find documents that correspond to the query  
    print(docs[0].page_content)  
    


```
[/code]


