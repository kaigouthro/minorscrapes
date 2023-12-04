

Skip to main content

On this page

# Tools

info

For documentation on built-in tool integrations, visit Integrations.

Tools are interfaces that an agent can use to interact with the world.

## Getting Started​

Tools are functions that agents can use to interact with the world. These tools can be generic utilities (e.g. search), other chains, or even other agents.

Currently, tools can be loaded using the following snippet:

[code]
```python




    from langchain.agents import load_tools  
    tool_names = [...]  
    tools = load_tools(tool_names)  
    


```
[/code]


Some tools (e.g. chains, agents) may require a base LLM to use to initialize them. In that case, you can pass in an LLM as well:

[code]
```python




    from langchain.agents import load_tools  
    tool_names = [...]  
    llm = ...  
    tools = load_tools(tool_names, llm=llm)  
    


```
[/code]


