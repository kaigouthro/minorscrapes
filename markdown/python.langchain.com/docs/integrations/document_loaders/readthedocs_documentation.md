

Skip to main content

# ReadTheDocs Documentation

> Read the Docs is an open-sourced free software documentation hosting platform. It generates documentation written with the `Sphinx` documentation generator.

This notebook covers how to load content from HTML that was generated as part of a `Read-The-Docs` build.

For an example of this in the wild, see here.

This assumes that the HTML has already been scraped into a folder. This can be done by uncommenting and running the following command

[code]
```python




    #!pip install beautifulsoup4  
    


```
[/code]


[code]
```python




    #!wget -r -A.html -P rtdocs https://python.langchain.com/en/latest/  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import ReadTheDocsLoader  
    


```
[/code]


[code]
```python




    loader = ReadTheDocsLoader("rtdocs", features="html.parser")  
    


```
[/code]


[code]
```python




    docs = loader.load()  
    


```
[/code]


