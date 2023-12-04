

Skip to main content

On this page

# Vectorstore

This notebook showcases an agent designed to retrieve information from one or more vectorstores, either with or without sources.

## Create Vectorstores​

```python




    from langchain.embeddings.openai import OpenAIEmbeddings
    from langchain.llms import OpenAI
    from langchain.text_splitter import CharacterTextSplitter
    from langchain.vectorstores import Chroma

    llm = OpenAI(temperature=0)



```


```python




    from langchain.document_loaders import TextLoader

    loader = TextLoader("../../modules/state_of_the_union.txt")
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    state_of_union_store = Chroma.from_documents(
        texts, embeddings, collection_name="state-of-union"
    )



```


```python




        Running Chroma using direct local API.
        Using DuckDB in-memory for database. Data will be transient.



```


```python




    from langchain.document_loaders import WebBaseLoader

    loader = WebBaseLoader("https://beta.ruff.rs/docs/faq/")
    docs = loader.load()
    ruff_texts = text_splitter.split_documents(docs)
    ruff_store = Chroma.from_documents(ruff_texts, embeddings, collection_name="ruff")



```


```python




        Running Chroma using direct local API.
        Using DuckDB in-memory for database. Data will be transient.



```


## Initialize Toolkit and Agent​

First, we'll create an agent with a single vectorstore.

```python




    from langchain.agents.agent_toolkits import (
        VectorStoreInfo,
        VectorStoreToolkit,
        create_vectorstore_agent,
    )

    vectorstore_info = VectorStoreInfo(
        name="state_of_union_address",
        description="the most recent state of the Union adress",
        vectorstore=state_of_union_store,
    )
    toolkit = VectorStoreToolkit(vectorstore_info=vectorstore_info)
    agent_executor = create_vectorstore_agent(llm=llm, toolkit=toolkit, verbose=True)



```


## Examples​

```python




    agent_executor.run(
        "What did biden say about ketanji brown jackson in the state of the union address?"
    )



```


```python






        > Entering new AgentExecutor chain...
         I need to find the answer in the state of the union address
        Action: state_of_union_address
        Action Input: What did biden say about ketanji brown jackson
        Observation:  Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.
        Thought: I now know the final answer
        Final Answer: Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.

        > Finished chain.





        "Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence."



```


```python




    agent_executor.run(
        "What did biden say about ketanji brown jackson in the state of the union address? List the source."
    )



```


```python






        > Entering new AgentExecutor chain...
         I need to use the state_of_union_address_with_sources tool to answer this question.
        Action: state_of_union_address_with_sources
        Action Input: What did biden say about ketanji brown jackson
        Observation: {"answer": " Biden said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson to the United States Supreme Court, and that she is one of the nation's top legal minds who will continue Justice Breyer's legacy of excellence.\n", "sources": "../../state_of_the_union.txt"}
        Thought: I now know the final answer
        Final Answer: Biden said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson to the United States Supreme Court, and that she is one of the nation's top legal minds who will continue Justice Breyer's legacy of excellence. Sources: ../../state_of_the_union.txt

        > Finished chain.





        "Biden said that he nominated Circuit Court of Appeals Judge Ketanji Brown Jackson to the United States Supreme Court, and that she is one of the nation's top legal minds who will continue Justice Breyer's legacy of excellence. Sources: ../../state_of_the_union.txt"



```


## Multiple Vectorstores​

We can also easily use this initialize an agent with multiple vectorstores and use the agent to route between them. To do this. This agent is optimized for routing, so it is a different toolkit and
initializer.

```python




    from langchain.agents.agent_toolkits import (
        VectorStoreInfo,
        VectorStoreRouterToolkit,
        create_vectorstore_router_agent,
    )



```


```python




    ruff_vectorstore_info = VectorStoreInfo(
        name="ruff",
        description="Information about the Ruff python linting library",
        vectorstore=ruff_store,
    )
    router_toolkit = VectorStoreRouterToolkit(
        vectorstores=[vectorstore_info, ruff_vectorstore_info], llm=llm
    )
    agent_executor = create_vectorstore_router_agent(
        llm=llm, toolkit=router_toolkit, verbose=True
    )



```


## Examples​

```python




    agent_executor.run(
        "What did biden say about ketanji brown jackson in the state of the union address?"
    )



```


```python






        > Entering new AgentExecutor chain...
         I need to use the state_of_union_address tool to answer this question.
        Action: state_of_union_address
        Action Input: What did biden say about ketanji brown jackson
        Observation:  Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.
        Thought: I now know the final answer
        Final Answer: Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence.

        > Finished chain.





        "Biden said that Ketanji Brown Jackson is one of the nation's top legal minds and that she will continue Justice Breyer's legacy of excellence."



```


```python




    agent_executor.run("What tool does ruff use to run over Jupyter Notebooks?")



```


```python






        > Entering new AgentExecutor chain...
         I need to find out what tool ruff uses to run over Jupyter Notebooks
        Action: ruff
        Action Input: What tool does ruff use to run over Jupyter Notebooks?
        Observation:  Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.html
        Thought: I now know the final answer
        Final Answer: Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.html

        > Finished chain.





        'Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.html'



```


```python




    agent_executor.run(
        "What tool does ruff use to run over Jupyter Notebooks? Did the president mention that tool in the state of the union?"
    )



```


```python






        > Entering new AgentExecutor chain...
         I need to find out what tool ruff uses and if the president mentioned it in the state of the union.
        Action: ruff
        Action Input: What tool does ruff use to run over Jupyter Notebooks?
        Observation:  Ruff is integrated into nbQA, a tool for running linters and code formatters over Jupyter Notebooks. After installing ruff and nbqa, you can run Ruff over a notebook like so: > nbqa ruff Untitled.html
        Thought: I need to find out if the president mentioned nbQA in the state of the union.
        Action: state_of_union_address
        Action Input: Did the president mention nbQA in the state of the union?
        Observation:  No, the president did not mention nbQA in the state of the union.
        Thought: I now know the final answer.
        Final Answer: No, the president did not mention nbQA in the state of the union.

        > Finished chain.





        'No, the president did not mention nbQA in the state of the union.'



```
