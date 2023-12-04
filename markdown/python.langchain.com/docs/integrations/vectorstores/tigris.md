

Skip to main content

On this page

# Tigris

> Tigris is an open-source Serverless NoSQL Database and Search Platform designed to simplify building high-performance vector search applications. `Tigris` eliminates the infrastructure complexity of
> managing, operating, and synchronizing multiple tools, allowing you to focus on building great applications instead.

This notebook guides you how to use Tigris as your VectorStore

 **Pre requisites**

  1. An OpenAI account. You can sign up for an account here
  2. Sign up for a free Tigris account. Once you have signed up for the Tigris account, create a new project called `vectordemo`. Next, make a note of the _Uri_ for the region you've created your project in, the **clientId** and **clientSecret**. You can get all this information from the **Application Keys** section of the project.

Let's first install our dependencies:

[code]
```python




    pip install tigrisdb openapi-schema-pydantic openai tiktoken  
    


```
[/code]


We will load the `OpenAI` api key and `Tigris` credentials in our environment

[code]
```python




    import getpass  
    import os  
      
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    os.environ["TIGRIS_PROJECT"] = getpass.getpass("Tigris Project Name:")  
    os.environ["TIGRIS_CLIENT_ID"] = getpass.getpass("Tigris Client Id:")  
    os.environ["TIGRIS_CLIENT_SECRET"] = getpass.getpass("Tigris Client Secret:")  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Tigris  
    


```
[/code]


### Initialize Tigris vector store​

Let's import our test dataset:

[code]
```python




    loader = TextLoader("../../../state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    vector_store = Tigris.from_documents(docs, embeddings, index_name="my_embeddings")  
    


```
[/code]


### Similarity Search​

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    found_docs = vector_store.similarity_search(query)  
    print(found_docs)  
    


```
[/code]


### Similarity Search with score (vector distance)​

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    result = vector_store.similarity_search_with_score(query)  
    for doc, score in result:  
        print(f"document={doc}, score={score}")  
    


```
[/code]


