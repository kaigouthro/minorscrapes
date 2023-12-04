

Skip to main content

On this page

# Redis

Redis vector database introduction and langchain integration guide.

## What is Redis?​

Most developers from a web services background are probably familiar with Redis. At it's core, Redis is an open-source key-value store that can be used as a cache, message broker, and database.
Developers choose Redis because it is fast, has a large ecosystem of client libraries, and has been deployed by major enterprises for years.

On top of these traditional use cases, Redis provides additional capabilities like the Search and Query capability that allows users to create secondary index structures within Redis. This allows
Redis to be a Vector Database, at the speed of a cache.

## Redis as a Vector Database​

Redis uses compressed, inverted indexes for fast indexing with a low memory footprint. It also supports a number of advanced features such as:

  * Indexing of multiple fields in Redis hashes and JSON
  * Vector similarity search (with HNSW (ANN) or FLAT (KNN))
  * Vector Range Search (e.g. find all vectors within a radius of a query vector)
  * Incremental indexing without performance loss
  * Document ranking (using tf-idf, with optional user-provided weights)
  * Field weighting
  * Complex boolean queries with AND, OR, and NOT operators
  * Prefix matching, fuzzy matching, and exact-phrase queries
  * Support for double-metaphone phonetic matching
  * Auto-complete suggestions (with fuzzy prefix suggestions)
  * Stemming-based query expansion in many languages (using Snowball)
  * Support for Chinese-language tokenization and querying (using Friso)
  * Numeric filters and ranges
  * Geospatial searches using Redis geospatial indexing
  * A powerful aggregations engine
  * Supports for all utf-8 encoded text
  * Retrieve full documents, selected fields, or only the document IDs
  * Sorting results (for example, by creation date)

## Clients​

Since redis is much more than just a vector database, there are often use cases that demand usage of a Redis client besides just the langchain integration. You can use any standard Redis client
library to run Search and Query commands, but it's easiest to use a library that wraps the Search and Query API. Below are a few examples, but you can find more client libraries here.

Project| Language| License| Author| Stars  
---|---|---|---|---  
jedis| Java| MIT| Redis|  
redisvl| Python| MIT| Redis|  
redis-py| Python| MIT| Redis|  
node-redis| Node.js| MIT| Redis|  
nredisstack| .NET| MIT| Redis|  
  
## Deployment Options​

There are many ways to deploy Redis with RediSearch. The easiest way to get started is to use Docker, but there are are many potential options for deployment such as

  * Redis Cloud
  * Docker (Redis Stack)
  * Cloud marketplaces: AWS Marketplace, Google Marketplace, or Azure Marketplace
  * On-premise: Redis Enterprise Software
  * Kubernetes: Redis Enterprise Software on Kubernetes

## Examples​

Many examples can be found in the Redis AI team's GitHub

  * Awesome Redis AI Resources \- List of examples of using Redis in AI workloads
  * Azure OpenAI Embeddings Q&A \- OpenAI and Redis as a Q&A service on Azure.
  * ArXiv Paper Search \- Semantic search over arXiv scholarly papers
  * Vector Search on Azure \- Vector search on Azure using Azure Cache for Redis and Azure OpenAI

## More Resources​

For more information on how to use Redis as a vector database, check out the following resources:

  * RedisVL Documentation \- Documentation for the Redis Vector Library Client
  * Redis Vector Similarity Docs \- Redis official docs for Vector Search.
  * Redis-py Search Docs \- Documentation for redis-py client library
  * Vector Similarity Search: From Basics to Production \- Introductory blog post to VSS and Redis as a VectorDB.

## Install Redis Python Client​

Redis-py is the officially supported client by Redis. Recently released is the RedisVL client which is purpose-built for the Vector Database use cases. Both can be installed with pip.

[code]
```python




    pip install redis redisvl openai tiktoken  
    


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




    from langchain.embeddings import OpenAIEmbeddings  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


## Sample Data​

First we will describe some sample data so that the various attributes of the Redis vector store can be demonstrated.

[code]
```python




    metadata = [  
        {  
            "user": "john",  
            "age": 18,  
            "job": "engineer",  
            "credit_score": "high",  
        },  
        {  
            "user": "derrick",  
            "age": 45,  
            "job": "doctor",  
            "credit_score": "low",  
        },  
        {  
            "user": "nancy",  
            "age": 94,  
            "job": "doctor",  
            "credit_score": "high",  
        },  
        {  
            "user": "tyler",  
            "age": 100,  
            "job": "engineer",  
            "credit_score": "high",  
        },  
        {  
            "user": "joe",  
            "age": 35,  
            "job": "dentist",  
            "credit_score": "medium",  
        },  
    ]  
    texts = ["foo", "foo", "foo", "bar", "bar"]  
    


