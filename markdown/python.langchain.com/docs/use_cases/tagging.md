

Skip to main content

On this page

## Use case​

Tagging means labeling a document with classes such as:

  * sentiment
  * language
  * style (formal, informal etc.)
  * covered topics
  * political tendency

## Overview​

Tagging has a few components:

  * `function`: Like extraction, tagging uses functions to specify how the model should tag a document
  * `schema`: defines how we want to tag the document

## Quickstart​

Let's see a very straightforward example of how we can use OpenAI functions for tagging in LangChain.

[code]
```python




    pip install langchain openai  
      
    # Set env var OPENAI_API_KEY or load from a .env file:  
    # import dotenv  
    # dotenv.load_dotenv()  
    


```
[/code]


[code]
```python




    from langchain.chains import create_tagging_chain, create_tagging_chain_pydantic  
    from langchain.chat_models import ChatOpenAI  
    


```
[/code]


We specify a few properties with their expected type in our schema.

[code]
```python




    # Schema  
    schema = {  
        "properties": {  
            "sentiment": {"type": "string"},  
            "aggressiveness": {"type": "integer"},  
            "language": {"type": "string"},  
        }  
    }  
      
    # LLM  
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")  
    chain = create_tagging_chain(schema, llm)  
    


```
[/code]


[code]
```python




    inp = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"  
    chain.run(inp)  
    


```
[/code]


[code]
```python




        {'sentiment': 'positive', 'language': 'Spanish'}  
    


```
[/code]


[code]
```python




    inp = "Estoy muy enojado con vos! Te voy a dar tu merecido!"  
    chain.run(inp)  
    


```
[/code]


[code]
```python




        {'sentiment': 'enojado', 'aggressiveness': 1, 'language': 'es'}  
    


```
[/code]


As we can see in the examples, it correctly interprets what we want.

The results vary so that we get, for example, sentiments in different languages ('positive', 'enojado' etc.).

We will see how to control these results in the next section.

## Finer control​

Careful schema definition gives us more control over the model's output.

Specifically, we can define:

  * possible values for each property
  * description to make sure that the model understands the property
  * required properties to be returned

Here is an example of how we can use `_enum_`, `_description_`, and `_required_` to control for each of the previously mentioned aspects:

[code]
```python




    schema = {  
        "properties": {  
            "aggressiveness": {  
                "type": "integer",  
                "enum": [1, 2, 3, 4, 5],  
                "description": "describes how aggressive the statement is, the higher the number the more aggressive",  
            },  
            "language": {  
                "type": "string",  
                "enum": ["spanish", "english", "french", "german", "italian"],  
            },  
        },  
        "required": ["language", "sentiment", "aggressiveness"],  
    }  
    


```
[/code]


[code]
```python




    chain = create_tagging_chain(schema, llm)  
    


```
[/code]


Now the answers are much better!

[code]
```python




    inp = "Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"  
    chain.run(inp)  
    


```
[/code]


[code]
```python




        {'aggressiveness': 0, 'language': 'spanish'}  
    


```
[/code]


[code]
```python




    inp = "Estoy muy enojado con vos! Te voy a dar tu merecido!"  
    chain.run(inp)  
    


```
[/code]


[code]
```python




        {'aggressiveness': 5, 'language': 'spanish'}  
    


```
[/code]


[code]
```python




    inp = "Weather is ok here, I can go outside without much more than a coat"  
    chain.run(inp)  
    


```
[/code]


[code]
```python




        {'aggressiveness': 0, 'language': 'english'}  
    


```
[/code]


The LangSmith trace lets us peek under the hood:

  * As with extraction, we call the `information_extraction` function here on the input string.
  * This OpenAI function extraction information based upon the provided schema.

## Pydantic​

We can also use a Pydantic schema to specify the required properties and types.

We can also send other arguments, such as `enum` or `description`, to each field.

This lets us specify our schema in the same manner that we would a new class or function in Python with purely Pythonic types.

[code]
```python




    from pydantic import BaseModel, Field  
    


```
[/code]


[code]
```python




    class Tags(BaseModel):  
        sentiment: str = Field(..., enum=["happy", "neutral", "sad"])  
        aggressiveness: int = Field(  
            ...,  
            description="describes how aggressive the statement is, the higher the number the more aggressive",  
            enum=[1, 2, 3, 4, 5],  
        )  
        language: str = Field(  
            ..., enum=["spanish", "english", "french", "german", "italian"]  
        )  
    


```
[/code]


[code]
```python




    chain = create_tagging_chain_pydantic(Tags, llm)  
    


```
[/code]


[code]
```python




    inp = "Estoy muy enojado con vos! Te voy a dar tu merecido!"  
    res = chain.run(inp)  
    


```
[/code]


[code]
```python




    res  
    


```
[/code]


[code]
```python




        Tags(sentiment='sad', aggressiveness=5, language='spanish')  
    


```
[/code]


### Going deeper​

  * You can use the metadata tagger document transformer to extract metadata from a LangChain `Document`. 
  * This covers the same basic functionality as the tagging chain, only applied to a LangChain `Document`.

