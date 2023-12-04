

Skip to main content

On this page

# Astra DB

This page provides a quickstart for using Astra DB and Apache Cassandra® as a Vector Store.

 _Note: in addition to access to the database, an OpenAI API Key is required to run the full example._

### Setup and general dependencies​

Use of the integration requires the following Python package.

[code]
```python




    pip install --quiet "astrapy>=0.5.3"  
    


```
[/code]


 _Note: depending on your LangChain setup, you may need to install/upgrade other dependencies needed for this demo_ _(specifically, recent versions of`datasets`, `openai`, `pypdf` and `tiktoken` are
required)._

[code]
```python




    import os  
    from getpass import getpass  
      
    from datasets import (  
        load_dataset,  
    )  
    from langchain.chat_models import ChatOpenAI  
    from langchain.document_loaders import PyPDFLoader  
    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.prompts import ChatPromptTemplate  
    from langchain.schema import Document  
    from langchain.schema.output_parser import StrOutputParser  
    from langchain.schema.runnable import RunnablePassthrough  
    from langchain.text_splitter import RecursiveCharacterTextSplitter  
    


```
[/code]


[code]
```python




    os.environ["OPENAI_API_KEY"] = getpass("OPENAI_API_KEY = ")  
    


```
[/code]


[code]
```python




    embe = OpenAIEmbeddings()  
    


```
[/code]


 _Keep reading to connect with Astra DB. For usage with Apache Cassandra and Astra DB through CQL, scroll to the section below._

## Astra DB​

DataStax Astra DB is a serverless vector-capable database built on Cassandra and made conveniently available through an easy-to-use JSON API.

[code]
```python




    from langchain.vectorstores import AstraDB  
    


```
[/code]


### Astra DB connection parameters​

  * the API Endpoint looks like `https://01234567-89ab-cdef-0123-456789abcdef-us-east1.apps.astra.datastax.com`
  * the Token looks like `AstraCS:6gBhNmsk135....`

[code]
```python




    ASTRA_DB_API_ENDPOINT = input("ASTRA_DB_API_ENDPOINT = ")  
    ASTRA_DB_APPLICATION_TOKEN = getpass("ASTRA_DB_APPLICATION_TOKEN = ")  
    


```
[/code]


[code]
```python




    vstore = AstraDB(  
        embedding=embe,  
        collection_name="astra_vector_demo",  
        api_endpoint=ASTRA_DB_API_ENDPOINT,  
        token=ASTRA_DB_APPLICATION_TOKEN,  
    )  
    


```
[/code]


### Load a dataset​

Convert each entry in the source dataset into a `Document`, then write them into the vector store:

[code]
```python




    philo_dataset = load_dataset("datastax/philosopher-quotes")["train"]  
      
    docs = []  
    for entry in philo_dataset:  
        metadata = {"author": entry["author"]}  
        doc = Document(page_content=entry["quote"], metadata=metadata)  
        docs.append(doc)  
      
    inserted_ids = vstore.add_documents(docs)  
    print(f"\nInserted {len(inserted_ids)} documents.")  
    


```
[/code]


In the above, `metadata` dictionaries are created from the source data and are part of the `Document`.

 _Note: check theAstra DB API Docs for the valid metadata field names: some characters are reserved and cannot be used._

Add some more entries, this time with `add_texts`:

[code]
```python




    texts = ["I think, therefore I am.", "To the things themselves!"]  
    metadatas = [{"author": "descartes"}, {"author": "husserl"}]  
    ids = ["desc_01", "huss_xy"]  
      
    inserted_ids_2 = vstore.add_texts(texts=texts, metadatas=metadatas, ids=ids)  
    print(f"\nInserted {len(inserted_ids_2)} documents.")  
    


```
[/code]


 _Note: you may want to speed up the execution of`add_texts` and `add_documents` by increasing the concurrency level for_ _these bulk operations - check out the`*_concurrency` parameters in the class
constructor and the `add_texts` docstrings_ _for more details. Depending on the network and the client machine specifications, your best-performing choice of parameters may vary._

### Run simple searches​