```
[/code]


## Initializing Redis​

To locally deploy Redis, run:

[code]
```python




    docker run -d -p 6379:6379 -p 8001:8001 redis/redis-stack:latest  
    


```
[/code]


If things are running correctly you should see a nice Redis UI at http://localhost:8001. See the Deployment Options section above for other ways to deploy.

The Redis VectorStore instance can be initialized in a number of ways. There are multiple class methods that can be used to initialize a Redis VectorStore instance.

  * `Redis.__init__` \- Initialize directly
  * `Redis.from_documents` \- Initialize from a list of `Langchain.docstore.Document` objects
  * `Redis.from_texts` \- Initialize from a list of texts (optionally with metadata)
  * `Redis.from_texts_return_keys` \- Initialize from a list of texts (optionally with metadata) and return the keys
  * `Redis.from_existing_index` \- Initialize from an existing Redis index

Below we will use the `Redis.from_texts` method.

[code]
```python




    from langchain.vectorstores.redis import Redis  
      
    rds = Redis.from_texts(  
        texts,  
        embeddings,  
        metadatas=metadata,  
        redis_url="redis://localhost:6379",  
        index_name="users",  
    )  
    


```
[/code]


[code]
```python




    rds.index_name  
    


```
[/code]


[code]
```python




        'users'  
    


```
[/code]


## Inspecting the Created Index​

Once the `Redis` VectorStore object has been constructed, an index will have been created in Redis if it did not already exist. The index can be inspected with both the `rvl`and the `redis-cli`
command line tool. If you installed `redisvl` above, you can use the `rvl` command line tool to inspect the index.

[code]
```python




    # assumes you're running Redis locally (use --host, --port, --password, --username, to change this)  
    rvl index listall  
    


```
[/code]


[code]
```python




        16:58:26 [RedisVL] INFO   Indices:  
        16:58:26 [RedisVL] INFO   1. users  
    


```
[/code]


The `Redis` VectorStore implementation will attempt to generate index schema (fields for filtering) for any metadata passed through the `from_texts`, `from_texts_return_keys`, and `from_documents`
methods. This way, whatever metadata is passed will be indexed into the Redis search index allowing for filtering on those fields.

Below we show what fields were created from the metadata we defined above

[code]
```python




    rvl index info -i users  
    


```
[/code]


[code]
```python




          
          
        Index Information:  
        ╭──────────────┬────────────────┬───────────────┬─────────────────┬────────────╮  
        │ Index Name   │ Storage Type   │ Prefixes      │ Index Options   │   Indexing │  
        ├──────────────┼────────────────┼───────────────┼─────────────────┼────────────┤  
        │ users        │ HASH           │ ['doc:users'] │ []              │          0 │  
        ╰──────────────┴────────────────┴───────────────┴─────────────────┴────────────╯  
        Index Fields:  
        ╭────────────────┬────────────────┬─────────┬────────────────┬────────────────╮  
        │ Name           │ Attribute      │ Type    │ Field Option   │   Option Value │  
        ├────────────────┼────────────────┼─────────┼────────────────┼────────────────┤  
        │ user           │ user           │ TEXT    │ WEIGHT         │              1 │  
        │ job            │ job            │ TEXT    │ WEIGHT         │              1 │  
        │ credit_score   │ credit_score   │ TEXT    │ WEIGHT         │              1 │  
        │ content        │ content        │ TEXT    │ WEIGHT         │              1 │  
        │ age            │ age            │ NUMERIC │                │                │  
        │ content_vector │ content_vector │ VECTOR  │                │                │  
        ╰────────────────┴────────────────┴─────────┴────────────────┴────────────────╯  
    


```
[/code]


[code]
```python




    rvl stats -i users  
    


