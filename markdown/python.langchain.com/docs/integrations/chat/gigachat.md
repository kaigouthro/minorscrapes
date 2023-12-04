

Skip to main content

On this page

# GigaChat

This notebook shows how to use LangChain with GigaChat. To use you need to install `gigachat` python package.

[code]
```python




    # !pip install gigachat  
    


```
[/code]


To get GigaChat credentials you need to create account and get access to API

## Example​

[code]
```python




    import os  
    from getpass import getpass  
      
    os.environ["GIGACHAT_CREDENTIALS"] = getpass()  
    


```
[/code]


[code]
```python




    from langchain.chat_models import GigaChat  
      
    chat = GigaChat(verify_ssl_certs=False)  
    


```
[/code]


[code]
```python




    from langchain.schema import HumanMessage, SystemMessage  
      
    messages = [  
        SystemMessage(  
            content="You are a helpful AI that shares everything you know. Talk in English."  
        ),  
        HumanMessage(content="Tell me a joke"),  
    ]  
      
    print(chat(messages).content)  
    


```
[/code]


[code]
```python




        What do you get when you cross a goat and a skunk? A smelly goat!  
    


```
[/code]


