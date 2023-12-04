

Skip to main content

On this page

# MongoDB Atlas

> MongoDB Atlas is a fully-managed cloud database available in AWS, Azure, and GCP. It now has support for native Vector Search on your MongoDB document data.

This notebook shows how to use MongoDB Atlas Vector Search to store your embeddings in MongoDB documents, create a vector search index, and perform KNN search with an approximate nearest neighbor
algorithm (`Hierarchical Navigable Small Worlds`). It uses the $vectorSearch MQL Stage.

To use MongoDB Atlas, you must first deploy a cluster. We have a Forever-Free tier of clusters available. To get started head over to Atlas here: quick start.

> Note:
>
>   * This feature is in Public Preview and available for evaluation purposes, to validate functionality, and to gather feedback from public preview users. It is not recommended for production
> deployments as we may introduce breaking changes.
>   * The langchain version 0.0.305 (release notes) introduces the support for $vectorSearch MQL stage, which is available with MongoDB Atlas 6.0.11 and 7.0.2. Users utilizing earlier versions of
> MongoDB Atlas need to pin their LangChain version to <=0.0.304
>

In the notebook we will demonstrate how to perform `Retrieval Augmented Generation` (RAG) using MongoDB Atlas, OpenAI and Langchain. We will be performing Similarity Search and Question Answering over
the PDF document for GPT 4 technical report that came out in March 2023 and hence is not part of the OpenAI's Large Language Model(LLM)'s parametric memory, which had a knowledge cutoff of September
2021.

We want to use `OpenAIEmbeddings` so we need to set up our OpenAI API Key.

[code]
```python




    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


Now we will setup the environment variables for the MongoDB Atlas cluster

[code]
```python




    pip install langchain pypdf pymongo openai tiktoken  
    


```
[/code]


[code]
```python




    import getpass  
      
    MONGODB_ATLAS_CLUSTER_URI = getpass.getpass("MongoDB Atlas Cluster URI:")  
    


```
[/code]


[code]
```python




    from pymongo import MongoClient  
      
    # initialize MongoDB python client  
    client = MongoClient(MONGODB_ATLAS_CLUSTER_URI)  
      
    DB_NAME = "langchain_db"  
    COLLECTION_NAME = "test"  
    ATLAS_VECTOR_SEARCH_INDEX_NAME = "default"  
      
    MONGODB_COLLECTION = client[DB_NAME][COLLECTION_NAME]  
    


```
[/code]


[code]
```python




    # Create Vector Search Index  
    


```
[/code]


Now, let's create a vector search index on your cluster. In the below example, `embedding` is the name of the field that contains the embedding vector. Please refer to the documentation to get more
details on how to define an Atlas Vector Search index. You can name the index `{ATLAS_VECTOR_SEARCH_INDEX_NAME}` and create the index on the namespace `{DB_NAME}.{COLLECTION_NAME}`. Finally, write the
following definition in the JSON editor on MongoDB Atlas:

[code]
```python




    {  
      "mappings": {  
        "dynamic": true,  
        "fields": {  
          "embedding": {  
            "dimensions": 1536,  
            "similarity": "cosine",  
            "type": "knnVector"  
          }  
        }  
      }  
    }  
    


```
[/code]


# Insert Data

[code]
```python




    from langchain.document_loaders import PyPDFLoader  
      
    # Load the PDF  
    loader = PyPDFLoader("https://arxiv.org/pdf/2303.08774.pdf")  
    data = loader.load()  
    


```
[/code]


[code]
```python




    from langchain.text_splitter import RecursiveCharacterTextSplitter  
      
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)  
    docs = text_splitter.split_documents(data)  
    


```
[/code]


[code]
```python




    print(docs[0])  
    


```
[/code]


[code]
```python




    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.vectorstores import MongoDBAtlasVectorSearch  
      
    # insert the documents in MongoDB Atlas with their embedding  
    vector_search = MongoDBAtlasVectorSearch.from_documents(  
        documents=docs,  
        embedding=OpenAIEmbeddings(disallowed_special=()),  
        collection=MONGODB_COLLECTION,  
        index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,  
    )  
    


```
[/code]


[code]
```python




    # Perform a similarity search between the embedding of the query and the embeddings of the documents  
    query = "What were the compute requirements for training GPT 4"  
    results = vector_search.similarity_search(query)  
      
    print(results[0].page_content)  
    


```
[/code]


# Querying data

We can also instantiate the vector store directly and execute a query as follows:

[code]
```python




    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.vectorstores import MongoDBAtlasVectorSearch  
      
    vector_search = MongoDBAtlasVectorSearch.from_connection_string(  
        MONGODB_ATLAS_CLUSTER_URI,  
        DB_NAME + "." + COLLECTION_NAME,  
        OpenAIEmbeddings(disallowed_special=()),  
        index_name=ATLAS_VECTOR_SEARCH_INDEX_NAME,  
    )  
    


```
[/code]


## Similarity Search with Score​

[code]
```python




    query = "What were the compute requirements for training GPT 4"  
      
    results = vector_search.similarity_search_with_score(  
        query=query,  
        k=5,  
    )  
      
    # Display results  
    for result in results:  
        print(result)  
    


```
[/code]


## Question Answering​

[code]
```python




    qa_retriever = vector_search.as_retriever(  
        search_type="similarity",  
        search_kwargs={"k": 100, "post_filter_pipeline": [{"$limit": 25}]},  
    )  
    


```
[/code]


[code]
```python




    from langchain.prompts import PromptTemplate  
      
    prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.  
      
    {context}  
      
    Question: {question}  
    """  
    PROMPT = PromptTemplate(  
        template=prompt_template, input_variables=["context", "question"]  
    )  
    


```
[/code]


[code]
```python




    from langchain.chains import RetrievalQA  
    from langchain.llms import OpenAI  
      
    qa = RetrievalQA.from_chain_type(  
        llm=OpenAI(),  
        chain_type="stuff",  
        retriever=qa_retriever,  
        return_source_documents=True,  
        chain_type_kwargs={"prompt": PROMPT},  
    )  
      
    docs = qa({"query": "gpt-4 compute requirements"})  
      
    print(docs["result"])  
    print(docs["source_documents"])  
    


```
[/code]


GPT-4 requires significantly more compute than earlier GPT models. On a dataset derived from OpenAI's internal codebase, GPT-4 requires 100p (petaflops) of compute to reach the lowest loss, while the
smaller models require 1-10n (nanoflops).