```
[/code]


[code]
```python




          
        Statistics:  
        ╭─────────────────────────────┬─────────────╮  
        │ Stat Key                    │ Value       │  
        ├─────────────────────────────┼─────────────┤  
        │ num_docs                    │ 5           │  
        │ num_terms                   │ 15          │  
        │ max_doc_id                  │ 5           │  
        │ num_records                 │ 33          │  
        │ percent_indexed             │ 1           │  
        │ hash_indexing_failures      │ 0           │  
        │ number_of_uses              │ 4           │  
        │ bytes_per_record_avg        │ 4.60606     │  
        │ doc_table_size_mb           │ 0.000524521 │  
        │ inverted_sz_mb              │ 0.000144958 │  
        │ key_table_size_mb           │ 0.000193596 │  
        │ offset_bits_per_record_avg  │ 8           │  
        │ offset_vectors_sz_mb        │ 2.19345e-05 │  
        │ offsets_per_term_avg        │ 0.69697     │  
        │ records_per_doc_avg         │ 6.6         │  
        │ sortable_values_size_mb     │ 0           │  
        │ total_indexing_time         │ 0.32        │  
        │ total_inverted_index_blocks │ 16          │  
        │ vector_index_sz_mb          │ 6.0126      │  
        ╰─────────────────────────────┴─────────────╯  
    


```
[/code]


It's important to note that we have not specified that the `user`, `job`, `credit_score` and `age` in the metadata should be fields within the index, this is because the `Redis` VectorStore object
automatically generate the index schema from the passed metadata. For more information on the generation of index fields, see the API documentation.

## Querying​

There are multiple ways to query the `Redis` VectorStore implementation based on what use case you have:

  * `similarity_search`: Find the most similar vectors to a given vector.
  * `similarity_search_with_score`: Find the most similar vectors to a given vector and return the vector distance
  * `similarity_search_limit_score`: Find the most similar vectors to a given vector and limit the number of results to the `score_threshold`
  * `similarity_search_with_relevance_scores`: Find the most similar vectors to a given vector and return the vector similarities
  * `max_marginal_relevance_search`: Find the most similar vectors to a given vector while also optimizing for diversity

[code]
```python




    results = rds.similarity_search("foo")  
    print(results[0].page_content)  
    


```
[/code]


[code]
```python




        foo  
    


```
[/code]


[code]
```python




    # return metadata  
    results = rds.similarity_search("foo", k=3)  
    meta = results[1].metadata  
    print("Key of the document in Redis: ", meta.pop("id"))  
    print("Metadata of the document: ", meta)  
    


```
[/code]


[code]
```python




        Key of the document in Redis:  doc:users:a70ca43b3a4e4168bae57c78753a200f  
        Metadata of the document:  {'user': 'derrick', 'job': 'doctor', 'credit_score': 'low', 'age': '45'}  
    


```
[/code]


[code]
```python




    # with scores (distances)  
    results = rds.similarity_search_with_score("foo", k=5)  
    for result in results:  
        print(f"Content: {result[0].page_content} --- Score: {result[1]}")  
    


```
[/code]


[code]
```python




        Content: foo --- Score: 0.0  
        Content: foo --- Score: 0.0  
        Content: foo --- Score: 0.0  
        Content: bar --- Score: 0.1566  
        Content: bar --- Score: 0.1566  
    


```
[/code]


[code]
```python




    # limit the vector distance that can be returned  
    results = rds.similarity_search_with_score("foo", k=5, distance_threshold=0.1)  
    for result in results:  
        print(f"Content: {result[0].page_content} --- Score: {result[1]}")  
    


```
[/code]


[code]
```python




        Content: foo --- Score: 0.0  
        Content: foo --- Score: 0.0  
        Content: foo --- Score: 0.0  
    


```
[/code]


[code]
```python




    # with scores  
    results = rds.similarity_search_with_relevance_scores("foo", k=5)  
    for result in results:  
        print(f"Content: {result[0].page_content} --- Similiarity: {result[1]}")  
    


```
[/code]


[code]
```python




        Content: foo --- Similiarity: 1.0  
        Content: foo --- Similiarity: 1.0  
        Content: foo --- Similiarity: 1.0  
        Content: bar --- Similiarity: 0.8434  
        Content: bar --- Similiarity: 0.8434  
    


```
[/code]


[code]
```python




    # limit scores (similarities have to be over .9)  
    results = rds.similarity_search_with_relevance_scores("foo", k=5, score_threshold=0.9)  
    for result in results:  
        print(f"Content: {result[0].page_content} --- Similarity: {result[1]}")  
    


