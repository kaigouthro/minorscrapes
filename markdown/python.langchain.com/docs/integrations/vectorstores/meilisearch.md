

Skip to main content

On this page

# Meilisearch

> Meilisearch is an open-source, lightning-fast, and hyper relevant search engine. It comes with great defaults to help developers build snappy search experiences.
>
> You can self-host Meilisearch or run on Meilisearch Cloud.

Meilisearch v1.3 supports vector search. This page guides you through integrating Meilisearch as a vector store and using it to perform vector search.

## Setup​

### Launching a Meilisearch instance​

You will need a running Meilisearch instance to use as your vector store. You can run Meilisearch in local or create a Meilisearch Cloud account.

As of Meilisearch v1.3, vector storage is an experimental feature. After launching your Meilisearch instance, you need to **enable vector storage**. For self-hosted Meilisearch, read the docs on
enabling experimental features. On **Meilisearch Cloud** , enable _Vector Store_ via your project _Settings_ page.

You should now have a running Meilisearch instance with vector storage enabled. 🎉

### Credentials​

To interact with your Meilisearch instance, the Meilisearch SDK needs a host (URL of your instance) and an API key.

 **Host**

  * In **local** , the default host is `localhost:7700`
  * On **Meilisearch Cloud** , find the host in your project _Settings_ page

 **API keys**

Meilisearch instance provides you with three API keys out of the box:

  * A `MASTER KEY` — it should only be used to create your Meilisearch instance
  * A `ADMIN KEY` — use it only server-side to update your database and its settings
  * A `SEARCH KEY` — a key that you can safely share in front-end applications

You can create additional API keys as needed.

### Installing dependencies​

This guide uses the Meilisearch Python SDK. You can install it by running:

[code]
```python




    pip install meilisearch  
    


```
[/code]


For more information, refer to the Meilisearch Python SDK documentation.

## Examples​

There are multiple ways to initialize the Meilisearch vector store: providing a Meilisearch client or the _URL_ and _API key_ as needed. In our examples, the credentials will be loaded from the
environment.

You can make environment variables available in your Notebook environment by using `os` and `getpass`. You can use this technique for all the following examples.

[code]
```python




    import getpass  
    import os  
      
    os.environ["MEILI_HTTP_ADDR"] = getpass.getpass("Meilisearch HTTP address and port:")  
    os.environ["MEILI_MASTER_KEY"] = getpass.getpass("Meilisearch API Key:")  
    


```
[/code]


We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.

[code]
```python




    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


### Adding text and embeddings​

This example adds text to the Meilisearch vector database without having to initialize a Meilisearch vector store.

[code]
```python




    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Meilisearch  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    with open("../../modules/state_of_the_union.txt") as f:  
        state_of_the_union = f.read()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    texts = text_splitter.split_text(state_of_the_union)  
    


```
[/code]


[code]
```python




    # Use Meilisearch vector store to store texts & associated embeddings as vector  
    vector_store = Meilisearch.from_texts(texts=texts, embedding=embeddings)  
    


```
[/code]


Behind the scenes, Meilisearch will convert the text to multiple vectors. This will bring us to the same result as the following example.

### Adding documents and embeddings​

In this example, we'll use Langchain TextSplitter to split the text in multiple documents. Then, we'll store these documents along with their embeddings.

[code]
```python




    from langchain.document_loaders import TextLoader  
      
    # Load text  
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
      
    # Create documents  
    docs = text_splitter.split_documents(documents)  
      
    # Import documents & embeddings in the vector store  
    vector_store = Meilisearch.from_documents(documents=documents, embedding=embeddings)  
      
    # Search in our vector store  
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vector_store.similarity_search(query)  
    print(docs[0].page_content)  
    


```
[/code]


## Add documents by creating a Meilisearch Vectorstore​

In this approach, we create a vector store object and add documents to it.

[code]
```python




    import meilisearch  
    from langchain.vectorstores import Meilisearch  
      
    client = meilisearch.Client(url="http://127.0.0.1:7700", api_key="***")  
    vector_store = Meilisearch(  
        embedding=embeddings, client=client, index_name="langchain_demo", text_key="text"  
    )  
    vector_store.add_documents(documents)  
    


```
[/code]


## Similarity Search with score​

This specific method allows you to return the documents and the distance score of the query to them.

[code]
```python




    docs_and_scores = vector_store.similarity_search_with_score(query)  
    docs_and_scores[0]  
    


```
[/code]


## Similarity Search by vector​

[code]
```python




    embedding_vector = embeddings.embed_query(query)  
    docs_and_scores = vector_store.similarity_search_by_vector(embedding_vector)  
    docs_and_scores[0]  
    


```
[/code]


## Additional resources​

Documentation

  * Meilisearch
  * Meilisearch Python SDK

Open-source repositories

  * Meilisearch repository
  * Meilisearch Python SDK

