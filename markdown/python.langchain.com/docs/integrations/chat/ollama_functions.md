

Skip to main content

On this page

# Ollama Functions

This notebook shows how to use an experimental wrapper around Ollama that gives it the same API as OpenAI Functions.

Note that more powerful and capable models will perform better with complex schema and/or multiple functions. The examples below use Mistral. For a complete list of supported models and model
variants, see the Ollama model library.

## Setup​

Follow these instructions to set up and run a local Ollama instance.

## Usage​

You can initialize OllamaFunctions in a similar way to how you'd initialize a standard ChatOllama instance:

[code]
```python




    from langchain_experimental.llms.ollama_functions import OllamaFunctions  
      
    model = OllamaFunctions(model="mistral")  
    


```
[/code]


You can then bind functions defined with JSON Schema parameters and a `function_call` parameter to force the model to call the given function:

[code]
```python




    model = model.bind(  
        functions=[  
            {  
                "name": "get_current_weather",  
                "description": "Get the current weather in a given location",  
                "parameters": {  
                    "type": "object",  
                    "properties": {  
                        "location": {  
                            "type": "string",  
                            "description": "The city and state, " "e.g. San Francisco, CA",  
                        },  
                        "unit": {  
                            "type": "string",  
                            "enum": ["celsius", "fahrenheit"],  
                        },  
                    },  
                    "required": ["location"],  
                },  
            }  
        ],  
        function_call={"name": "get_current_weather"},  
    )  
    


```
[/code]


Calling a function with this model then results in JSON output matching the provided schema:

[code]
```python




    from langchain.schema import HumanMessage  
      
    model.invoke("what is the weather in Boston?")  
    


```
[/code]


[code]
```python




        AIMessage(content='', additional_kwargs={'function_call': {'name': 'get_current_weather', 'arguments': '{"location": "Boston, MA", "unit": "celsius"}'}})  
    


```
[/code]


## Using for extraction​

One useful thing you can do with function calling here is extracting properties from a given input in a structured format:

[code]
```python




    from langchain.chains import create_extraction_chain  
      
    # Schema  
    schema = {  
        "properties": {  
            "name": {"type": "string"},  
            "height": {"type": "integer"},  
            "hair_color": {"type": "string"},  
        },  
        "required": ["name", "height"],  
    }  
      
    # Input  
    input = """Alex is 5 feet tall. Claudia is 1 feet taller than Alex and jumps higher than him. Claudia is a brunette and Alex is blonde."""  
      
    # Run chain  
    llm = OllamaFunctions(model="mistral", temperature=0)  
    chain = create_extraction_chain(schema, llm)  
    chain.run(input)  
    


```
[/code]


[code]
```python




        [{'name': 'Alex', 'height': 5, 'hair_color': 'blonde'},  
         {'name': 'Claudia', 'height': 6, 'hair_color': 'brunette'}]  
    


```
[/code]


