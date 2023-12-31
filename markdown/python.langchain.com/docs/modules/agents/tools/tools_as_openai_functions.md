

Skip to main content

# Tools as OpenAI Functions

This notebook goes over how to use LangChain tools as OpenAI functions.

[code]
```python




    from langchain.chat_models import ChatOpenAI  
    from langchain.schema import HumanMessage  
    


```
[/code]


[code]
```python




    model = ChatOpenAI(model="gpt-3.5-turbo-0613")  
    


```
[/code]


[code]
```python




    from langchain.tools import MoveFileTool, format_tool_to_openai_function  
    


```
[/code]


[code]
```python




    tools = [MoveFileTool()]  
    functions = [format_tool_to_openai_function(t) for t in tools]  
    


```
[/code]


[code]
```python




    message = model.predict_messages(  
        [HumanMessage(content="move file foo to bar")], functions=functions  
    )  
    


```
[/code]


[code]
```python




    message  
    


```
[/code]


[code]
```python




        AIMessage(content='', additional_kwargs={'function_call': {'name': 'move_file', 'arguments': '{\n  "source_path": "foo",\n  "destination_path": "bar"\n}'}}, example=False)  
    


```
[/code]


[code]
```python




    message.additional_kwargs["function_call"]  
    


```
[/code]


[code]
```python




        {'name': 'move_file',  
         'arguments': '{\n  "source_path": "foo",\n  "destination_path": "bar"\n}'}  
    


```
[/code]


