

Skip to main content

On this page

# Azure ML Endpoint

> Azure Machine Learning is a platform used to build, train, and deploy machine learning models. Users can explore the types of models to deploy in the Model Catalog, which provides Azure Foundation
> Models and OpenAI Models. `Azure Foundation Models` include various open-source models and popular Hugging Face models. Users can also import models of their liking into AzureML.
>
> Azure Machine Learning Online Endpoints. After you train machine learning models or pipelines, you need to deploy them to production so that others can use them for inference. Inference is the
> process of applying new input data to the machine learning model or pipeline to generate outputs. While these outputs are typically referred to as "predictions," inferencing can be used to generate
> outputs for other machine learning tasks, such as classification and clustering. In `Azure Machine Learning`, you perform inferencing by using endpoints and deployments. `Endpoints` and
> `Deployments` allow you to decouple the interface of your production workload from the implementation that serves it.

This notebook goes over how to use a chat model hosted on an `Azure Machine Learning Endpoint`.

[code]
```python




    from langchain.chat_models.azureml_endpoint import AzureMLChatOnlineEndpoint  
    


```
[/code]


## Set up​

To use the wrapper, you must deploy a model on AzureML and obtain the following parameters:

  * `endpoint_api_key`: The API key provided by the endpoint
  * `endpoint_url`: The REST endpoint url provided by the endpoint

## Content Formatter​

The `content_formatter` parameter is a handler class for transforming the request and response of an AzureML endpoint to match with required schema. Since there are a wide range of models in the model
catalog, each of which may process data differently from one another, a `ContentFormatterBase` class is provided to allow users to transform data to their liking. The following content formatters are
provided:

  * `LLamaContentFormatter`: Formats request and response data for LLaMa2-chat

[code]
```python




    from langchain.chat_models.azureml_endpoint import LlamaContentFormatter  
    from langchain.schema import HumanMessage  
      
    chat = AzureMLChatOnlineEndpoint(  
        endpoint_url="https://<your-endpoint>.<your_region>.inference.ml.azure.com/score",  
        endpoint_api_key="my-api-key",  
        content_formatter=LlamaContentFormatter,  
    )  
    response = chat(  
        messages=[HumanMessage(content="Will the Collatz conjecture ever be solved?")]  
    )  
    response  
    


```
[/code]


[code]
```python




        AIMessage(content='  The Collatz Conjecture is one of the most famous unsolved problems in mathematics, and it has been the subject of much study and research for many years. While it is impossible to predict with certainty whether the conjecture will ever be solved, there are several reasons why it is considered a challenging and important problem:\n\n1. Simple yet elusive: The Collatz Conjecture is a deceptively simple statement that has proven to be extraordinarily difficult to prove or disprove. Despite its simplicity, the conjecture has eluded some of the brightest minds in mathematics, and it remains one of the most famous open problems in the field.\n2. Wide-ranging implications: The Collatz Conjecture has far-reaching implications for many areas of mathematics, including number theory, algebra, and analysis. A solution to the conjecture could have significant impacts on these fields and potentially lead to new insights and discoveries.\n3. Computational evidence: While the conjecture remains unproven, extensive computational evidence supports its validity. In fact, no counterexample to the conjecture has been found for any starting value up to 2^64 (a number', additional_kwargs={}, example=False)  
    


```
[/code]


