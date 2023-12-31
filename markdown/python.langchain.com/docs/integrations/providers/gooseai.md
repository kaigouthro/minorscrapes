

Skip to main content

On this page

# GooseAI

This page covers how to use the GooseAI ecosystem within LangChain. It is broken into two parts: installation and setup, and then references to specific GooseAI wrappers.

## Installation and Setup​

  * Install the Python SDK with `pip install openai`
  * Get your GooseAI api key from this link here.
  * Set the environment variable (`GOOSEAI_API_KEY`).

[code]
```python




    import os  
    os.environ["GOOSEAI_API_KEY"] = "YOUR_API_KEY"  
    


```
[/code]


## Wrappers​

### LLM​

There exists an GooseAI LLM wrapper, which you can access with:

[code]
```python




    from langchain.llms import GooseAI  
    


```
[/code]


