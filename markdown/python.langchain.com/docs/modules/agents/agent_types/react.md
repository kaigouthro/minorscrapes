

Skip to main content

On this page

# ReAct

This walkthrough showcases using an agent to implement the ReAct logic.

[code]
```python




    from langchain.agents import AgentType, initialize_agent, load_tools  
    from langchain.llms import OpenAI  
    


```
[/code]


First, let's load the language model we're going to use to control the agent.

[code]
```python




    llm = OpenAI(temperature=0)  
    


```
[/code]


Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.

[code]
```python




    tools = load_tools(["serpapi", "llm-math"], llm=llm)  
    


```
[/code]


## Using LCEL​

We will first show how to create the agent using LCEL

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




    prompt = hub.pull("hwchase17/react")  
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
         I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.  
        Action: Search  
        Action Input: "Leo DiCaprio girlfriend"model Vittoria Ceretti I need to find out Vittoria Ceretti's age  
        Action: Search  
        Action Input: "Vittoria Ceretti age"25 years I need to calculate 25 raised to the 0.43 power  
        Action: Calculator  
        Action Input: 25^0.43Answer: 3.991298452658078 I now know the final answer  
        Final Answer: Leo DiCaprio's girlfriend is Vittoria Ceretti and her current age raised to the 0.43 power is 3.991298452658078.  
          
        > Finished chain.  
      
      
      
      
      
        {'input': "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?",  
         'output': "Leo DiCaprio's girlfriend is Vittoria Ceretti and her current age raised to the 0.43 power is 3.991298452658078."}  
    


```
[/code]


## Using ZeroShotReactAgent​

We will now show how to use the agent with an off-the-shelf agent implementation

[code]
```python




    agent_executor = initialize_agent(  
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True  
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


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
         I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.  
        Action: Search  
        Action Input: "Leo DiCaprio girlfriend"  
        Observation: model Vittoria Ceretti  
        Thought: I need to find out Vittoria Ceretti's age  
        Action: Search  
        Action Input: "Vittoria Ceretti age"  
        Observation: 25 years  
        Thought: I need to calculate 25 raised to the 0.43 power  
        Action: Calculator  
        Action Input: 25^0.43  
        Observation: Answer: 3.991298452658078  
        Thought: I now know the final answer  
        Final Answer: Leo DiCaprio's girlfriend is Vittoria Ceretti and her current age raised to the 0.43 power is 3.991298452658078.  
          
        > Finished chain.  
      
      
      
      
      
        {'input': "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?",  
         'output': "Leo DiCaprio's girlfriend is Vittoria Ceretti and her current age raised to the 0.43 power is 3.991298452658078."}  
    


```
[/code]


## Using chat models​

You can also create ReAct agents that use chat models instead of LLMs as the agent driver.

The main difference here is a different prompt. We will use JSON to encode the agent's actions (chat models are a bit tougher to steet, so using JSON helps to enforce the output format).

[code]
```python




    from langchain.chat_models import ChatOpenAI  
    


```
[/code]


[code]
```python




    chat_model = ChatOpenAI(temperature=0)  
    


```
[/code]


[code]
```python




    prompt = hub.pull("hwchase17/react-json")  
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




    from langchain.agents.output_parsers import ReActJsonSingleInputOutputParser  
    


```
[/code]


[code]
```python




    agent = (  
        {  
            "input": lambda x: x["input"],  
            "agent_scratchpad": lambda x: format_log_to_str(x["intermediate_steps"]),  
        }  
        | prompt  
        | chat_model_with_stop  
        | ReActJsonSingleInputOutputParser()  
    )  
    


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


We can also use an off-the-shelf agent class

[code]
```python




    agent = initialize_agent(  
        tools, chat_model, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True  
    )  
    agent.run(  
        "Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?"  
    )  
    


```
[/code]


