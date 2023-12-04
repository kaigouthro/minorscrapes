

Skip to main content

On this page

# Neo4j Vector Index

> Neo4j is an open-source graph database with integrated support for vector similarity search

It supports:

  * approximate nearest neighbor search
  * Euclidean similarity and cosine similarity
  * Hybrid search combining vector and keyword searches

This notebook shows how to use the Neo4j vector index (`Neo4jVector`).

See the installation instruction.

[code]
```python




    # Pip install necessary package  
    pip install neo4j  
    pip install openai  
    pip install tiktoken  
    


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




    from langchain.docstore.document import Document  
    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Neo4jVector  
    


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


[code]
```python




    # Neo4jVector requires the Neo4j database credentials  
      
    url = "bolt://localhost:7687"  
    username = "neo4j"  
    password = "pleaseletmein"  
      
    # You can also use environment variables instead of directly passing named parameters  
    # os.environ["NEO4J_URI"] = "bolt://localhost:7687"  
    # os.environ["NEO4J_USERNAME"] = "neo4j"  
    # os.environ["NEO4J_PASSWORD"] = "pleaseletmein"  
    


```
[/code]


## Similarity Search with Cosine Distance (Default)​

[code]
```python




    # The Neo4jVector Module will connect to Neo4j and create a vector index if needed.  
      
    db = Neo4jVector.from_documents(  
        docs, OpenAIEmbeddings(), url=url, username=username, password=password  
    )  
    


```
[/code]


[code]
```python




        /home/tomaz/neo4j/langchain/libs/langchain/langchain/vectorstores/neo4j_vector.py:165: ExperimentalWarning: The configuration may change in the future.  
          self._driver.verify_connectivity()  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs_with_score = db.similarity_search_with_score(query, k=2)  
    


```
[/code]


[code]
```python




    for doc, score in docs_with_score:  
        print("-" * 80)  
        print("Score: ", score)  
        print(doc.page_content)  
        print("-" * 80)  
    


```
[/code]


[code]
```python




        --------------------------------------------------------------------------------  
        Score:  0.9099836349487305  
        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   
          
        Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   
          
        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
        --------------------------------------------------------------------------------  
        --------------------------------------------------------------------------------  
        Score:  0.9099686145782471  
        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   
          
        Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   
          
        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
        --------------------------------------------------------------------------------  
    


```
[/code]


## Working with vectorstore​

Above, we created a vectorstore from scratch. However, often times we want to work with an existing vectorstore. In order to do that, we can initialize it directly.

[code]
```python




    index_name = "vector"  # default index name  
      
    store = Neo4jVector.from_existing_index(  
        OpenAIEmbeddings(),  
        url=url,  
        username=username,  
        password=password,  
        index_name=index_name,  
    )  
    


```
[/code]


[code]
```python




        /home/tomaz/neo4j/langchain/libs/langchain/langchain/vectorstores/neo4j_vector.py:165: ExperimentalWarning: The configuration may change in the future.  
          self._driver.verify_connectivity()  
    


```
[/code]


We can also initialize a vectorstore from existing graph using the `from_existing_graph` method. This method pulls relevant text information from the database, and calculates and stores the text
embeddings back to the database.

[code]
```python




    # First we create sample data in graph  
    store.query("CREATE (p:Person {name: 'Tomaz', location:'Slovenia', hobby:'Bicycle'})")  
    


```
[/code]


[code]
```python




        []  
    


```
[/code]


[code]
```python




    # Now we initialize from existing graph  
    existing_graph = Neo4jVector.from_existing_graph(  
        embedding=OpenAIEmbeddings(),  
        url=url,  
        username=username,  
        password=password,  
        index_name="person_index",  
        node_label="Person",  
        text_node_properties=["name", "location"],  
        embedding_node_property="embedding",  
    )  
    result = existing_graph.similarity_search("Slovenia", k=1)  
    


