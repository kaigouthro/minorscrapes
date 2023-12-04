

Skip to main content

On this page

# SingleStoreDB

> SingleStoreDB is a high-performance distributed SQL database that supports deployment both in the cloud and on-premises. It provides vector storage, and vector functions including dot_product and
> euclidean_distance, thereby supporting AI applications that require text similarity matching.

This notebook shows how to use a retriever that uses `SingleStoreDB`.

[code]
```python




    # Establishing a connection to the database is facilitated through the singlestoredb Python connector.  
    # Please ensure that this connector is installed in your working environment.  
    pip install singlestoredb  
    


```
[/code]


## Create Retriever from vector store​

[code]
```python




    import getpass  
    import os  
      
    # We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.  
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
      
    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import SingleStoreDB  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
      
    # Setup connection url as environment variable  
    os.environ["SINGLESTOREDB_URL"] = "root:pass@localhost:3306/db"  
      
    # Load documents to the store  
    docsearch = SingleStoreDB.from_documents(  
        docs,  
        embeddings,  
        table_name="notebook",  # use table with a custom name  
    )  
      
    # create retriever from the vector store  
    retriever = docsearch.as_retriever(search_kwargs={"k": 2})  
    


```
[/code]


## Search with retriever​

[code]
```python




    result = retriever.get_relevant_documents(  
        "What did the president say about Ketanji Brown Jackson"  
    )  
    print(docs[0].page_content)  
    


```
[/code]


