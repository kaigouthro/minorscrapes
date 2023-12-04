

Skip to main content

On this page

# Anthropic Functions

This notebook shows how to use an experimental wrapper around Anthropic that gives it the same API as OpenAI Functions.

[code]
```python




    from langchain_experimental.llms.anthropic_functions import AnthropicFunctions  
    


```
[/code]


[code]
```python




        /Users/harrisonchase/.pyenv/versions/3.9.1/envs/langchain/lib/python3.9/site-packages/deeplake/util/check_latest_version.py:32: UserWarning: A newer version of deeplake (3.6.14) is available. It's recommended that you update to the latest version using `pip install -U deeplake`.  
          warnings.warn(  
    


```
[/code]


## Initialize Model​

You can initialize this wrapper the same way you'd initialize ChatAnthropic

[code]
```python




    model = AnthropicFunctions(model="claude-2")  
    


```
[/code]


## Passing in functions​

You can now pass in functions in a similar way

[code]
```python




    functions = [  
        {  
            "name": "get_current_weather",  
            "description": "Get the current weather in a given location",  
            "parameters": {  
                "type": "object",  
                "properties": {  
                    "location": {  
                        "type": "string",  
                        "description": "The city and state, e.g. San Francisco, CA",  
                    },  
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},  
                },  
                "required": ["location"],  
            },  
        }  
    ]  
    


```
[/code]


[code]
```python




    from langchain.schema import HumanMessage  
    


```
[/code]


[code]
```python




    response = model.predict_messages(  
        [HumanMessage(content="whats the weater in boston?")], functions=functions  
    )  
    


```
[/code]


[code]
```python




    response  
    


```
[/code]


[code]
```python




        AIMessage(content=' ', additional_kwargs={'function_call': {'name': 'get_current_weather', 'arguments': '{"location": "Boston, MA", "unit": "fahrenheit"}'}}, example=False)  
    


```
[/code]


## Using for extraction​

You can now use this for extraction.

[code]
```python




    from langchain.chains import create_extraction_chain  
      
    schema = {  
        "properties": {  
            "name": {"type": "string"},  
            "height": {"type": "integer"},  
            "hair_color": {"type": "string"},  
        },  
        "required": ["name", "height"],  
    }  
    inp = """  
    Alex is 5 feet tall. Claudia is 1 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.  
            """  
    


```
[/code]


[code]
```python




    chain = create_extraction_chain(schema, model)  
    


```
[/code]


[code]
```python




    chain.run(inp)  
    


```
[/code]


[code]
```python




        [{'name': 'Alex', 'height': '5', 'hair_color': 'blonde'},  
         {'name': 'Claudia', 'height': '6', 'hair_color': 'brunette'}]  
    


```
[/code]


## Using for tagging​

You can now use this for tagging

[code]
```python




    from langchain.chains import create_tagging_chain  
    


```
[/code]


[code]
```python




    schema = {  
        "properties": {  
            "sentiment": {"type": "string"},  
            "aggressiveness": {"type": "integer"},  
            "language": {"type": "string"},  
        }  
    }  
    


```
[/code]


[code]
```python




    chain = create_tagging_chain(schema, model)  
    


```
[/code]


[code]
```python




    chain.run("this is really cool")  
    


```
[/code]


[code]
```python




        {'sentiment': 'positive', 'aggressiveness': '0', 'language': 'english'}  
    


```
[/code]