```
[/code]


[code]
```python




        /home/tomaz/neo4j/langchain/libs/langchain/langchain/vectorstores/neo4j_vector.py:165: ExperimentalWarning: The configuration may change in the future.  
          self._driver.verify_connectivity()  
    


```
[/code]


[code]
```python




    result[0]  
    


```
[/code]


[code]
```python




        Document(page_content='\nname: Tomaz\nlocation: Slovenia', metadata={'hobby': 'Bicycle'})  
    


```
[/code]


### Add documents​

We can add documents to the existing vectorstore.

[code]
```python




    store.add_documents([Document(page_content="foo")])  
    


```
[/code]


[code]
```python




        ['187fc53a-5dde-11ee-ad78-1f6b05bf8513']  
    


```
[/code]


[code]
```python




    docs_with_score = store.similarity_search_with_score("foo")  
    


```
[/code]


[code]
```python




    docs_with_score[0]  
    


```
[/code]


[code]
```python




        (Document(page_content='foo', metadata={}), 1.0)  
    


```
[/code]


## Hybrid search (vector + keyword)​

Neo4j integrates both vector and keyword indexes, which allows you to use a hybrid search approach

[code]
```python




    # The Neo4jVector Module will connect to Neo4j and create a vector and keyword indices if needed.  
    hybrid_db = Neo4jVector.from_documents(  
        docs,  
        OpenAIEmbeddings(),  
        url=url,  
        username=username,  
        password=password,  
        search_type="hybrid",  
    )  
    


```
[/code]


[code]
```python




        /home/tomaz/neo4j/langchain/libs/langchain/langchain/vectorstores/neo4j_vector.py:165: ExperimentalWarning: The configuration may change in the future.  
          self._driver.verify_connectivity()  
    


```
[/code]


To load the hybrid search from existing indexes, you have to provide both the vector and keyword indices

[code]
```python




    index_name = "vector"  # default index name  
    keyword_index_name = "keyword"  # default keyword index name  
      
    store = Neo4jVector.from_existing_index(  
        OpenAIEmbeddings(),  
        url=url,  
        username=username,  
        password=password,  
        index_name=index_name,  
        keyword_index_name=keyword_index_name,  
        search_type="hybrid",  
    )  
    


```
[/code]


[code]
```python




        /home/tomaz/neo4j/langchain/libs/langchain/langchain/vectorstores/neo4j_vector.py:165: ExperimentalWarning: The configuration may change in the future.  
          self._driver.verify_connectivity()  
    


```
[/code]


## Retriever options​

This section shows how to use `Neo4jVector` as a retriever.

[code]
```python




    retriever = store.as_retriever()  
    retriever.get_relevant_documents(query)[0]  
    


```
[/code]


[code]
```python




        Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. \n\nTonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \n\nAnd I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': '../../modules/state_of_the_union.txt'})  
    


```
[/code]


## Question Answering with Sources​

This section goes over how to do question-answering with sources over an Index. It does this by using the `RetrievalQAWithSourcesChain`, which does the lookup of the documents from an Index.

[code]
```python




    from langchain.chains import RetrievalQAWithSourcesChain  
    from langchain.chat_models import ChatOpenAI  
    


```
[/code]


[code]
```python




    chain = RetrievalQAWithSourcesChain.from_chain_type(  
        ChatOpenAI(temperature=0), chain_type="stuff", retriever=retriever  
    )  
    


```
[/code]


[code]
```python




    chain(  
        {"question": "What did the president say about Justice Breyer"},  
        return_only_outputs=True,  
    )  
    


```
[/code]


[code]
```python




        {'answer': "The president honored Justice Stephen Breyer, who is retiring from the United States Supreme Court. He thanked him for his service and mentioned that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson to continue Justice Breyer's legacy of excellence. \n",  
         'sources': '../../modules/state_of_the_union.txt'}  
    


```
[/code]


