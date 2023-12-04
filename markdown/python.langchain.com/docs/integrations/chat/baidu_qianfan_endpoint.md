

Skip to main content

On this page

# Baidu Qianfan

Baidu AI Cloud Qianfan Platform is a one-stop large model development and service operation platform for enterprise developers. Qianfan not only provides including the model of Wenxin Yiyan (ERNIE-
Bot) and the third-party open-source models, but also provides various AI development tools and the whole set of development environment, which facilitates customers to use and develop large model
applications easily.

Basically, those model are split into the following type:

  * Embedding
  * Chat
  * Completion

In this notebook, we will introduce how to use langchain with Qianfan mainly in `Chat` corresponding to the package `langchain/chat_models` in langchain:

## API Initialization​

To use the LLM services based on Baidu Qianfan, you have to initialize these parameters:

You could either choose to init the AK,SK in environment variables or init params:

[code]
```python




    export QIANFAN_AK=XXX  
    export QIANFAN_SK=XXX  
    


```
[/code]


## Current supported models:​

  * ERNIE-Bot-turbo (default models)
  * ERNIE-Bot
  * BLOOMZ-7B
  * Llama-2-7b-chat
  * Llama-2-13b-chat
  * Llama-2-70b-chat
  * Qianfan-BLOOMZ-7B-compressed
  * Qianfan-Chinese-Llama-2-7B
  * ChatGLM2-6B-32K
  * AquilaChat-7B

[code]
```python




    """For basic init and call"""  
    import os  
      
    from langchain.chat_models import QianfanChatEndpoint  
    from langchain.chat_models.base import HumanMessage  
      
    os.environ["QIANFAN_AK"] = "your_ak"  
    os.environ["QIANFAN_SK"] = "your_sk"  
      
    chat = QianfanChatEndpoint(  
        streaming=True,  
    )  
    res = chat([HumanMessage(content="write a funny joke")])  
    


```
[/code]


[code]
```python




        [INFO] [09-15 20:00:29] logging.py:55 [t:139698882193216]: requesting llm api endpoint: /chat/eb-instant  
    


```
[/code]


[code]
```python




    from langchain.chat_models import QianfanChatEndpoint  
    from langchain.schema import HumanMessage  
      
    chatLLM = QianfanChatEndpoint(  
        streaming=True,  
    )  
    res = chatLLM.stream([HumanMessage(content="hi")], streaming=True)  
    for r in res:  
        print("chat resp:", r)  
      
      
    async def run_aio_generate():  
        resp = await chatLLM.agenerate(  
            messages=[[HumanMessage(content="write a 20 words sentence about sea.")]]  
        )  
        print(resp)  
      
      
    await run_aio_generate()  
      
      
    async def run_aio_stream():  
        async for res in chatLLM.astream(  
            [HumanMessage(content="write a 20 words sentence about sea.")]  
        ):  
            print("astream", res)  
      
      
    await run_aio_stream()  
    


```
[/code]


[code]
```python




        [INFO] [09-15 20:00:36] logging.py:55 [t:139698882193216]: requesting llm api endpoint: /chat/eb-instant  
        [INFO] [09-15 20:00:37] logging.py:55 [t:139698882193216]: async requesting llm api endpoint: /chat/eb-instant  
      
      
        chat resp: content='您好，您似乎输入' additional_kwargs={} example=False  
        chat resp: content='了一个话题标签，请问需要我帮您找到什么资料或者帮助您解答什么问题吗？' additional_kwargs={} example=False  
        chat resp: content='' additional_kwargs={} example=False  
      
      
        [INFO] [09-15 20:00:39] logging.py:55 [t:139698882193216]: async requesting llm api endpoint: /chat/eb-instant  
      
      
        generations=[[ChatGeneration(text="The sea is a vast expanse of water that covers much of the Earth's surface. It is a source of travel, trade, and entertainment, and is also a place of scientific exploration and marine conservation. The sea is an important part of our world, and we should cherish and protect it.", generation_info={'finish_reason': 'finished'}, message=AIMessage(content="The sea is a vast expanse of water that covers much of the Earth's surface. It is a source of travel, trade, and entertainment, and is also a place of scientific exploration and marine conservation. The sea is an important part of our world, and we should cherish and protect it.", additional_kwargs={}, example=False))]] llm_output={} run=[RunInfo(run_id=UUID('d48160a6-5960-4c1d-8a0e-90e6b51a209b'))]  
        astream content='The sea is a vast' additional_kwargs={} example=False  
        astream content=' expanse of water, a place of mystery and adventure. It is the source of many cultures and civilizations, and a center of trade and exploration. The sea is also a source of life and beauty, with its unique marine life and diverse' additional_kwargs={} example=False  
        astream content=' coral reefs. Whether you are swimming, diving, or just watching the sea, it is a place that captivates the imagination and transforms the spirit.' additional_kwargs={} example=False  
    


```
[/code]


## Use different models in Qianfan​

In the case you want to deploy your own model based on Ernie Bot or third-party open-source model, you could follow these steps:

  *     1. （Optional, if the model are included in the default models, skip it）Deploy your model in Qianfan Console, get your own customized deploy endpoint.
  *     2. Set up the field called `endpoint` in the initialization:

[code]
```python




    chatBloom = QianfanChatEndpoint(  
        streaming=True,  
        model="BLOOMZ-7B",  
    )  
    res = chatBloom([HumanMessage(content="hi")])  
    print(res)  
    


```
[/code]


[code]
```python




        [INFO] [09-15 20:00:50] logging.py:55 [t:139698882193216]: requesting llm api endpoint: /chat/bloomz_7b1  
      
      
        content='你好！很高兴见到你。' additional_kwargs={} example=False  
    


```
[/code]


## Model Params:​

For now, only `ERNIE-Bot` and `ERNIE-Bot-turbo` support model params below, we might support more models in the future.

  * temperature
  * top_p
  * penalty_score

[code]
```python




    res = chat.stream(  
        [HumanMessage(content="hi")],  
        **{"top_p": 0.4, "temperature": 0.1, "penalty_score": 1},  
    )  
      
    for r in res:  
        print(r)  
    


```
[/code]


[code]
```python




        [INFO] [09-15 20:00:57] logging.py:55 [t:139698882193216]: requesting llm api endpoint: /chat/eb-instant  
      
      
        content='您好，您似乎输入' additional_kwargs={} example=False  
        content='了一个文本字符串，但并没有给出具体的问题或场景。' additional_kwargs={} example=False  
        content='如果您能提供更多信息，我可以更好地回答您的问题。' additional_kwargs={} example=False  
        content='' additional_kwargs={} example=False  
    


```
[/code]


