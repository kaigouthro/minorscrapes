

Skip to main content

On this page

# Slack

This notebook walks through connecting LangChain to your `Slack` account.

To use this toolkit, you will need to get a token explained in the Slack API docs. Once you've received a SLACK_USER_TOKEN, you can input it as an environmental variable below.

[code]
```python




    pip install --upgrade slack_sdk > /dev/null  
    pip install beautifulsoup4 > /dev/null # This is optional but is useful for parsing HTML messages  
    


```
[/code]


## Assign Environmental Variables​

The toolkit will read the SLACK_USER_TOKEN environmental variable to authenticate the user so you need to set them here. You will also need to set your OPENAI_API_KEY to use the agent later.

[code]
```python




    # Set environmental variables here  
    


```
[/code]


## Create the Toolkit and Get Tools​

To start, you need to create the toolkit, so you can access its tools later.

[code]
```python




    from langchain.agents.agent_toolkits import SlackToolkit  
      
    toolkit = SlackToolkit()  
    tools = toolkit.get_tools()  
    tools  
    


```
[/code]


## Use within an Agent​

[code]
```python




    from langchain.agents import AgentType, initialize_agent  
    from langchain.llms import OpenAI  
    


```
[/code]


[code]
```python




    llm = OpenAI(temperature=0)  
    agent = initialize_agent(  
        tools=toolkit.get_tools(),  
        llm=llm,  
        verbose=False,  
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  
    )  
    


```
[/code]


[code]
```python




    agent.run("Send a greeting to my coworkers in the #general channel.")  
    


```
[/code]


[code]
```python




    agent.run("How many channels are in the workspace? Please list out their names.")  
    


```
[/code]


[code]
```python




    agent.run(  
        "Tell me the number of messages sent in the #introductions channel from the past month."  
    )  
    


```
[/code]


