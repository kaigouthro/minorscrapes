

Skip to main content

On this page

# WeChat

There is not yet a straightforward way to export personal WeChat messages. However if you just need no more than few hundreds of messages for model fine-tuning or few-shot examples, this notebook
shows how to create your own chat loader that works on copy-pasted WeChat messages to a list of LangChain messages.

> Highly inspired by https://python.langchain.com/docs/integrations/chat_loaders/discord

The process has five steps:

  1. Open your chat in the WeChat desktop app. Select messages you need by mouse-dragging or right-click. Due to restrictions, you can select up to 100 messages once a time. `CMD`/`Ctrl` \+ `C` to copy.
  2. Create the chat .txt file by pasting selected messages in a file on your local computer.
  3. Copy the chat loader definition from below to a local file.
  4. Initialize the `WeChatChatLoader` with the file path pointed to the text file.
  5. Call `loader.load()` (or `loader.lazy_load()`) to perform the conversion.

## 1\. Create message dump​

This loader only supports .txt files in the format generated by copying messages in the app to your clipboard and pasting in a file. Below is an example.

wechat_chats.txt

```python




    女朋友 2023/09/16 2:51 PM
    天气有点凉

    男朋友 2023/09/16 2:51 PM
    珍簟凉风著，瑶琴寄恨生。嵇君懒书札，底物慰秋情。

    女朋友 2023/09/16 3:06 PM
    忙什么呢

    男朋友 2023/09/16 3:06 PM
    今天只干成了一件像样的事
    那就是想你

    女朋友 2023/09/16 3:06 PM
    [动画表情]



```


## 2\. Define chat loader​

LangChain currently does not support

```python




    import logging
    import re
    from typing import Iterator, List

    from langchain.chat_loaders import base as chat_loaders
    from langchain.schema import BaseMessage, HumanMessage

    logger = logging.getLogger()


    class WeChatChatLoader(chat_loaders.BaseChatLoader):
        def __init__(self, path: str):
            """
            Initialize the Discord chat loader.

            Args:
                path: Path to the exported Discord chat text file.
            """
            self.path = path
            self._message_line_regex = re.compile(
                r"(?P<sender>.+?) (?P<timestamp>\d{4}/\d{2}/\d{2} \d{1,2}:\d{2} (?:AM|PM))",  # noqa
                # flags=re.DOTALL,
            )

        def _append_message_to_results(
            self,
            results: List,
            current_sender: str,
            current_timestamp: str,
            current_content: List[str],
        ):
            content = "\n".join(current_content).strip()
            # skip non-text messages like stickers, images, etc.
            if not re.match(r"\[.*\]", content):
                results.append(
                    HumanMessage(
                        content=content,
                        additional_kwargs={
                            "sender": current_sender,
                            "events": [{"message_time": current_timestamp}],
                        },
                    )
                )
            return results

        def _load_single_chat_session_from_txt(
            self, file_path: str
        ) -> chat_loaders.ChatSession:
            """
            Load a single chat session from a text file.

            Args:
                file_path: Path to the text file containing the chat messages.

            Returns:
                A `ChatSession` object containing the loaded chat messages.
            """
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            results: List[BaseMessage] = []
            current_sender = None
            current_timestamp = None
            current_content = []
            for line in lines:
                if re.match(self._message_line_regex, line):
                    if current_sender and current_content:
                        results = self._append_message_to_results(
                            results, current_sender, current_timestamp, current_content
                        )
                    current_sender, current_timestamp = re.match(
                        self._message_line_regex, line
                    ).groups()
                    current_content = []
                else:
                    current_content.append(line.strip())

            if current_sender and current_content:
                results = self._append_message_to_results(
                    results, current_sender, current_timestamp, current_content
                )

            return chat_loaders.ChatSession(messages=results)

        def lazy_load(self) -> Iterator[chat_loaders.ChatSession]:
            """
            Lazy load the messages from the chat file and yield them in the required format.

            Yields:
                A `ChatSession` object containing the loaded chat messages.
            """
            yield self._load_single_chat_session_from_txt(self.path)



```


## 2\. Create loader​

We will point to the file we just wrote to disk.

```python




    loader = WeChatChatLoader(
        path="./wechat_chats.txt",
    )



```


## 3\. Load Messages​

Assuming the format is correct, the loader will convert the chats to langchain messages.

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
    # Convert messages from "男朋友" to AI messages
    messages: List[ChatSession] = list(map_ai_messages(merged_messages, sender="男朋友"))



```


```python




    messages



```


```python




        [{'messages': [HumanMessage(content='天气有点凉', additional_kwargs={'sender': '女朋友', 'events': [{'message_time': '2023/09/16 2:51 PM'}]}, example=False),
           AIMessage(content='珍簟凉风著，瑶琴寄恨生。嵇君懒书札，底物慰秋情。', additional_kwargs={'sender': '男朋友', 'events': [{'message_time': '2023/09/16 2:51 PM'}]}, example=False),
           HumanMessage(content='忙什么呢', additional_kwargs={'sender': '女朋友', 'events': [{'message_time': '2023/09/16 3:06 PM'}]}, example=False),
           AIMessage(content='今天只干成了一件像样的事\n那就是想你', additional_kwargs={'sender': '男朋友', 'events': [{'message_time': '2023/09/16 3:06 PM'}]}, example=False)]}]



```


### Next Steps​

You can then use these messages how you see fit, such as fine-tuning a model, few-shot example selection, or directly make predictions for the next message

```python




    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI()

    for chunk in llm.stream(messages[0]["messages"]):
        print(chunk.content, end="", flush=True)



```