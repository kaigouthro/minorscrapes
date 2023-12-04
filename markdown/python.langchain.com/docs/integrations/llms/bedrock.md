

Skip to main content

On this page

# Bedrock

Amazon Bedrock is a fully managed service that makes FMs from leading AI startups and Amazon available via an API, so you can choose from a wide range of FMs to find the model that is best suited for
your use case

```python




    %pip install boto3



```


```python




    from langchain.llms import Bedrock

    llm = Bedrock(
        credentials_profile_name="bedrock-admin", model_id="amazon.titan-text-express-v1"
    )



```


### Using in a conversation chain​

```python




    from langchain.chains import ConversationChain
    from langchain.memory import ConversationBufferMemory

    conversation = ConversationChain(
        llm=llm, verbose=True, memory=ConversationBufferMemory()
    )

    conversation.predict(input="Hi there!")



```


### Conversation Chain With Streaming​

```python




    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    from langchain.llms import Bedrock

    llm = Bedrock(
        credentials_profile_name="bedrock-admin",
        model_id="amazon.titan-text-express-v1",
        streaming=True,
        callbacks=[StreamingStdOutCallbackHandler()],
    )



```


```python




    conversation = ConversationChain(
        llm=llm, verbose=True, memory=ConversationBufferMemory()
    )

    conversation.predict(input="Hi there!")



```
