

Skip to main content

# Zilliz

> Zilliz Cloud is a fully managed service on cloud for `LF AI Milvus®`,

This notebook shows how to use functionality related to the Zilliz Cloud managed vector database.

To run, you should have a `Zilliz Cloud` instance up and running. Here are the installation instructions

[code]
```python




    pip install pymilvus  
    


```
[/code]


We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

[code]
```python




    import getpass  
    import os  
      
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




        OpenAI API Key:········  
    


```
[/code]


[code]
```python




    # replace  
    ZILLIZ_CLOUD_URI = ""  # example: "https://in01-17f69c292d4a5sa.aws-us-west-2.vectordb.zillizcloud.com:19536"  
    ZILLIZ_CLOUD_USERNAME = ""  # example: "username"  
    ZILLIZ_CLOUD_PASSWORD = ""  # example: "*********"  
    ZILLIZ_CLOUD_API_KEY = ""  # example: "*********" (for serverless clusters which can be used as replacements for user and password)  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Milvus  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    vector_db = Milvus.from_documents(  
        docs,  
        embeddings,  
        connection_args={  
            "uri": ZILLIZ_CLOUD_URI,  
            "user": ZILLIZ_CLOUD_USERNAME,  
            "password": ZILLIZ_CLOUD_PASSWORD,  
            # "token": ZILLIZ_CLOUD_API_KEY,  # API key, for serverless clusters which can be used as replacements for user and password  
            "secure": True,  
        },  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = vector_db.similarity_search(query)  
    


```
[/code]


[code]
```python




    docs[0].page_content  
    


```
[/code]


[code]
```python




        'Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. \n\nTonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \n\nAnd I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.'  
    


```
[/code]


