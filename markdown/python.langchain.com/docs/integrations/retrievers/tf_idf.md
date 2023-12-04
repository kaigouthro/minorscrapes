

Skip to main content

On this page

# TF-IDF

> TF-IDF means term-frequency times inverse document-frequency.

This notebook goes over how to use a retriever that under the hood uses TF-IDF using `scikit-learn` package.

For more information on the details of TF-IDF see this blog post.

[code]
```python




    # !pip install scikit-learn  
    


```
[/code]


[code]
```python




    from langchain.retrievers import TFIDFRetriever  
    


```
[/code]


## Create New Retriever with Texts​

[code]
```python




    retriever = TFIDFRetriever.from_texts(["foo", "bar", "world", "hello", "foo bar"])  
    


```
[/code]


## Create a New Retriever with Documents​

You can now create a new retriever with the documents you created.

[code]
```python




    from langchain.schema import Document  
      
    retriever = TFIDFRetriever.from_documents(  
        [  
            Document(page_content="foo"),  
            Document(page_content="bar"),  
            Document(page_content="world"),  
            Document(page_content="hello"),  
            Document(page_content="foo bar"),  
        ]  
    )  
    


```
[/code]


## Use Retriever​

We can now use the retriever!

[code]
```python




    result = retriever.get_relevant_documents("foo")  
    


```
[/code]


[code]
```python




    result  
    


```
[/code]


[code]
```python




        [Document(page_content='foo', metadata={}),  
         Document(page_content='foo bar', metadata={}),  
         Document(page_content='hello', metadata={}),  
         Document(page_content='world', metadata={})]  
    


```
[/code]


## Save and load​

You can easily save and load this retriever, making it handy for local development!

[code]
```python




    retriever.save_local("testing.pkl")  
    


```
[/code]


[code]
```python




    retriever_copy = TFIDFRetriever.load_local("testing.pkl")  
    


```
[/code]


[code]
```python




    retriever_copy.get_relevant_documents("foo")  
    


```
[/code]


[code]
```python




        [Document(page_content='foo', metadata={}),  
         Document(page_content='foo bar', metadata={}),  
         Document(page_content='hello', metadata={}),  
         Document(page_content='world', metadata={})]  
    


```
[/code]


