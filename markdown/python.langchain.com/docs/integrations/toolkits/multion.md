

Skip to main content

On this page

# MultiOn

This notebook walks you through connecting LangChain to the `MultiOn` Client in your browser

To use this toolkit, you will need to add `MultiOn Extension` to your browser as explained in the MultiOn for Chrome.

[code]
```python




    pip install --upgrade multion langchain -q  
    


```
[/code]


[code]
```python




    from langchain.agents.agent_toolkits import MultionToolkit  
      
    toolkit = MultionToolkit()  
      
    toolkit  
    


```
[/code]


[code]
```python




    tools = toolkit.get_tools()  
    tools  
    


```
[/code]


## MultiOn Setup​

Login to establish connection with your extension.

[code]
```python




    # Authorize connection to your Browser extention  
    import multion  
      
    multion.login()  
    


```
[/code]


## Use Multion Toolkit within an Agent​

[code]
```python




    from langchain.agents import AgentType, initialize_agent  
    from langchain.llms import OpenAI  
      
    llm = OpenAI(temperature=0)  
    from langchain.agents.agent_toolkits import MultionToolkit  
      
    toolkit = MultionToolkit()  
    tools = toolkit.get_tools()  
    agent = initialize_agent(  
        tools=toolkit.get_tools(),  
        llm=llm,  
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  
        verbose=True,  
    )  
    


```
[/code]


[code]
```python




    agent.run("Tweet 'Hi from MultiOn'")  
    


```
[/code]