This section demonstrates metadata filtering and getting the similarity scores back:

[code]
```python




    results = vstore.similarity_search("Our life is what we make of it", k=3)  
    for res in results:  
        print(f"* {res.page_content} [{res.metadata}]")  
    


```
[/code]


[code]
```python




    results_filtered = vstore.similarity_search(  
        "Our life is what we make of it",  
        k=3,  
        filter={"author": "plato"},  
    )  
    for res in results_filtered:  
        print(f"* {res.page_content} [{res.metadata}]")  
    


```
[/code]


[code]
```python




    results = vstore.similarity_search_with_score("Our life is what we make of it", k=3)  
    for res, score in results:  
        print(f"* [SIM={score:3f}] {res.page_content} [{res.metadata}]")  
    


```
[/code]


### MMR (Maximal-marginal-relevance) search​

[code]
```python




    results = vstore.max_marginal_relevance_search(  
        "Our life is what we make of it",  
        k=3,  
        filter={"author": "aristotle"},  
    )  
    for res in results:  
        print(f"* {res.page_content} [{res.metadata}]")  
    


```
[/code]


### Deleting stored documents​

[code]
```python




    delete_1 = vstore.delete(inserted_ids[:3])  
    print(f"all_succeed={delete_1}")  # True, all documents deleted  
    


```
[/code]


[code]
```python




    delete_2 = vstore.delete(inserted_ids[2:5])  
    print(f"some_succeeds={delete_2}")  # True, though some IDs were gone already  
    


```
[/code]


### A minimal RAG chain​

The next cells will implement a simple RAG pipeline:

  * download a sample PDF file and load it onto the store;
  * create a RAG chain with LCEL (LangChain Expression Language), with the vector store at its heart;
  * run the question-answering chain.

[code]
```python




    curl -L \  
        "https://github.com/awesome-astra/datasets/blob/main/demo-resources/what-is-philosophy/what-is-philosophy.pdf?raw=true" \  
        -o "what-is-philosophy.pdf"  
    


```
[/code]


[code]
```python




    pdf_loader = PyPDFLoader("what-is-philosophy.pdf")  
    splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=64)  
    docs_from_pdf = pdf_loader.load_and_split(text_splitter=splitter)  
      
    print(f"Documents from PDF: {len(docs_from_pdf)}.")  
    inserted_ids_from_pdf = vstore.add_documents(docs_from_pdf)  
    print(f"Inserted {len(inserted_ids_from_pdf)} documents.")  
    


```
[/code]


[code]
```python




    retriever = vstore.as_retriever(search_kwargs={"k": 3})  
      
    philo_template = """  
    You are a philosopher that draws inspiration from great thinkers of the past  
    to craft well-thought answers to user questions. Use the provided context as the basis  
    for your answers and do not make up new reasoning paths - just mix-and-match what you are given.  
    Your answers must be concise and to the point, and refrain from answering about other topics than philosophy.  
      
    CONTEXT:  
    {context}  
      
    QUESTION: {question}  
      
    YOUR ANSWER:"""  
      
    philo_prompt = ChatPromptTemplate.from_template(philo_template)  
      
    llm = ChatOpenAI()  
      
    chain = (  
        {"context": retriever, "question": RunnablePassthrough()}  
        | philo_prompt  
        | llm  
        | StrOutputParser()  
    )  
    


```
[/code]


[code]
```python




    chain.invoke("How does Russel elaborate on Peirce's idea of the security blanket?")  
    


```
[/code]


For more, check out a complete RAG template using Astra DB here.

### Cleanup​

If you want to completely delete the collection from your Astra DB instance, run this.

 _(You will lose the data you stored in it.)_

[code]
```python




     vstore.delete_collection()  
    


```
[/code]


## Apache Cassandra and Astra DB through CQL​

Cassandra is a NoSQL, row-oriented, highly scalable and highly available database.Starting with version 5.0, the database ships with vector search capabilities.

DataStax Astra DB through CQL is a managed serverless database built on Cassandra, offering the same interface and strengths.

#### What sets this case apart from "Astra DB" above?​

