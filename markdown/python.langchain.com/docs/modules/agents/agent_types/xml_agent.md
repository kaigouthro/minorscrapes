

Skip to main content

On this page

# XML Agent

Some language models (like Anthropic's Claude) are particularly good at reasoning/writing XML. This goes over how to use an agent that uses XML when prompting.

## Initialize the tools​

We will initialize some fake tools for demo purposes

[code]
```python




    from langchain.agents import tool  
      
      
    @tool  
    def search(query: str) -> str:  
        """Search things about current events."""  
        return "32 degrees"  
    


```
[/code]


[code]
```python




    tools = [search]  
    


```
[/code]


[code]
```python




    from langchain.chat_models import ChatAnthropic  
      
    model = ChatAnthropic(model="claude-2")  
    


```
[/code]


## Use LangChain Expression Language​

We will first show how to create this agent using LangChain Expression Language

[code]
```python




    from langchain import hub  
    from langchain.agents.format_scratchpad import format_xml  
    from langchain.agents.output_parsers import XMLAgentOutputParser  
    from langchain.tools.render import render_text_description  
    


```
[/code]


[code]
```python




    prompt = hub.pull("hwchase17/xml-agent")  
    


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




    llm_with_stop = model.bind(stop=["</tool_input>"])  
    


```
[/code]


[code]
```python




    agent = (  
        {  
            "question": lambda x: x["question"],  
            "agent_scratchpad": lambda x: format_xml(x["intermediate_steps"]),  
        }  
        | prompt  
        | llm_with_stop  
        | XMLAgentOutputParser()  
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




    agent_executor.invoke({"question": "whats the weather in New york?"})  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
         <tool>search</tool>  
        <tool_input>weather in new york32 degrees <tool>search</tool>  
        <tool_input>weather in new york32 degrees <final_answer>  
        The weather in New York is 32 degrees.  
        </final_answer>  
          
        > Finished chain.  
      
      
      
      
      
        {'question': 'whats the weather in New york?',  
         'output': '\nThe weather in New York is 32 degrees.\n'}  
    


```
[/code]


## Use off-the-shelf agent​

[code]
```python




    from langchain.agents import XMLAgent  
    from langchain.chains import LLMChain  
    


```
[/code]


[code]
```python




    chain = LLMChain(  
        llm=model,  
        prompt=XMLAgent.get_default_prompt(),  
        output_parser=XMLAgent.get_default_output_parser(),  
    )  
    agent = XMLAgent(tools=tools, llm_chain=chain)  
    


```
[/code]


[code]
```python




    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  
    


```
[/code]


[code]
```python




    agent_executor.invoke({"input": "whats the weather in New york?"})  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
         <tool>search</tool>  
        <tool_input>weather in new york32 degrees  
          
        <final_answer>The weather in New York is 32 degrees  
          
        > Finished chain.  
      
      
      
      
      
        {'input': 'whats the weather in New york?',  
         'output': 'The weather in New York is 32 degrees'}  
    


```
[/code]


