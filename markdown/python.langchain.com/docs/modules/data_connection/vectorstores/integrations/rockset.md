

Skip to main content

On this page

# Rockset

> Rockset is a real-time search and analytics database built for the cloud. Rockset uses a Converged Index™ with an efficient store for vector embeddings to serve low latency, high concurrency search
> queries at scale. Rockset has full support for metadata filtering and handles real-time ingestion for constantly updating, streaming data.

This notebook demonstrates how to use `Rockset` as a vector store in LangChain. Before getting started, make sure you have access to a `Rockset` account and an API key available. Start your free trial
today.

## Setting Up Your Environment​

  1. Leverage the `Rockset` console to create a collection with the Write API as your source. In this walkthrough, we create a collection named `langchain_demo`. 

Configure the following ingest transformation to mark your embeddings field and take advantage of performance and storage optimizations:

(We used OpenAI `text-embedding-ada-002` for this examples, where #length_of_vector_embedding = 1536)

[code]
```python




    SELECT _input.* EXCEPT(_meta),   
    VECTOR_ENFORCE(_input.description_embedding, #length_of_vector_embedding, 'float') as description_embedding   
    FROM _input  
    


```
[/code]


  2. After creating your collection, use the console to retrieve an API key. For the purpose of this notebook, we assume you are using the `Oregon(us-west-2)` region.

  3. Install the rockset-python-client to enable LangChain to communicate directly with `Rockset`.

[code]
```python




    pip install rockset  
    


```
[/code]


## LangChain Tutorial​

Follow along in your own Python notebook to generate and store vector embeddings in Rockset. Start using Rockset to search for documents similar to your search queries.

### 1\. Define Key Variables​

[code]
```python




    import os  
      
    import rockset  
      
    ROCKSET_API_KEY = os.environ.get(  
        "ROCKSET_API_KEY"  
    )  # Verify ROCKSET_API_KEY environment variable  
    ROCKSET_API_SERVER = rockset.Regions.usw2a1  # Verify Rockset region  
    rockset_client = rockset.RocksetClient(ROCKSET_API_SERVER, ROCKSET_API_KEY)  
      
    COLLECTION_NAME = "langchain_demo"  
    TEXT_KEY = "description"  
    EMBEDDING_KEY = "description_embedding"  
    


```
[/code]


### 2\. Prepare Documents​

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Rockset  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
    


```
[/code]


### 3\. Insert Documents​

[code]
```python




    embeddings = OpenAIEmbeddings()  # Verify OPENAI_API_KEY environment variable  
      
    docsearch = Rockset(  
        client=rockset_client,  
        embeddings=embeddings,  
        collection_name=COLLECTION_NAME,  
        text_key=TEXT_KEY,  
        embedding_key=EMBEDDING_KEY,  
    )  
      
    ids = docsearch.add_texts(  
        texts=[d.page_content for d in docs],  
        metadatas=[d.metadata for d in docs],  
    )  
    


```
[/code]


### 4\. Search for Similar Documents​

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    output = docsearch.similarity_search_with_relevance_scores(  
        query, 4, Rockset.DistanceFunction.COSINE_SIM  
    )  
    print("output length:", len(output))  
    for d, dist in output:  
        print(dist, d.metadata, d.page_content[:20] + "...")  
      
    ##  
    # output length: 4  
    # 0.764990692109871 {'source': '../../../state_of_the_union.txt'} Madam Speaker, Madam...  
    # 0.7485416901622112 {'source': '../../../state_of_the_union.txt'} And I’m taking robus...  
    # 0.7468678973398306 {'source': '../../../state_of_the_union.txt'} And so many families...  
    # 0.7436231261419488 {'source': '../../../state_of_the_union.txt'} Groups of citizens b...  
    


```
[/code]


### 5\. Search for Similar Documents with Filtering​

[code]
```python




    output = docsearch.similarity_search_with_relevance_scores(  
        query,  
        4,  
        Rockset.DistanceFunction.COSINE_SIM,  
        where_str="{} NOT LIKE '%citizens%'".format(TEXT_KEY),  
    )  
    print("output length:", len(output))  
    for d, dist in output:  
        print(dist, d.metadata, d.page_content[:20] + "...")  
      
    ##  
    # output length: 4  
    # 0.7651359650263554 {'source': '../../../state_of_the_union.txt'} Madam Speaker, Madam...  
    # 0.7486265516824893 {'source': '../../../state_of_the_union.txt'} And I’m taking robus...  
    # 0.7469625542348115 {'source': '../../../state_of_the_union.txt'} And so many families...  
    # 0.7344177777547739 {'source': '../../../state_of_the_union.txt'} We see the unity amo...  
    


```
[/code]


### 6\. [Optional] Delete Inserted Documents​

You must have the unique ID associated with each document to delete them from your collection. Define IDs when inserting documents with `Rockset.add_texts()`. Rockset will otherwise generate a unique
ID for each document. Regardless, `Rockset.add_texts()` returns the IDs of inserted documents.

To delete these docs, simply use the `Rockset.delete_texts()` function.

[code]
```python




    docsearch.delete_texts(ids)  
    


```
[/code]


## Summary​

In this tutorial, we successfully created a `Rockset` collection, `inserted` documents with OpenAI embeddings, and searched for similar documents with and without metadata filters.

Keep an eye on https://rockset.com/ for future updates in this space.

