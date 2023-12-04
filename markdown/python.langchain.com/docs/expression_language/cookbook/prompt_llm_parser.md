Skip to main content

On this page

# Prompt + LLM

The most common and valuable composition is taking:

`PromptTemplate` / `ChatPromptTemplate` -> `LLM` / `ChatModel` -> `OutputParser`

Almost any other chains you build will use this building block.

## PromptTemplate + LLM​

The simplest composition is just combining a prompt and model to create a chain that takes user input, adds it to a prompt, passes it to a model, and returns the raw model output.

Note, you can mix and match PromptTemplate/ChatPromptTemplates and LLMs/ChatModels as you like here.

\[code\]

```python


    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts import ChatPromptTemplate  
      
    prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")  
    model = ChatOpenAI()  
    chain = prompt | model  
    
```

\[/code\]

\[code\]

```python


    chain.invoke({"foo": "bears"})  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content="Why don't bears wear shoes?\n\nBecause they have bear feet!", additional_kwargs={}, example=False)  
    
```

\[/code\]

Often times we want to attach kwargs that'll be passed to each model call. Here are a few examples of that:

### Attaching Stop Sequences​

\[code\]

```python


    chain = prompt | model.bind(stop=["\n"])  
    
```

\[/code\]

\[code\]

```python


    chain.invoke({"foo": "bears"})  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content='Why did the bear never wear shoes?', additional_kwargs={}, example=False)  
    
```

\[/code\]

### Attaching Function Call information​

\[code\]

```python


    functions = [  
        {  
            "name": "joke",  
            "description": "A joke",  
            "parameters": {  
                "type": "object",  
                "properties": {  
                    "setup": {"type": "string", "description": "The setup for the joke"},  
                    "punchline": {  
                        "type": "string",  
                        "description": "The punchline for the joke",  
                    },  
                },  
                "required": ["setup", "punchline"],  
            },  
        }  
    ]  
    chain = prompt | model.bind(function_call={"name": "joke"}, functions=functions)  
    
```

\[/code\]

\[code\]

```python


    chain.invoke({"foo": "bears"}, config={})  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content='', additional_kwargs={'function_call': {'name': 'joke', 'arguments': '{\n  "setup": "Why don\'t bears wear shoes?",\n  "punchline": "Because they have bear feet!"\n}'}}, example=False)  
    
```

\[/code\]

## PromptTemplate + LLM + OutputParser​

We can also add in an output parser to easily transform the raw LLM/ChatModel output into a more workable format

\[code\]

```python


    from langchain.schema.output_parser import StrOutputParser  
      
    chain = prompt | model | StrOutputParser()  
    
```

\[/code\]

Notice that this now returns a string - a much more workable format for downstream tasks

\[code\]

```python


    chain.invoke({"foo": "bears"})  
    
```

\[/code\]

\[code\]

```python


        "Why don't bears wear shoes?\n\nBecause they have bear feet!"  
    
```

\[/code\]

### Functions Output Parser​

When you specify the function to return, you may just want to parse that directly

\[code\]

```python


    from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser  
      
    chain = (  
        prompt  
        | model.bind(function_call={"name": "joke"}, functions=functions)  
        | JsonOutputFunctionsParser()  
    )  
    
```

\[/code\]

\[code\]

```python


    chain.invoke({"foo": "bears"})  
    
```

\[/code\]

\[code\]

```python


        {'setup': "Why don't bears like fast food?",  
         'punchline': "Because they can't catch it!"}  
    
```

\[/code\]

\[code\]

```python


    from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser  
      
    chain = (  
        prompt  
        | model.bind(function_call={"name": "joke"}, functions=functions)  
        | JsonKeyOutputFunctionsParser(key_name="setup")  
    )  
    
```

\[/code\]

\[code\]

```python


    chain.invoke({"foo": "bears"})  
    
```

\[/code\]

\[code\]

```python


        "Why don't bears wear shoes?"  
    
```

\[/code\]

## Simplifying input​

To make invocation even simpler, we can add a `RunnableMap` to take care of creating the prompt input dict for us:

\[code\]

```python


    from langchain.schema.runnable import RunnableMap, RunnablePassthrough  
      
    map_ = RunnableMap(foo=RunnablePassthrough())  
    chain = (  
        map_  
        | prompt  
        | model.bind(function_call={"name": "joke"}, functions=functions)  
        | JsonKeyOutputFunctionsParser(key_name="setup")  
    )  
    
```

\[/code\]

\[code\]

```python


    chain.invoke("bears")  
    
```

\[/code\]

\[code\]

```python


        "Why don't bears wear shoes?"  
    
```

\[/code\]

Since we're composing our map with another Runnable, we can even use some syntactic sugar and just use a dict:

\[code\]

```python


    chain = (  
        {"foo": RunnablePassthrough()}  
        | prompt  
        | model.bind(function_call={"name": "joke"}, functions=functions)  
        | JsonKeyOutputFunctionsParser(key_name="setup")  
    )  
    
```

\[/code\]

\[code\]

```python


    chain.invoke("bears")  
    
```

\[/code\]

\[code\]

```python


        "Why don't bears like fast food?"  
    
```

\[/code\]
