

Skip to main content

# Obsidian

> Obsidian is a powerful and extensible knowledge base that works on top of your local folder of plain text files.

This notebook covers how to load documents from an `Obsidian` database.

Since `Obsidian` is just stored on disk as a folder of Markdown files, the loader just takes a path to this directory.

`Obsidian` files also sometimes contain metadata which is a YAML block at the top of the file. These values will be added to the document's metadata. (`ObsidianLoader` can also be passed a
`collect_metadata=False` argument to disable this behavior.)

[code]
```python




    from langchain.document_loaders import ObsidianLoader  
    


```
[/code]


[code]
```python




    loader = ObsidianLoader("<path-to-obsidian>")  
    


```
[/code]


[code]
```python




    docs = loader.load()  
    


```
[/code]


