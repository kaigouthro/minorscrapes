

Skip to main content

On this page

# Installation

## Official release​

To install LangChain run:

  * Pip
  * Conda

[code]
```python




    pip install langchain  
    


```
[/code]


[code]
```python




    conda install langchain -c conda-forge  
    


```
[/code]


This will install the bare minimum requirements of LangChain. A lot of the value of LangChain comes when integrating it with various model providers, datastores, etc. By default, the dependencies
needed to do that are NOT installed. You will need to install the dependencies for specific integrations separately.

## From source​

If you want to install from source, you can do so by cloning the repo and be sure that the directory is `PATH/TO/REPO/langchain/libs/langchain` running:

[code]
```python




    pip install -e .  
    


```
[/code]


## LangChain experimental​

The `langchain-experimental` package holds experimental LangChain code, intended for research and experimental uses. Install with:

[code]
```python




    pip install langchain-experimental  
    


```
[/code]


## LangServe​

LangServe helps developers deploy LangChain runnables and chains as a REST API. LangServe is automatically installed by LangChain CLI. If not using LangChain CLI, install with:

[code]
```python




    pip install "langserve[all]"  
    


```
[/code]


for both client and server dependencies. Or `pip install "langserve[client]"` for client code, and `pip install "langserve[server]"` for server code.

## LangChain CLI​

The LangChain CLI is useful for working with LangChain templates and other LangServe projects. Install with:

[code]
```python




    pip install langchain-cli  
    


```
[/code]


## LangSmith SDK​

The LangSmith SDK is automatically installed by LangChain. If not using LangChain, install with:

[code]
```python




    pip install langsmith  
    


```
[/code]


