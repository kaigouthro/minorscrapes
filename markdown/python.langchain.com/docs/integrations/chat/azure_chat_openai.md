

Skip to main content

On this page

# Azure OpenAI

> Azure OpenAI Service provides REST API access to OpenAI's powerful language models including the GPT-4, GPT-3.5-Turbo, and Embeddings model series. These models can be easily adapted to your
> specific task including but not limited to content generation, summarization, semantic search, and natural language to code translation. Users can access the service through REST APIs, Python SDK,
> or a web-based interface in the Azure OpenAI Studio.

This notebook goes over how to connect to an Azure-hosted OpenAI endpoint. We recommend having version `openai>=1` installed.

[code]
```python




    import os  
      
    from langchain.chat_models import AzureChatOpenAI  
    from langchain.schema import HumanMessage  
    


```
[/code]


[code]
```python




    os.environ["AZURE_OPENAI_API_KEY"] = "..."  
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://<your-endpoint>.openai.azure.com/"  
    


```
[/code]


[code]
```python




    model = AzureChatOpenAI(  
        openai_api_version="2023-05-15",  
        azure_deployment="your-deployment-name",  
    )  
    


```
[/code]


[code]
```python




    message = HumanMessage(  
        content="Translate this sentence from English to French. I love programming."  
    )  
    model([message])  
    


```
[/code]


[code]
```python




        AIMessage(content="J'adore la programmation.")  
    


```
[/code]


## Model Version​

Azure OpenAI responses contain `model` property, which is name of the model used to generate the response. However unlike native OpenAI responses, it does not contain the version of the model, which
is set on the deployment in Azure. This makes it tricky to know which version of the model was used to generate the response, which as result can lead to e.g. wrong total cost calculation with
`OpenAICallbackHandler`.

To solve this problem, you can pass `model_version` parameter to `AzureChatOpenAI` class, which will be added to the model name in the llm output. This way you can easily distinguish between different
versions of the model.

[code]
```python




    from langchain.callbacks import get_openai_callback  
    


```
[/code]


[code]
```python




    model = AzureChatOpenAI(  
        openai_api_version="2023-05-15",  
        azure_deployment="gpt-35-turbo",  # in Azure, this deployment has version 0613 - input and output tokens are counted separately  
    )  
    with get_openai_callback() as cb:  
        model([message])  
        print(  
            f"Total Cost (USD): ${format(cb.total_cost, '.6f')}"  
        )  # without specifying the model version, flat-rate 0.002 USD per 1k input and output tokens is used  
    


```
[/code]


We can provide the model version to `AzureChatOpenAI` constructor. It will get appended to the model name returned by Azure OpenAI and cost will be counted correctly.

[code]
```python




    model0613 = AzureChatOpenAI(  
        openai_api_version="2023-05-15",  
        deployment_name="gpt-35-turbo",  
        model_version="0613",  
    )  
    with get_openai_callback() as cb:  
        model0613([message])  
        print(f"Total Cost (USD): ${format(cb.total_cost, '.6f')}")  
    


```
[/code]


[code]
```python




        Total Cost (USD): $0.000044  
    


```
[/code]