```
[/code]


[code]
```python




        Content: foo --- Similarity: 1.0  
        Content: foo --- Similarity: 1.0  
        Content: foo --- Similarity: 1.0  
    


```
[/code]


[code]
```python




    # you can also add new documents as follows  
    new_document = ["baz"]  
    new_metadata = [{"user": "sam", "age": 50, "job": "janitor", "credit_score": "high"}]  
    # both the document and metadata must be lists  
    rds.add_texts(new_document, new_metadata)  
    


```
[/code]


[code]
```python




        ['doc:users:b9c71d62a0a34241a37950b448dafd38']  
    


```
[/code]


[code]
```python




    # now query the new document  
    results = rds.similarity_search("baz", k=3)  
    print(results[0].metadata)  
    


```
[/code]


[code]
```python




        {'id': 'doc:users:b9c71d62a0a34241a37950b448dafd38', 'user': 'sam', 'job': 'janitor', 'credit_score': 'high', 'age': '50'}  
    


```
[/code]


[code]
```python




    # use maximal marginal relevance search to diversify results  
    results = rds.max_marginal_relevance_search("foo")  
    


```
[/code]


[code]
```python




    # the lambda_mult parameter controls the diversity of the results, the lower the more diverse  
    results = rds.max_marginal_relevance_search("foo", lambda_mult=0.1)  
    


```
[/code]


## Connect to an Existing Index​

In order to have the same metadata indexed when using the `Redis` VectorStore. You will need to have the same `index_schema` passed in either as a path to a yaml file or as a dictionary. The following
shows how to obtain the schema from an index and connect to an existing index.

[code]
```python




    # write the schema to a yaml file  
    rds.write_schema("redis_schema.yaml")  
    


```
[/code]


The schema file for this example should look something like:

[code]
```python




    numeric:  
    - name: age  
      no_index: false  
      sortable: false  
    text:  
    - name: user  
      no_index: false  
      no_stem: false  
      sortable: false  
      weight: 1  
      withsuffixtrie: false  
    - name: job  
      no_index: false  
      no_stem: false  
      sortable: false  
      weight: 1  
      withsuffixtrie: false  
    - name: credit_score  
      no_index: false  
      no_stem: false  
      sortable: false  
      weight: 1  
      withsuffixtrie: false  
    - name: content  
      no_index: false  
      no_stem: false  
      sortable: false  
      weight: 1  
      withsuffixtrie: false  
    vector:  
    - algorithm: FLAT  
      block_size: 1000  
      datatype: FLOAT32  
      dims: 1536  
      distance_metric: COSINE  
      initial_cap: 20000  
      name: content_vector  
    


```
[/code]


 **Notice** , this include **all** possible fields for the schema. You can remove any fields that you don't need.

[code]
```python




    # now we can connect to our existing index as follows  
      
    new_rds = Redis.from_existing_index(  
        embeddings,  
        index_name="users",  
        redis_url="redis://localhost:6379",  
        schema="redis_schema.yaml",  
    )  
    results = new_rds.similarity_search("foo", k=3)  
    print(results[0].metadata)  
    


```
[/code]


[code]
```python




        {'id': 'doc:users:8484c48a032d4c4cbe3cc2ed6845fabb', 'user': 'john', 'job': 'engineer', 'credit_score': 'high', 'age': '18'}  
    


```
[/code]


[code]
```python




    # see the schemas are the same  
    new_rds.schema == rds.schema  
    


```
[/code]


[code]
```python




        True  
    


```
[/code]


## Custom Metadata Indexing​

In some cases, you may want to control what fields the metadata maps to. For example, you may want the `credit_score` field to be a categorical field instead of a text field (which is the default
behavior for all string fields). In this case, you can use the `index_schema` parameter in each of the initialization methods above to specify the schema for the index. Custom index schema can either
be passed as a dictionary or as a path to a yaml file.

All arguments in the schema have defaults besides the name, so you can specify only the fields you want to change. All the names correspond to the snake/lowercase versions of the arguments you would
use on the command line with `redis-cli` or in `redis-py`. For more on the arguments for each field, see the documentation

The below example shows how to specify the schema for the `credit_score` field as a Tag (categorical) field instead of a text field.

[code]
```python




    # index_schema.yml  
    tag:  
        - name: credit_score  
    text:  
        - name: user  
        - name: job  
    numeric:  
        - name: age  
    


