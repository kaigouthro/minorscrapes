

Skip to main content

On this page

# SVM

> Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

This notebook goes over how to use a retriever that under the hood uses an `SVM` using `scikit-learn` package.

Largely based on https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.html

[code]
```python




    #!pip install scikit-learn  
    


```
[/code]


[code]
```python




    #!pip install lark  
    


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




    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.retrievers import SVMRetriever  
    


```
[/code]


## Create New Retriever with Texts​

[code]
```python




    retriever = SVMRetriever.from_texts(  
        ["foo", "bar", "world", "hello", "foo bar"], OpenAIEmbeddings()  
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


