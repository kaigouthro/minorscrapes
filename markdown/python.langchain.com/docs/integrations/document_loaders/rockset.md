

Skip to main content

On this page

# Rockset

> Rockset is a real-time analytics database which enables queries on massive, semi-structured data without operational burden. With Rockset, ingested data is queryable within one second and analytical
> queries against that data typically execute in milliseconds. Rockset is compute optimized, making it suitable for serving high concurrency applications in the sub-100TB range (or larger than 100s of
> TBs with rollups).

This notebook demonstrates how to use Rockset as a document loader in langchain. To get started, make sure you have a Rockset account and an API key available.

## Setting up the environment​

  1. Go to the Rockset console and get an API key. Find your API region from the API reference. For the purpose of this notebook, we will assume you're using Rockset from `Oregon(us-west-2)`.
  2. Set your the environment variable `ROCKSET_API_KEY`.
  3. Install the Rockset python client, which will be used by langchain to interact with the Rockset database.

[code]
```python




    pip install rockset  
    


```
[/code]


# Loading Documents

The Rockset integration with LangChain allows you to load documents from Rockset collections with SQL queries. In order to do this you must construct a `RocksetLoader` object. Here is an example
snippet that initializes a `RocksetLoader`.

[code]
```python




    from langchain.document_loaders import RocksetLoader  
    from rockset import Regions, RocksetClient, models  
      
    loader = RocksetLoader(  
        RocksetClient(Regions.usw2a1, "<api key>"),  
        models.QueryRequestSql(query="SELECT * FROM langchain_demo LIMIT 3"),  # SQL query  
        ["text"],  # content columns  
        metadata_keys=["id", "date"],  # metadata columns  
    )  
    


```
[/code]


Here, you can see that the following query is run:

[code]
```python




    SELECT * FROM langchain_demo LIMIT 3  
    


```
[/code]


The `text` column in the collection is used as the page content, and the record's `id` and `date` columns are used as metadata (if you do not pass anything into `metadata_keys`, the whole Rockset
document will be used as metadata).

To execute the query and access an iterator over the resulting `Document`s, run:

[code]
```python




    loader.lazy_load()  
    


```
[/code]


To execute the query and access all resulting `Document`s at once, run:

[code]
```python




    loader.load()  
    


```
[/code]


Here is an example response of `loader.load()`:

[code]
```python




    [  
        Document(  
            page_content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas a libero porta, dictum ipsum eget, hendrerit neque. Morbi blandit, ex ut suscipit viverra, enim velit tincidunt tellus, a tempor velit nunc et ex. Proin hendrerit odio nec convallis lobortis. Aenean in purus dolor. Vestibulum orci orci, laoreet eget magna in, commodo euismod justo.",   
            metadata={"id": 83209, "date": "2022-11-13T18:26:45.000000Z"}  
        ),  
        Document(  
            page_content="Integer at finibus odio. Nam sit amet enim cursus lacus gravida feugiat vestibulum sed libero. Aenean eleifend est quis elementum tincidunt. Curabitur sit amet ornare erat. Nulla id dolor ut magna volutpat sodales fringilla vel ipsum. Donec ultricies, lacus sed fermentum dignissim, lorem elit aliquam ligula, sed suscipit sapien purus nec ligula.",   
            metadata={"id": 89313, "date": "2022-11-13T18:28:53.000000Z"}  
        ),  
        Document(  
            page_content="Morbi tortor enim, commodo id efficitur vitae, fringilla nec mi. Nullam molestie faucibus aliquet. Praesent a est facilisis, condimentum justo sit amet, viverra erat. Fusce volutpat nisi vel purus blandit, et facilisis felis accumsan. Phasellus luctus ligula ultrices tellus tempor hendrerit. Donec at ultricies leo.",   
            metadata={"id": 87732, "date": "2022-11-13T18:49:04.000000Z"}  
        )  
    ]  
    


```
[/code]


## Using multiple columns as content​

You can choose to use multiple columns as content:

[code]
```python




    from langchain.document_loaders import RocksetLoader  
    from rockset import Regions, RocksetClient, models  
      
    loader = RocksetLoader(  
        RocksetClient(Regions.usw2a1, "<api key>"),  
        models.QueryRequestSql(query="SELECT * FROM langchain_demo LIMIT 1 WHERE id=38"),  
        ["sentence1", "sentence2"],  # TWO content columns  
    )  
    


```
[/code]


Assuming the "sentence1" field is `"This is the first sentence."` and the "sentence2" field is `"This is the second sentence."`, the `page_content` of the resulting `Document` would be:

[code]
```python




    This is the first sentence.  
    This is the second sentence.  
    


```
[/code]


You can define you own function to join content columns by setting the `content_columns_joiner` argument in the `RocksetLoader` constructor. `content_columns_joiner` is a method that takes in a
`List[Tuple[str, Any]]]` as an argument, representing a list of tuples of (column name, column value). By default, this is a method that joins each column value with a new line.

For example, if you wanted to join sentence1 and sentence2 with a space instead of a new line, you could set `content_columns_joiner` like so:

[code]
```python




    RocksetLoader(  
        RocksetClient(Regions.usw2a1, "<api key>"),  
        models.QueryRequestSql(query="SELECT * FROM langchain_demo LIMIT 1 WHERE id=38"),  
        ["sentence1", "sentence2"],  
        content_columns_joiner=lambda docs: " ".join(  
            [doc[1] for doc in docs]  
        ),  # join with space instead of /n  
    )  
    


```
[/code]


The `page_content` of the resulting `Document` would be:

[code]
```python




    This is the first sentence. This is the second sentence.  
    


```
[/code]


Oftentimes you want to include the column name in the `page_content`. You can do that like this:

[code]
```python




    RocksetLoader(  
        RocksetClient(Regions.usw2a1, "<api key>"),  
        models.QueryRequestSql(query="SELECT * FROM langchain_demo LIMIT 1 WHERE id=38"),  
        ["sentence1", "sentence2"],  
        content_columns_joiner=lambda docs: "\n".join(  
            [f"{doc[0]}: {doc[1]}" for doc in docs]  
        ),  
    )  
    


```
[/code]


This would result in the following `page_content`:

[code]
```python




    sentence1: This is the first sentence.  
    sentence2: This is the second sentence.  
    


```
[/code]


