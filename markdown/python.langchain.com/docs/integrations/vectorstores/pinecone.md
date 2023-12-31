

Skip to main content

On this page

# Pinecone

> Pinecone is a vector database with broad functionality.

This notebook shows how to use functionality related to the `Pinecone` vector database.

To use Pinecone, you must have an API key. Here are the installation instructions.

[code]
```python




    pip install pinecone-client openai tiktoken langchain  
    


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




    os.environ["PINECONE_ENV"] = getpass.getpass("Pinecone Environment:")  
    


```
[/code]


We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

[code]
```python




    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Pinecone  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
      
    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    import pinecone  
      
    # initialize pinecone  
    pinecone.init(  
        api_key=os.getenv("PINECONE_API_KEY"),  # find at app.pinecone.io  
        environment=os.getenv("PINECONE_ENV"),  # next to api key in console  
    )  
      
    index_name = "langchain-demo"  
      
    # First, check if our index already exists. If it doesn't, we create it  
    if index_name not in pinecone.list_indexes():  
        # we create a new index  
        pinecone.create_index(name=index_name, metric="cosine", dimension=1536)  
    # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`  
    docsearch = Pinecone.from_documents(docs, embeddings, index_name=index_name)  
      
    # if you already have an index, you can load it like this  
    # docsearch = Pinecone.from_existing_index(index_name, embeddings)  
      
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = docsearch.similarity_search(query)  
    


```
[/code]


[code]
```python




    print(docs[0].page_content)  
    


```
[/code]


### Adding More Text to an Existing Index​

More text can embedded and upserted to an existing Pinecone index using the `add_texts` function

[code]
```python




    index = pinecone.Index("langchain-demo")  
    vectorstore = Pinecone(index, embeddings.embed_query, "text")  
      
    vectorstore.add_texts("More text!")  
    


```
[/code]


### Maximal Marginal Relevance Searches​

In addition to using similarity search in the retriever object, you can also use `mmr` as retriever.

[code]
```python




    retriever = docsearch.as_retriever(search_type="mmr")  
    matched_docs = retriever.get_relevant_documents(query)  
    for i, d in enumerate(matched_docs):  
        print(f"\n## Document {i}\n")  
        print(d.page_content)  
    


```
[/code]


Or use `max_marginal_relevance_search` directly:

[code]
```python




    found_docs = docsearch.max_marginal_relevance_search(query, k=2, fetch_k=10)  
    for i, doc in enumerate(found_docs):  
        print(f"{i + 1}.", doc.page_content, "\n")  
    


```
[/code]