```
[/code]


In Python this would look like:

[code]
```python




      
    index_schema = {  
        "tag": [{"name": "credit_score"}],  
        "text": [{"name": "user"}, {"name": "job"}],  
        "numeric": [{"name": "age"}],  
    }  
      
    


```
[/code]


Notice that only the `name` field needs to be specified. All other fields have defaults.

[code]
```python




    # create a new index with the new schema defined above  
    index_schema = {  
        "tag": [{"name": "credit_score"}],  
        "text": [{"name": "user"}, {"name": "job"}],  
        "numeric": [{"name": "age"}],  
    }  
      
    rds, keys = Redis.from_texts_return_keys(  
        texts,  
        embeddings,  
        metadatas=metadata,  
        redis_url="redis://localhost:6379",  
        index_name="users_modified",  
        index_schema=index_schema,  # pass in the new index schema  
    )  
    


```
[/code]


[code]
```python




        `index_schema` does not match generated metadata schema.  
        If you meant to manually override the schema, please ignore this message.  
        index_schema: {'tag': [{'name': 'credit_score'}], 'text': [{'name': 'user'}, {'name': 'job'}], 'numeric': [{'name': 'age'}]}  
        generated_schema: {'text': [{'name': 'user'}, {'name': 'job'}, {'name': 'credit_score'}], 'numeric': [{'name': 'age'}], 'tag': []}  
          
    


```
[/code]


The above warning is meant to notify users when they are overriding the default behavior. Ignore it if you are intentionally overriding the behavior.

## Hybrid Filtering​

With the Redis Filter Expression language built into langchain, you can create arbitrarily long chains of hybrid filters that can be used to filter your search results. The expression language is
derived from the RedisVL Expression Syntax and is designed to be easy to use and understand.

The following are the available filter types:

  * `RedisText`: Filter by full-text search against metadata fields. Supports exact, fuzzy, and wildcard matching.
  * `RedisNum`: Filter by numeric range against metadata fields.
  * `RedisTag`: Filter by exact match against string based categorical metadata fields. Multiple tags can be specified like "tag1,tag2,tag3".

The following are examples of utilizing these filters.

[code]
```python




      
    from langchain.vectorstores.redis import RedisText, RedisNum, RedisTag  
      
    # exact matching  
    has_high_credit = RedisTag("credit_score") == "high"  
    does_not_have_high_credit = RedisTag("credit_score") != "low"  
      
    # fuzzy matching  
    job_starts_with_eng = RedisText("job") % "eng*"  
    job_is_engineer = RedisText("job") == "engineer"  
    job_is_not_engineer = RedisText("job") != "engineer"  
      
    # numeric filtering  
    age_is_18 = RedisNum("age") == 18  
    age_is_not_18 = RedisNum("age") != 18  
    age_is_greater_than_18 = RedisNum("age") > 18  
    age_is_less_than_18 = RedisNum("age") < 18  
    age_is_greater_than_or_equal_to_18 = RedisNum("age") >= 18  
    age_is_less_than_or_equal_to_18 = RedisNum("age") <= 18  
      
    


```
[/code]


The `RedisFilter` class can be used to simplify the import of these filters as follows

[code]
```python




      
    from langchain.vectorstores.redis import RedisFilter  
      
    # same examples as above  
    has_high_credit = RedisFilter.tag("credit_score") == "high"  
    does_not_have_high_credit = RedisFilter.num("age") > 8  
    job_starts_with_eng = RedisFilter.text("job") % "eng*"  
    


```
[/code]


The following are examples of using hybrid filter for search

[code]
```python




    from langchain.vectorstores.redis import RedisText  
      
    is_engineer = RedisText("job") == "engineer"  
    results = rds.similarity_search("foo", k=3, filter=is_engineer)  
      
    print("Job:", results[0].metadata["job"])  
    print("Engineers in the dataset:", len(results))  
    


```
[/code]


[code]
```python




        Job: engineer  
        Engineers in the dataset: 2  
    


```
[/code]


[code]
```python




    # fuzzy match  
    starts_with_doc = RedisText("job") % "doc*"  
    results = rds.similarity_search("foo", k=3, filter=starts_with_doc)  
      
    for result in results:  
        print("Job:", result.metadata["job"])  
    print("Jobs in dataset that start with 'doc':", len(results))  
    


```
[/code]


[code]
```python




        Job: doctor  
        Job: doctor  
        Jobs in dataset that start with 'doc': 2  
    


