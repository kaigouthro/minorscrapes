

Skip to main content

On this page

# Qdrant

> Qdrant (read: quadrant ) is a vector similarity search engine. It provides a production-ready service with a convenient API to store, search, and manage points - vectors with an additional payload.
> `Qdrant` is tailored to extended filtering support. It makes it useful for all sorts of neural network or semantic-based matching, faceted search, and other applications.

This notebook shows how to use functionality related to the `Qdrant` vector database.

There are various modes of how to run `Qdrant`, and depending on the chosen one, there will be some subtle differences. The options include:

  * Local mode, no server required
  * On-premise server deployment
  * Qdrant Cloud

See the installation instructions.

[code]
```python




    pip install qdrant-client  
    


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




        OpenAI API Key: ········  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Qdrant  
    


```
[/code]


[code]
```python




    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


## Connecting to Qdrant from LangChain​

### Local mode​

Python client allows you to run the same code in local mode without running the Qdrant server. That's great for testing things out and debugging or if you plan to store just a small amount of vectors.
The embeddings might be fully kepy in memory or persisted on disk.

#### In-memory​

For some testing scenarios and quick experiments, you may prefer to keep all the data in memory only, so it gets lost when the client is destroyed - usually at the end of your script/notebook.

[code]
```python




    qdrant = Qdrant.from_documents(  
        docs,  
        embeddings,  
        location=":memory:",  # Local mode with in-memory storage only  
        collection_name="my_documents",  
    )  
    


```
[/code]


#### On-disk storage​

Local mode, without using the Qdrant server, may also store your vectors on disk so they're persisted between runs.

[code]
```python




    qdrant = Qdrant.from_documents(  
        docs,  
        embeddings,  
        path="/tmp/local_qdrant",  
        collection_name="my_documents",  
    )  
    


```
[/code]


### On-premise server deployment​

No matter if you choose to launch Qdrant locally with a Docker container, or select a Kubernetes deployment with the official Helm chart, the way you're going to connect to such an instance will be
identical. You'll need to provide a URL pointing to the service.

[code]
```python




    url = "<---qdrant url here --->"  
    qdrant = Qdrant.from_documents(  
        docs,  
        embeddings,  
        url=url,  
        prefer_grpc=True,  
        collection_name="my_documents",  
    )  
    


```
[/code]


### Qdrant Cloud​

If you prefer not to keep yourself busy with managing the infrastructure, you can choose to set up a fully-managed Qdrant cluster on Qdrant Cloud. There is a free forever 1GB cluster included for
trying out. The main difference with using a managed version of Qdrant is that you'll need to provide an API key to secure your deployment from being accessed publicly.

[code]
```python




    url = "<---qdrant cloud cluster url here --->"  
    api_key = "<---api key here--->"  
    qdrant = Qdrant.from_documents(  
        docs,  
        embeddings,  
        url=url,  
        prefer_grpc=True,  
        api_key=api_key,  
        collection_name="my_documents",  
    )  
    


```
[/code]


## Recreating the collection​

Both `Qdrant.from_texts` and `Qdrant.from_documents` methods are great to start using Qdrant with Langchain. In the previous versions the collection was recreated every time you called any of them.
That behaviour has changed. Currently, the collection is going to be reused if it already exists. Setting `force_recreate` to `True` allows to remove the old collection and start from scratch.

[code]
```python




    url = "<---qdrant url here --->"  
    qdrant = Qdrant.from_documents(  
        docs,  
        embeddings,  
        url=url,  
        prefer_grpc=True,  
        collection_name="my_documents",  
        force_recreate=True,  
    )  
    


```
[/code]


## Similarity search​

The simplest scenario for using Qdrant vector store is to perform a similarity search. Under the hood, our query will be encoded with the `embedding_function` and used to find similar documents in
Qdrant collection.

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    found_docs = qdrant.similarity_search(query)  
    


```
[/code]


[code]
```python




    print(found_docs[0].page_content)  
    


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


## Similarity search with score​

Sometimes we might want to perform the search, but also obtain a relevancy score to know how good is a particular result. The returned distance score is cosine distance. Therefore, a lower score is
better.

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    found_docs = qdrant.similarity_search_with_score(query)  
    


```
[/code]


[code]
```python




    document, score = found_docs[0]  
    print(document.page_content)  
    print(f"\nScore: {score}")  
    


```
[/code]


