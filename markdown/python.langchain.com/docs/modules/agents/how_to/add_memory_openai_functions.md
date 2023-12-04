

Skip to main content

# Add Memory to OpenAI Functions Agent

This notebook goes over how to add memory to an OpenAI Functions agent.

[code]
```python




    from langchain.agents import AgentType, Tool, initialize_agent  
    from langchain.chains import LLMMathChain  
    from langchain.chat_models import ChatOpenAI  
    from langchain.utilities import SerpAPIWrapper, SQLDatabase  
    from langchain_experimental.sql import SQLDatabaseChain  
    


```
[/code]


[code]
```python




    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")  
    search = SerpAPIWrapper()  
    llm_math_chain = LLMMathChain.from_llm(llm=llm, verbose=True)  
    db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")  
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)  
    tools = [  
        Tool(  
            name="Search",  
            func=search.run,  
            description="useful for when you need to answer questions about current events. You should ask targeted questions",  
        ),  
        Tool(  
            name="Calculator",  
            func=llm_math_chain.run,  
            description="useful for when you need to answer questions about math",  
        ),  
        Tool(  
            name="FooBar-DB",  
            func=db_chain.run,  
            description="useful for when you need to answer questions about FooBar. Input should be in the form of a question containing full context",  
        ),  
    ]  
    


```
[/code]


[code]
```python




    from langchain.memory import ConversationBufferMemory  
    from langchain.prompts import MessagesPlaceholder  
      
    agent_kwargs = {  
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],  
    }  
    memory = ConversationBufferMemory(memory_key="memory", return_messages=True)  
    


```
[/code]


[code]
```python




    agent = initialize_agent(  
        tools,  
        llm,  
        agent=AgentType.OPENAI_FUNCTIONS,  
        verbose=True,  
        agent_kwargs=agent_kwargs,  
        memory=memory,  
    )  
    


```
[/code]


[code]
```python




    agent.run("hi")  
    


```
[/code]


[code]
```python




          
          
        > Entering new  chain...  
        Hello! How can I assist you today?  
          
        > Finished chain.  
      
      
      
      
      
        'Hello! How can I assist you today?'  
    


```
[/code]


[code]
```python




    agent.run("my name is bob")  
    


```
[/code]


[code]
```python




          
          
        > Entering new  chain...  
        Nice to meet you, Bob! How can I help you today?  
          
        > Finished chain.  
      
      
      
      
      
        'Nice to meet you, Bob! How can I help you today?'  
    


```
[/code]


[code]
```python




    agent.run("whats my name")  
    


```
[/code]


[code]
```python




          
          
        > Entering new  chain...  
        Your name is Bob.  
          
        > Finished chain.  
      
      
      
      
      
        'Your name is Bob.'  
    


```
[/code]


