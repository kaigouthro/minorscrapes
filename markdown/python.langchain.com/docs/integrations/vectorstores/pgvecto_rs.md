

Skip to main content

On this page

# PGVecto.rs

This notebook shows how to use functionality related to the Postgres vector database (pgvecto.rs). You need to install SQLAlchemy >= 2 manually.

[code]
```python




    ## Loading Environment Variables  
    from dotenv import load_dotenv  
      
    load_dotenv()  
    


```
[/code]


[code]
```python




    from typing import List  
      
    from langchain.docstore.document import Document  
    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores.pgvecto_rs import PGVecto_rs  
    


```
[/code]


[code]
```python




    loader = TextLoader("../../../state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


Start the database with the official demo docker image.

[code]
```python




    docker run --name pgvecto-rs-demo -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d tensorchord/pgvecto-rs:latest  
    


```
[/code]


Then contruct the db URL

[code]
```python




    ## PGVecto.rs needs the connection string to the database.  
    ## We will load it from the environment variables.  
    import os  
      
    PORT = os.getenv("DB_PORT", 5432)  
    HOST = os.getenv("DB_HOST", "localhost")  
    USER = os.getenv("DB_USER", "postgres")  
    PASS = os.getenv("DB_PASS", "mysecretpassword")  
    DB_NAME = os.getenv("DB_NAME", "postgres")  
      
    # Run tests with shell:  
    URL = "postgresql+psycopg://{username}:{password}@{host}:{port}/{db_name}".format(  
        port=PORT,  
        host=HOST,  
        username=USER,  
        password=PASS,  
        db_name=DB_NAME,  
    )  
    


```
[/code]


Finally, create the VectorStore from the documents:

[code]
```python




    db1 = PGVecto_rs.from_documents(  
        documents=docs,  
        embedding=embeddings,  
        db_url=URL,  
        # The table name is f"collection_{collection_name}", so that it should be unique.  
        collection_name="state_of_the_union",  
    )  
    


```
[/code]


You can connect to the table laterly with:

[code]
```python




    # Create new empty vectorstore with collection_name.  
    # Or connect to an existing vectorstore in database if exists.  
    # Arguments should be the same as when the vectorstore was created.  
    db1 = PGVecto_rs.from_collection_name(  
        embedding=embeddings,  
        db_url=URL,  
        collection_name="state_of_the_union",  
    )  
    


```
[/code]


Make sure that the user is permitted to create a table.

## Similarity search with score​

### Similarity Search with Euclidean Distance (Default)​

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs: List[Document] = db1.similarity_search(query, k=4)  
    


```
[/code]


[code]
```python




    for doc in docs:  
        print(doc.page_content)  
        print("======================")  
    


```
[/code]


