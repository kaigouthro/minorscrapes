

Skip to main content

On this page

# DocArray

> DocArray is a versatile, open-source tool for managing your multi-modal data. It lets you shape your data however you want, and offers the flexibility to store and search it using various document
> index backends. Plus, it gets even better - you can utilize your `DocArray` document index to create a `DocArrayRetriever`, and build awesome Langchain apps!

This notebook is split into two sections. The first section offers an introduction to all five supported document index backends. It provides guidance on setting up and indexing each backend and also
instructs you on how to build a `DocArrayRetriever` for finding relevant documents. In the second section, we'll select one of these backends and illustrate how to use it through a basic example.

## Document Index Backends​

[code]
```python




    import random  
      
    from docarray import BaseDoc  
    from docarray.typing import NdArray  
    from langchain.embeddings import FakeEmbeddings  
    from langchain.retrievers import DocArrayRetriever  
      
    embeddings = FakeEmbeddings(size=32)  
    


```
[/code]


Before you start building the index, it's important to define your document schema. This determines what fields your documents will have and what type of data each field will hold.

For this demonstration, we'll create a somewhat random schema containing 'title' (str), 'title_embedding' (numpy array), 'year' (int), and 'color' (str)

[code]
```python




    class MyDoc(BaseDoc):  
        title: str  
        title_embedding: NdArray[32]  
        year: int  
        color: str  
    


```
[/code]


### InMemoryExactNNIndex​

`InMemoryExactNNIndex` stores all Documents in memory. It is a great starting point for small datasets, where you may not want to launch a database server.

Learn more here: https://docs.docarray.org/user_guide/storing/index_in_memory/

[code]
```python




    from docarray.index import InMemoryExactNNIndex  
      
    # initialize the index  
    db = InMemoryExactNNIndex[MyDoc]()  
    # index data  
    db.index(  
        [  
            MyDoc(  
                title=f"My document {i}",  
                title_embedding=embeddings.embed_query(f"query {i}"),  
                year=i,  
                color=random.choice(["red", "green", "blue"]),  
            )  
            for i in range(100)  
        ]  
    )  
    # optionally, you can create a filter query  
    filter_query = {"year": {"$lte": 90}}  
    


```
[/code]


[code]
```python




    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="title_embedding",  
        content_field="title",  
        filters=filter_query,  
    )  
      
    # find the relevant document  
    doc = retriever.get_relevant_documents("some query")  
    print(doc)  
    


```
[/code]


[code]
```python




        [Document(page_content='My document 56', metadata={'id': '1f33e58b6468ab722f3786b96b20afe6', 'year': 56, 'color': 'red'})]  
    


```
[/code]


### HnswDocumentIndex​

`HnswDocumentIndex` is a lightweight Document Index implementation that runs fully locally and is best suited for small- to medium-sized datasets. It stores vectors on disk in hnswlib, and stores all
other data in SQLite.

Learn more here: https://docs.docarray.org/user_guide/storing/index_hnswlib/

[code]
```python




    from docarray.index import HnswDocumentIndex  
      
    # initialize the index  
    db = HnswDocumentIndex[MyDoc](work_dir="hnsw_index")  
      
    # index data  
    db.index(  
        [  
            MyDoc(  
                title=f"My document {i}",  
                title_embedding=embeddings.embed_query(f"query {i}"),  
                year=i,  
                color=random.choice(["red", "green", "blue"]),  
            )  
            for i in range(100)  
        ]  
    )  
    # optionally, you can create a filter query  
    filter_query = {"year": {"$lte": 90}}  
    


```
[/code]


[code]
```python




    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="title_embedding",  
        content_field="title",  
        filters=filter_query,  
    )  
      
    # find the relevant document  
    doc = retriever.get_relevant_documents("some query")  
    print(doc)  
    


```
[/code]


[code]
```python




        [Document(page_content='My document 28', metadata={'id': 'ca9f3f4268eec7c97a7d6e77f541cb82', 'year': 28, 'color': 'red'})]  
    


```
[/code]


### WeaviateDocumentIndex​

`WeaviateDocumentIndex` is a document index that is built upon Weaviate vector database.

Learn more here: https://docs.docarray.org/user_guide/storing/index_weaviate/

[code]
```python




    # There's a small difference with the Weaviate backend compared to the others.  
    # Here, you need to 'mark' the field used for vector search with 'is_embedding=True'.  
    # So, let's create a new schema for Weaviate that takes care of this requirement.  
      
    from pydantic import Field  
      
      
    class WeaviateDoc(BaseDoc):  
        title: str  
        title_embedding: NdArray[32] = Field(is_embedding=True)  
        year: int  
        color: str  
    


```
[/code]


