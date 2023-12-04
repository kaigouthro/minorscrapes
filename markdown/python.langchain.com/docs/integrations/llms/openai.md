

Skip to main content

# OpenAI

OpenAI offers a spectrum of models with different levels of power suitable for different tasks.

This example goes over how to use LangChain to interact with `OpenAI` models

```python




    # get a token: https://platform.openai.com/account/api-keys

    from getpass import getpass

    OPENAI_API_KEY = getpass()



```


```python




    import os

    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY



```


Should you need to specify your organization ID, you can use the following cell. However, it is not required if you are only part of a single organization or intend to use your default organization.
You can check your default organization here.

To specify your organization, you can use this:

```python




    OPENAI_ORGANIZATION = getpass()

    os.environ["OPENAI_ORGANIZATION"] = OPENAI_ORGANIZATION



```


```python




    from langchain.chains import LLMChain
    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate



```


```python




    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])



```


```python




    llm = OpenAI()



```


If you manually want to specify your OpenAI API key and/or organization ID, you can use the following:

```python




    llm = OpenAI(openai_api_key="YOUR_API_KEY", openai_organization="YOUR_ORGANIZATION_ID")



```


Remove the openai_organization parameter should it not apply to you.

```python




    llm_chain = LLMChain(prompt=prompt, llm=llm)



```


```python




    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

    llm_chain.run(question)



```


```python




        ' Justin Bieber was born in 1994, so the NFL team that won the Super Bowl in 1994 was the Dallas Cowboys.'



```


If you are behind an explicit proxy, you can use the OPENAI_PROXY environment variable to pass through

```python




    os.environ["OPENAI_PROXY"] = "http://proxy.yourcompany.com:8080"



```
