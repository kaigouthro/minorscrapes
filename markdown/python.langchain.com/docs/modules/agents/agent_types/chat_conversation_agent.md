

Skip to main content

On this page

# Conversational

This walkthrough demonstrates how to use an agent optimized for conversation. Other agents are often optimized for using tools to figure out the best response, which is not ideal in a conversational
setting where you may want the agent to be able to chat with the user as well.

If we compare it to the standard ReAct agent, the main difference is the prompt. We want it to be much more conversational.

[code]
```python




    from langchain.agents import AgentType, Tool, initialize_agent  
    from langchain.llms import OpenAI  
    from langchain.memory import ConversationBufferMemory  
    from langchain.utilities import SerpAPIWrapper  
    


```
[/code]


[code]
```python




    search = SerpAPIWrapper()  
    tools = [  
        Tool(  
            name="Current Search",  
            func=search.run,  
            description="useful for when you need to answer questions about current events or the current state of the world",  
        ),  
    ]  
    


```
[/code]


[code]
```python




    llm = OpenAI(temperature=0)  
    


```
[/code]


## Using LCEL​

We will first show how to create this agent using LCEL

[code]
```python




    from langchain import hub  
    from langchain.agents.format_scratchpad import format_log_to_str  
    from langchain.agents.output_parsers import ReActSingleInputOutputParser  
    from langchain.tools.render import render_text_description  
    


```
[/code]


[code]
```python




    prompt = hub.pull("hwchase17/react-chat")  
    


```
[/code]


[code]
```python




    prompt = prompt.partial(  
        tools=render_text_description(tools),  
        tool_names=", ".join([t.name for t in tools]),  
    )  
    


```
[/code]


[code]
```python




    llm_with_stop = llm.bind(stop=["\nObservation"])  
    


```
[/code]


[code]
```python




    agent = (  
        {  
            "input": lambda x: x["input"],  
            "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),  
            "chat_history": lambda x: x["chat_history"],  
        }  
        | prompt  
        | llm_with_stop  
        | ReActSingleInputOutputParser()  
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




    memory = ConversationBufferMemory(memory_key="chat_history")  
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory)  
    


```
[/code]


[code]
```python




    agent_executor.invoke({"input": "hi, i am bob"})["output"]  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
          
        Thought: Do I need to use a tool? No  
        Final Answer: Hi Bob, nice to meet you! How can I help you today?  
          
        > Finished chain.  
      
      
      
      
      
        'Hi Bob, nice to meet you! How can I help you today?'  
    


```
[/code]


[code]
```python




    agent_executor.invoke({"input": "whats my name?"})["output"]  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
          
        Thought: Do I need to use a tool? No  
        Final Answer: Your name is Bob.  
          
        > Finished chain.  
      
      
      
      
      
        'Your name is Bob.'  
    


```
[/code]


[code]
```python




    agent_executor.invoke({"input": "what are some movies showing 9/21/2023?"})["output"]  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
          
        Thought: Do I need to use a tool? Yes  
        Action: Current Search  
        Action Input: Movies showing 9/21/2023['September 2023 Movies: The Creator • Dumb Money • Expend4bles • The Kill Room • The Inventor • The Equalizer 3 • PAW Patrol: The Mighty Movie, ...'] Do I need to use a tool? No  
        Final Answer: According to current search, some movies showing on 9/21/2023 are The Creator, Dumb Money, Expend4bles, The Kill Room, The Inventor, The Equalizer 3, and PAW Patrol: The Mighty Movie.  
          
        > Finished chain.  
      
      
      
      
      
        'According to current search, some movies showing on 9/21/2023 are The Creator, Dumb Money, Expend4bles, The Kill Room, The Inventor, The Equalizer 3, and PAW Patrol: The Mighty Movie.'  
    


```
[/code]


## Use the off-the-shelf agent​

We can also create this agent using the off-the-shelf agent class

[code]
```python




    agent_executor = initialize_agent(  
        tools,  
        llm,  
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,  
        verbose=True,  
        memory=memory,  
    )  
    


```
[/code]


## Use a chat model​

