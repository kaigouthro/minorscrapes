Skip to main content

# Code writing

Example of how to use LCEL to write Python code.

\[code\]

```python

    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import (
        ChatPromptTemplate,
    )
    from langchain.schema.output_parser import StrOutputParser
    from langchain_experimental.utilities import PythonREPL

```

\[/code\]

\[code\]

`

```python

    template = """Write some python code to solve the user's problem.

    Return only python code in Markdown format, e.g.:

    ```python
    ....
    ```"""
    prompt = ChatPromptTemplate.from_messages([("system", template), ("human", "{input}")])

    model = ChatOpenAI()

````

\[/code\]

\[code\]

`

```python

    def _sanitize_output(text: str):
        _, after = text.split("```python")
        return after.split("```")[0]

````

\[/code\]

\[code\]

```python

    chain = prompt | model | StrOutputParser() | _sanitize_output | PythonREPL().run

```

\[/code\]

\[code\]

```python

    chain.invoke({"input": "whats 2 plus 2"})

```

\[/code\]

\[code\]

```python

        Python REPL can execute arbitrary code. Use with caution.

        '4\n'

```

\[/code\]
