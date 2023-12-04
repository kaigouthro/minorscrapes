

Skip to main content

On this page

# Redis

> Redis is an open-source key-value store that can be used as a cache, message broker, database, vector database and more.

In the notebook, we'll demo the `SelfQueryRetriever` wrapped around a `Redis` vector store.

## Creating a Redis vector store​

First we'll want to create a Redis vector store and seed it with some data. We've created a small demo set of documents that contain summaries of movies.

 **Note:** The self-query retriever requires you to have `lark` installed (`pip install lark`) along with integration-specific requirements.

[code]
```python




    # !pip install redis redisvl openai tiktoken lark  
    


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




    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.schema import Document  
    from langchain.vectorstores import Redis  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    docs = [  
        Document(  
            page_content="A bunch of scientists bring back dinosaurs and mayhem breaks loose",  
            metadata={  
                "year": 1993,  
                "rating": 7.7,  
                "director": "Steven Spielberg",  
                "genre": "science fiction",  
            },  
        ),  
        Document(  
            page_content="Leo DiCaprio gets lost in a dream within a dream within a dream within a ...",  
            metadata={  
                "year": 2010,  
                "director": "Christopher Nolan",  
                "genre": "science fiction",  
                "rating": 8.2,  
            },  
        ),  
        Document(  
            page_content="A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea",  
            metadata={  
                "year": 2006,  
                "director": "Satoshi Kon",  
                "genre": "science fiction",  
                "rating": 8.6,  
            },  
        ),  
        Document(  
            page_content="A bunch of normal-sized women are supremely wholesome and some men pine after them",  
            metadata={  
                "year": 2019,  
                "director": "Greta Gerwig",  
                "genre": "drama",  
                "rating": 8.3,  
            },  
        ),  
        Document(  
            page_content="Toys come alive and have a blast doing so",  
            metadata={  
                "year": 1995,  
                "director": "John Lasseter",  
                "genre": "animated",  
                "rating": 9.1,  
            },  
        ),  
        Document(  
            page_content="Three men walk into the Zone, three men walk out of the Zone",  
            metadata={  
                "year": 1979,  
                "rating": 9.9,  
                "director": "Andrei Tarkovsky",  
                "genre": "science fiction",  
            },  
        ),  
    ]  
    


```
[/code]


[code]
```python




    index_schema = {  
        "tag": [{"name": "genre"}],  
        "text": [{"name": "director"}],  
        "numeric": [{"name": "year"}, {"name": "rating"}],  
    }  
      
    vectorstore = Redis.from_documents(  
        docs,  
        embeddings,  
        redis_url="redis://localhost:6379",  
        index_name="movie_reviews",  
        index_schema=index_schema,  
    )  
    


```
[/code]


[code]
```python




        `index_schema` does not match generated metadata schema.  
        If you meant to manually override the schema, please ignore this message.  
        index_schema: {'tag': [{'name': 'genre'}], 'text': [{'name': 'director'}], 'numeric': [{'name': 'year'}, {'name': 'rating'}]}  
        generated_schema: {'text': [{'name': 'director'}, {'name': 'genre'}], 'numeric': [{'name': 'year'}, {'name': 'rating'}], 'tag': []}  
          
    


```
[/code]


## Creating our self-querying retriever​

Now we can instantiate our retriever. To do this we'll need to provide some information upfront about the metadata fields that our documents support and a short description of the document contents.

[code]
```python




    from langchain.chains.query_constructor.base import AttributeInfo  
    from langchain.llms import OpenAI  
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
    


```
[/code]


[code]
```python




    llm = OpenAI(temperature=0)  
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




        /Users/bagatur/langchain/libs/langchain/langchain/chains/llm.py:278: UserWarning: The predict_and_parse method is deprecated, instead pass an output parser directly to LLMChain.  
          warnings.warn(  
      
      
        query='dinosaur' filter=None limit=None  
      
      
      
      
      
        [Document(page_content='A bunch of scientists bring back dinosaurs and mayhem breaks loose', metadata={'id': 'doc:movie_reviews:7b5481d753bc4135851b66fa61def7fb', 'director': 'Steven Spielberg', 'genre': 'science fiction', 'year': '1993', 'rating': '7.7'}),  
         Document(page_content='Toys come alive and have a blast doing so', metadata={'id': 'doc:movie_reviews:9e4e84daa0374941a6aa4274e9bbb607', 'director': 'John Lasseter', 'genre': 'animated', 'year': '1995', 'rating': '9.1'}),  
         Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'id': 'doc:movie_reviews:2cc66f38bfbd438eb3a045d90a1a4088', 'director': 'Andrei Tarkovsky', 'genre': 'science fiction', 'year': '1979', 'rating': '9.9'}),  
         Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'id': 'doc:movie_reviews:edf567b1d5334e02b2a4c692d853c80c', 'director': 'Satoshi Kon', 'genre': 'science fiction', 'year': '2006', 'rating': '8.6'})]  
    


```
[/code]


