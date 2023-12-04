

Skip to main content

On this page

# GigaChat

This notebook shows how to use LangChain with GigaChat. To use you need to install `gigachat` python package.

```python




    # !pip install gigachat



```


To get GigaChat credentials you need to create account and get access to API

## Example​

```python




    import os
    from getpass import getpass

    os.environ["GIGACHAT_CREDENTIALS"] = getpass()



```


```python




    from langchain.llms import GigaChat

    llm = GigaChat(verify_ssl_certs=False)



```


```python




    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate

    template = "What is capital of {country}?"

    prompt = PromptTemplate(template=template, input_variables=["country"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    generated = llm_chain.run(country="Russia")
    print(generated)



```


```python




        The capital of Russia is Moscow.



```
