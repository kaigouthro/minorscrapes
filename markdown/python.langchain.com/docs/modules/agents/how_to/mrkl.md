

Skip to main content

On this page

# Replicating MRKL

This walkthrough demonstrates how to replicate the MRKL system using agents.

This uses the example Chinook database. To set it up, follow the instructions on https://database.guide/2-sample-databases-sqlite/ and place the `.db` file in a "notebooks" folder at the root of this
repository.

[code]
```python




    from langchain.chains import LLMMathChain  
    from langchain.llms import OpenAI  
    from langchain.utilities import SerpAPIWrapper  
    from langchain.utilities import SQLDatabase  
    from langchain_experimental.sql import SQLDatabaseChain  
    from langchain.agents import initialize_agent, Tool  
    from langchain.agents import AgentType  
    


```
[/code]


[code]
```python




    llm = OpenAI(temperature=0)  
    search = SerpAPIWrapper()  
    llm_math_chain = LLMMathChain(llm=llm, verbose=True)  
    db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")  
    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)  
    tools = [  
        Tool(  
            name="Search",  
            func=search.run,  
            description="useful for when you need to answer questions about current events. You should ask targeted questions"  
        ),  
        Tool(  
            name="Calculator",  
            func=llm_math_chain.run,  
            description="useful for when you need to answer questions about math"  
        ),  
        Tool(  
            name="FooBar DB",  
            func=db_chain.run,  
            description="useful for when you need to answer questions about FooBar. Input should be in the form of a question containing full context"  
        )  
    ]  
    


```
[/code]


[code]
```python




    mrkl = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)  
    


```
[/code]


[code]
```python




    mrkl.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")  
    


```
[/code]


[code]
```python




        > Entering new AgentExecutor chain...  
         I need to find out who Leo DiCaprio's girlfriend is and then calculate her age raised to the 0.43 power.  
        Action: Search  
        Action Input: "Who is Leo DiCaprio's girlfriend?"  
        Observation: DiCaprio met actor Camila Morrone in December 2017, when she was 20 and he was 43. They were spotted at Coachella and went on multiple vacations together. Some reports suggested that DiCaprio was ready to ask Morrone to marry him. The couple made their red carpet debut at the 2020 Academy Awards.  
        Thought: I need to calculate Camila Morrone's age raised to the 0.43 power.  
        Action: Calculator  
        Action Input: 21^0.43  
      
        > Entering new LLMMathChain chain...  
        21^0.43  
        ```text  
        21**0.43  
        ```  
        ...numexpr.evaluate("21**0.43")...  
      
        Answer: 3.7030049853137306  
        > Finished chain.  
      
        Observation: Answer: 3.7030049853137306  
        Thought: I now know the final answer.  
        Final Answer: Camila Morrone is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is 3.7030049853137306.  
      
        > Finished chain.  
      
      
        "Camila Morrone is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is 3.7030049853137306."  
    


```
[/code]


[code]
```python




    mrkl.run("What is the full name of the artist who recently released an album called 'The Storm Before the Calm' and are they in the FooBar database? If so, what albums of theirs are in the FooBar database?")  
    


```
[/code]


[code]
```python




        > Entering new AgentExecutor chain...  
         I need to find out the artist's full name and then search the FooBar database for their albums.  
        Action: Search  
        Action Input: "The Storm Before the Calm" artist  
        Observation: The Storm Before the Calm (stylized in all lowercase) is the tenth (and eighth international) studio album by Canadian-American singer-songwriter Alanis Morissette, released June 17, 2022, via Epiphany Music and Thirty Tigers, as well as by RCA Records in Europe.  
        Thought: I now need to search the FooBar database for Alanis Morissette's albums.  
        Action: FooBar DB  
        Action Input: What albums by Alanis Morissette are in the FooBar database?  
      
        > Entering new SQLDatabaseChain chain...  
        What albums by Alanis Morissette are in the FooBar database?  
        SQLQuery:  
      
        /Users/harrisonchase/workplace/langchain/langchain/sql_database.py:191: SAWarning: Dialect sqlite+pysqlite does *not* support Decimal objects natively, and SQLAlchemy must convert from floating point - rounding errors and other issues may occur. Please consider storing Decimal numbers as strings or integers on this platform for lossless storage.  
          sample_rows = connection.execute(command)  
      
      
         SELECT "Title" FROM "Album" INNER JOIN "Artist" ON "Album"."ArtistId" = "Artist"."ArtistId" WHERE "Name" = 'Alanis Morissette' LIMIT 5;  
        SQLResult: [('Jagged Little Pill',)]  
        Answer: The albums by Alanis Morissette in the FooBar database are Jagged Little Pill.  
        > Finished chain.  
      
        Observation:  The albums by Alanis Morissette in the FooBar database are Jagged Little Pill.  
        Thought: I now know the final answer.  
        Final Answer: The artist who released the album 'The Storm Before the Calm' is Alanis Morissette and the albums of hers in the FooBar database are Jagged Little Pill.  
      
        > Finished chain.  
      
      
        "The artist who released the album 'The Storm Before the Calm' is Alanis Morissette and the albums of hers in the FooBar database are Jagged Little Pill."  
    


```
[/code]


