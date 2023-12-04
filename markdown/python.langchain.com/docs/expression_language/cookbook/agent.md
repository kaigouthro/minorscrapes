Skip to main content

# Agents

You can pass a Runnable into an agent.

\[code\]

```python


    from langchain.agents import AgentExecutor, XMLAgent, tool
    from langchain.chat_models import ChatAnthropic

```

\[/code\]

\[code\]

```python


    model = ChatAnthropic(model="claude-2")

```

\[/code\]

\[code\]

```python


    @tool
    def search(query: str) -> str:
        """Search things about current events."""
        return "32 degrees"

```

\[/code\]

\[code\]

```python


    tool_list = [search]

```

\[/code\]

\[code\]

```python


    # Get prompt to use
    prompt = XMLAgent.get_default_prompt()

```

\[/code\]

\[code\]

```python


    # Logic for going from intermediate steps to a string to pass into model
    # This is pretty tied to the prompt
    def convert_intermediate_steps(intermediate_steps):
        log = ""
        for action, observation in intermediate_steps:
            log += (
                f"<tool>{action.tool}</tool><tool_input>{action.tool_input}"
                f"</tool_input><observation>{observation}</observation>"
            )
        return log


    # Logic for converting tools to string to go in prompt
    def convert_tools(tools):
        return "\n".join([f"{tool.name}: {tool.description}" for tool in tools])

```

\[/code\]

Building an agent from a runnable usually involves a few things:

1. Data processing for the intermediate steps. These need to represented in a way that the language model can recognize them. This should be pretty tightly coupled to the instructions in the prompt

1. The prompt itself

1. The model, complete with stop tokens if needed

1. The output parser - should be in sync with how the prompt specifies things to be formatted.

\[code\]

```python


    agent = (
        {
            "question": lambda x: x["question"],
            "intermediate_steps": lambda x: convert_intermediate_steps(
                x["intermediate_steps"]
            ),
        }
        | prompt.partial(tools=convert_tools(tool_list))
        | model.bind(stop=["</tool_input>", "</final_answer>"])
        | XMLAgent.get_default_output_parser()
    )

```

\[/code\]

\[code\]

```python


    agent_executor = AgentExecutor(agent=agent, tools=tool_list, verbose=True)

```

\[/code\]

\[code\]

```python


    agent_executor.invoke({"question": "whats the weather in New york?"})

```

\[/code\]

\[code\]

```python




        > Entering new AgentExecutor chain...
         <tool>search</tool>
        <tool_input>weather in new york32 degrees

        <final_answer>The weather in New York is 32 degrees

        > Finished chain.





        {'question': 'whats the weather in New york?',
         'output': 'The weather in New York is 32 degrees'}

```

\[/code\]
