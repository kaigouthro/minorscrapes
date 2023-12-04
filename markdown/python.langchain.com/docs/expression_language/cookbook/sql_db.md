Skip to main content

# Querying a SQL DB

We can replicate our SQLDatabaseChain with Runnables.

\[code\]

```python


    from langchain.prompts import ChatPromptTemplate  
      
    template = """Based on the table schema below, write a SQL query that would answer the user's question:  
    {schema}  
      
    Question: {question}  
    SQL Query:"""  
    prompt = ChatPromptTemplate.from_template(template)  
    
```

\[/code\]

\[code\]

```python


    from langchain.utilities import SQLDatabase  
    
```

\[/code\]

We'll need the Chinook sample DB for this example. There's many places to download it from, e.g. https://database.guide/2-sample-databases-sqlite/

\[code\]

```python


    db = SQLDatabase.from_uri("sqlite:///./Chinook.db")  
    
```

\[/code\]

\[code\]

```python


    def get_schema(_):  
        return db.get_table_info()  
    
```

\[/code\]

\[code\]

```python


    def run_query(query):  
        return db.run(query)  
    
```

\[/code\]

\[code\]

```python


    from langchain.chat_models import ChatOpenAI  
    from langchain.schema.output_parser import StrOutputParser  
    from langchain.schema.runnable import RunnablePassthrough  
      
    model = ChatOpenAI()  
      
    sql_response = (  
        RunnablePassthrough.assign(schema=get_schema)  
        | prompt  
        | model.bind(stop=["\nSQLResult:"])  
        | StrOutputParser()  
    )  
    
```

\[/code\]

\[code\]

```python


    sql_response.invoke({"question": "How many employees are there?"})  
    
```

\[/code\]

\[code\]

```python


        'SELECT COUNT(*) FROM Employee'  
    
```

\[/code\]

\[code\]

```python


    template = """Based on the table schema below, question, sql query, and sql response, write a natural language response:  
    {schema}  
      
    Question: {question}  
    SQL Query: {query}  
    SQL Response: {response}"""  
    prompt_response = ChatPromptTemplate.from_template(template)  
    
```

\[/code\]

\[code\]

```python


    full_chain = (  
        RunnablePassthrough.assign(query=sql_response)  
        | RunnablePassthrough.assign(  
            schema=get_schema,  
            response=lambda x: db.run(x["query"]),  
        )  
        | prompt_response  
        | model  
    )  
    
```

\[/code\]

\[code\]

```python


    full_chain.invoke({"question": "How many employees are there?"})  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content='There are 8 employees.', additional_kwargs={}, example=False)  
    
```

\[/code\]