[code]
```python




    from docarray.index import WeaviateDocumentIndex  
      
    # initialize the index  
    dbconfig = WeaviateDocumentIndex.DBConfig(host="http://localhost:8080")  
    db = WeaviateDocumentIndex[WeaviateDoc](db_config=dbconfig)  
      
    # index data  
    db.index(  
        [  
            MyDoc(  
                title=f"My document {i}",  
                title_embedding=embeddings.embed_query(f"query {i}"),  
                year=i,  
                color=random.choice(["red", "green", "blue"]),  
            )  
            for i in range(100)  
        ]  
    )  
    # optionally, you can create a filter query  
    filter_query = {"path": ["year"], "operator": "LessThanEqual", "valueInt": "90"}  
    


```
[/code]


[code]
```python




    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="title_embedding",  
        content_field="title",  
        filters=filter_query,  
    )  
      
    # find the relevant document  
    doc = retriever.get_relevant_documents("some query")  
    print(doc)  
    


```
[/code]


[code]
```python




        [Document(page_content='My document 17', metadata={'id': '3a5b76e85f0d0a01785dc8f9d965ce40', 'year': 17, 'color': 'red'})]  
    


```
[/code]


### ElasticDocIndex​

`ElasticDocIndex` is a document index that is built upon ElasticSearch

Learn more here

[code]
```python




    from docarray.index import ElasticDocIndex  
      
    # initialize the index  
    db = ElasticDocIndex[MyDoc](  
        hosts="http://localhost:9200", index_name="docarray_retriever"  
    )  
      
    # index data  
    db.index(  
        [  
            MyDoc(  
                title=f"My document {i}",  
                title_embedding=embeddings.embed_query(f"query {i}"),  
                year=i,  
                color=random.choice(["red", "green", "blue"]),  
            )  
            for i in range(100)  
        ]  
    )  
    # optionally, you can create a filter query  
    filter_query = {"range": {"year": {"lte": 90}}}  
    


```
[/code]


[code]
```python




    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="title_embedding",  
        content_field="title",  
        filters=filter_query,  
    )  
      
    # find the relevant document  
    doc = retriever.get_relevant_documents("some query")  
    print(doc)  
    


```
[/code]


[code]
```python




        [Document(page_content='My document 46', metadata={'id': 'edbc721bac1c2ad323414ad1301528a4', 'year': 46, 'color': 'green'})]  
    


```
[/code]


### QdrantDocumentIndex​

`QdrantDocumentIndex` is a document index that is built upon Qdrant vector database

Learn more here

[code]
```python




    from docarray.index import QdrantDocumentIndex  
    from qdrant_client.http import models as rest  
      
    # initialize the index  
    qdrant_config = QdrantDocumentIndex.DBConfig(path=":memory:")  
    db = QdrantDocumentIndex[MyDoc](qdrant_config)  
      
    # index data  
    db.index(  
        [  
            MyDoc(  
                title=f"My document {i}",  
                title_embedding=embeddings.embed_query(f"query {i}"),  
                year=i,  
                color=random.choice(["red", "green", "blue"]),  
            )  
            for i in range(100)  
        ]  
    )  
    # optionally, you can create a filter query  
    filter_query = rest.Filter(  
        must=[  
            rest.FieldCondition(  
                key="year",  
                range=rest.Range(  
                    gte=10,  
                    lt=90,  
                ),  
            )  
        ]  
    )  
    


```
[/code]


[code]
```python




        WARNING:root:Payload indexes have no effect in the local Qdrant. Please use server Qdrant if you need payload indexes.  
    


```
[/code]


[code]
```python




    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="title_embedding",  
        content_field="title",  
        filters=filter_query,  
    )  
      
    # find the relevant document  
    doc = retriever.get_relevant_documents("some query")  
    print(doc)  
    


```
[/code]


[code]
```python




        [Document(page_content='My document 80', metadata={'id': '97465f98d0810f1f330e4ecc29b13d20', 'year': 80, 'color': 'blue'})]  
    


```
[/code]


## Movie Retrieval using HnswDocumentIndex​

