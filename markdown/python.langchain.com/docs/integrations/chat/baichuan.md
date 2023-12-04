

Skip to main content

On this page

# Baichuan Chat

Baichuan chat models API by Baichuan Intelligent Technology. For more information, see https://platform.baichuan-ai.com/docs/api

[code]
```python




    from langchain.chat_models import ChatBaichuan  
    from langchain.schema import HumanMessage  
    


```
[/code]


[code]
```python




    chat = ChatBaichuan(  
        baichuan_api_key="YOUR_API_KEY", baichuan_secret_key="YOUR_SECRET_KEY"  
    )  
    


```
[/code]


or you can set `api_key` and `secret_key` in your environment variables

[code]
```python




    export BAICHUAN_API_KEY=YOUR_API_KEY  
    export BAICHUAN_SECRET_KEY=YOUR_SECRET_KEY  
    


```
[/code]


[code]
```python




    chat([HumanMessage(content="我日薪8块钱，请问在闰年的二月，我月薪多少")])  
    


```
[/code]


[code]
```python




        AIMessage(content='首先，我们需要确定闰年的二月有多少天。闰年的二月有29天。\n\n然后，我们可以计算你的月薪：\n\n日薪 = 月薪 / (当月天数)\n\n所以，你的月薪 = 日薪 * 当月天数\n\n将数值代入公式：\n\n月薪 = 8元/天 * 29天 = 232元\n\n因此，你在闰年的二月的月薪是232元。')  
    


```
[/code]


## For ChatBaichuan with Streaming​

[code]
```python




    chat = ChatBaichuan(  
        baichuan_api_key="YOUR_API_KEY",  
        baichuan_secret_key="YOUR_SECRET_KEY",  
        streaming=True,  
    )  
    


```
[/code]


[code]
```python




    chat([HumanMessage(content="我日薪8块钱，请问在闰年的二月，我月薪多少")])  
    


```
[/code]


[code]
```python




        AIMessageChunk(content='首先，我们需要确定闰年的二月有多少天。闰年的二月有29天。\n\n然后，我们可以计算你的月薪：\n\n日薪 = 月薪 / (当月天数)\n\n所以，你的月薪 = 日薪 * 当月天数\n\n将数值代入公式：\n\n月薪 = 8元/天 * 29天 = 232元\n\n因此，你在闰年的二月的月薪是232元。')  
    


```
[/code]


