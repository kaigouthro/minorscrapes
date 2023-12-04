

Skip to main content

On this page

# Structured tool chat

The structured tool chat agent is capable of using multi-input tools.

Older agents are configured to specify an action input as a single string, but this agent can use the provided tools' `args_schema` to populate the action input.

[code]
```python




    from langchain.agents import AgentType, initialize_agent  
    from langchain.chat_models import ChatOpenAI  
    


```
[/code]


## Initialize Tools​

We will test the agent using a web browser

[code]
```python




    # This import is required only for jupyter notebooks, since they have their own eventloop  
    import nest_asyncio  
    from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit  
    from langchain.tools.playwright.utils import (  
        create_async_playwright_browser,  # A synchronous browser is available, though it isn't compatible with jupyter.  
    )  
      
    nest_asyncio.apply()  
    


```
[/code]


[code]
```python




    pip install playwright  
    playwright install  
    


```
[/code]


[code]
```python




    async_browser = create_async_playwright_browser()  
    browser_toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)  
    tools = browser_toolkit.get_tools()  
    


```
[/code]


## Use LCEL​

We can first construct this agent using LangChain Expression Language

[code]
```python




    from langchain import hub  
    


```
[/code]


[code]
```python




    prompt = hub.pull("hwchase17/react-multi-input-json")  
    


```
[/code]


[code]
```python




    from langchain.tools.render import render_text_description_and_args  
    


```
[/code]


[code]
```python




    prompt = prompt.partial(  
        tools=render_text_description_and_args(tools),  
        tool_names=", ".join([t.name for t in tools]),  
    )  
    


```
[/code]


[code]
```python




    llm = ChatOpenAI(temperature=0)  
    llm_with_stop = llm.bind(stop=["Observation"])  
    


```
[/code]


[code]
```python




    from langchain.agents.format_scratchpad import format_log_to_str  
    from langchain.agents.output_parsers import JSONAgentOutputParser  
    


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




    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  
    


```
[/code]


[code]
```python




    response = await agent_executor.ainvoke(  
        {"input": "Browse to blog.langchain.dev and summarize the text, please."}  
    )  
    print(response["output"])  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
        Action:  
        ```  
        {  
          "action": "navigate_browser",  
          "action_input": {  
            "url": "https://blog.langchain.dev"  
          }  
        }  
        ```  
        Navigating to https://blog.langchain.dev returned status code 200Action:  
        ```  
        {  
          "action": "extract_text",  
          "action_input": {}  
        }  
        ```  
          
        LangChain LangChain Home GitHub Docs By LangChain Release Notes Write with Us Sign in Subscribe The official LangChain blog. Subscribe now Login Featured Posts Announcing LangChain Hub Using LangSmith to Support Fine-tuning Announcing LangSmith, a unified platform for debugging, testing, evaluating, and monitoring your LLM applications Sep 20 Peering Into the Soul of AI Decision-Making with LangSmith 10 min read Sep 20 LangChain + Docugami Webinar: Lessons from Deploying LLMs with LangSmith 3 min read Sep 18 TED AI Hackathon Kickoff (and projects we’d love to see) 2 min read Sep 12 How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel 6 min read Sep 12 OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change 4 min read Load more LangChain © 2023 Sign up Powered by GhostAction:  
        ```  
        {  
          "action": "Final Answer",  
          "action_input": "The LangChain blog features posts on topics such as using LangSmith for fine-tuning, AI decision-making with LangSmith, deploying LLMs with LangSmith, and more. It also includes information on LangChain Hub and upcoming webinars. LangChain is a platform for debugging, testing, evaluating, and monitoring LLM applications."  
        }  
        ```  
          
        > Finished chain.  
        The LangChain blog features posts on topics such as using LangSmith for fine-tuning, AI decision-making with LangSmith, deploying LLMs with LangSmith, and more. It also includes information on LangChain Hub and upcoming webinars. LangChain is a platform for debugging, testing, evaluating, and monitoring LLM applications.  
    


```
[/code]


## Use off the shelf agent​

[code]
```python




    llm = ChatOpenAI(temperature=0)  # Also works well with Anthropic models  
    agent_chain = initialize_agent(  
        tools,  
        llm,  
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,  
        verbose=True,  
    )  
    


```
[/code]


[code]
```python




    response = await agent_chain.ainvoke(  
        {"input": "Browse to blog.langchain.dev and summarize the text, please."}  
    )  
    print(response["output"])  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
        Action:  
        ```  
        {  
          "action": "navigate_browser",  
          "action_input": {  
            "url": "https://blog.langchain.dev"  
          }  
        }  
        ```  
        Observation: Navigating to https://blog.langchain.dev returned status code 200  
        Thought:I have successfully navigated to the blog.langchain.dev website. Now I need to extract the text from the webpage to summarize it.  
        Action:  
        ```  
        {  
          "action": "extract_text",  
          "action_input": {}  
        }  
        ```  
        Observation: LangChain LangChain Home GitHub Docs By LangChain Release Notes Write with Us Sign in Subscribe The official LangChain blog. Subscribe now Login Featured Posts Announcing LangChain Hub Using LangSmith to Support Fine-tuning Announcing LangSmith, a unified platform for debugging, testing, evaluating, and monitoring your LLM applications Sep 20 Peering Into the Soul of AI Decision-Making with LangSmith 10 min read Sep 20 LangChain + Docugami Webinar: Lessons from Deploying LLMs with LangSmith 3 min read Sep 18 TED AI Hackathon Kickoff (and projects we’d love to see) 2 min read Sep 12 How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel 6 min read Sep 12 OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change 4 min read Load more LangChain © 2023 Sign up Powered by Ghost  
        Thought:I have successfully navigated to the blog.langchain.dev website. The text on the webpage includes featured posts such as "Announcing LangChain Hub," "Using LangSmith to Support Fine-tuning," "Peering Into the Soul of AI Decision-Making with LangSmith," "LangChain + Docugami Webinar: Lessons from Deploying LLMs with LangSmith," "TED AI Hackathon Kickoff (and projects we’d love to see)," "How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel," and "OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change." There are also links to other pages on the website.  
          
        > Finished chain.  
        I have successfully navigated to the blog.langchain.dev website. The text on the webpage includes featured posts such as "Announcing LangChain Hub," "Using LangSmith to Support Fine-tuning," "Peering Into the Soul of AI Decision-Making with LangSmith," "LangChain + Docugami Webinar: Lessons from Deploying LLMs with LangSmith," "TED AI Hackathon Kickoff (and projects we’d love to see)," "How to Safely Query Enterprise Data with LangChain Agents + SQL + OpenAI + Gretel," and "OpaquePrompts x LangChain: Enhance the privacy of your LangChain application with just one code change." There are also links to other pages on the website.  
    


```
[/code]


