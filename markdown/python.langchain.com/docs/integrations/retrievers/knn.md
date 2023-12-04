

Skip to main content

On this page

# kNN

> In statistics, the k-nearest neighbors algorithm (k-NN) is a non-parametric supervised learning method first developed by Evelyn Fix and Joseph Hodges in 1951, and later expanded by Thomas Cover. It
> is used for classification and regression.

This notebook goes over how to use a retriever that under the hood uses an kNN.

Largely based on https://github.com/karpathy/randomfun/blob/master/knn_vs_svm.html

[code]
```python




    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.retrievers import KNNRetriever  
    


```
[/code]


## Create New Retriever with Texts​

[code]
```python




    retriever = KNNRetriever.from_texts(  
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
         Document(page_content='bar', metadata={})]  
    


```
[/code]