[code]
```python




        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   
          
        Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   
          
        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
          
        Score: 0.8153784913324512  
    


```
[/code]


### Metadata filtering​

Qdrant has an extensive filtering system with rich type support. It is also possible to use the filters in Langchain, by passing an additional param to both the `similarity_search_with_score` and
`similarity_search` methods.

[code]
```python




    from qdrant_client.http import models as rest  
      
    query = "What did the president say about Ketanji Brown Jackson"  
    found_docs = qdrant.similarity_search_with_score(query, filter=rest.Filter(...))  
    


```
[/code]


## Maximum marginal relevance search (MMR)​

If you'd like to look up for some similar documents, but you'd also like to receive diverse results, MMR is method you should consider. Maximal marginal relevance optimizes for similarity to query AND
diversity among selected documents.

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    found_docs = qdrant.max_marginal_relevance_search(query, k=2, fetch_k=10)  
    


```
[/code]


[code]
```python




    for i, doc in enumerate(found_docs):  
        print(f"{i + 1}.", doc.page_content, "\n")  
    


```
[/code]


[code]
```python




        1. Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   
          
        Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   
          
        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.   
          
        2. We can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together.   
          
        I recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera.   
          
        They were responding to a 9-1-1 call when a man shot and killed them with a stolen gun.   
          
        Officer Mora was 27 years old.   
          
        Officer Rivera was 22.   
          
        Both Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers.   
          
        I spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves.   
          
        I’ve worked on these issues a long time.   
          
        I know what works: Investing in crime prevention and community police officers who’ll walk the beat, who’ll know the neighborhood, and who can restore trust and safety.   
          
    


```
[/code]


## Qdrant as a Retriever​

Qdrant, as all the other vector stores, is a LangChain Retriever, by using cosine similarity.

[code]
```python




    retriever = qdrant.as_retriever()  
    retriever  
    


```
[/code]


[code]
```python




        VectorStoreRetriever(vectorstore=<langchain.vectorstores.qdrant.Qdrant object at 0x7fc4e5720a00>, search_type='similarity', search_kwargs={})  
    


```
[/code]


It might be also specified to use MMR as a search strategy, instead of similarity.

[code]
```python




    retriever = qdrant.as_retriever(search_type="mmr")  
    retriever  
    


```
[/code]


[code]
```python




        VectorStoreRetriever(vectorstore=<langchain.vectorstores.qdrant.Qdrant object at 0x7fc4e5720a00>, search_type='mmr', search_kwargs={})  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    retriever.get_relevant_documents(query)[0]  
    


```
[/code]


[code]
```python




        Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. \n\nTonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \n\nAnd I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../../state_of_the_union.txt'})  
    


```
[/code]


## Customizing Qdrant​

There are some options to use an existing Qdrant collection within your Langchain application. In such cases you may need to define how to map Qdrant point into the Langchain `Document`.

### Named vectors​

Qdrant supports multiple vectors per point by named vectors. Langchain requires just a single embedding per document and, by default, uses a single vector. However, if you work with a collection
created externally or want to have the named vector used, you can configure it by providing its name.

[code]
```python




    Qdrant.from_documents(  
        docs,  
        embeddings,  
        location=":memory:",  
        collection_name="my_documents_2",  
        vector_name="custom_vector",  
    )  
    


```
[/code]


As a Langchain user, you won't see any difference whether you use named vectors or not. Qdrant integration will handle the conversion under the hood.

### Metadata​

Qdrant stores your vector embeddings along with the optional JSON-like payload. Payloads are optional, but since LangChain assumes the embeddings are generated from the documents, we keep the context
data, so you can extract the original texts as well.

By default, your document is going to be stored in the following payload structure:

[code]
```python




    {  
        "page_content": "Lorem ipsum dolor sit amet",  
        "metadata": {  
            "foo": "bar"  
        }  
    }  
    


```
[/code]


You can, however, decide to use different keys for the page content and metadata. That's useful if you already have a collection that you'd like to reuse.

[code]
```python




    Qdrant.from_documents(  
        docs,  
        embeddings,  
        location=":memory:",  
        collection_name="my_documents_2",  
        content_payload_key="my_page_content_key",  
        metadata_payload_key="my_meta",  
    )  
    


```
[/code]


[code]
```python




        <langchain.vectorstores.qdrant.Qdrant at 0x7fc4e2baa230>  
    


```
[/code]


