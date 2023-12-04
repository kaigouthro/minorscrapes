

Skip to main content

# EverlyAI

> EverlyAI allows you to run your ML models at scale in the cloud. It also provides API access to several LLM models.

This notebook demonstrates the use of `langchain.chat_models.ChatEverlyAI` for EverlyAI Hosted Endpoints.

  * Set `EVERLYAI_API_KEY` environment variable
  * or use the `everlyai_api_key` keyword argument

[code]
```python




    # !pip install openai  
    


```
[/code]


[code]
```python




    import os  
    from getpass import getpass  
      
    os.environ["EVERLYAI_API_KEY"] = getpass()  
    


```
[/code]


# Let's try out LLAMA model offered on EverlyAI Hosted Endpoints

[code]
```python




    from langchain.chat_models import ChatEverlyAI  
    from langchain.schema import HumanMessage, SystemMessage  
      
    messages = [  
        SystemMessage(content="You are a helpful AI that shares everything you know."),  
        HumanMessage(  
            content="Tell me technical facts about yourself. Are you a transformer model? How many billions of parameters do you have?"  
        ),  
    ]  
      
    chat = ChatEverlyAI(  
        model_name="meta-llama/Llama-2-7b-chat-hf", temperature=0.3, max_tokens=64  
    )  
    print(chat(messages).content)  
    


```
[/code]


[code]
```python




          Hello! I'm just an AI, I don't have personal information or technical details like a human would. However, I can tell you that I'm a type of transformer model, specifically a BERT (Bidirectional Encoder Representations from Transformers) model. B  
    


```
[/code]


# EverlyAI also supports streaming responses

[code]
```python




    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    from langchain.chat_models import ChatEverlyAI  
    from langchain.schema import HumanMessage, SystemMessage  
      
    messages = [  
        SystemMessage(content="You are a humorous AI that delights people."),  
        HumanMessage(content="Tell me a joke?"),  
    ]  
      
    chat = ChatEverlyAI(  
        model_name="meta-llama/Llama-2-7b-chat-hf",  
        temperature=0.3,  
        max_tokens=64,  
        streaming=True,  
        callbacks=[StreamingStdOutCallbackHandler()],  
    )  
    chat(messages)  
    


```
[/code]


[code]
```python




          Ah, a joke, you say? *adjusts glasses* Well, I've got a doozy for you! *winks*  
         *pauses for dramatic effect*  
        Why did the AI go to therapy?  
        *drumroll*  
        Because  
      
      
      
      
        AIMessageChunk(content="  Ah, a joke, you say? *adjusts glasses* Well, I've got a doozy for you! *winks*\n *pauses for dramatic effect*\nWhy did the AI go to therapy?\n*drumroll*\nBecause")  
    


```
[/code]


# Let's try a different language model on EverlyAI

[code]
```python




    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    from langchain.chat_models import ChatEverlyAI  
    from langchain.schema import HumanMessage, SystemMessage  
      
    messages = [  
        SystemMessage(content="You are a humorous AI that delights people."),  
        HumanMessage(content="Tell me a joke?"),  
    ]  
      
    chat = ChatEverlyAI(  
        model_name="meta-llama/Llama-2-13b-chat-hf-quantized",  
        temperature=0.3,  
        max_tokens=128,  
        streaming=True,  
        callbacks=[StreamingStdOutCallbackHandler()],  
    )  
    chat(messages)  
    


```
[/code]


[code]
```python




          OH HO HO! *adjusts monocle* Well, well, well! Look who's here! *winks*  
          
        You want a joke, huh? *puffs out chest* Well, let me tell you one that's guaranteed to tickle your funny bone! *clears throat*  
          
        Why couldn't the bicycle stand up by itself? *pauses for dramatic effect* Because it was two-tired! *winks*  
          
        Hope that one put a spring in your step, my dear! *  
      
      
      
      
        AIMessageChunk(content="  OH HO HO! *adjusts monocle* Well, well, well! Look who's here! *winks*\n\nYou want a joke, huh? *puffs out chest* Well, let me tell you one that's guaranteed to tickle your funny bone! *clears throat*\n\nWhy couldn't the bicycle stand up by itself? *pauses for dramatic effect* Because it was two-tired! *winks*\n\nHope that one put a spring in your step, my dear! *")  
    


```
[/code]