We can also use a chat model here. The main difference here is in the prompts used.

[code]
```python




    from langchain import hub  
    from langchain.chat_models import ChatOpenAI  
    


```
[/code]


[code]
```python




    prompt = hub.pull("hwchase17/react-chat-json")  
    chat_model = ChatOpenAI(temperature=0, model="gpt-4")  
    


```
[/code]


[code]
```python




    prompt = prompt.partial(  
        tools=render_text_description(tools),  
        tool_names=", ".join([t.name for t in tools]),  
    )  
    


```
[/code]


[code]
```python




    chat_model_with_stop = chat_model.bind(stop=["\nObservation"])  
    


```
[/code]


[code]
```python




    from langchain.agents.format_scratchpad import format_log_to_messages  
    from langchain.agents.output_parsers import JSONAgentOutputParser  
    


```
[/code]


[code]
```python




    # We need some extra steering, or the chat model forgets how to respond sometimes  
    TEMPLATE_TOOL_RESPONSE = """TOOL RESPONSE:   
    ---------------------  
    {observation}  
      
    USER'S INPUT  
    --------------------  
      
    Okay, so what is the response to my last comment? If using information obtained from the tools you must mention it explicitly without mentioning the tool names - I have forgotten all TOOL RESPONSES! Remember to respond with a markdown code snippet of a json blob with a single action, and NOTHING else - even if you just want to respond to the user. Do NOT respond with anything except a JSON snippet no matter what!"""  
      
    agent = (  
        {  
            "input": lambda x: x["input"],  
            "agent_scratchpad": lambda x: format_log_to_messages(  
                x["intermediate_steps"], template_tool_response=TEMPLATE_TOOL_RESPONSE  
            ),  
            "chat_history": lambda x: x["chat_history"],  
        }  
        | prompt  
        | chat_model_with_stop  
        | JSONAgentOutputParser()  
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




    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)  
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory)  
    


```
[/code]


[code]
```python




    agent_executor.invoke({"input": "hi, i am bob"})["output"]  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
        ```json  
        {  
            "action": "Final Answer",  
            "action_input": "Hello Bob, how can I assist you today?"  
        }  
        ```  
          
        > Finished chain.  
      
      
      
      
      
        'Hello Bob, how can I assist you today?'  
    


```
[/code]


[code]
```python




    agent_executor.invoke({"input": "whats my name?"})["output"]  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
        ```json  
        {  
            "action": "Final Answer",  
            "action_input": "Your name is Bob."  
        }  
        ```  
          
        > Finished chain.  
      
      
      
      
      
        'Your name is Bob.'  
    


```
[/code]


[code]
```python




    agent_executor.invoke({"input": "what are some movies showing 9/21/2023?"})["output"]  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
        ```json  
        {  
            "action": "Current Search",  
            "action_input": "movies showing on 9/21/2023"  
        }  
        ```['September 2023 Movies: The Creator • Dumb Money • Expend4bles • The Kill Room • The Inventor • The Equalizer 3 • PAW Patrol: The Mighty Movie, ...']```json  
        {  
            "action": "Final Answer",  
            "action_input": "Some movies that are showing on 9/21/2023 include 'The Creator', 'Dumb Money', 'Expend4bles', 'The Kill Room', 'The Inventor', 'The Equalizer 3', and 'PAW Patrol: The Mighty Movie'."  
        }  
        ```  
          
        > Finished chain.  
      
      
      
      
      
        "Some movies that are showing on 9/21/2023 include 'The Creator', 'Dumb Money', 'Expend4bles', 'The Kill Room', 'The Inventor', 'The Equalizer 3', and 'PAW Patrol: The Mighty Movie'."  
    


```
[/code]


We can also initialize the agent executor with a predefined agent type

[code]
```python




    from langchain.chat_models import ChatOpenAI  
    from langchain.memory import ConversationBufferMemory  
    


```
[/code]


[code]
```python




    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)  
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)  
    agent_chain = initialize_agent(  
        tools,  
        llm,  
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,  
        verbose=True,  
        memory=memory,  
    )  
    


```
[/code]


