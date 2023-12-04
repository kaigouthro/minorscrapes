

Skip to main content

On this page

# Using OpenAI functions

This walkthrough demonstrates how to incorporate OpenAI function-calling API's in a chain. We'll go over:

  1. How to use functions to get structured outputs from ChatOpenAI
  2. How to create a generic chain that uses (multiple) functions
  3. How to create a chain that actually executes the chosen function

[code]
```python




    from typing import Optional  
      
    from langchain.chains.openai_functions import (  
        create_openai_fn_chain,  
        create_openai_fn_runnable,  
        create_structured_output_chain,  
        create_structured_output_runnable,  
    )  
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts import ChatPromptTemplate  
    


```
[/code]


## Getting structured outputs​

We can take advantage of OpenAI functions to try and force the model to return a particular kind of structured output. We'll use `create_structured_output_runnable` to create our chain, which takes
the desired structured output either as a Pydantic class or as JsonSchema.

### Using Pydantic classes​

When passing in Pydantic classes to structure our text, we need to make sure to have a docstring description for the class. It also helps to have descriptions for each of the classes attributes.

[code]
```python




    from langchain.pydantic_v1 import BaseModel, Field  
      
      
    class Person(BaseModel):  
        """Identifying information about a person."""  
      
        name: str = Field(..., description="The person's name")  
        age: int = Field(..., description="The person's age")  
        fav_food: Optional[str] = Field(None, description="The person's favorite food")  
    


```
[/code]


[code]
```python




    # If we pass in a model explicitly, we need to make sure it supports the OpenAI function-calling API.  
    llm = ChatOpenAI(model="gpt-4", temperature=0)  
    prompt = ChatPromptTemplate.from_messages(  
        [  
            (  
                "system",  
                "You are a world class algorithm for extracting information in structured formats.",  
            ),  
            (  
                "human",  
                "Use the given format to extract information from the following input: {input}",  
            ),  
            ("human", "Tip: Make sure to answer in the correct format"),  
        ]  
    )  
      
    runnable = create_structured_output_runnable(Person, llm, prompt)  
    runnable.invoke({"input": "Sally is 13"})  
    


```
[/code]


[code]
```python




        Person(name='Sally', age=13, fav_food='Unknown')  
    


```
[/code]


To extract arbitrarily many structured outputs of a given format, we can just create a wrapper Pydantic class that takes a sequence of the original class.

[code]
```python




    from typing import Sequence  
      
      
    class People(BaseModel):  
        """Identifying information about all people in a text."""  
      
        people: Sequence[Person] = Field(..., description="The people in the text")  
      
      
    runnable = create_structured_output_runnable(People, llm, prompt)  
    runnable.invoke(  
        {  
            "input": "Sally is 13, Joey just turned 12 and loves spinach. Caroline is 10 years older than Sally."  
        }  
    )  
    


```
[/code]


[code]
```python




        People(people=[Person(name='Sally', age=13, fav_food=''), Person(name='Joey', age=12, fav_food='spinach'), Person(name='Caroline', age=23, fav_food='')])  
    


```
[/code]


### Using JsonSchema​

We can also pass in JsonSchema instead of Pydantic classes to specify the desired structure. When we do this, our chain will output JSON corresponding to the properties described in the JsonSchema,
instead of a Pydantic class.

[code]
```python




    json_schema = {  
        "title": "Person",  
        "description": "Identifying information about a person.",  
        "type": "object",  
        "properties": {  
            "name": {"title": "Name", "description": "The person's name", "type": "string"},  
            "age": {"title": "Age", "description": "The person's age", "type": "integer"},  
            "fav_food": {  
                "title": "Fav Food",  
                "description": "The person's favorite food",  
                "type": "string",  
            },  
        },  
        "required": ["name", "age"],  
    }  
    


```
[/code]


[code]
```python




    runnable = create_structured_output_runnable(json_schema, llm, prompt)  
    runnable.invoke({"input": "Sally is 13"})  
    


```
[/code]


[code]
```python




        {'name': 'Sally', 'age': 13}  
    


```
[/code]


### [Legacy] LLMChain-based approach​

[code]
```python




    chain = create_structured_output_chain(Person, llm, prompt, verbose=True)  
    chain.run("Sally is 13")  
    


```
[/code]


[code]
```python




          
          
        > Entering new LLMChain chain...  
        Prompt after formatting:  
        System: You are a world class algorithm for extracting information in structured formats.  
        Human: Use the given format to extract information from the following input: Sally is 13  
        Human: Tip: Make sure to answer in the correct format  
          
        > Finished chain.  
      
      
      
      
      
        Person(name='Sally', age=13, fav_food='Unknown')  
    


```
[/code]


## Creating a generic OpenAI functions chain​

To create a generic OpenAI functions chain, we can use the `create_openai_fn_runnable` method. This is the same as `create_structured_output_runnable` except that instead of taking a single output
schema, it takes a sequence of function definitions.

Functions can be passed in as:

  * dicts conforming to OpenAI functions spec,
  * Pydantic classes, in which case they should have docstring descriptions of the function they represent and descriptions for each of the parameters,
  * Python functions, in which case they should have docstring descriptions of the function and args, along with type hints.

### Using Pydantic classes​

