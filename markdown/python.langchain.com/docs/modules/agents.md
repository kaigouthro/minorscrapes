

Skip to main content

On this page

The core idea of agents is to use a language model to choose a sequence of actions to take. In chains, a sequence of actions is hardcoded (in code). In agents, a language model is used as a reasoning
engine to determine which actions to take and in which order.

## Concepts​

There are several key components here:

### Agent​

This is the chain responsible for deciding what step to take next. This is powered by a language model and a prompt. The inputs to this chain are:

  1. Tools: Descriptions of available tools
  2. User input: The high level objective
  3. Intermediate steps: Any (action, tool output) pairs previously executed in order to achieve the user input

The output is the next action(s) to take or the final response to send to the user (`AgentAction`s or `AgentFinish`). An action specifies a tool and the input to that tool.

Different agents have different prompting styles for reasoning, different ways of encoding inputs, and different ways of parsing the output. For a full list of built-in agents see agent types. You can
also **easily build custom agents** , which we show how to do in the Get started section below.

### Tools​

Tools are functions that an agent can invoke. There are two important design considerations around tools:

  1. Giving the agent access to the right tools
  2. Describing the tools in a way that is most helpful to the agent

Without thinking through both, you won't be able to build a working agent. If you don't give the agent access to a correct set of tools, it will never be able to accomplish the objectives you give it.
If you don't describe the tools well, the agent won't know how to use them properly.

LangChain provides a wide set of built-in tools, but also makes it easy to define your own (including custom descriptions). For a full list of built-in tools, see the tools integrations section

### Toolkits​

For many common tasks, an agent will need a set of related tools. For this LangChain provides the concept of toolkits - groups of around 3-5 tools needed to accomplish specific objectives. For
example, the GitHub toolkit has a tool for searching through GitHub issues, a tool for reading a file, a tool for commenting, etc.

LangChain provides a wide set of toolkits to get started. For a full list of built-in toolkits, see the toolkits integrations section

### AgentExecutor​

The agent executor is the runtime for an agent. This is what actually calls the agent, executes the actions it chooses, passes the action outputs back to the agent, and repeats. In pseudocode, this
looks roughly like:

[code]
```python




    next_action = agent.get_action(...)  
    while next_action != AgentFinish:  
        observation = run(next_action)  
        next_action = agent.get_action(..., next_action, observation)  
    return next_action  
    


```
[/code]


While this may seem simple, there are several complexities this runtime handles for you, including:

  1. Handling cases where the agent selects a non-existent tool
  2. Handling cases where the tool errors
  3. Handling cases where the agent produces output that cannot be parsed into a tool invocation
  4. Logging and observability at all levels (agent decisions, tool calls) to stdout and/or to LangSmith.

### Other types of agent runtimes​

The `AgentExecutor` class is the main agent runtime supported by LangChain. However, there are other, more experimental runtimes we also support. These include:

  * Plan-and-execute Agent
  * Baby AGI
  * Auto GPT

You can also always create your own custom execution logic, which we show how to do below.

## Get started​

To best understand the agent framework, lets build an agent from scratch using LangChain Expression Language (LCEL). We'll need to build the agent itself, define custom tools, and run the agent and
tools in a custom loop. At the end we'll show how to use the standard LangChain `AgentExecutor` to make execution easier.

Some important terminology (and schema) to know:

  1. `AgentAction`: This is a dataclass that represents the action an agent should take. It has a `tool` property (which is the name of the tool that should be invoked) and a `tool_input` property (the input to that tool)
  2. `AgentFinish`: This is a dataclass that signifies that the agent has finished and should return to the user. It has a `return_values` parameter, which is a dictionary to return. It often only has one key - `output` \- that is a string, and so often it is just this key that is returned.
  3. `intermediate_steps`: These represent previous agent actions and corresponding outputs that are passed around. These are important to pass to future iteration so the agent knows what work it has already done. This is typed as a `List[Tuple[AgentAction, Any]]`. Note that observation is currently left as type `Any` to be maximally flexible. In practice, this is often a string.

### Setup: LangSmith​

By definition, agents take a self-determined, input-dependent sequence of steps before returning a user-facing output. This makes debugging these systems particularly tricky, and observability
particularly important. LangSmith is especially useful for such cases.

When building with LangChain, any built-in agent or custom agent built with LCEL will automatically be traced in LangSmith. And if we use the `AgentExecutor`, we'll get full tracing of not only the
agent planning steps but also the tool inputs and outputs.

To set up LangSmith we just need set the following environment variables:

