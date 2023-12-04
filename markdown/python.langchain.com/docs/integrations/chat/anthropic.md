

Skip to main content

On this page

# Anthropic

This notebook covers how to get started with Anthropic chat models.

[code]
```python




    from langchain.chat_models import ChatAnthropic  
    from langchain.schema import HumanMessage  
    


```
[/code]


[code]
```python




    chat = ChatAnthropic()  
    


```
[/code]


[code]
```python




    messages = [  
        HumanMessage(  
            content="Translate this sentence from English to French. I love programming."  
        )  
    ]  
    chat(messages)  
    


```
[/code]


[code]
```python




        AIMessage(content=" J'aime la programmation.", additional_kwargs={}, example=False)  
    


```
[/code]


## `ChatAnthropic` also supports async and streaming functionality:​

[code]
```python




    from langchain.callbacks.manager import CallbackManager  
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    


```
[/code]


[code]
```python




    await chat.agenerate([messages])  
    


```
[/code]


[code]
```python




        LLMResult(generations=[[ChatGeneration(text=" J'aime programmer.", generation_info=None, message=AIMessage(content=" J'aime programmer.", additional_kwargs={}, example=False))]], llm_output={}, run=[RunInfo(run_id=UUID('8cc8fb68-1c35-439c-96a0-695036a93652'))])  
    


```
[/code]


[code]
```python




    chat = ChatAnthropic(  
        streaming=True,  
        verbose=True,  
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),  
    )  
    chat(messages)  
    


```
[/code]


[code]
```python




         J'aime la programmation.  
      
      
      
      
        AIMessage(content=" J'aime la programmation.", additional_kwargs={}, example=False)  
    


```
[/code]