Thanks to LangChain having a standardized `VectorStore` interface, most of the "Astra DB" section above applies to this case as well. However, this time the database uses the CQL protocol, which means
you'll use a _different_ class this time and instantiate it in another way.

The cells below show how you should get your `vstore` object in this case and how you can clean up the database resources at the end: for the rest, i.e. the actual usage of the vector store, you will
be able to run the very code that was shown above.

In other words, running this demo in full with Cassandra or Astra DB through CQL means:

  *  **initialization as shown below**
  * "Load a dataset", _see above section_
  * "Run simple searches", _see above section_
  * "MMR search", _see above section_
  * "Deleting stored documents", _see above section_
  * "A minimal RAG chain", _see above section_
  *  **cleanup as shown below**

### Initialization​

The class to use is the following:

[code]
```python




    from langchain.vectorstores import Cassandra  
    


```
[/code]


Now, depending on whether you connect to a Cassandra cluster or to Astra DB through CQL, you will provide different parameters when creating the vector store object.

#### Initialization (Cassandra cluster)​

In this case, you first need to create a `cassandra.cluster.Session` object, as described in the Cassandra driver documentation. The details vary (e.g. with network settings and authentication), but
this might be something like:

[code]
```python




    from cassandra.cluster import Cluster  
      
    cluster = Cluster(["127.0.0.1"])  
    session = cluster.connect()  
    


```
[/code]


You can now set the session, along with your desired keyspace name, as a global CassIO parameter:

[code]
```python




    import cassio  
      
    CASSANDRA_KEYSPACE = input("CASSANDRA_KEYSPACE = ")  
      
    cassio.init(session=session, keyspace=CASSANDRA_KEYSPACE)  
    


```
[/code]


Now you can create the vector store:

[code]
```python




    vstore = Cassandra(  
        embedding=embe,  
        table_name="cassandra_vector_demo",  
        # session=None, keyspace=None  # Uncomment on older versions of LangChain  
    )  
    


```
[/code]


#### Initialization (Astra DB through CQL)​

In this case you initialize CassIO with the following connection parameters:

  * the Database ID, e.g. `01234567-89ab-cdef-0123-456789abcdef`
  * the Token, e.g. `AstraCS:6gBhNmsk135....` (it must be a "Database Administrator" token)
  * Optionally a Keyspace name (if omitted, the default one for the database will be used)

[code]
```python




    ASTRA_DB_ID = input("ASTRA_DB_ID = ")  
    ASTRA_DB_APPLICATION_TOKEN = getpass("ASTRA_DB_APPLICATION_TOKEN = ")  
      
    desired_keyspace = input("ASTRA_DB_KEYSPACE (optional, can be left empty) = ")  
    if desired_keyspace:  
        ASTRA_DB_KEYSPACE = desired_keyspace  
    else:  
        ASTRA_DB_KEYSPACE = None  
    


```
[/code]


[code]
```python




    import cassio  
      
    cassio.init(  
        database_id=ASTRA_DB_ID,  
        token=ASTRA_DB_APPLICATION_TOKEN,  
        keyspace=ASTRA_DB_KEYSPACE,  
    )  
    


```
[/code]


Now you can create the vector store:

[code]
```python




    vstore = Cassandra(  
        embedding=embe,  
        table_name="cassandra_vector_demo",  
        # session=None, keyspace=None  # Uncomment on older versions of LangChain  
    )  
    


```
[/code]


### Usage of the vector store​

 _See the sections "Load a dataset" through "A minimal RAG chain" above._

Speaking of the latter, you can check out a full RAG template for Astra DB through CQL here.

### Cleanup​

the following essentially retrieves the `Session` object from CassIO and runs a CQL `DROP TABLE` statement with it:

[code]
```python




    cassio.config.resolve_session().execute(  
        f"DROP TABLE {cassio.config.resolve_keyspace()}.cassandra_vector_demo;"  
    )  
    


```
[/code]


### Learn more​

For more information, extended quickstarts and additional usage examples, please visit the CassIO documentation for more on using the LangChain `Cassandra` vector store.

