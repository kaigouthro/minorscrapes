

Skip to main content

On this page

# Telegram

This notebook shows how to use the Telegram chat loader. This class helps map exported Telegram conversations to LangChain chat messages.

The process has three steps:

  1. Export the chat .txt file by copying chats from the Discord app and pasting them in a file on your local computer
  2. Create the `TelegramChatLoader` with the file path pointed to the json file or directory of JSON files
  3. Call `loader.load()` (or `loader.lazy_load()`) to perform the conversion. Optionally use `merge_chat_runs` to combine message from the same sender in sequence, and/or `map_ai_messages` to convert messages from the specified sender to the "AIMessage" class.

## 1\. Create message dump​

Currently (2023/08/23) this loader best supports json files in the format generated by exporting your chat history from the Telegram Desktop App.

 **Important:** There are 'lite' versions of telegram such as "Telegram for MacOS" that lack the export functionality. Please make sure you use the correct app to export the file.

To make the export:

  1. Download and open telegram desktop
  2. Select a conversation
  3. Navigate to the conversation settings (currently the three dots in the top right corner)
  4. Click "Export Chat History"
  5. Unselect photos and other media. Select "Machine-readable JSON" format to export.

An example is below:

telegram_conversation.json

```python




    {
     "name": "Jiminy",
     "type": "personal_chat",
     "id": 5965280513,
     "messages": [
      {
       "id": 1,
       "type": "message",
       "date": "2023-08-23T13:11:23",
       "date_unixtime": "1692821483",
       "from": "Jiminy Cricket",
       "from_id": "user123450513",
       "text": "You better trust your conscience",
       "text_entities": [
        {
         "type": "plain",
         "text": "You better trust your conscience"
        }
       ]
      },
      {
       "id": 2,
       "type": "message",
       "date": "2023-08-23T13:13:20",
       "date_unixtime": "1692821600",
       "from": "Batman & Robin",
       "from_id": "user6565661032",
       "text": "What did you just say?",
       "text_entities": [
        {
         "type": "plain",
         "text": "What did you just say?"
        }
       ]
      }
     ]
    }



```


## 2\. Create the Chat Loader​

All that's required is the file path. You can optionally specify the user name that maps to an ai message as well an configure whether to merge message runs.

```python




    from langchain.chat_loaders.telegram import TelegramChatLoader



```


```python




    loader = TelegramChatLoader(
        path="./telegram_conversation.json",
    )



```


## 3\. Load messages​

The `load()` (or `lazy_load`) methods return a list of "ChatSessions" that currently just contain a list of messages per loaded conversation.

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
    # Convert messages from "Jiminy Cricket" to AI messages
    messages: List[ChatSession] = list(
        map_ai_messages(merged_messages, sender="Jiminy Cricket")
    )



```


### Next Steps​

You can then use these messages how you see fit, such as fine-tuning a model, few-shot example selection, or directly make predictions for the next message

```python




    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI()

    for chunk in llm.stream(messages[0]["messages"]):
        print(chunk.content, end="", flush=True)



```


```python




        I said, "You better trust your conscience."



```
