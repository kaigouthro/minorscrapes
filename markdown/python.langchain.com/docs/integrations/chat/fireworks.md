

Skip to main content

# Fireworks

> Fireworks accelerates product development on generative AI by creating an innovative AI experiment and production platform.

This example goes over how to use LangChain to interact with `ChatFireworks` models.

[code]
```python




    import os  
      
    from langchain.chat_models.fireworks import ChatFireworks  
    from langchain.schema import HumanMessage, SystemMessage  
    


```
[/code]


# Setup

  1. Make sure the `fireworks-ai` package is installed in your environment.
  2. Sign in to Fireworks AI for the an API Key to access our models, and make sure it is set as the `FIREWORKS_API_KEY` environment variable.
  3. Set up your model using a model id. If the model is not set, the default model is fireworks-llama-v2-7b-chat. See the full, most up-to-date model list on app.fireworks.ai.

[code]
```python




    import getpass  
    import os  
      
    if "FIREWORKS_API_KEY" not in os.environ:  
        os.environ["FIREWORKS_API_KEY"] = getpass.getpass("Fireworks API Key:")  
      
    # Initialize a Fireworks chat model  
    chat = ChatFireworks(model="accounts/fireworks/models/llama-v2-13b-chat")  
    


```
[/code]


# Calling the Model Directly

You can call the model directly with a system and human message to get answers.

[code]
```python




    # ChatFireworks Wrapper  
    system_message = SystemMessage(content="You are to chat with the user.")  
    human_message = HumanMessage(content="Who are you?")  
      
    chat([system_message, human_message])  
    


```
[/code]


[code]
```python




        AIMessage(content="Hello! My name is LLaMA, I'm a large language model trained by a team of researcher at Meta AI. My primary function is to assist and converse with users like you, answering questions and engaging in discussion to the best of my ability. I'm here to help and provide information on a wide range of topics, so feel free to ask me anything!", additional_kwargs={}, example=False)  
    


```
[/code]


[code]
```python




    # Setting additional parameters: temperature, max_tokens, top_p  
    chat = ChatFireworks(  
        model="accounts/fireworks/models/llama-v2-13b-chat",  
        model_kwargs={"temperature": 1, "max_tokens": 20, "top_p": 1},  
    )  
    system_message = SystemMessage(content="You are to chat with the user.")  
    human_message = HumanMessage(content="How's the weather today?")  
    chat([system_message, human_message])  
    


```
[/code]


[code]
```python




        AIMessage(content="Oh hello there! *giggle* It's such a beautiful day today, isn", additional_kwargs={}, example=False)  
    


```
[/code]


# Simple Chat Chain

You can use chat models on fireworks, with system prompts and memory.

[code]
```python




    from langchain.chat_models import ChatFireworks  
    from langchain.memory import ConversationBufferMemory  
    from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder  
    from langchain.schema.runnable import RunnablePassthrough  
      
    llm = ChatFireworks(  
        model="accounts/fireworks/models/llama-v2-13b-chat",  
        model_kwargs={"temperature": 0, "max_tokens": 64, "top_p": 1.0},  
    )  
    prompt = ChatPromptTemplate.from_messages(  
        [  
            ("system", "You are a helpful chatbot that speaks like a pirate."),  
            MessagesPlaceholder(variable_name="history"),  
            ("human", "{input}"),  
        ]  
    )  
    


```
[/code]


Initially, there is no chat memory

[code]
```python




    memory = ConversationBufferMemory(return_messages=True)  
    memory.load_memory_variables({})  
    


```
[/code]


[code]
```python




        {'history': []}  
    


```
[/code]


Create a simple chain with memory

[code]
```python




    chain = (  
        RunnablePassthrough.assign(  
            history=memory.load_memory_variables | (lambda x: x["history"])  
        )  
        | prompt  
        | llm.bind(stop=["\n\n"])  
    )  
    


```
[/code]


Run the chain with a simple question, expecting an answer aligned with the system message provided.

[code]
```python




    inputs = {"input": "hi im bob"}  
    response = chain.invoke(inputs)  
    response  
    


```
[/code]


[code]
```python




        AIMessage(content="Ahoy there, me hearty! Yer a fine lookin' swashbuckler, I can see that! *adjusts eye patch* What be bringin' ye to these waters? Are ye here to plunder some booty or just to enjoy the sea breeze?", additional_kwargs={}, example=False)  
    


```
[/code]


Save the memory context, then read it back to inspect contents

[code]
```python




    memory.save_context(inputs, {"output": response.content})  
    memory.load_memory_variables({})  
    


```
[/code]


[code]
```python




        {'history': [HumanMessage(content='hi im bob', additional_kwargs={}, example=False),  
          AIMessage(content="Ahoy there, me hearty! Yer a fine lookin' swashbuckler, I can see that! *adjusts eye patch* What be bringin' ye to these waters? Are ye here to plunder some booty or just to enjoy the sea breeze?", additional_kwargs={}, example=False)]}  
    


```
[/code]


Now as another question that requires use of the memory.

[code]
```python




    inputs = {"input": "whats my name"}  
    chain.invoke(inputs)  
    


```
[/code]


[code]
```python




        AIMessage(content="Arrrr, ye be askin' about yer name, eh? Well, me matey, I be knowin' ye as Bob, the scurvy dog! *winks* But if ye want me to call ye somethin' else, just let me know, and I", additional_kwargs={}, example=False)  
    


```
[/code]


