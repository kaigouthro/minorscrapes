

Skip to main content

On this page

# Ollama

Ollama allows you to run open-source large language models, such as LLaMA2, locally.

Ollama bundles model weights, configuration, and data into a single package, defined by a Modelfile.

It optimizes setup and configuration details, including GPU usage.

For a complete list of supported models and model variants, see the Ollama model library.

## Setup​

First, follow these instructions to set up and run a local Ollama instance:

  * Download
  * Fetch a model via `ollama pull <model family>`
  * e.g., for `Llama-7b`: `ollama pull llama2`
  * This will download the most basic version of the model (e.g., minimum # parameters and 4-bit quantization)
  * On Mac, it will download to:

`~/.ollama/models/manifests/registry.ollama.ai/library/<model family>/latest`

  * And we can specify a particular version, e.g., for `ollama pull vicuna:13b-v1.5-16k-q4_0`
  * The file is here with the model version in place of `latest`

`~/.ollama/models/manifests/registry.ollama.ai/library/vicuna/13b-v1.5-16k-q4_0`

You can easily access models in a few ways:

1/ if the app is running:

  * All of your local models are automatically served on `localhost:11434`
  * Select your model when setting `llm = Ollama(..., model="<model family>:<version>")`
  * If you set `llm = Ollama(..., model="<model family")` withoout a version it will simply look for `latest`

2/ if building from source or just running the binary:

  * Then you must run `ollama serve`
  * All of your local models are automatically served on `localhost:11434`
  * Then, select as shown above

## Usage​

You can see a full list of supported parameters on the API reference page.

If you are using a LLaMA `chat` model (e.g., `ollama pull llama2:7b-chat`) then you can use the `ChatOllama` interface.

This includes special tokens for system message and user input.

[code]
```python




    from langchain.callbacks.manager import CallbackManager  
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    from langchain.chat_models import ChatOllama  
      
    chat_model = ChatOllama(  
        model="llama2:7b-chat",  
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),  
    )  
    


```
[/code]


With `StreamingStdOutCallbackHandler`, you will see tokens streamed.

[code]
```python




    from langchain.schema import HumanMessage  
      
    messages = [HumanMessage(content="Tell me about the history of AI")]  
    chat_model(messages)  
    


```
[/code]


[code]
```python




         Artificial intelligence (AI) has a rich and varied history that spans several decades. Hinweis: The following is a brief overview of the major milestones in the history of AI, but it is by no means exhaustive.  
          
        1. Early Beginnings (1950s-1960s): The term "Artificial Intelligence" was coined in 1956 by computer scientist John McCarthy. However, the concept of creating machines that can think and learn like humans dates back to ancient times. In the 1950s and 1960s, researchers began exploring the possibilities of AI using simple algorithms and machine learning techniques.  
        2. Rule-Based Systems (1970s-1980s): In the 1970s and 1980s, AI research focused on developing rule-based systems, which use predefined rules to reason and make decisions. This led to the development of expert systems, which were designed to mimic the decision-making abilities of human experts in specific domains.  
        3. Machine Learning (1980s-1990s): The 1980s saw a shift towards machine learning, which enables machines to learn from data without being explicitly programmed. This led to the development of algorithms such as decision trees, neural networks, and support vector machines.  
        4. Deep Learning (2000s-present): In the early 2000s, deep learning emerged as a subfield of machine learning, focusing on neural networks with multiple layers. These networks can learn complex representations of data, leading to breakthroughs in image and speech recognition, natural language processing, and other areas.  
        5. Natural Language Processing (NLP) (1980s-present): NLP has been an active area of research since the 1980s, with a focus on developing algorithms that can understand and generate human language. This has led to applications such as chatbots, voice assistants, and language translation systems.  
        6. Robotics (1970s-present): The development of robotics has been closely tied to AI research, with a focus on creating machines that can perform tasks that typically require human intelligence, such as manipulation and locomotion.  
        7. Computer Vision (1980s-present): Computer vision has been an active area of research since the 1980s, with a focus on enabling machines to interpret and understand visual data from the world around us. This has led to applications such as image recognition, object detection, and autonomous driving.  
        8. Ethics and Society (1990s-present): As AI technology has become more advanced and integrated into various aspects of society, there has been a growing concern about the ethical implications of AI. This includes issues related to privacy, bias, and job displacement.  
        9. Reinforcement Learning (2000s-present): Reinforcement learning is a subfield of machine learning that involves training machines to make decisions based on feedback from their environment. This has led to breakthroughs in areas such as game playing, robotics, and autonomous driving.  
        10. Generative Models (2010s-present): Generative models are a class of AI algorithms that can generate new data that is similar to a given dataset. This has led to applications such as image synthesis, music generation, and language creation.  
          
        These are just a few of the many developments in the history of AI. As the field continues to evolve, we can expect even more exciting breakthroughs and innovations in the years to come.  
      
      
      
      
        AIMessage(content=' Artificial intelligence (AI) has a rich and varied history that spans several decades. Hinweis: The following is a brief overview of the major milestones in the history of AI, but it is by no means exhaustive.\n\n1. Early Beginnings (1950s-1960s): The term "Artificial Intelligence" was coined in 1956 by computer scientist John McCarthy. However, the concept of creating machines that can think and learn like humans dates back to ancient times. In the 1950s and 1960s, researchers began exploring the possibilities of AI using simple algorithms and machine learning techniques.\n2. Rule-Based Systems (1970s-1980s): In the 1970s and 1980s, AI research focused on developing rule-based systems, which use predefined rules to reason and make decisions. This led to the development of expert systems, which were designed to mimic the decision-making abilities of human experts in specific domains.\n3. Machine Learning (1980s-1990s): The 1980s saw a shift towards machine learning, which enables machines to learn from data without being explicitly programmed. This led to the development of algorithms such as decision trees, neural networks, and support vector machines.\n4. Deep Learning (2000s-present): In the early 2000s, deep learning emerged as a subfield of machine learning, focusing on neural networks with multiple layers. These networks can learn complex representations of data, leading to breakthroughs in image and speech recognition, natural language processing, and other areas.\n5. Natural Language Processing (NLP) (1980s-present): NLP has been an active area of research since the 1980s, with a focus on developing algorithms that can understand and generate human language. This has led to applications such as chatbots, voice assistants, and language translation systems.\n6. Robotics (1970s-present): The development of robotics has been closely tied to AI research, with a focus on creating machines that can perform tasks that typically require human intelligence, such as manipulation and locomotion.\n7. Computer Vision (1980s-present): Computer vision has been an active area of research since the 1980s, with a focus on enabling machines to interpret and understand visual data from the world around us. This has led to applications such as image recognition, object detection, and autonomous driving.\n8. Ethics and Society (1990s-present): As AI technology has become more advanced and integrated into various aspects of society, there has been a growing concern about the ethical implications of AI. This includes issues related to privacy, bias, and job displacement.\n9. Reinforcement Learning (2000s-present): Reinforcement learning is a subfield of machine learning that involves training machines to make decisions based on feedback from their environment. This has led to breakthroughs in areas such as game playing, robotics, and autonomous driving.\n10. Generative Models (2010s-present): Generative models are a class of AI algorithms that can generate new data that is similar to a given dataset. This has led to applications such as image synthesis, music generation, and language creation.\n\nThese are just a few of the many developments in the history of AI. As the field continues to evolve, we can expect even more exciting breakthroughs and innovations in the years to come.', additional_kwargs={}, example=False)  
    


```
[/code]


## Extraction​

Update your version of Ollama and supply the `format` flag.

We can enforce the model to produce JSON.

 **Note:** You can also try out the experimental OllamaFunctions wrapper for convenience.

[code]
```python




    from langchain.callbacks.manager import CallbackManager  
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    from langchain.chat_models import ChatOllama  
      
    chat_model = ChatOllama(  
        model="llama2",  
        format="json",  
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),  
    )  
    


```
[/code]


[code]
```python




    from langchain.schema import HumanMessage  
      
    messages = [  
        HumanMessage(  
            content="What color is the sky at different times of the day? Respond using JSON"  
        )  
    ]  
      
    chat_model_response = chat_model(messages)  
    


```
[/code]


[code]
```python




         Sure! Here's a JSON response with the colors of the sky at different times of the day:  
         Begriffe und Abkürzungen:  
          
        * `time`: The time of day (in 24-hour format)  
        * `sky_color`: The color of the sky at that time (as a hex code)  
          
        Here are the colors of the sky at different times of the day:  
        ```json  
        [  
          {  
            "time": "6am",  
            "sky_color": "#0080c0"  
          },  
          {  
            "time": "9am",  
            "sky_color": "#3498db"  
          },  
          {  
            "time": "12pm",  
            "sky_color": "#ef7c00"  
          },  
          {  
            "time": "3pm",  
            "sky_color": "#9564b6"  
          },  
          {  
            "time": "6pm",  
            "sky_color": "#e78ac3"  
          },  
          {  
            "time": "9pm",  
            "sky_color": "#5f006a"  
          }  
        ]  
        ```  
        In this response, the `time` property is a string in 24-hour format, representing the time of day. The `sky_color` property is a hex code representing the color of the sky at that time. For example, at 6am, the sky is blue (#0080c0), while at 9pm, it's dark blue (#5f006a).  
    


```
[/code]


[code]
```python




    import json  
      
    from langchain.schema import HumanMessage  
      
    json_schema = {  
        "title": "Person",  
        "description": "Identifying information about a person.",  
        "type": "object",  
        "properties": {  
            "name": {"title": "Name", "description": "The person's name", "type": "string"},  
            "age": {"title": "Age", "description": "The person's age", "type": "integer"},  
            "fav_food": {  
                "title": "Fav Food",  
                "description": "The person's favorite food",  
                "type": "string",  
            },  
        },  
        "required": ["name", "age"],  
    }  
      
    messages = [  
        HumanMessage(  
            content="Please tell me about a person using the following JSON schema:"  
        ),  
        HumanMessage(content=json.dumps(json_schema, indent=2)),  
        HumanMessage(  
            content="Now, considering the schema, tell me about a person named John who is 35 years old and loves pizza."  
        ),  
    ]  
      
    chat_model_response = chat_model(messages)  
    


```
[/code]


[code]
```python




         Sure! Based on the JSON schema you provided, here's the information we can gather about a person named John who is 35 years old and loves pizza:  
          
        **Name:** John  
          
        **Age:** 35 (integer)  
          
        **Favorite food:** Pizza (string)  
          
        So, the JSON object for John would look like this:  
        ```json  
        {  
          "name": "John",  
          "age": 35,  
          "fav_food": "pizza"  
        }  
        ```  
        Note that we cannot provide additional information about John beyond what is specified in the schema. For example, we do not have any information about his gender, occupation, or address, as those fields are not included in the schema.  
    


```
[/code]


## RAG​

We can use Olama with RAG, just as shown here.

Let's use the 13b model:

[code]
```python




    ollama pull llama2:13b  
    


```
[/code]


Let's also use local embeddings from `OllamaEmbeddings` and `Chroma`.

[code]
```python




    pip install chromadb  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import WebBaseLoader  
      
    loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")  
    data = loader.load()  
      
    from langchain.text_splitter import RecursiveCharacterTextSplitter  
      
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)  
    all_splits = text_splitter.split_documents(data)  
    


```
[/code]


[code]
```python




    from langchain.embeddings import OllamaEmbeddings  
    from langchain.vectorstores import Chroma  
      
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OllamaEmbeddings())  
    


```
[/code]


[code]
```python




    question = "What are the approaches to Task Decomposition?"  
    docs = vectorstore.similarity_search(question)  
    len(docs)  
    


```
[/code]


[code]
```python




        4  
    


```
[/code]


[code]
```python




    from langchain.prompts import PromptTemplate  
      
    # Prompt  
    template = """[INST] <<SYS>> Use the following pieces of context to answer the question at the end.   
    If you don't know the answer, just say that you don't know, don't try to make up an answer.   
    Use three sentences maximum and keep the answer as concise as possible. <</SYS>>  
    {context}  
    Question: {question}  
    Helpful Answer:[/INST]"""  
    QA_CHAIN_PROMPT = PromptTemplate(  
        input_variables=["context", "question"],  
        template=template,  
    )  
    


```
[/code]


[code]
```python




    # Chat model  
    from langchain.callbacks.manager import CallbackManager  
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    from langchain.chat_models import ChatOllama  
      
    chat_model = ChatOllama(  
        model="llama2:13b",  
        verbose=True,  
        callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),  
    )  
    


```
[/code]


[code]
```python




    # QA chain  
    from langchain.chains import RetrievalQA  
      
    qa_chain = RetrievalQA.from_chain_type(  
        chat_model,  
        retriever=vectorstore.as_retriever(),  
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},  
    )  
    


```
[/code]


[code]
```python




    question = "What are the various approaches to Task Decomposition for AI Agents?"  
    result = qa_chain({"query": question})  
    


```
[/code]


[code]
```python




         Based on the provided context, there are three approaches to task decomposition for AI agents:  
          
        1. LLM with simple prompting, such as "Steps for XYZ." or "What are the subgoals for achieving XYZ?"  
        2. Task-specific instructions, such as "Write a story outline" for writing a novel.  
        3. Human inputs.  
    


```
[/code]


You can also get logging for tokens.

[code]
```python




    from langchain.callbacks.base import BaseCallbackHandler  
    from langchain.schema import LLMResult  
      
      
    class GenerationStatisticsCallback(BaseCallbackHandler):  
        def on_llm_end(self, response: LLMResult, **kwargs) -> None:  
            print(response.generations[0][0].generation_info)  
      
      
    callback_manager = CallbackManager(  
        [StreamingStdOutCallbackHandler(), GenerationStatisticsCallback()]  
    )  
      
    chat_model = ChatOllama(  
        model="llama2:13b-chat", verbose=True, callback_manager=callback_manager  
    )  
      
    qa_chain = RetrievalQA.from_chain_type(  
        chat_model,  
        retriever=vectorstore.as_retriever(),  
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},  
    )  
      
    question = "What are the approaches to Task Decomposition?"  
    result = qa_chain({"query": question})  
    


```
[/code]


[code]
```python




         Based on the given context, here is the answer to the question "What are the approaches to Task Decomposition?"  
          
        There are three approaches to task decomposition:  
          
        1. LLM with simple prompting, such as "Steps for XYZ." or "What are the subgoals for achieving XYZ?"  
        2. Using task-specific instructions, like "Write a story outline" for writing a novel.  
        3. With human inputs.{'model': 'llama2:13b-chat', 'created_at': '2023-08-23T15:37:51.469127Z', 'done': True, 'context': [1, 29871, 1, 29961, 25580, 29962, 518, 25580, 29962, 518, 25580, 29962, 3532, 14816, 29903, 6778, 4803, 278, 1494, 12785, 310, 3030, 304, 1234, 278, 1139, 472, 278, 1095, 29889, 29871, 13, 3644, 366, 1016, 29915, 29873, 1073, 278, 1234, 29892, 925, 1827, 393, 366, 1016, 29915, 29873, 1073, 29892, 1016, 29915, 29873, 1018, 304, 1207, 701, 385, 1234, 29889, 29871, 13, 11403, 2211, 25260, 7472, 322, 3013, 278, 1234, 408, 3022, 895, 408, 1950, 29889, 529, 829, 14816, 29903, 6778, 13, 5398, 26227, 508, 367, 2309, 313, 29896, 29897, 491, 365, 26369, 411, 2560, 9508, 292, 763, 376, 7789, 567, 363, 1060, 29979, 29999, 7790, 29876, 29896, 19602, 376, 5618, 526, 278, 1014, 1484, 1338, 363, 3657, 15387, 1060, 29979, 29999, 29973, 613, 313, 29906, 29897, 491, 773, 3414, 29899, 14940, 11994, 29936, 321, 29889, 29887, 29889, 376, 6113, 263, 5828, 27887, 1213, 363, 5007, 263, 9554, 29892, 470, 313, 29941, 29897, 411, 5199, 10970, 29889, 13, 13, 5398, 26227, 508, 367, 2309, 313, 29896, 29897, 491, 365, 26369, 411, 2560, 9508, 292, 763, 376, 7789, 567, 363, 1060, 29979, 29999, 7790, 29876, 29896, 19602, 376, 5618, 526, 278, 1014, 1484, 1338, 363, 3657, 15387, 1060, 29979, 29999, 29973, 613, 313, 29906, 29897, 491, 773, 3414, 29899, 14940, 11994, 29936, 321, 29889, 29887, 29889, 376, 6113, 263, 5828, 27887, 1213, 363, 5007, 263, 9554, 29892, 470, 313, 29941, 29897, 411, 5199, 10970, 29889, 13, 13, 1451, 16047, 267, 297, 1472, 29899, 8489, 18987, 322, 3414, 26227, 29901, 1858, 9450, 975, 263, 3309, 29891, 4955, 322, 17583, 3902, 8253, 278, 1650, 2913, 3933, 18066, 292, 29889, 365, 26369, 29879, 21117, 304, 10365, 13900, 746, 20050, 411, 15668, 4436, 29892, 3907, 963, 3109, 16424, 9401, 304, 25618, 1058, 5110, 515, 14260, 322, 1059, 29889, 13, 13, 1451, 16047, 267, 297, 1472, 29899, 8489, 18987, 322, 3414, 26227, 29901, 1858, 9450, 975, 263, 3309, 29891, 4955, 322, 17583, 3902, 8253, 278, 1650, 2913, 3933, 18066, 292, 29889, 365, 26369, 29879, 21117, 304, 10365, 13900, 746, 20050, 411, 15668, 4436, 29892, 3907, 963, 3109, 16424, 9401, 304, 25618, 1058, 5110, 515, 14260, 322, 1059, 29889, 13, 16492, 29901, 1724, 526, 278, 13501, 304, 9330, 897, 510, 3283, 29973, 13, 29648, 1319, 673, 10834, 29914, 25580, 29962, 518, 29914, 25580, 29962, 518, 29914, 25580, 29962, 29871, 16564, 373, 278, 2183, 3030, 29892, 1244, 338, 278, 1234, 304, 278, 1139, 376, 5618, 526, 278, 13501, 304, 9330, 897, 510, 3283, 3026, 13, 13, 8439, 526, 2211, 13501, 304, 3414, 26227, 29901, 13, 13, 29896, 29889, 365, 26369, 411, 2560, 9508, 292, 29892, 1316, 408, 376, 7789, 567, 363, 1060, 29979, 29999, 1213, 470, 376, 5618, 526, 278, 1014, 1484, 1338, 363, 3657, 15387, 1060, 29979, 29999, 3026, 13, 29906, 29889, 5293, 3414, 29899, 14940, 11994, 29892, 763, 376, 6113, 263, 5828, 27887, 29908, 363, 5007, 263, 9554, 29889, 13, 29941, 29889, 2973, 5199, 10970, 29889, 2], 'total_duration': 9514823750, 'load_duration': 795542, 'sample_count': 99, 'sample_duration': 68732000, 'prompt_eval_count': 146, 'prompt_eval_duration': 6206275000, 'eval_count': 98, 'eval_duration': 3229641000}  
    


```
[/code]


`eval_count` / (`eval_duration`/10e9) gets `tok / s`

[code]
```python




    98 / (3229641000 / 1000 / 1000 / 1000)  
    


```
[/code]


[code]
```python




        30.343929867127645  
    


```
[/code]


