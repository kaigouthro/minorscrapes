

Skip to main content

On this page

# Org-mode

> A Org Mode document is a document editing, formatting, and organizing mode, designed for notes, planning, and authoring within the free software text editor Emacs.

## `UnstructuredOrgModeLoader`​

You can load data from Org-mode files with `UnstructuredOrgModeLoader` using the following workflow.

[code]
```python




    from langchain.document_loaders import UnstructuredOrgModeLoader  
    


```
[/code]


[code]
```python




    loader = UnstructuredOrgModeLoader(file_path="example_data/README.org", mode="elements")  
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




        page_content='Example Docs' metadata={'source': 'example_data/README.org', 'filename': 'README.org', 'file_directory': 'example_data', 'filetype': 'text/org', 'page_number': 1, 'category': 'Title'}  
    


```
[/code]


