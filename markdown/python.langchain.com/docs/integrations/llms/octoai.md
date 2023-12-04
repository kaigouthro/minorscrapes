

Skip to main content

On this page

# OctoAI

> OctoML is a service with efficient compute. It enables users to integrate their choice of AI models into applications. The `OctoAI` compute service helps you run, tune, and scale AI applications.

This example goes over how to use LangChain to interact with `OctoAI` LLM endpoints

## Setup​

To run our example app, there are four simple steps to take:

  1. Clone the MPT-7B demo template to your OctoAI account by visiting https://octoai.cloud/templates/mpt-7b-demo then clicking "Clone Template."

    1. If you want to use a different LLM model, you can also containerize the model and make a custom OctoAI endpoint yourself, by following Build a Container from Python and Create a Custom Endpoint from a Container
  2. Paste your Endpoint URL in the code cell below

  3. Get an API Token from your OctoAI account page.

  4. Paste your API key in in the code cell below

```python




    import os

    os.environ["OCTOAI_API_TOKEN"] = "OCTOAI_API_TOKEN"
    os.environ["ENDPOINT_URL"] = "https://mpt-7b-demo-f1kzsig6xes9.octoai.run/generate"



```


```python




    from langchain.chains import LLMChain
    from langchain.llms.octoai_endpoint import OctoAIEndpoint
    from langchain.prompts import PromptTemplate



```


## Example​

```python




    template = """Below is an instruction that describes a task. Write a response that appropriately completes the request.\n Instruction:\n{question}\n Response: """
    prompt = PromptTemplate(template=template, input_variables=["question"])



```


```python




    llm = OctoAIEndpoint(
        model_kwargs={
            "max_new_tokens": 200,
            "temperature": 0.75,
            "top_p": 0.95,
            "repetition_penalty": 1,
            "seed": None,
            "stop": [],
        },
    )



```


```python




    question = "Who was leonardo davinci?"

    llm_chain = LLMChain(prompt=prompt, llm=llm)

    llm_chain.run(question)



```


```python




        '\nLeonardo da Vinci was an Italian polymath and painter regarded by many as one of the greatest painters of all time. He is best known for his masterpieces including Mona Lisa, The Last Supper, and The Virgin of the Rocks. He was a draftsman, sculptor, architect, and one of the most important figures in the history of science. Da Vinci flew gliders, experimented with water turbines and windmills, and invented the catapult and a joystick-type human-powered aircraft control. He may have pioneered helicopters. As a scholar, he was interested in anatomy, geology, botany, engineering, mathematics, and astronomy.\nOther painters and patrons claimed to be more talented, but Leonardo da Vinci was an incredibly productive artist, sculptor, engineer, anatomist, and scientist.'



```
