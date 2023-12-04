

Skip to main content

On this page

# Microsoft Word

> Microsoft Word is a word processor developed by Microsoft.

This covers how to load `Word` documents into a document format that we can use downstream.

## Using Docx2txt​

Load .docx using `Docx2txt` into a document.

[code]
```python




    pip install docx2txt  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import Docx2txtLoader  
    


```
[/code]


[code]
```python




    loader = Docx2txtLoader("example_data/fake.docx")  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


[code]
```python




    data  
    


```
[/code]


[code]
```python




        [Document(page_content='Lorem ipsum dolor sit amet.', metadata={'source': 'example_data/fake.docx'})]  
    


```
[/code]


## Using Unstructured​

[code]
```python




    from langchain.document_loaders import UnstructuredWordDocumentLoader  
    


```
[/code]


[code]
```python




    loader = UnstructuredWordDocumentLoader("example_data/fake.docx")  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


[code]
```python




    data  
    


```
[/code]


[code]
```python




        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': 'fake.docx'}, lookup_index=0)]  
    


```
[/code]


## Retain Elements​

Under the hood, Unstructured creates different "elements" for different chunks of text. By default we combine those together, but you can easily keep that separation by specifying `mode="elements"`.

[code]
```python




    loader = UnstructuredWordDocumentLoader("example_data/fake.docx", mode="elements")  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


[code]
```python




    data[0]  
    


```
[/code]


[code]
```python




        Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': 'fake.docx', 'filename': 'fake.docx', 'category': 'Title'}, lookup_index=0)  
    


```
[/code]


