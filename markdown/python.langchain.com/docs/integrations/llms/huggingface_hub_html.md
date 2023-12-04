

Skip to main content

On this page

# Hugging Face Hub

> The Hugging Face Hub is a platform with over 120k models, 20k datasets, and 50k demo apps (Spaces), all open source and publicly available, in an online platform where people can easily collaborate
> and build ML together.

This example showcases how to connect to the `Hugging Face Hub` and use different models.

## Installation and Setup​

To use, you should have the `huggingface_hub` python package installed.

```python




    pip install huggingface_hub



```


```python




    # get a token: https://huggingface.co/docs/api-inference/quicktour#get-your-api-token

    from getpass import getpass

    HUGGINGFACEHUB_API_TOKEN = getpass()



```


```python




         ········



```


```python




    import os

    os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN



```


## Prepare Examples​

```python




    from langchain.llms import HuggingFaceHub



```


```python




    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate



```


```python




    question = "Who won the FIFA World Cup in the year 1994? "

    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])



```


## Examples​

Below are some examples of models you can access through the `Hugging Face Hub` integration.

### `Flan`, by `Google`​

```python




    repo_id = "google/flan-t5-xxl"  # See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads for some other options



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    print(llm_chain.run(question))



```


```python




        The FIFA World Cup was held in the year 1994. West Germany won the FIFA World Cup in 1994



```


### `Dolly`, by `Databricks`​

See Databricks organization page for a list of available models.

```python




    repo_id = "databricks/dolly-v2-3b"



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))



```


```python




         First of all, the world cup was won by the Germany. Then the Argentina won the world cup in 2022. So, the Argentina won the world cup in 1994.


        Question: Who



```


### `Camel`, by `Writer`​

See Writer's organization page for a list of available models.

```python




    repo_id = "Writer/camel-5b-hf"  # See https://huggingface.co/Writer for other options



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))



```


### `XGen`, by `Salesforce`​

See more information.

```python




    repo_id = "Salesforce/xgen-7b-8k-base"



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))



```


### `Falcon`, by `Technology Innovation Institute (TII)`​

See more information.

```python




    repo_id = "tiiuae/falcon-40b"



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 64}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))



```


### `InternLM-Chat`, by `Shanghai AI Laboratory`​

See more information.

```python




    repo_id = "internlm/internlm-chat-7b"



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"max_length": 128, "temperature": 0.8}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))



```


### `Qwen`, by `Alibaba Cloud`​

> `Tongyi Qianwen-7B` (`Qwen-7B`) is a model with a scale of 7 billion parameters in the `Tongyi Qianwen` large model series developed by `Alibaba Cloud`. `Qwen-7B` is a large language model based on
> Transformer, which is trained on ultra-large-scale pre-training data.

See more information on HuggingFace of on GitHub.

See here a big example for LangChain integration and Qwen.

```python




    repo_id = "Qwen/Qwen-7B"



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"max_length": 128, "temperature": 0.5}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))



```


### `Yi` series models, by `01.ai`​

> The `Yi` series models are large language models trained from scratch by developers at 01.ai. The first public release contains two bilingual(English/Chinese) base models with the parameter sizes of
> 6B(`Yi-6B`) and 34B(`Yi-34B`). Both of them are trained with 4K sequence length and can be extended to 32K during inference time. The `Yi-6B-200K` and `Yi-34B-200K` are base model with 200K context
> length.

Here we test the Yi-34B model.

```python




    repo_id = "01-ai/Yi-34B"



```


```python




    llm = HuggingFaceHub(
        repo_id=repo_id, model_kwargs={"max_length": 128, "temperature": 0.5}
    )
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    print(llm_chain.run(question))



```
