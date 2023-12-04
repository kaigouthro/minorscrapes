

Skip to main content

On this page

# DashVector

> DashVector is a fully managed vector DB service that supports high-dimension dense and sparse vectors, real-time insertion and filtered search. It is built to scale automatically and can adapt to
> different application requirements. The vector retrieval service `DashVector` is based on the `Proxima` core of the efficient vector engine independently developed by `DAMO Academy`, and provides a
> cloud-native, fully managed vector retrieval service with horizontal expansion capabilities. `DashVector` exposes its powerful vector management, vector query and other diversified capabilities
> through a simple and easy-to-use SDK/API interface, which can be quickly integrated by upper-layer AI applications, thereby providing services including large model ecology, multi-modal AI search,
> molecular structure A variety of application scenarios, including analysis, provide the required efficient vector retrieval capabilities.

In this notebook, we'll demo the `SelfQueryRetriever` with a `DashVector` vector store.

## Create DashVector vectorstore​

First we'll want to create a `DashVector` VectorStore and seed it with some data. We've created a small demo set of documents that contain summaries of movies.

To use DashVector, you have to have `dashvector` package installed, and you must have an API key and an Environment. Here are the installation instructions.

NOTE: The self-query retriever requires you to have `lark` package installed.

[code]
```python




    # !pip install lark dashvector  
    


```
[/code]


[code]
```python




    import os  
      
    import dashvector  
      
    client = dashvector.Client(api_key=os.environ["DASHVECTOR_API_KEY"])  
    


```
[/code]


[code]
```python




    from langchain.embeddings import DashScopeEmbeddings  
    from langchain.schema import Document  
    from langchain.vectorstores import DashVector  
      
    embeddings = DashScopeEmbeddings()  
      
    # create DashVector collection  
    client.create("langchain-self-retriever-demo", dimension=1536)  
    


```
[/code]


[code]
```python




    docs = [  
        Document(  
            page_content="A bunch of scientists bring back dinosaurs and mayhem breaks loose",  
            metadata={"year": 1993, "rating": 7.7, "genre": "action"},  
        ),  
        Document(  
            page_content="Leo DiCaprio gets lost in a dream within a dream within a dream within a ...",  
            metadata={"year": 2010, "director": "Christopher Nolan", "rating": 8.2},  
        ),  
        Document(  
            page_content="A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea",  
            metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6},  
        ),  
        Document(  
            page_content="A bunch of normal-sized women are supremely wholesome and some men pine after them",  
            metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},  
        ),  
        Document(  
            page_content="Toys come alive and have a blast doing so",  
            metadata={"year": 1995, "genre": "animated"},  
        ),  
        Document(  
            page_content="Three men walk into the Zone, three men walk out of the Zone",  
            metadata={  
                "year": 1979,  
                "director": "Andrei Tarkovsky",  
                "genre": "science fiction",  
                "rating": 9.9,  
            },  
        ),  
    ]  
    vectorstore = DashVector.from_documents(  
        docs, embeddings, collection_name="langchain-self-retriever-demo"  
    )  
    


```
[/code]


## Create your self-querying retriever​

Now we can instantiate our retriever. To do this we'll need to provide some information upfront about the metadata fields that our documents support and a short description of the document contents.

[code]
```python




    from langchain.chains.query_constructor.base import AttributeInfo  
    from langchain.llms import Tongyi  
    from langchain.retrievers.self_query.base import SelfQueryRetriever  
      
    metadata_field_info = [  
        AttributeInfo(  
            name="genre",  
            description="The genre of the movie",  
            type="string or list[string]",  
        ),  
        AttributeInfo(  
            name="year",  
            description="The year the movie was released",  
            type="integer",  
        ),  
        AttributeInfo(  
            name="director",  
            description="The name of the movie director",  
            type="string",  
        ),  
        AttributeInfo(  
            name="rating", description="A 1-10 rating for the movie", type="float"  
        ),  
    ]  
    document_content_description = "Brief summary of a movie"  
    llm = Tongyi(temperature=0)  
    retriever = SelfQueryRetriever.from_llm(  
        llm, vectorstore, document_content_description, metadata_field_info, verbose=True  
    )  
    


```
[/code]