## Using a Chat Model​

[code]
```python




    from langchain.chat_models import ChatOpenAI  
      
    llm = ChatOpenAI(temperature=0)  
    llm1 = OpenAI(temperature=0)  
    search = SerpAPIWrapper()  
    llm_math_chain = LLMMathChain(llm=llm1, verbose=True)  
    db = SQLDatabase.from_uri("sqlite:///../../../../../notebooks/Chinook.db")  
    db_chain = SQLDatabaseChain.from_llm(llm1, db, verbose=True)  
    tools = [  
        Tool(  
            name="Search",  
            func=search.run,  
            description="useful for when you need to answer questions about current events. You should ask targeted questions"  
        ),  
        Tool(  
            name="Calculator",  
            func=llm_math_chain.run,  
            description="useful for when you need to answer questions about math"  
        ),  
        Tool(  
            name="FooBar DB",  
            func=db_chain.run,  
            description="useful for when you need to answer questions about FooBar. Input should be in the form of a question containing full context"  
        )  
    ]  
    


```
[/code]


[code]
```python




    mrkl = initialize_agent(tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)  
    


```
[/code]


[code]
```python




    mrkl.run("Who is Leo DiCaprio's girlfriend? What is her current age raised to the 0.43 power?")  
    


```
[/code]


[code]
```python




        > Entering new AgentExecutor chain...  
        Thought: The first question requires a search, while the second question requires a calculator.  
        Action:  
        ```  
        {  
          "action": "Search",  
          "action_input": "Leo DiCaprio girlfriend"  
        }  
        ```  
      
        Observation: Gigi Hadid: 2022 Leo and Gigi were first linked back in September 2022, when a source told Us Weekly that Leo had his “sights set" on her (alarming way to put it, but okay).  
        Thought:For the second question, I need to calculate the age raised to the 0.43 power. I will use the calculator tool.  
        Action:  
        ```  
        {  
          "action": "Calculator",  
          "action_input": "((2022-1995)^0.43)"  
        }  
        ```  
      
      
        > Entering new LLMMathChain chain...  
        ((2022-1995)^0.43)  
        ```text  
        (2022-1995)**0.43  
        ```  
        ...numexpr.evaluate("(2022-1995)**0.43")...  
      
        Answer: 4.125593352125936  
        > Finished chain.  
      
        Observation: Answer: 4.125593352125936  
        Thought:I now know the final answer.  
        Final Answer: Gigi Hadid is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is approximately 4.13.  
      
        > Finished chain.  
      
      
        "Gigi Hadid is Leo DiCaprio's girlfriend and her current age raised to the 0.43 power is approximately 4.13."  
    


```
[/code]


[code]
```python




    mrkl.run("What is the full name of the artist who recently released an album called 'The Storm Before the Calm' and are they in the FooBar database? If so, what albums of theirs are in the FooBar database?")  
    


```
[/code]


[code]
```python




        > Entering new AgentExecutor chain...  
        Question: What is the full name of the artist who recently released an album called 'The Storm Before the Calm' and are they in the FooBar database? If so, what albums of theirs are in the FooBar database?  
        Thought: I should use the Search tool to find the answer to the first part of the question and then use the FooBar DB tool to find the answer to the second part.  
        Action:  
        ```  
        {  
          "action": "Search",  
          "action_input": "Who recently released an album called 'The Storm Before the Calm'"  
        }  
        ```  
      
        Observation: Alanis Morissette  
        Thought:Now that I know the artist's name, I can use the FooBar DB tool to find out if they are in the database and what albums of theirs are in it.  
        Action:  
        ```  
        {  
          "action": "FooBar DB",  
          "action_input": "What albums does Alanis Morissette have in the database?"  
        }  
        ```  
      
      
        > Entering new SQLDatabaseChain chain...  
        What albums does Alanis Morissette have in the database?  
        SQLQuery:  
      
        /Users/harrisonchase/workplace/langchain/langchain/sql_database.py:191: SAWarning: Dialect sqlite+pysqlite does *not* support Decimal objects natively, and SQLAlchemy must convert from floating point - rounding errors and other issues may occur. Please consider storing Decimal numbers as strings or integers on this platform for lossless storage.  
          sample_rows = connection.execute(command)  
      
      
         SELECT "Title" FROM "Album" WHERE "ArtistId" IN (SELECT "ArtistId" FROM "Artist" WHERE "Name" = 'Alanis Morissette') LIMIT 5;  
        SQLResult: [('Jagged Little Pill',)]  
        Answer: Alanis Morissette has the album Jagged Little Pill in the database.  
        > Finished chain.  
      
        Observation:  Alanis Morissette has the album Jagged Little Pill in the database.  
        Thought:The artist Alanis Morissette is in the FooBar database and has the album Jagged Little Pill in it.  
        Final Answer: Alanis Morissette is in the FooBar database and has the album Jagged Little Pill in it.  
      
        > Finished chain.  
      
      
        'Alanis Morissette is in the FooBar database and has the album Jagged Little Pill in it.'  
    


```
[/code]