[code]
```python




    # This example only specifies a filter  
    retriever.get_relevant_documents("I want to watch a movie rated higher than 8.4")  
    


```
[/code]


[code]
```python




        query=' ' filter=Comparison(comparator=<Comparator.GT: 'gt'>, attribute='rating', value=8.4) limit=None  
      
      
      
      
      
        [Document(page_content='Toys come alive and have a blast doing so', metadata={'id': 'doc:movie_reviews:9e4e84daa0374941a6aa4274e9bbb607', 'director': 'John Lasseter', 'genre': 'animated', 'year': '1995', 'rating': '9.1'}),  
         Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'id': 'doc:movie_reviews:2cc66f38bfbd438eb3a045d90a1a4088', 'director': 'Andrei Tarkovsky', 'genre': 'science fiction', 'year': '1979', 'rating': '9.9'}),  
         Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'id': 'doc:movie_reviews:edf567b1d5334e02b2a4c692d853c80c', 'director': 'Satoshi Kon', 'genre': 'science fiction', 'year': '2006', 'rating': '8.6'})]  
    


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




        query='women' filter=Comparison(comparator=<Comparator.EQ: 'eq'>, attribute='director', value='Greta Gerwig') limit=None  
      
      
      
      
      
        [Document(page_content='A bunch of normal-sized women are supremely wholesome and some men pine after them', metadata={'id': 'doc:movie_reviews:bb899807b93c442083fd45e75a4779d5', 'director': 'Greta Gerwig', 'genre': 'drama', 'year': '2019', 'rating': '8.3'})]  
    


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




        query=' ' filter=Operation(operator=<Operator.AND: 'and'>, arguments=[Comparison(comparator=<Comparator.GTE: 'gte'>, attribute='rating', value=8.5), Comparison(comparator=<Comparator.CONTAIN: 'contain'>, attribute='genre', value='science fiction')]) limit=None  
      
      
      
      
      
        [Document(page_content='Three men walk into the Zone, three men walk out of the Zone', metadata={'id': 'doc:movie_reviews:2cc66f38bfbd438eb3a045d90a1a4088', 'director': 'Andrei Tarkovsky', 'genre': 'science fiction', 'year': '1979', 'rating': '9.9'}),  
         Document(page_content='A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea', metadata={'id': 'doc:movie_reviews:edf567b1d5334e02b2a4c692d853c80c', 'director': 'Satoshi Kon', 'genre': 'science fiction', 'year': '2006', 'rating': '8.6'})]  
    


```
[/code]


[code]
```python




    # This example specifies a query and composite filter  
    retriever.get_relevant_documents(  
        "What's a movie after 1990 but before 2005 that's all about toys, and preferably is animated"  
    )  
    


```
[/code]


[code]
```python




        query='toys' filter=Operation(operator=<Operator.AND: 'and'>, arguments=[Comparison(comparator=<Comparator.GT: 'gt'>, attribute='year', value=1990), Comparison(comparator=<Comparator.LT: 'lt'>, attribute='year', value=2005), Comparison(comparator=<Comparator.CONTAIN: 'contain'>, attribute='genre', value='animated')]) limit=None  
      
      
      
      
      
        [Document(page_content='Toys come alive and have a blast doing so', metadata={'id': 'doc:movie_reviews:9e4e84daa0374941a6aa4274e9bbb607', 'director': 'John Lasseter', 'genre': 'animated', 'year': '1995', 'rating': '9.1'})]  
    


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




        query='dinosaur' filter=None limit=2  
      
      
      
      
      
        [Document(page_content='A bunch of scientists bring back dinosaurs and mayhem breaks loose', metadata={'id': 'doc:movie_reviews:7b5481d753bc4135851b66fa61def7fb', 'director': 'Steven Spielberg', 'genre': 'science fiction', 'year': '1993', 'rating': '7.7'}),  
         Document(page_content='Toys come alive and have a blast doing so', metadata={'id': 'doc:movie_reviews:9e4e84daa0374941a6aa4274e9bbb607', 'director': 'John Lasseter', 'genre': 'animated', 'year': '1995', 'rating': '9.1'})]  
    


```
[/code]


