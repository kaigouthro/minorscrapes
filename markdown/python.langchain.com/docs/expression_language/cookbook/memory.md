Skip to main content

# Adding memory

This shows how to add memory to an arbitrary chain. Right now, you can use the memory classes but need to hook it up manually

\[code\]

```python


    from operator import itemgetter  
      
    from langchain.chat_models import ChatOpenAI  
    from langchain.memory import ConversationBufferMemory  
    from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder  
    from langchain.schema.runnable import RunnableLambda, RunnablePassthrough  
      
    model = ChatOpenAI()  
    prompt = ChatPromptTemplate.from_messages(  
        [  
            ("system", "You are a helpful chatbot"),  
            MessagesPlaceholder(variable_name="history"),  
            ("human", "{input}"),  
        ]  
    )  
    
```

\[/code\]

\[code\]

```python


    memory = ConversationBufferMemory(return_messages=True)  
    
```

\[/code\]

\[code\]

```python


    memory.load_memory_variables({})  
    
```

\[/code\]

\[code\]

```python


        {'history': []}  
    
```

\[/code\]

\[code\]

```python


    chain = (  
        RunnablePassthrough.assign(  
            history=RunnableLambda(memory.load_memory_variables) | itemgetter("history")  
        )  
        | prompt  
        | model  
    )  
    
```

\[/code\]

\[code\]

```python


    inputs = {"input": "hi im bob"}  
    response = chain.invoke(inputs)  
    response  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content='Hello Bob! How can I assist you today?', additional_kwargs={}, example=False)  
    
```

\[/code\]

\[code\]

```python


    memory.save_context(inputs, {"output": response.content})  
    
```

\[/code\]

\[code\]

```python


    memory.load_memory_variables({})  
    
```

\[/code\]

\[code\]

```python


        {'history': [HumanMessage(content='hi im bob', additional_kwargs={}, example=False),  
          AIMessage(content='Hello Bob! How can I assist you today?', additional_kwargs={}, example=False)]}  
    
```

\[/code\]

\[code\]

```python


    inputs = {"input": "whats my name"}  
    response = chain.invoke(inputs)  
    response  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content='Your name is Bob.', additional_kwargs={}, example=False)  
    
```

\[/code\]