[code]
```python




    export LANGCHAIN_TRACING_V2="true"  
    export LANGCHAIN_API_KEY="<your-api-key>"  
    


```
[/code]


### Define the agent​

We first need to create our agent. This is the chain responsible for determining what action to take next.

In this example, we will use OpenAI Function Calling to create this agent. **This is generally the most reliable way to create agents.**

For this guide, we will construct a custom agent that has access to a custom tool. We are choosing this example because for most real world use cases you will NEED to customize either the agent or the
tools. We'll create a simple tool that computes the length of a word. This is useful because it's actually something LLMs can mess up due to tokenization. We will first create it WITHOUT memory, but
we will then show how to add memory in. Memory is needed to enable conversation.

First, let's load the language model we're going to use to control the agent.

[code]
```python




    from langchain.chat_models import ChatOpenAI  
      
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)  
    


```
[/code]


We can see that it struggles to count the letters in the string "educa".

[code]
```python




    llm.invoke("how many letters in the word educa?")  
    


```
[/code]


[code]
```python




        AIMessage(content='There are 6 letters in the word "educa".')  
    


```
[/code]


Next, let's define some tools to use. Let's write a really simple Python function to calculate the length of a word that is passed in.

[code]
```python




    from langchain.agents import tool  
      
      
    @tool  
    def get_word_length(word: str) -> int:  
        """Returns the length of a word."""  
        return len(word)  
      
      
    tools = [get_word_length]  
    


```
[/code]


Now let us create the prompt. Because OpenAI Function Calling is finetuned for tool usage, we hardly need any instructions on how to reason, or how to output format. We will just have two input
variables: `input` and `agent_scratchpad`. `input` should be a string containing the user objective. `agent_scratchpad` should be a sequence of messages that contains the previous agent tool
invocations and the corresponding tool outputs.

[code]
```python




    from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder  
      
    prompt = ChatPromptTemplate.from_messages(  
        [  
            (  
                "system",  
                "You are very powerful assistant, but bad at calculating lengths of words.",  
            ),  
            ("user", "{input}"),  
            MessagesPlaceholder(variable_name="agent_scratchpad"),  
        ]  
    )  
    


```
[/code]


How does the agent know what tools it can use? In this case we're relying on OpenAI function calling LLMs, which take functions as a separate argument and have been specifically trained to know when
to invoke those functions.

To pass in our tools to the agent, we just need to format them to the OpenAI function format and pass them to our model. (By `bind`-ing the functions, we're making sure that they're passed in each
time the model is invoked.)

[code]
```python




    from langchain.tools.render import format_tool_to_openai_function  
      
    llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])  
    


```
[/code]


Putting those pieces together, we can now create the agent. We will import two last utility functions: a component for formatting intermediate steps (agent action, tool output pairs) to input messages
that can be sent to the model, and a component for converting the output message into an agent action/agent finish.

[code]
```python




    from langchain.agents.format_scratchpad import format_to_openai_function_messages  
    from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser  
      
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


Now that we have our agent, let's play around with it! Let's pass in a simple question and empty intermediate steps and see what it returns:

[code]
```python




    agent.invoke({"input": "how many letters in the word educa?", "intermediate_steps": []})  
    


```
[/code]


[code]
```python




        AgentActionMessageLog(tool='get_word_length', tool_input={'word': 'educa'}, log="\nInvoking: `get_word_length` with `{'word': 'educa'}`\n\n\n", message_log=[AIMessage(content='', additional_kwargs={'function_call': {'arguments': '{\n  "word": "educa"\n}', 'name': 'get_word_length'}})])  
    


```
[/code]


We can see that it responds with an `AgentAction` to take (it's actually an `AgentActionMessageLog` \- a subclass of `AgentAction` which also tracks the full message log).

If we've set up LangSmith, we'll see a trace that let's us inspect the input and output to each step in the sequence: https://smith.langchain.com/public/04110122-01a8-413c-8cd0-b4df6eefa4b7/r

### Define the runtime​

So this is just the first step - now we need to write a runtime for this. The simplest one is just one that continuously loops, calling the agent, then taking the action, and repeating until an
`AgentFinish` is returned. Let's code that up below:

[code]
```python




    from langchain.schema.agent import AgentFinish  
      
    user_input = "how many letters in the word educa?"  
    intermediate_steps = []  
    while True:  
        output = agent.invoke(  
            {  
                "input": user_input,  
                "intermediate_steps": intermediate_steps,  
            }  
        )  
        if isinstance(output, AgentFinish):  
            final_result = output.return_values["output"]  
            break  
        else:  
            print(f"TOOL NAME: {output.tool}")  
            print(f"TOOL INPUT: {output.tool_input}")  
            tool = {"get_word_length": get_word_length}[output.tool]  
            observation = tool.run(output.tool_input)  
            intermediate_steps.append((output, observation))  
    print(final_result)  
    


