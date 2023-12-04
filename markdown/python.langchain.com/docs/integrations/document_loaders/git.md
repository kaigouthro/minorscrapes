

Skip to main content

On this page

# Git

> Git is a distributed version control system that tracks changes in any set of computer files, usually used for coordinating work among programmers collaboratively developing source code during
> software development.

This notebook shows how to load text files from `Git` repository.

## Load existing repository from disk​

[code]
```python




    pip install GitPython  
    


```
[/code]


[code]
```python




    from git import Repo  
      
    repo = Repo.clone_from(  
        "https://github.com/langchain-ai/langchain", to_path="./example_data/test_repo1"  
    )  
    branch = repo.head.reference  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import GitLoader  
    


```
[/code]


[code]
```python




    loader = GitLoader(repo_path="./example_data/test_repo1/", branch=branch)  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


[code]
```python




    len(data)  
    


```
[/code]


[code]
```python




    print(data[0])  
    


```
[/code]


[code]
```python




        page_content='.venv\n.github\n.git\n.mypy_cache\n.pytest_cache\nDockerfile' metadata={'file_path': '.dockerignore', 'file_name': '.dockerignore', 'file_type': ''}  
    


```
[/code]


## Clone repository from url​

[code]
```python




    from langchain.document_loaders import GitLoader  
    


```
[/code]


[code]
```python




    loader = GitLoader(  
        clone_url="https://github.com/langchain-ai/langchain",  
        repo_path="./example_data/test_repo2/",  
        branch="master",  
    )  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


[code]
```python




    len(data)  
    


```
[/code]


[code]
```python




        1074  
    


```
[/code]


## Filtering files to load​

[code]
```python




    from langchain.document_loaders import GitLoader  
      
    # e.g. loading only python files  
    loader = GitLoader(  
        repo_path="./example_data/test_repo1/",  
        file_filter=lambda file_path: file_path.endswith(".py"),  
    )  
    


```
[/code]


