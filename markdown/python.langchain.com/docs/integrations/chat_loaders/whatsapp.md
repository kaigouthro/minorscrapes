

Skip to main content

On this page

# WhatsApp

This notebook shows how to use the WhatsApp chat loader. This class helps map exported WhatsApp conversations to LangChain chat messages.

The process has three steps:

  1. Export the chat conversations to computer
  2. Create the `WhatsAppChatLoader` with the file path pointed to the json file or directory of JSON files
  3. Call `loader.load()` (or `loader.lazy_load()`) to perform the conversion.

## 1\. Create message dump​

To make the export of your WhatsApp conversation(s), complete the following steps:

  1. Open the target conversation
  2. Click the three dots in the top right corner and select "More".
  3. Then select "Export chat" and choose "Without media".

An example of the data format for each conversation is below:

whatsapp_chat.txt

```python




    [8/15/23, 9:12:33 AM] Dr. Feather: ‎Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them.
    [8/15/23, 9:12:43 AM] Dr. Feather: I spotted a rare Hyacinth Macaw yesterday in the Amazon Rainforest. Such a magnificent creature!
    ‎[8/15/23, 9:12:48 AM] Dr. Feather: ‎image omitted
    [8/15/23, 9:13:15 AM] Jungle Jane: That's stunning! Were you able to observe its behavior?
    ‎[8/15/23, 9:13:23 AM] Dr. Feather: ‎image omitted
    [8/15/23, 9:14:02 AM] Dr. Feather: Yes, it seemed quite social with other macaws. They're known for their playful nature.
    [8/15/23, 9:14:15 AM] Jungle Jane: How's the research going on parrot communication?
    ‎[8/15/23, 9:14:30 AM] Dr. Feather: ‎image omitted
    [8/15/23, 9:14:50 AM] Dr. Feather: It's progressing well. We're learning so much about how they use sound and color to communicate.
    [8/15/23, 9:15:10 AM] Jungle Jane: That's fascinating! Can't wait to read your paper on it.
    [8/15/23, 9:15:20 AM] Dr. Feather: Thank you! I'll send you a draft soon.
    [8/15/23, 9:25:16 PM] Jungle Jane: Looking forward to it! Keep up the great work.



```


## 2\. Create the Chat Loader​

The WhatsAppChatLoader accepts the resulting zip file, unzipped directory, or the path to any of the chat `.txt` files therein.

Provide that as well as the user name you want to take on the role of "AI" when fine-tuning.

```python




    from langchain.chat_loaders.whatsapp import WhatsAppChatLoader



```


```python




    loader = WhatsAppChatLoader(
        path="./whatsapp_chat.txt",
    )



```


## 3\. Load messages​

The `load()` (or `lazy_load`) methods return a list of "ChatSessions" that currently store the list of messages per loaded conversation.

```python




    from typing import List

    from langchain.chat_loaders.base import ChatSession
    from langchain.chat_loaders.utils import (
        map_ai_messages,
        merge_chat_runs,
    )

    raw_messages = loader.lazy_load()
    # Merge consecutive messages from the same sender into a single message
    merged_messages = merge_chat_runs(raw_messages)
    # Convert messages from "Dr. Feather" to AI messages
    messages: List[ChatSession] = list(
        map_ai_messages(merged_messages, sender="Dr. Feather")
    )



```


```python




        [{'messages': [AIMessage(content='I spotted a rare Hyacinth Macaw yesterday in the Amazon Rainforest. Such a magnificent creature!', additional_kwargs={'sender': 'Dr. Feather', 'events': [{'message_time': '8/15/23, 9:12:43 AM'}]}, example=False),
           HumanMessage(content="That's stunning! Were you able to observe its behavior?", additional_kwargs={'sender': 'Jungle Jane', 'events': [{'message_time': '8/15/23, 9:13:15 AM'}]}, example=False),
           AIMessage(content="Yes, it seemed quite social with other macaws. They're known for their playful nature.", additional_kwargs={'sender': 'Dr. Feather', 'events': [{'message_time': '8/15/23, 9:14:02 AM'}]}, example=False),
           HumanMessage(content="How's the research going on parrot communication?", additional_kwargs={'sender': 'Jungle Jane', 'events': [{'message_time': '8/15/23, 9:14:15 AM'}]}, example=False),
           AIMessage(content="It's progressing well. We're learning so much about how they use sound and color to communicate.", additional_kwargs={'sender': 'Dr. Feather', 'events': [{'message_time': '8/15/23, 9:14:50 AM'}]}, example=False),
           HumanMessage(content="That's fascinating! Can't wait to read your paper on it.", additional_kwargs={'sender': 'Jungle Jane', 'events': [{'message_time': '8/15/23, 9:15:10 AM'}]}, example=False),
           AIMessage(content="Thank you! I'll send you a draft soon.", additional_kwargs={'sender': 'Dr. Feather', 'events': [{'message_time': '8/15/23, 9:15:20 AM'}]}, example=False),
           HumanMessage(content='Looking forward to it! Keep up the great work.', additional_kwargs={'sender': 'Jungle Jane', 'events': [{'message_time': '8/15/23, 9:25:16 PM'}]}, example=False)]}]



```


### Next Steps​

You can then use these messages how you see fit, such as fine-tuning a model, few-shot example selection, or directly make predictions for the next message.

```python




    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI()

    for chunk in llm.stream(messages[0]["messages"]):
        print(chunk.content, end="", flush=True)



```


```python




        Thank you for the encouragement! I'll do my best to continue studying and sharing fascinating insights about parrot communication.



```