```
[/code]


[code]
```python




    from langchain.vectorstores.redis import RedisNum  
      
    is_over_18 = RedisNum("age") > 18  
    is_under_99 = RedisNum("age") < 99  
    age_range = is_over_18 & is_under_99  
    results = rds.similarity_search("foo", filter=age_range)  
      
    for result in results:  
        print("User:", result.metadata["user"], "is", result.metadata["age"])  
    


```
[/code]


[code]
```python




        User: derrick is 45  
        User: nancy is 94  
        User: joe is 35  
    


```
[/code]


[code]
```python




    # make sure to use parenthesis around FilterExpressions  
    # if initializing them while constructing them  
    age_range = (RedisNum("age") > 18) & (RedisNum("age") < 99)  
    results = rds.similarity_search("foo", filter=age_range)  
      
    for result in results:  
        print("User:", result.metadata["user"], "is", result.metadata["age"])  
    


```
[/code]


[code]
```python




        User: derrick is 45  
        User: nancy is 94  
        User: joe is 35  
    


```
[/code]


## Redis as Retriever​

Here we go over different options for using the vector store as a retriever.

There are three different search methods we can use to do retrieval. By default, it will use semantic similarity.

[code]
```python




    query = "foo"  
    results = rds.similarity_search_with_score(query, k=3, return_metadata=True)  
      
    for result in results:  
        print("Content:", result[0].page_content, " --- Score: ", result[1])  
    


```
[/code]


[code]
```python




        Content: foo  --- Score:  0.0  
        Content: foo  --- Score:  0.0  
        Content: foo  --- Score:  0.0  
    


```
[/code]


[code]
```python




    retriever = rds.as_retriever(search_type="similarity", search_kwargs={"k": 4})  
    


```
[/code]


[code]
```python




    docs = retriever.get_relevant_documents(query)  
    docs  
    


```
[/code]


[code]
```python




        [Document(page_content='foo', metadata={'id': 'doc:users_modified:988ecca7574048e396756efc0e79aeca', 'user': 'john', 'job': 'engineer', 'credit_score': 'high', 'age': '18'}),  
         Document(page_content='foo', metadata={'id': 'doc:users_modified:009b1afeb4084cc6bdef858c7a99b48e', 'user': 'derrick', 'job': 'doctor', 'credit_score': 'low', 'age': '45'}),  
         Document(page_content='foo', metadata={'id': 'doc:users_modified:7087cee9be5b4eca93c30fbdd09a2731', 'user': 'nancy', 'job': 'doctor', 'credit_score': 'high', 'age': '94'}),  
         Document(page_content='bar', metadata={'id': 'doc:users_modified:01ef6caac12b42c28ad870aefe574253', 'user': 'tyler', 'job': 'engineer', 'credit_score': 'high', 'age': '100'})]  
    


```
[/code]


There is also the `similarity_distance_threshold` retriever which allows the user to specify the vector distance

[code]
```python




    retriever = rds.as_retriever(  
        search_type="similarity_distance_threshold",  
        search_kwargs={"k": 4, "distance_threshold": 0.1},  
    )  
    


```
[/code]


[code]
```python




    docs = retriever.get_relevant_documents(query)  
    docs  
    


```
[/code]


[code]
```python




        [Document(page_content='foo', metadata={'id': 'doc:users_modified:988ecca7574048e396756efc0e79aeca', 'user': 'john', 'job': 'engineer', 'credit_score': 'high', 'age': '18'}),  
         Document(page_content='foo', metadata={'id': 'doc:users_modified:009b1afeb4084cc6bdef858c7a99b48e', 'user': 'derrick', 'job': 'doctor', 'credit_score': 'low', 'age': '45'}),  
         Document(page_content='foo', metadata={'id': 'doc:users_modified:7087cee9be5b4eca93c30fbdd09a2731', 'user': 'nancy', 'job': 'doctor', 'credit_score': 'high', 'age': '94'})]  
    


```
[/code]


Lastly, the `similarity_score_threshold` allows the user to define the minimum score for similar documents

[code]
```python




    retriever = rds.as_retriever(  
        search_type="similarity_score_threshold",  
        search_kwargs={"score_threshold": 0.9, "k": 10},  
    )  
    


```
[/code]


[code]
```python




    retriever.get_relevant_documents("foo")  
    


