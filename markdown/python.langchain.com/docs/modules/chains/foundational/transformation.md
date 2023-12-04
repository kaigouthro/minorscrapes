

Skip to main content

On this page

# Transformation

Often we want to transform inputs as they are passed from one component to another.

As an example, we will create a dummy transformation that takes in a super long text, filters the text to only the first 3 paragraphs, and then passes that into a chain to summarize those.

```python




    from langchain.prompts import PromptTemplate

    prompt = PromptTemplate.from_template(
        """Summarize this text:

    {output_text}

    Summary:"""
    )



```


```python




    with open("../../state_of_the_union.txt") as f:
        state_of_the_union = f.read()



```


## Using LCEL​

With LCEL this is trivial, since we can add functions in any `RunnableSequence`.

```python




    from langchain.chat_models import ChatOpenAI
    from langchain.schema import StrOutputParser

    runnable = (
        {"output_text": lambda text: "\n\n".join(text.split("\n\n")[:3])}
        | prompt
        | ChatOpenAI()
        | StrOutputParser()
    )
    runnable.invoke(state_of_the_union)



```


```python




        'The speaker acknowledges the presence of important figures in the government and addresses the audience as fellow Americans. They highlight the impact of COVID-19 on keeping people apart in the previous year but express joy in being able to come together again. The speaker emphasizes the unity of Democrats, Republicans, and Independents as Americans.'



```


## [Legacy] TransformationChain​

This is a legacy class, using LCEL as shown above is preffered.

This notebook showcases using a generic transformation chain.

```python




    from langchain.chains import LLMChain, SimpleSequentialChain, TransformChain
    from langchain.llms import OpenAI



```


```python




    def transform_func(inputs: dict) -> dict:
        text = inputs["text"]
        shortened_text = "\n\n".join(text.split("\n\n")[:3])
        return {"output_text": shortened_text}


    transform_chain = TransformChain(
        input_variables=["text"], output_variables=["output_text"], transform=transform_func
    )



```


```python




    template = """Summarize this text:

    {output_text}

    Summary:"""
    prompt = PromptTemplate(input_variables=["output_text"], template=template)
    llm_chain = LLMChain(llm=OpenAI(), prompt=prompt)



```


```python




    sequential_chain = SimpleSequentialChain(chains=[transform_chain, llm_chain])



```


```python




    sequential_chain.run(state_of_the_union)



```


```python




        ' In an address to the nation, the speaker acknowledges the hardships of the past year due to the COVID-19 pandemic, but emphasizes that regardless of political affiliation, all Americans can come together.'



```
