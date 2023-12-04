

Skip to main content

On this page

# OpenAI

All functionality related to OpenAI

> OpenAI is American artificial intelligence (AI) research laboratory consisting of the non-profit `OpenAI Incorporated` and its for-profit subsidiary corporation `OpenAI Limited Partnership`.
> `OpenAI` conducts AI research with the declared intention of promoting and developing a friendly AI. `OpenAI` systems run on an `Azure`-based supercomputing platform from `Microsoft`.

> The OpenAI API is powered by a diverse set of models with different capabilities and price points.
>
> ChatGPT is the Artificial Intelligence (AI) chatbot developed by `OpenAI`.

## Installation and Setup​

  * Install the Python SDK with

[code]
```python




    pip install openai  
    


```
[/code]


  * Get an OpenAI api key and set it as an environment variable (`OPENAI_API_KEY`)
  * If you want to use OpenAI's tokenizer (only available for Python 3.9+), install it

[code]
```python




    pip install tiktoken  
    


```
[/code]


## LLM​

See a usage example.

[code]
```python




    from langchain.llms import OpenAI  
    


```
[/code]


If you are using a model hosted on `Azure`, you should use different wrapper for that:

[code]
```python




    from langchain.llms import AzureOpenAI  
    


```
[/code]


For a more detailed walkthrough of the `Azure` wrapper, see here

## Chat model​

See a usage example.

[code]
```python




    from langchain.chat_models import ChatOpenAI  
    


```
[/code]


If you are using a model hosted on `Azure`, you should use different wrapper for that:

[code]
```python




    from langchain.llms import AzureChatOpenAI  
    


```
[/code]


For a more detailed walkthrough of the `Azure` wrapper, see here

## Text Embedding Model​

See a usage example

[code]
```python




    from langchain.embeddings import OpenAIEmbeddings  
    


```
[/code]


## Tokenizer​

There are several places you can use the `tiktoken` tokenizer. By default, it is used to count tokens for OpenAI LLMs.

You can also use it to count tokens when splitting documents with

[code]
```python




    from langchain.text_splitter import CharacterTextSplitter  
    CharacterTextSplitter.from_tiktoken_encoder(...)  
    


```
[/code]


For a more detailed walkthrough of this, see this notebook

## Document Loader​

See a usage example.

[code]
```python




    from langchain.document_loaders.chatgpt import ChatGPTLoader  
    


```
[/code]


## Retriever​

See a usage example.

[code]
```python




    from langchain.retrievers import ChatGPTPluginRetriever  
    


```
[/code]


## Chain​

See a usage example.

[code]
```python




    from langchain.chains import OpenAIModerationChain  
    


```
[/code]


## Adapter​

See a usage example.

[code]
```python




    from langchain.adapters import openai as lc_openai  
    


```
[/code]