```
[/code]


[code]
```python




        [Document(page_content='foo', metadata={'id': 'doc:users_modified:988ecca7574048e396756efc0e79aeca', 'user': 'john', 'job': 'engineer', 'credit_score': 'high', 'age': '18'}),  
         Document(page_content='foo', metadata={'id': 'doc:users_modified:009b1afeb4084cc6bdef858c7a99b48e', 'user': 'derrick', 'job': 'doctor', 'credit_score': 'low', 'age': '45'}),  
         Document(page_content='foo', metadata={'id': 'doc:users_modified:7087cee9be5b4eca93c30fbdd09a2731', 'user': 'nancy', 'job': 'doctor', 'credit_score': 'high', 'age': '94'})]  
    


```
[/code]


[code]
```python




    retriever = rds.as_retriever(  
        search_type="mmr", search_kwargs={"fetch_k": 20, "k": 4, "lambda_mult": 0.1}  
    )  
    


```
[/code]


[code]
```python




    retriever.get_relevant_documents("foo")  
    


```
[/code]


[code]
```python




        [Document(page_content='foo', metadata={'id': 'doc:users:8f6b673b390647809d510112cde01a27', 'user': 'john', 'job': 'engineer', 'credit_score': 'high', 'age': '18'}),  
         Document(page_content='bar', metadata={'id': 'doc:users:93521560735d42328b48c9c6f6418d6a', 'user': 'tyler', 'job': 'engineer', 'credit_score': 'high', 'age': '100'}),  
         Document(page_content='foo', metadata={'id': 'doc:users:125ecd39d07845eabf1a699d44134a5b', 'user': 'nancy', 'job': 'doctor', 'credit_score': 'high', 'age': '94'}),  
         Document(page_content='foo', metadata={'id': 'doc:users:d6200ab3764c466082fde3eaab972a2a', 'user': 'derrick', 'job': 'doctor', 'credit_score': 'low', 'age': '45'})]  
    


```
[/code]


# Delete keys

To delete your entries you have to address them by their keys.

[code]
```python




    Redis.delete(keys, redis_url="redis://localhost:6379")  
    


```
[/code]


[code]
```python




        True  
    


```
[/code]


[code]
```python




    # delete the indices too  
    Redis.drop_index(  
        index_name="users", delete_documents=True, redis_url="redis://localhost:6379"  
    )  
    Redis.drop_index(  
        index_name="users_modified",  
        delete_documents=True,  
        redis_url="redis://localhost:6379",  
    )  
    


```
[/code]


[code]
```python




        True  
    


```
[/code]


### Redis connection Url examples​

Valid Redis Url scheme are:

  1. `redis://` \- Connection to Redis standalone, unencrypted
  2. `rediss://` \- Connection to Redis standalone, with TLS encryption
  3. `redis+sentinel://` \- Connection to Redis server via Redis Sentinel, unencrypted
  4. `rediss+sentinel://` \- Connection to Redis server via Redis Sentinel, booth connections with TLS encryption

More information about additional connection parameter can be found in the redis-py documentation at https://redis-py.readthedocs.io/en/stable/connections.html

[code]
```python




    # connection to redis standalone at localhost, db 0, no password  
    redis_url = "redis://localhost:6379"  
    # connection to host "redis" port 7379 with db 2 and password "secret" (old style authentication scheme without username / pre 6.x)  
    redis_url = "redis://:secret@redis:7379/2"  
    # connection to host redis on default port with user "joe", pass "secret" using redis version 6+ ACLs  
    redis_url = "redis://joe:secret@redis/0"  
      
    # connection to sentinel at localhost with default group mymaster and db 0, no password  
    redis_url = "redis+sentinel://localhost:26379"  
    # connection to sentinel at host redis with default port 26379 and user "joe" with password "secret" with default group mymaster and db 0  
    redis_url = "redis+sentinel://joe:secret@redis"  
    # connection to sentinel, no auth with sentinel monitoring group "zone-1" and database 2  
    redis_url = "redis+sentinel://redis:26379/zone-1/2"  
      
    # connection to redis standalone at localhost, db 0, no password but with TLS support  
    redis_url = "rediss://localhost:6379"  
    # connection to redis sentinel at localhost and default port, db 0, no password  
    # but with TLS support for booth Sentinel and Redis server  
    redis_url = "rediss+sentinel://localhost"  
    


```
[/code]


