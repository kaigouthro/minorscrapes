

Skip to main content

On this page

# DingoDB

> DingoDB is a distributed multi-mode vector database, which combines the characteristics of data lakes and vector databases, and can store data of any type and size (Key-Value, PDF, audio, video,
> etc.). It has real-time low-latency processing capabilities to achieve rapid insight and response, and can efficiently conduct instant analysis and process multi-modal data.

This notebook shows how to use functionality related to the DingoDB vector database.

To run, you should have a DingoDB instance up and running.

[code]
```python




    pip install dingodb  
    # or install latest:  
    pip install git+https://git@github.com/dingodb/pydingo.git  
    


```
[/code]


We want to use OpenAIEmbeddings so we have to get the OpenAI API Key.

[code]
```python




    import getpass  
    import os  
      
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




        OpenAI API Key:········  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Dingo  
    


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




    from dingodb import DingoDB  
      
    index_name = "langchain_demo"  
      
    dingo_client = DingoDB(user="", password="", host=["127.0.0.1:13000"])  
    # First, check if our index already exists. If it doesn't, we create it  
    if (  
        index_name not in dingo_client.get_index()  
        and index_name.upper() not in dingo_client.get_index()  
    ):  
        # we create a new index, modify to your own  
        dingo_client.create_index(  
            index_name=index_name, dimension=1536, metric_type="cosine", auto_id=False  
        )  
      
    # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`  
    docsearch = Dingo.from_documents(  
        docs, embeddings, client=dingo_client, index_name=index_name  
    )  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Dingo  
    


```
[/code]


[code]
```python




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

More text can embedded and upserted to an existing Dingo index using the `add_texts` function

[code]
```python




    vectorstore = Dingo(embeddings, "text", client=dingo_client, index_name=index_name)  
      
    vectorstore.add_texts(["More text!"])  
    


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


