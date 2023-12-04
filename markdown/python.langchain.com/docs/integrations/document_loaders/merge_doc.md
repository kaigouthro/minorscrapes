

Skip to main content

# Merge Documents Loader

Merge the documents returned from a set of specified data loaders.

[code]
```python




    from langchain.document_loaders import WebBaseLoader  
      
    loader_web = WebBaseLoader(  
        "https://github.com/basecamp/handbook/blob/master/37signals-is-you.md"  
    )  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import PyPDFLoader  
      
    loader_pdf = PyPDFLoader("../MachineLearning-Lecture01.pdf")  
    


```
[/code]


[code]
```python




    from langchain.document_loaders.merge import MergedDataLoader  
      
    loader_all = MergedDataLoader(loaders=[loader_web, loader_pdf])  
    


```
[/code]


[code]
```python




    docs_all = loader_all.load()  
    


```
[/code]


[code]
```python




    len(docs_all)  
    


```
[/code]


[code]
```python




        23  
    


```
[/code]


