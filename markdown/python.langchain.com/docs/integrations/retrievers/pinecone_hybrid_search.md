

Skip to main content

On this page

# Pinecone Hybrid Search

> Pinecone is a vector database with broad functionality.

This notebook goes over how to use a retriever that under the hood uses Pinecone and Hybrid Search.

The logic of this retriever is taken from this documentation

To use Pinecone, you must have an API key and an Environment. Here are the installation instructions.

[code]
```python




    #!pip install pinecone-client pinecone-text  
    


```
[/code]


[code]
```python




    import getpass  
    import os  
      
    os.environ["PINECONE_API_KEY"] = getpass.getpass("Pinecone API Key:")  
    


```
[/code]


[code]
```python




    from langchain.retrievers import PineconeHybridSearchRetriever  
    


```
[/code]


[code]
```python




    os.environ["PINECONE_ENVIRONMENT"] = getpass.getpass("Pinecone Environment:")  
    


```
[/code]


We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

[code]
```python




    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


## Setup Pinecone​

You should only have to do this part once.

Note: it's important to make sure that the "context" field that holds the document text in the metadata is not indexed. Currently you need to specify explicitly the fields you do want to index. For
more information checkout Pinecone's docs.

[code]
```python




    import os  
      
    import pinecone  
      
    api_key = os.getenv("PINECONE_API_KEY") or "PINECONE_API_KEY"  
    # find environment next to your API key in the Pinecone console  
    env = os.getenv("PINECONE_ENVIRONMENT") or "PINECONE_ENVIRONMENT"  
      
    index_name = "langchain-pinecone-hybrid-search"  
      
    pinecone.init(api_key=api_key, environment=env)  
    pinecone.whoami()  
    


```
[/code]


[code]
```python




        WhoAmIResponse(username='load', user_label='label', projectname='load-test')  
    


```
[/code]


[code]
```python




    # create the index  
    pinecone.create_index(  
        name=index_name,  
        dimension=1536,  # dimensionality of dense model  
        metric="dotproduct",  # sparse values supported only for dotproduct  
        pod_type="s1",  
        metadata_config={"indexed": []},  # see explanation above  
    )  
    


```
[/code]


Now that its created, we can use it

[code]
```python




    index = pinecone.Index(index_name)  
    


```
[/code]


## Get embeddings and sparse encoders​

Embeddings are used for the dense vectors, tokenizer is used for the sparse vector

[code]
```python




    from langchain.embeddings import OpenAIEmbeddings  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


To encode the text to sparse values you can either choose SPLADE or BM25. For out of domain tasks we recommend using BM25.

For more information about the sparse encoders you can checkout pinecone-text library docs.

[code]
```python




    from pinecone_text.sparse import BM25Encoder  
      
    # or from pinecone_text.sparse import SpladeEncoder if you wish to work with SPLADE  
      
    # use default tf-idf values  
    bm25_encoder = BM25Encoder().default()  
    


```
[/code]


The above code is using default tfids values. It's highly recommended to fit the tf-idf values to your own corpus. You can do it as follow:

[code]
```python




    corpus = ["foo", "bar", "world", "hello"]  
      
    # fit tf-idf values on your corpus  
    bm25_encoder.fit(corpus)  
      
    # store the values to a json file  
    bm25_encoder.dump("bm25_values.json")  
      
    # load to your BM25Encoder object  
    bm25_encoder = BM25Encoder().load("bm25_values.json")  
    


```
[/code]


## Load Retriever​

We can now construct the retriever!

[code]
```python




    retriever = PineconeHybridSearchRetriever(  
        embeddings=embeddings, sparse_encoder=bm25_encoder, index=index  
    )  
    


```
[/code]


## Add texts (if necessary)​

We can optionally add texts to the retriever (if they aren't already in there)

[code]
```python




    retriever.add_texts(["foo", "bar", "world", "hello"])  
    


```
[/code]


[code]
```python




        100%|██████████| 1/1 [00:02<00:00,  2.27s/it]  
    


```
[/code]


## Use Retriever​

We can now use the retriever!

[code]
```python




    result = retriever.get_relevant_documents("foo")  
    


```
[/code]


[code]
```python




    result[0]  
    


```
[/code]


[code]
```python




        Document(page_content='foo', metadata={})  
    


```
[/code]


