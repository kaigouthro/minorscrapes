

Skip to main content

On this page

# ScaNN

ScaNN (Scalable Nearest Neighbors) is a method for efficient vector similarity search at scale.

ScaNN includes search space pruning and quantization for Maximum Inner Product Search and also supports other distance functions such as Euclidean distance. The implementation is optimized for x86
processors with AVX2 support. See its Google Research github for more details.

## Installation​

Install ScaNN through pip. Alternatively, you can follow instructions on the ScaNN Website to install from source.

[code]
```python




    pip install scann  
    


```
[/code]


## Retrieval Demo​

Below we show how to use ScaNN in conjunction with Huggingface Embeddings.

[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings import HuggingFaceEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import ScaNN  
      
    loader = TextLoader("state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
      
    embeddings = HuggingFaceEmbeddings()  
      
    db = ScaNN.from_documents(docs, embeddings)  
    query = "What did the president say about Ketanji Brown Jackson"  
    docs = db.similarity_search(query)  
      
    docs[0]  
    


```
[/code]


[code]
```python




        Document(page_content='Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections. \n\nTonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \n\nAnd I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.', metadata={'source': 'state_of_the_union.txt'})  
    


```
[/code]


## RetrievalQA Demo​

Next, we demonstrate using ScaNN in conjunction with Google PaLM API.

You can obtain an API key from https://developers.generativeai.google/tutorials/setup

[code]
```python




    from langchain.chains import RetrievalQA  
    from langchain.chat_models import google_palm  
      
    palm_client = google_palm.ChatGooglePalm(google_api_key="YOUR_GOOGLE_PALM_API_KEY")  
      
    qa = RetrievalQA.from_chain_type(  
        llm=palm_client,  
        chain_type="stuff",  
        retriever=db.as_retriever(search_kwargs={"k": 10}),  
    )  
    


```
[/code]


[code]
```python




    print(qa.run("What did the president say about Ketanji Brown Jackson?"))  
    


```
[/code]


[code]
```python




        The president said that Ketanji Brown Jackson is one of our nation's top legal minds, who will continue Justice Breyer's legacy of excellence.  
    


```
[/code]


[code]
```python




    print(qa.run("What did the president say about Michael Phelps?"))  
    


```
[/code]


[code]
```python




        The president did not mention Michael Phelps in his speech.  
    


```
[/code]


## Save and loading local retrieval index​

[code]
```python




    db.save_local("/tmp/db", "state_of_union")  
    restored_db = ScaNN.load_local("/tmp/db", embeddings, index_name="state_of_union")  
    


```
[/code]


