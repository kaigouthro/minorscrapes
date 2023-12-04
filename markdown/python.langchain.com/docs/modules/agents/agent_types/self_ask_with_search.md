

Skip to main content

On this page

# Self-ask with search

This walkthrough showcases the self-ask with search chain.

[code]
```python




    from langchain.agents import AgentType, Tool, initialize_agent  
    from langchain.llms import OpenAI  
    from langchain.utilities import SerpAPIWrapper  
      
    llm = OpenAI(temperature=0)  
    search = SerpAPIWrapper()  
    tools = [  
        Tool(  
            name="Intermediate Answer",  
            func=search.run,  
            description="useful for when you need to ask with search",  
        )  
    ]  
    


```
[/code]


## Using LangChain Expression Language​

First we will show how to construct this agent from components using LangChain Expression Language

[code]
```python




    from langchain import hub  
    from langchain.agents.format_scratchpad import format_log_to_str  
    from langchain.agents.output_parsers import SelfAskOutputParser  
    


```
[/code]


[code]
```python




    prompt = hub.pull("hwchase17/self-ask-with-search")  
    


```
[/code]


[code]
```python




    llm_with_stop = llm.bind(stop=["\nIntermediate answer:"])  
    


```
[/code]


[code]
```python




    agent = (  
        {  
            "input": lambda x: x["input"],  
            # Use some custom observation_prefix/llm_prefix for formatting  
            "agent_scratchpad": lambda x: format_log_to_str(  
                x["intermediate_steps"],  
                observation_prefix="\nIntermediate answer: ",  
                llm_prefix="",  
            ),  
        }  
        | prompt  
        | llm_with_stop  
        | SelfAskOutputParser()  
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
        {"input": "What is the hometown of the reigning men's U.S. Open champion?"}  
    )  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
         Yes.  
        Follow up: Who is the reigning men's U.S. Open champion?Men's US Open Tennis Champions Novak Djokovic earned his 24th major singles title against 2021 US Open champion Daniil Medvedev, 6-3, 7-6 (7-5), 6-3. The victory ties the Serbian player with the legendary Margaret Court for the most Grand Slam wins across both men's and women's singles.  
        Follow up: Where is Novak Djokovic from?Belgrade, Serbia  
        So the final answer is: Belgrade, Serbia  
          
        > Finished chain.  
      
      
      
      
      
        {'input': "What is the hometown of the reigning men's U.S. Open champion?",  
         'output': 'Belgrade, Serbia'}  
    


```
[/code]


## Use off-the-shelf agent​

[code]
```python




    self_ask_with_search = initialize_agent(  
        tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True  
    )  
    self_ask_with_search.run(  
        "What is the hometown of the reigning men's U.S. Open champion?"  
    )  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
         Yes.  
        Follow up: Who is the reigning men's U.S. Open champion?  
        Intermediate answer: Men's US Open Tennis Champions Novak Djokovic earned his 24th major singles title against 2021 US Open champion Daniil Medvedev, 6-3, 7-6 (7-5), 6-3. The victory ties the Serbian player with the legendary Margaret Court for the most Grand Slam wins across both men's and women's singles.  
          
        Follow up: Where is Novak Djokovic from?  
        Intermediate answer: Belgrade, Serbia  
        So the final answer is: Belgrade, Serbia  
          
        > Finished chain.  
      
      
      
      
      
        'Belgrade, Serbia'  
    


```
[/code]


