Skip to main content

# Adding moderation

This shows how to add in moderation (or other safeguards) around your LLM application.

\[code\]

```python


    from langchain.chains import OpenAIModerationChain  
    from langchain.llms import OpenAI  
    from langchain.prompts import ChatPromptTemplate  
    
```

\[/code\]

\[code\]

```python


    moderate = OpenAIModerationChain()  
    
```

\[/code\]

\[code\]

```python


    model = OpenAI()  
    prompt = ChatPromptTemplate.from_messages([("system", "repeat after me: {input}")])  
    
```

\[/code\]

\[code\]

```python


    chain = prompt | model  
    
```

\[/code\]

\[code\]

```python


    chain.invoke({"input": "you are stupid"})  
    
```

\[/code\]

\[code\]

```python


        '\n\nYou are stupid.'  
    
```

\[/code\]

\[code\]

```python


    moderated_chain = chain | moderate  
    
```

\[/code\]

\[code\]

```python


    moderated_chain.invoke({"input": "you are stupid"})  
    
```

\[/code\]

\[code\]

```python


        {'input': '\n\nYou are stupid',  
         'output': "Text was found that violates OpenAI's content policy."}  
    
```

\[/code\]