[code]
```python




    class RecordPerson(BaseModel):  
        """Record some identifying information about a pe."""  
      
        name: str = Field(..., description="The person's name")  
        age: int = Field(..., description="The person's age")  
        fav_food: Optional[str] = Field(None, description="The person's favorite food")  
      
      
    class RecordDog(BaseModel):  
        """Record some identifying information about a dog."""  
      
        name: str = Field(..., description="The dog's name")  
        color: str = Field(..., description="The dog's color")  
        fav_food: Optional[str] = Field(None, description="The dog's favorite food")  
    


```
[/code]


[code]
```python




    from langchain.chains.openai_functions import (  
        convert_to_openai_function,  
        get_openai_output_parser,  
    )  
      
    prompt = ChatPromptTemplate.from_messages(  
        [  
            ("system", "You are a world class algorithm for recording entities."),  
            (  
                "human",  
                "Make calls to the relevant function to record the entities in the following input: {input}",  
            ),  
            ("human", "Tip: Make sure to answer in the correct format"),  
        ]  
    )  
      
    openai_functions = [convert_to_openai_function(f) for f in (RecordPerson, RecordDog)]  
    llm_kwargs = {"functions": openai_functions}  
    if len(openai_functions) == 1:  
        llm_kwargs["function_call"] = {"name": openai_functions[0]["name"]}  
    output_parser = get_openai_output_parser((RecordPerson, RecordDog))  
    runnable = prompt | llm.bind(**llm_kwargs) | output_parser  
    


```
[/code]


[code]
```python




    runnable.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})  
    


```
[/code]


[code]
```python




        RecordDog(name='Harry', color='brown', fav_food='chicken')  
    


```
[/code]


For convenience we can use the `create_openai_fn_runnable` method to help build our Runnable

[code]
```python




    runnable = create_openai_fn_runnable([RecordPerson, RecordDog], llm, prompt)  
    runnable.invoke({"input": "Harry was a chubby brown beagle who loved chicken"})  
    


```
[/code]


[code]
```python




        RecordDog(name='Harry', color='brown', fav_food='chicken')  
    


```
[/code]


### Using Python functions​

We can pass in functions as Pydantic classes, directly as OpenAI function dicts, or Python functions. To pass Python function in directly, we'll want to make sure our parameters have type hints, we
have a docstring, and we use Google Python style docstrings to describe the parameters.

 **NOTE** : To use Python functions, make sure the function arguments are of primitive types (str, float, int, bool) or that they are Pydantic objects.

[code]
```python




    class OptionalFavFood(BaseModel):  
        """Either a food or null."""  
      
        food: Optional[str] = Field(  
            None,  
            description="Either the name of a food or null. Should be null if the food isn't known.",  
        )  
      
      
    def record_person(name: str, age: int, fav_food: OptionalFavFood) -> str:  
        """Record some basic identifying information about a person.  
      
        Args:  
            name: The person's name.  
            age: The person's age in years.  
            fav_food: An OptionalFavFood object that either contains the person's favorite food or a null value. Food should be null if it's not known.  
        """  
        return f"Recording person {name} of age {age} with favorite food {fav_food.food}!"  
      
      
    runnable = create_openai_fn_runnable([record_person], llm, prompt)  
    runnable.invoke(  
        {  
            "input": "The most important thing to remember about Tommy, my 12 year old, is that he'll do anything for apple pie."  
        }  
    )  
    


```
[/code]


[code]
```python




        {'name': 'Tommy', 'age': 12, 'fav_food': {'food': 'apple pie'}}  
    


```
[/code]


If we pass in multiple Python functions or OpenAI functions, then the returned output will be of the form:

[code]
```python




    {"name": "<<function_name>>", "arguments": {<<function_arguments>>}}  
    


```
[/code]


[code]
```python




    def record_dog(name: str, color: str, fav_food: OptionalFavFood) -> str:  
        """Record some basic identifying information about a dog.  
      
        Args:  
            name: The dog's name.  
            color: The dog's color.  
            fav_food: An OptionalFavFood object that either contains the dog's favorite food or a null value. Food should be null if it's not known.  
        """  
        return f"Recording dog {name} of color {color} with favorite food {fav_food}!"  
      
      
    runnable = create_openai_fn_runnable([record_person, record_dog], llm, prompt)  
    runnable.invoke(  
        {  
            "input": "I can't find my dog Henry anywhere, he's a small brown beagle. Could you send a message about him?"  
        }  
    )  
    


```
[/code]


[code]
```python




        {'name': 'record_dog',  
         'arguments': {'name': 'Henry', 'color': 'brown', 'fav_food': {'food': None}}}  
    


```
[/code]


## [Legacy] LLMChain-based approach​

[code]
```python




    chain = create_openai_fn_chain([RecordPerson, RecordDog], llm, prompt, verbose=True)  
    chain.run("Harry was a chubby brown beagle who loved chicken")  
    


```
[/code]


[code]
```python




          
          
        > Entering new LLMChain chain...  
        Prompt after formatting:  
        System: You are a world class algorithm for recording entities.  
        Human: Make calls to the relevant function to record the entities in the following input: Harry was a chubby brown beagle who loved chicken  
        Human: Tip: Make sure to answer in the correct format  
          
        > Finished chain.  
      
      
      
      
      
        RecordDog(name='Harry', color='brown', fav_food='chicken')  
    


```
[/code]


## Other Chains using OpenAI functions​

There are a number of more specific chains that use OpenAI functions.

  * Extraction: very similar to structured output chain, intended for information/entity extraction specifically.
  * Tagging: tag inputs.
  * OpenAPI: take an OpenAPI spec and create + execute valid requests against the API, using OpenAI functions under the hood.
  * QA with citations: use OpenAI functions ability to extract citations from text.

