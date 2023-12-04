

Skip to main content

# Azure Cosmos DB

> Azure Cosmos DB for MongoDB vCore makes it easy to create a database with full native MongoDB support. You can apply your MongoDB experience and continue to use your favorite MongoDB drivers, SDKs,
> and tools by pointing your application to the API for MongoDB vCore account's connection string. Use vector search in Azure Cosmos DB for MongoDB vCore to seamlessly integrate your AI-based
> applications with your data that's stored in Azure Cosmos DB.

This notebook shows you how to leverage the Vector Search capabilities within Azure Cosmos DB for Mongo vCore to store documents in collections, create indicies and perform vector search queries using
approximate nearest neighbor algorithms such as COS (cosine distance), L2 (Euclidean distance), and IP (inner product) to locate documents close to the query vectors.

Azure Cosmos DB for MongoDB vCore provides developers with a fully managed MongoDB-compatible database service for building modern applications with a familiar architecture.

With Cosmos DB for MongoDB vCore, developers can enjoy the benefits of native Azure integrations, low total cost of ownership (TCO), and the familiar vCore architecture when migrating existing
applications or building new ones.

Sign Up for free to get started today.

[code]
```python




    pip install pymongo  
    


```
[/code]


[code]
```python




        Requirement already satisfied: pymongo in /Users/iekpo/Langchain/langchain-python/.venv/lib/python3.10/site-packages (4.5.0)  
        Requirement already satisfied: dnspython<3.0.0,>=1.16.0 in /Users/iekpo/Langchain/langchain-python/.venv/lib/python3.10/site-packages (from pymongo) (2.4.2)  
    


```
[/code]


[code]
```python




    import os  
      
    CONNECTION_STRING = "AZURE COSMOS DB MONGO vCORE connection string"  
    INDEX_NAME = "izzy-test-index"  
    NAMESPACE = "izzy_test_db.izzy_test_collection"  
    DB_NAME, COLLECTION_NAME = NAMESPACE.split(".")  
    


```
[/code]


We want to use `OpenAIEmbeddings` so we need to set up our Azure OpenAI API Key alongside other environment variables.

[code]
```python




    # Set up the OpenAI Environment Variables  
    os.environ["OPENAI_API_TYPE"] = "azure"  
    os.environ["OPENAI_API_VERSION"] = "2023-05-15"  
    os.environ[  
        "OPENAI_API_BASE"  
    ] = "YOUR_OPEN_AI_ENDPOINT"  # https://example.openai.azure.com/  
    os.environ["OPENAI_API_KEY"] = "YOUR_OPEN_AI_KEY"  
    os.environ[  
        "OPENAI_EMBEDDINGS_DEPLOYMENT"  
    ] = "smart-agent-embedding-ada"  # the deployment name for the embedding model  
    os.environ["OPENAI_EMBEDDINGS_MODEL_NAME"] = "text-embedding-ada-002"  # the model name  
    


```
[/code]


Now, we need to load the documents into the collection, create the index and then run our queries against the index to retrieve matches.

Please refer to the documentation if you have questions about certain parameters

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores.azure_cosmos_db_vector_search import (  
        AzureCosmosDBVectorSearch,  
        CosmosDBSimilarityType,  
    )  
      
    SOURCE_FILE_NAME = "../../modules/state_of_the_union.txt"  
      
    loader = TextLoader(SOURCE_FILE_NAME)  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    # OpenAI Settings  
    model_deployment = os.getenv(  
        "OPENAI_EMBEDDINGS_DEPLOYMENT", "smart-agent-embedding-ada"  
    )  
    model_name = os.getenv("OPENAI_EMBEDDINGS_MODEL_NAME", "text-embedding-ada-002")  
      
      
    openai_embeddings: OpenAIEmbeddings = OpenAIEmbeddings(  
        deployment=model_deployment, model=model_name, chunk_size=1  
    )  
    


```
[/code]


[code]
```python




    from pymongo import MongoClient  
      
    INDEX_NAME = "izzy-test-index-2"  
    NAMESPACE = "izzy_test_db.izzy_test_collection"  
    DB_NAME, COLLECTION_NAME = NAMESPACE.split(".")  
      
    client: MongoClient = MongoClient(CONNECTION_STRING)  
    collection = client[DB_NAME][COLLECTION_NAME]  
      
    model_deployment = os.getenv(  
        "OPENAI_EMBEDDINGS_DEPLOYMENT", "smart-agent-embedding-ada"  
    )  
    model_name = os.getenv("OPENAI_EMBEDDINGS_MODEL_NAME", "text-embedding-ada-002")  
      
    vectorstore = AzureCosmosDBVectorSearch.from_documents(  
        docs,  
        openai_embeddings,  
        collection=collection,  
        index_name=INDEX_NAME,  
    )  
      
    num_lists = 100  
    dimensions = 1536  
    similarity_algorithm = CosmosDBSimilarityType.COS  
      
    vectorstore.create_index(num_lists, dimensions, similarity_algorithm)  
    


```
[/code]


[code]
```python




        {'raw': {'defaultShard': {'numIndexesBefore': 2,  
           'numIndexesAfter': 3,  
           'createdCollectionAutomatically': False,  
           'ok': 1}},  
         'ok': 1}  
    


```
[/code]


[code]
```python




    # perform a similarity search between the embedding of the query and the embeddings of the documents  
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vectorstore.similarity_search(query)  
    


```
[/code]


[code]
```python




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


Once the documents have been loaded and the index has been created, you can now instantiate the vector store directly and run queries against the index

[code]
```python




    vectorstore = AzureCosmosDBVectorSearch.from_connection_string(  
        CONNECTION_STRING, NAMESPACE, openai_embeddings, index_name=INDEX_NAME  
    )  
      
    # perform a similarity search between a query and the ingested documents  
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vectorstore.similarity_search(query)  
      
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


[code]
```python




    vectorstore = AzureCosmosDBVectorSearch(  
        collection, openai_embeddings, index_name=INDEX_NAME  
    )  
      
    # perform a similarity search between a query and the ingested documents  
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vectorstore.similarity_search(query)  
      
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


