

Skip to main content

On this page

# OpenAI functions

Certain OpenAI models (like gpt-3.5-turbo-0613 and gpt-4-0613) have been fine-tuned to detect when a function should be called and respond with the inputs that should be passed to the function. In an
API call, you can describe functions and have the model intelligently choose to output a JSON object containing arguments to call those functions. The goal of the OpenAI Function APIs is to more
reliably return valid and useful function calls than a generic text completion or chat API.

The OpenAI Functions Agent is designed to work with these models.

Install `openai`, `google-search-results` packages which are required as the LangChain packages call them internally.

[code]
```python




    pip install openai google-search-results  
    


```
[/code]


## Initialize tools​

We will first create some tools we can use

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


## Using LCEL​

We will first use LangChain Expression Language to create this agent

[code]
```python




    from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder  
    


```
[/code]


[code]
```python




    prompt = ChatPromptTemplate.from_messages(  
        [  
            ("system", "You are a helpful assistant"),  
            ("user", "{input}"),  
            MessagesPlaceholder(variable_name="agent_scratchpad"),  
        ]  
    )  
    


```
[/code]


[code]
```python




    from langchain.tools.render import format_tool_to_openai_function  
    


```
[/code]


[code]
```python




    llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])  
    


```
[/code]


[code]
```python




    from langchain.agents.format_scratchpad import format_to_openai_function_messages  
    from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser  
    


```
[/code]


[code]
```python




    agent = (  
        {  
            "input": lambda x: x["input"],  
            "agent_scratchpad": lambda x: format_to_openai_function_messages(  
                x["intermediate_steps"]  
            ),  
        }  
        | prompt  
        | llm_with_tools  
        | OpenAIFunctionsAgentOutputParser()  
    )  
    


```
[/code]


[code]
```python




    from langchain.agents import AgentExecutor  
    


```
[/code]


[code]
```python




    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  
    


```
[/code]


[code]
```python




    agent_executor.invoke(  
        {  
            "input": "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"  
        }  
    )  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
          
        Invoking: `Search` with `Leo DiCaprio's girlfriend`  
          
          
        ['Blake Lively and DiCaprio are believed to have enjoyed a whirlwind five-month romance in 2011. The pair were seen on a yacht together in Cannes, ...']  
        Invoking: `Calculator` with `0.43`  
          
          
          
          
        > Entering new LLMMathChain chain...  
        0.43```text  
        0.43  
        ```  
        ...numexpr.evaluate("0.43")...  
          
        Answer: 0.43  
        > Finished chain.  
        Answer: 0.43I'm sorry, but I couldn't find any information about Leo DiCaprio's current girlfriend. As for raising her age to the power of 0.43, I'm not sure what her current age is, so I can't provide an answer for that.  
          
        > Finished chain.  
      
      
      
      
      
        {'input': "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?",  
         'output': "I'm sorry, but I couldn't find any information about Leo DiCaprio's current girlfriend. As for raising her age to the power of 0.43, I'm not sure what her current age is, so I can't provide an answer for that."}  
    


```
[/code]


## Using OpenAIFunctionsAgent​

We can now use `OpenAIFunctionsAgent`, which creates this agent under the hood

[code]
```python




    agent_executor = initialize_agent(  
        tools, llm, agent=AgentType.OPENAI_FUNCTIONS, verbose=True  
    )  
    


```
[/code]


[code]
```python




    agent_executor.invoke(  
        {  
            "input": "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"  
        }  
    )  
    


```
[/code]


