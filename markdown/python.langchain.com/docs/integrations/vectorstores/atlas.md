

Skip to main content

On this page

# Atlas

> Atlas is a platform by Nomic made for interacting with both small and internet scale unstructured datasets. It enables anyone to visualize, search, and share massive datasets in their browser.

This notebook shows you how to use functionality related to the `AtlasDB` vectorstore.

[code]
```python




    pip install spacy  
    


```
[/code]


[code]
```python




    python3 -m spacy download en_core_web_sm  
    


```
[/code]


[code]
```python




    pip install nomic  
    


```
[/code]


### Load Packages​

[code]
```python




    import time  
      
    from langchain.document_loaders import TextLoader  
    from langchain.text_splitter import SpacyTextSplitter  
    from langchain.vectorstores import AtlasDB  
    


```
[/code]


[code]
```python




    ATLAS_TEST_API_KEY = "7xDPkYXSYDc1_ErdTPIcoAR9RNd8YDlkS3nVNXcVoIMZ6"  
    


```
[/code]


### Prepare the Data​

[code]
```python




    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = SpacyTextSplitter(separator="|")  
    texts = []  
    for doc in text_splitter.split_documents(documents):  
        texts.extend(doc.page_content.split("|"))  
      
    texts = [e.strip() for e in texts]  
    


```
[/code]


### Map the Data using Nomic's Atlas​

[code]
```python




    db = AtlasDB.from_texts(  
        texts=texts,  
        name="test_index_" + str(time.time()),  # unique name for your vector store  
        description="test_index",  # a description for your vector store  
        api_key=ATLAS_TEST_API_KEY,  
        index_kwargs={"build_topic_model": True},  
    )  
    


```
[/code]


[code]
```python




    db.project.wait_for_project_lock()  
    


```
[/code]


[code]
```python




    db.project  
    


```
[/code]


Here is a map with the result of this code. This map displays the texts of the State of the Union. https://atlas.nomic.ai/map/3e4de075-89ff-486a-845c-36c23f30bb67/d8ce2284-8edb-4050-8b9b-9bb543d7f647

