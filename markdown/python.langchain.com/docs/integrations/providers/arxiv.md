

Skip to main content

On this page

# Arxiv

> arXiv is an open-access archive for 2 million scholarly articles in the fields of physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical
> engineering and systems science, and economics.

## Installation and Setup​

First, you need to install `arxiv` python package.

[code]
```python




    pip install arxiv  
    


```
[/code]


Second, you need to install `PyMuPDF` python package which transforms PDF files downloaded from the `arxiv.org` site into the text format.

[code]
```python




    pip install pymupdf  
    


```
[/code]


## Document Loader​

See a usage example.

[code]
```python




    from langchain.document_loaders import ArxivLoader  
    


```
[/code]


## Retriever​

See a usage example.

[code]
```python




    from langchain.retrievers import ArxivRetriever  
    


```
[/code]


