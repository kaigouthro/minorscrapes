

Skip to main content

# Baidu Cloud ElasticSearch VectorSearch

> Baidu Cloud VectorSearch is a fully managed, enterprise-level distributed search and analysis service which is 100% compatible to open source. Baidu Cloud VectorSearch provides low-cost, high-
> performance, and reliable retrieval and analysis platform level product services for structured/unstructured data. As a vector database , it supports multiple index types and similarity distance
> methods.

> `Baidu Cloud ElasticSearch` provides a privilege management mechanism, for you to configure the cluster privileges freely, so as to further ensure data security.

This notebook shows how to use functionality related to the `Baidu Cloud ElasticSearch VectorStore`. To run, you should have an Baidu Cloud ElasticSearch instance up and running:

Read the help document to quickly familiarize and configure Baidu Cloud ElasticSearch instance.

After the instance is up and running, follow these steps to split documents, get embeddings, connect to the baidu cloud elasticsearch instance, index documents, and perform vector retrieval.

We need to install the following Python packages first.

[code]
```python




    #!pip install elasticsearch == 7.11.0  
    


```
[/code]


First, we want to use `QianfanEmbeddings` so we have to get the Qianfan AK and SK. Details for QianFan is related to Baidu Qianfan Workshop

[code]
```python




    import getpass  
    import os  
      
    os.environ["QIANFAN_AK"] = getpass.getpass("Your Qianfan AK:")  
    os.environ["QIANFAN_SK"] = getpass.getpass("Your Qianfan SK:")  
    


```
[/code]


Secondly, split documents and get embeddings.

[code]
```python




    from langchain.document_loaders import TextLoader  
      
    loader = TextLoader("../../../state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    from langchain.embeddings import QianfanEmbeddingsEndpoint  
      
    embeddings = QianfanEmbeddingsEndpoint()  
    


```
[/code]


Then, create a Baidu ElasticeSearch accessable instance.

[code]
```python




    # Create a bes instance and index docs.  
    from langchain.vectorstores import BESVectorStore  
      
    bes = BESVectorStore.from_documents(  
        documents=docs,  
        embedding=embeddings,  
        bes_url="your bes cluster url",  
        index_name="your vector index",  
    )  
    bes.client.indices.refresh(index="your vector index")  
    


```
[/code]


Finally, Query and retrive data

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = bes.similarity_search(query)  
    print(docs[0].page_content)  
    


```
[/code]


Please feel free to contact liuboyao@baidu.com or chenweixu01@baidu.com if you encounter any problems during use, and we will do our best to support you.