[code]
```python




    movies = [  
        {  
            "title": "Inception",  
            "description": "A thief who steals corporate secrets through the use of dream-sharing technology is given the task of planting an idea into the mind of a CEO.",  
            "director": "Christopher Nolan",  
            "rating": 8.8,  
        },  
        {  
            "title": "The Dark Knight",  
            "description": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.",  
            "director": "Christopher Nolan",  
            "rating": 9.0,  
        },  
        {  
            "title": "Interstellar",  
            "description": "Interstellar explores the boundaries of human exploration as a group of astronauts venture through a wormhole in space. In their quest to ensure the survival of humanity, they confront the vastness of space-time and grapple with love and sacrifice.",  
            "director": "Christopher Nolan",  
            "rating": 8.6,  
        },  
        {  
            "title": "Pulp Fiction",  
            "description": "The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",  
            "director": "Quentin Tarantino",  
            "rating": 8.9,  
        },  
        {  
            "title": "Reservoir Dogs",  
            "description": "When a simple jewelry heist goes horribly wrong, the surviving criminals begin to suspect that one of them is a police informant.",  
            "director": "Quentin Tarantino",  
            "rating": 8.3,  
        },  
        {  
            "title": "The Godfather",  
            "description": "An aging patriarch of an organized crime dynasty transfers control of his empire to his reluctant son.",  
            "director": "Francis Ford Coppola",  
            "rating": 9.2,  
        },  
    ]  
    


```
[/code]


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




    from docarray import BaseDoc, DocList  
    from docarray.typing import NdArray  
    from langchain.embeddings.openai import OpenAIEmbeddings  
      
      
    # define schema for your movie documents  
    class MyDoc(BaseDoc):  
        title: str  
        description: str  
        description_embedding: NdArray[1536]  
        rating: float  
        director: str  
      
      
    embeddings = OpenAIEmbeddings()  
      
      
    # get "description" embeddings, and create documents  
    docs = DocList[MyDoc](  
        [  
            MyDoc(  
                description_embedding=embeddings.embed_query(movie["description"]), **movie  
            )  
            for movie in movies  
        ]  
    )  
    


```
[/code]


[code]
```python




    from docarray.index import HnswDocumentIndex  
      
    # initialize the index  
    db = HnswDocumentIndex[MyDoc](work_dir="movie_search")  
      
    # add data  
    db.index(docs)  
    


```
[/code]


### Normal Retriever​

[code]
```python




    from langchain.retrievers import DocArrayRetriever  
      
    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="description_embedding",  
        content_field="description",  
    )  
      
    # find the relevant document  
    doc = retriever.get_relevant_documents("movie about dreams")  
    print(doc)  
    


```
[/code]


[code]
```python




        [Document(page_content='A thief who steals corporate secrets through the use of dream-sharing technology is given the task of planting an idea into the mind of a CEO.', metadata={'id': 'f1649d5b6776db04fec9a116bbb6bbe5', 'title': 'Inception', 'rating': 8.8, 'director': 'Christopher Nolan'})]  
    


```
[/code]


### Retriever with Filters​

[code]
```python




    from langchain.retrievers import DocArrayRetriever  
      
    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="description_embedding",  
        content_field="description",  
        filters={"director": {"$eq": "Christopher Nolan"}},  
        top_k=2,  
    )  
      
    # find relevant documents  
    docs = retriever.get_relevant_documents("space travel")  
    print(docs)  
    


```
[/code]


[code]
```python




        [Document(page_content='Interstellar explores the boundaries of human exploration as a group of astronauts venture through a wormhole in space. In their quest to ensure the survival of humanity, they confront the vastness of space-time and grapple with love and sacrifice.', metadata={'id': 'ab704cc7ae8573dc617f9a5e25df022a', 'title': 'Interstellar', 'rating': 8.6, 'director': 'Christopher Nolan'}), Document(page_content='A thief who steals corporate secrets through the use of dream-sharing technology is given the task of planting an idea into the mind of a CEO.', metadata={'id': 'f1649d5b6776db04fec9a116bbb6bbe5', 'title': 'Inception', 'rating': 8.8, 'director': 'Christopher Nolan'})]  
    


```
[/code]


### Retriever with MMR search​

[code]
```python




    from langchain.retrievers import DocArrayRetriever  
      
    # create a retriever  
    retriever = DocArrayRetriever(  
        index=db,  
        embeddings=embeddings,  
        search_field="description_embedding",  
        content_field="description",  
        filters={"rating": {"$gte": 8.7}},  
        search_type="mmr",  
        top_k=3,  
    )  
      
    # find relevant documents  
    docs = retriever.get_relevant_documents("action movies")  
    print(docs)  
    


```
[/code]


[code]
```python




        [Document(page_content="The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.", metadata={'id': 'e6aa313bbde514e23fbc80ab34511afd', 'title': 'Pulp Fiction', 'rating': 8.9, 'director': 'Quentin Tarantino'}), Document(page_content='A thief who steals corporate secrets through the use of dream-sharing technology is given the task of planting an idea into the mind of a CEO.', metadata={'id': 'f1649d5b6776db04fec9a116bbb6bbe5', 'title': 'Inception', 'rating': 8.8, 'director': 'Christopher Nolan'}), Document(page_content='When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.', metadata={'id': '91dec17d4272041b669fd113333a65f7', 'title': 'The Dark Knight', 'rating': 9.0, 'director': 'Christopher Nolan'})]  
    


```
[/code]


