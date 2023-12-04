

Skip to main content

# vLLM Chat

vLLM can be deployed as a server that mimics the OpenAI API protocol. This allows vLLM to be used as a drop-in replacement for applications using OpenAI API. This server can be queried in the same
format as OpenAI API.

This notebook covers how to get started with vLLM chat models using langchain's `ChatOpenAI` **as it is**.

[code]
```python




    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts.chat import (  
        ChatPromptTemplate,  
        HumanMessagePromptTemplate,  
        SystemMessagePromptTemplate,  
    )  
    from langchain.schema import HumanMessage, SystemMessage  
    


```
[/code]


[code]
```python




    inference_server_url = "http://localhost:8000/v1"  
      
    chat = ChatOpenAI(  
        model="mosaicml/mpt-7b",  
        openai_api_key="EMPTY",  
        openai_api_base=inference_server_url,  
        max_tokens=5,  
        temperature=0,  
    )  
    


```
[/code]


[code]
```python




    messages = [  
        SystemMessage(  
            content="You are a helpful assistant that translates English to Italian."  
        ),  
        HumanMessage(  
            content="Translate the following sentence from English to Italian: I love programming."  
        ),  
    ]  
    chat(messages)  
    


```
[/code]


[code]
```python




        AIMessage(content=' Io amo programmare', additional_kwargs={}, example=False)  
    


```
[/code]


You can make use of templating by using a `MessagePromptTemplate`. You can build a `ChatPromptTemplate` from one or more `MessagePromptTemplates`. You can use ChatPromptTemplate's format_prompt --
this returns a `PromptValue`, which you can convert to a string or `Message` object, depending on whether you want to use the formatted value as input to an llm or chat model.

For convenience, there is a `from_template` method exposed on the template. If you were to use this template, this is what it would look like:

[code]
```python




    template = (  
        "You are a helpful assistant that translates {input_language} to {output_language}."  
    )  
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)  
    human_template = "{text}"  
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)  
    


```
[/code]


[code]
```python




    chat_prompt = ChatPromptTemplate.from_messages(  
        [system_message_prompt, human_message_prompt]  
    )  
      
    # get a chat completion from the formatted messages  
    chat(  
        chat_prompt.format_prompt(  
            input_language="English", output_language="Italian", text="I love programming."  
        ).to_messages()  
    )  
    


```
[/code]


[code]
```python




        AIMessage(content=' I love programming too.', additional_kwargs={}, example=False)  
    


```
[/code]