## Testing it out​

And now we can try actually using our retriever!

[code]
```python




    # This example only specifies a relevant query  
    retriever.get_relevant_documents("What are some movies about dinosaurs")  
    


```
[/code]


[code]
```python




        query='dinosaurs' filter=None limit=None  
      
      
      
      
      
        [Document(page_content='A bunch of scientists bring back dinosaurs and mayhem breaks loose', metadata={'year': 1993, 'rating': 7.699999809265137, 'genre': 'action'}),  
         Document(page_content='Toys come alive and have a blast doing so', metadata={'year': 1995, 'genre': 'animated'}),  
         Document(page_content='Leo DiCaprio gets lost in a dream within a dream within a dream within a ...', metadata={'year': 2010, 'director': 'Christopher Nolan', 'rating': 8.199999809265137}),  
         Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'year': 2006, 'director': 'Satoshi Kon', 'rating': 8.600000381469727})]  
    


```
[/code]


[code]
```python




    # This example only specifies a filter  
    retriever.get_relevant_documents("I want to watch a movie rated higher than 8.5")  
    


```
[/code]


[code]
```python




        query=' ' filter=Comparison(comparator=<Comparator.GTE: 'gte'>, attribute='rating', value=8.5) limit=None  
      
      
      
      
      
        [Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'year': 1979, 'director': 'Andrei Tarkovsky', 'rating': 9.899999618530273, 'genre': 'science fiction'}),  
         Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'year': 2006, 'director': 'Satoshi Kon', 'rating': 8.600000381469727})]  
    


```
[/code]


[code]
```python




    # This example specifies a query and a filter  
    retriever.get_relevant_documents("Has Greta Gerwig directed any movies about women")  
    


```
[/code]


[code]
```python




        query='Greta Gerwig' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='director', value='Greta Gerwig') limit=None  
      
      
      
      
      
        [Document(page_content='A bunch of normal-sized women are supremely wholesome and some men pine after them', metadata={'year': 2019, 'director': 'Greta Gerwig', 'rating': 8.300000190734863})]  
    


```
[/code]


[code]
```python




    # This example specifies a composite filter  
    retriever.get_relevant_documents(  
        "What's a highly rated (above 8.5) science fiction film?"  
    )  
    


```
[/code]


[code]
```python




        query='science fiction' filter=Operation(operator=<Operator.AND: 'and'>, arguments=[Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='genre', value='science fiction'), Comparison(comparator=<Comparator.GT: 'gt'>, attribute='rating', value=8.5)]) limit=None  
      
      
      
      
      
        [Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'year': 1979, 'director': 'Andrei Tarkovsky', 'rating': 9.899999618530273, 'genre': 'science fiction'})]  
    


```
[/code]


## Filter k​

We can also use the self query retriever to specify `k`: the number of documents to fetch.

We can do this by passing `enable_limit=True` to the constructor.

[code]
```python




    retriever = SelfQueryRetriever.from_llm(  
        llm,  
        vectorstore,  
        document_content_description,  
        metadata_field_info,  
        enable_limit=True,  
        verbose=True,  
    )  
    


```
[/code]


[code]
```python




    # This example only specifies a relevant query  
    retriever.get_relevant_documents("what are two movies about dinosaurs")  
    


```
[/code]


[code]
```python




        query='dinosaurs' filter=None limit=2  
      
      
      
      
      
        [Document(page_content='A bunch of scientists bring back dinosaurs and mayhem breaks loose', metadata={'year': 1993, 'rating': 7.699999809265137, 'genre': 'action'}),  
         Document(page_content='Toys come alive and have a blast doing so', metadata={'year': 1995, 'genre': 'animated'})]  
    


```
[/code]


