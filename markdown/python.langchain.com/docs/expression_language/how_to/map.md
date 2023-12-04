

Skip to main content

On this page

# Parallelize steps

RunnableParallel (aka. RunnableMap) makes it easy to execute multiple Runnables in parallel, and to return the output of these Runnables as a map.

```python




    from langchain.chat_models import ChatOpenAI
    from langchain.prompts import ChatPromptTemplate
    from langchain.schema.runnable import RunnableParallel

    model = ChatOpenAI()
    joke_chain = ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
    poem_chain = (
        ChatPromptTemplate.from_template("write a 2-line poem about {topic}") | model
    )

    map_chain = RunnableParallel(joke=joke_chain, poem=poem_chain)

    map_chain.invoke({"topic": "bear"})



```


```python




        {'joke': AIMessage(content="Why don't bears wear shoes? \n\nBecause they have bear feet!", additional_kwargs={}, example=False),
         'poem': AIMessage(content="In woodland depths, bear prowls with might,\nSilent strength, nature's sovereign, day and night.", additional_kwargs={}, example=False)}



```


## Manipulating outputs/inputs​

Maps can be useful for manipulating the output of one Runnable to match the input format of the next Runnable in a sequence.

```python




    from langchain.embeddings import OpenAIEmbeddings
    from langchain.schema.output_parser import StrOutputParser
    from langchain.schema.runnable import RunnablePassthrough
    from langchain.vectorstores import FAISS

    vectorstore = FAISS.from_texts(
        ["harrison worked at kensho"], embedding=OpenAIEmbeddings()
    )
    retriever = vectorstore.as_retriever()
    template = """Answer the question based only on the following context:
    {context}

    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    retrieval_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )

    retrieval_chain.invoke("where did harrison work?")



```


```python




        'Harrison worked at Kensho.'



```


Here the input to prompt is expected to be a map with keys "context" and "question". The user input is just the question. So we need to get the context using our retriever and passthrough the user
input under the "question" key.

Note that when composing a RunnableParallel with another Runnable we don't even need to wrap our dictionary in the RunnableParallel class — the type conversion is handled for us.

## Parallelism​

RunnableParallel are also useful for running independent processes in parallel, since each Runnable in the map is executed in parallel. For example, we can see our earlier `joke_chain`, `poem_chain`
and `map_chain` all have about the same runtime, even though `map_chain` executes both of the other two.

```python




    joke_chain.invoke({"topic": "bear"})



```


```python




        958 ms ± 402 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)



```


```python




    poem_chain.invoke({"topic": "bear"})



```


```python




        1.22 s ± 508 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)



```


```python




    map_chain.invoke({"topic": "bear"})



```


```python




        1.15 s ± 119 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)



```
