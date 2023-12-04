

Skip to main content

On this page

# GooseAI

`GooseAI` is a fully managed NLP-as-a-Service, delivered via API. GooseAI provides access to these models.

This notebook goes over how to use Langchain with GooseAI.

## Install openai​

The `openai` package is required to use the GooseAI API. Install `openai` using `pip install openai`.

```python




    pip install openai



```


## Imports​

```python




    import os

    from langchain.chains import LLMChain
    from langchain.llms import GooseAI
    from langchain.prompts import PromptTemplate



```


## Set the Environment API Key​

Make sure to get your API key from GooseAI. You are given $10 in free credits to test different models.

```python




    from getpass import getpass

    GOOSEAI_API_KEY = getpass()



```


```python




    os.environ["GOOSEAI_API_KEY"] = GOOSEAI_API_KEY



```


## Create the GooseAI instance​

You can specify different parameters such as the model name, max tokens generated, temperature, etc.

```python




    llm = GooseAI()



```


## Create a Prompt Template​

We will create a prompt template for Question and Answer.

```python




    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])



```


## Initiate the LLMChain​

```python




    llm_chain = LLMChain(prompt=prompt, llm=llm)



```


## Run the LLMChain​

Provide a question and run the LLMChain.

```python




    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

    llm_chain.run(question)



```
