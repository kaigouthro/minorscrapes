

Skip to main content

On this page

# Bedrock Chat

> Amazon Bedrock is a fully managed service that offers a choice of high-performing foundation models (FMs) from leading AI companies like `AI21 Labs`, `Anthropic`, `Cohere`, `Meta`, `Stability AI`,
> and `Amazon` via a single API, along with a broad set of capabilities you need to build generative AI applications with security, privacy, and responsible AI. Using `Amazon Bedrock`, you can easily
> experiment with and evaluate top FMs for your use case, privately customize them with your data using techniques such as fine-tuning and `Retrieval Augmented Generation` (`RAG`), and build agents
> that execute tasks using your enterprise systems and data sources. Since `Amazon Bedrock` is serverless, you don't have to manage any infrastructure, and you can securely integrate and deploy
> generative AI capabilities into your applications using the AWS services you are already familiar with.
[code]
```python




    %pip install boto3  
    


```
[/code]


[code]
```python




    from langchain.chat_models import BedrockChat  
    from langchain.schema import HumanMessage  
    


```
[/code]


[code]
```python




    chat = BedrockChat(model_id="anthropic.claude-v2", model_kwargs={"temperature": 0.1})  
    


```
[/code]


[code]
```python




    messages = [  
        HumanMessage(  
            content="Translate this sentence from English to French. I love programming."  
        )  
    ]  
    chat(messages)  
    


```
[/code]


[code]
```python




        AIMessage(content=" Voici la traduction en français : J'adore programmer.", additional_kwargs={}, example=False)  
    


```
[/code]


### For BedrockChat with Streaming​

[code]
```python




    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
      
    chat = BedrockChat(  
        model_id="anthropic.claude-v2",  
        streaming=True,  
        callbacks=[StreamingStdOutCallbackHandler()],  
        model_kwargs={"temperature": 0.1},  
    )  
    


```
[/code]


[code]
```python




    messages = [  
        HumanMessage(  
            content="Translate this sentence from English to French. I love programming."  
        )  
    ]  
    chat(messages)  
    


```
[/code]


