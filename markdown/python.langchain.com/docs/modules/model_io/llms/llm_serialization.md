

Skip to main content

On this page

# Serialization

LangChain Python and LangChain JS share a serialization scheme. You can check if a LangChain class is serializable by running with the `is_lc_serializable` class method.

[code]
```python




    from langchain.llms import OpenAI  
    from langchain.llms.loading import load_llm  
    


```
[/code]


[code]
```python




    OpenAI.is_lc_serializable()  
    


```
[/code]


[code]
```python




        True  
    


```
[/code]


[code]
```python




    llm = OpenAI(model="gpt-3.5-turbo-instruct")  
    


```
[/code]


## Dump​

Any serializable object can be serialized to a dict or json string.

[code]
```python




    from langchain.load import dumpd, dumps  
      
    dumpd(llm)  
    


```
[/code]


[code]
```python




        {'lc': 1,  
         'type': 'constructor',  
         'id': ['langchain', 'llms', 'openai', 'OpenAI'],  
         'kwargs': {'model': 'gpt-3.5-turbo-instruct',  
          'openai_api_key': {'lc': 1, 'type': 'secret', 'id': ['OPENAI_API_KEY']}}}  
    


```
[/code]


[code]
```python




    dumps(llm)  
    


```
[/code]


[code]
```python




        '{"lc": 1, "type": "constructor", "id": ["langchain", "llms", "openai", "OpenAI"], "kwargs": {"model": "gpt-3.5-turbo-instruct", "openai_api_key": {"lc": 1, "type": "secret", "id": ["OPENAI_API_KEY"]}}}'  
    


```
[/code]


## Load​

Any serialized object can be loaded.

[code]
```python




    from langchain.load import loads  
    from langchain.load.load import load  
      
    loaded_1 = load(dumpd(llm))  
    loaded_2 = loads(dumps(llm))  
    


```
[/code]


[code]
```python




    print(loaded_1.invoke("How are you doing?"))  
    


```
[/code]


[code]
```python




          
          
        I am an AI and do not have the capability to experience emotions. But thank you for asking. Is there anything I can assist you with?  
    


```
[/code]