```
[/code]


[code]
```python




        TOOL NAME: get_word_length  
        TOOL INPUT: {'word': 'educa'}  
        There are 5 letters in the word "educa".  
    


```
[/code]


Woo! It's working.

### Using AgentExecutor​

To simplify this a bit, we can import and use the `AgentExecutor` class. This bundles up all of the above and adds in error handling, early stopping, tracing, and other quality-of-life improvements
that reduce safeguards you need to write.

[code]
```python




    from langchain.agents import AgentExecutor  
      
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  
    


```
[/code]


Now let's test it out!

[code]
```python




    agent_executor.invoke({"input": "how many letters in the word educa?"})  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
          
        Invoking: `get_word_length` with `{'word': 'educa'}`  
          
          
        5There are 5 letters in the word "educa".  
          
        > Finished chain.  
      
      
      
      
      
        {'input': 'how many letters in the word educa?',  
         'output': 'There are 5 letters in the word "educa".'}  
    


```
[/code]


And looking at the trace, we can see that all of our agent calls and tool invocations are automatically logged: https://smith.langchain.com/public/957b7e26-bef8-4b5b-9ca3-4b4f1c96d501/r

### Adding memory​

This is great - we have an agent! However, this agent is stateless - it doesn't remember anything about previous interactions. This means you can't ask follow up questions easily. Let's fix that by
adding in memory.

In order to do this, we need to do two things:

  1. Add a place for memory variables to go in the prompt
  2. Keep track of the chat history

First, let's add a place for memory in the prompt. We do this by adding a placeholder for messages with the key `"chat_history"`. Notice that we put this ABOVE the new user input (to follow the
conversation flow).

[code]
```python




    from langchain.prompts import MessagesPlaceholder  
      
    MEMORY_KEY = "chat_history"  
    prompt = ChatPromptTemplate.from_messages(  
        [  
            (  
                "system",  
                "You are very powerful assistant, but bad at calculating lengths of words.",  
            ),  
            MessagesPlaceholder(variable_name=MEMORY_KEY),  
            ("user", "{input}"),  
            MessagesPlaceholder(variable_name="agent_scratchpad"),  
        ]  
    )  
    


```
[/code]


We can then set up a list to track the chat history

[code]
```python




    from langchain.schema.messages import AIMessage, HumanMessage  
      
    chat_history = []  
    


```
[/code]


We can then put it all together!

[code]
```python




    agent = (  
        {  
            "input": lambda x: x["input"],  
            "agent_scratchpad": lambda x: format_to_openai_function_messages(  
                x["intermediate_steps"]  
            ),  
            "chat_history": lambda x: x["chat_history"],  
        }  
        | prompt  
        | llm_with_tools  
        | OpenAIFunctionsAgentOutputParser()  
    )  
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)  
    


```
[/code]


When running, we now need to track the inputs and outputs as chat history

[code]
```python




    input1 = "how many letters in the word educa?"  
    result = agent_executor.invoke({"input": input1, "chat_history": chat_history})  
    chat_history.extend(  
        [  
            HumanMessage(content=input1),  
            AIMessage(content=result["output"]),  
        ]  
    )  
    agent_executor.invoke({"input": "is that a real word?", "chat_history": chat_history})  
    


```
[/code]


[code]
```python




          
          
        > Entering new AgentExecutor chain...  
          
        Invoking: `get_word_length` with `{'word': 'educa'}`  
          
          
        5There are 5 letters in the word "educa".  
          
        > Finished chain.  
          
          
        > Entering new AgentExecutor chain...  
        No, "educa" is not a real word in English.  
          
        > Finished chain.  
      
      
      
      
      
        {'input': 'is that a real word?',  
         'chat_history': [HumanMessage(content='how many letters in the word educa?'),  
          AIMessage(content='There are 5 letters in the word "educa".')],  
         'output': 'No, "educa" is not a real word in English.'}  
    


```
[/code]


Here's the LangSmith trace: https://smith.langchain.com/public/1e1b7e07-3220-4a6c-8a1e-f04182a755b3/r

## Next Steps​

Awesome! You've now run your first end-to-end agent. To dive deeper, you can:

  * Check out all the different agent types supported
  * Learn all the controls for AgentExecutor
  * Explore the how-to's of tools and all the tool integrations
  * See a full list of all the off-the-shelf toolkits we provide

