

Skip to main content

On this page

# RST

> A reStructured Text (RST) file is a file format for textual data used primarily in the Python programming language community for technical documentation.

## `UnstructuredRSTLoader`​

You can load data from RST files with `UnstructuredRSTLoader` using the following workflow.

[code]
```python




    from langchain.document_loaders import UnstructuredRSTLoader  
    


```
[/code]


[code]
```python




    loader = UnstructuredRSTLoader(file_path="example_data/README.rst", mode="elements")  
    docs = loader.load()  
    


```
[/code]


[code]
```python




    print(docs[0])  
    


```
[/code]


[code]
```python




        page_content='Example Docs' metadata={'source': 'example_data/README.rst', 'filename': 'README.rst', 'file_directory': 'example_data', 'filetype': 'text/x-rst', 'page_number': 1, 'category': 'Title'}  
    


```
[/code]


