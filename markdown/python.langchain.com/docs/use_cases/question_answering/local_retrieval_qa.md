

Skip to main content

On this page

# RAG using local models

The popularity of projects like PrivateGPT, llama.cpp, and GPT4All underscore the importance of running LLMs locally.

LangChain has integrations with many open-source LLMs that can be run locally.

See here for setup instructions for these LLMs.

For example, here we show how to run `GPT4All` or `LLaMA2` locally (e.g., on your laptop) using local embeddings and a local LLM.

## Document Loading​

First, install packages needed for local embeddings and vector storage.

[code]
```python




    pip install gpt4all chromadb langchainhub  
    


```
[/code]


Load and split an example document.

We'll use a blog post on agents as an example.

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


Next, the below steps will download the `GPT4All` embeddings locally (if you don't already have them).

[code]
```python




    from langchain.embeddings import GPT4AllEmbeddings  
    from langchain.vectorstores import Chroma  
      
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())  
    


```
[/code]


[code]
```python




        Found model file at  /Users/rlm/.cache/gpt4all/ggml-all-MiniLM-L6-v2-f16.bin  
      
      
        objc[49534]: Class GGMLMetalClass is implemented in both /Users/rlm/miniforge3/envs/llama2/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/libreplit-mainline-metal.dylib (0x131614208) and /Users/rlm/miniforge3/envs/llama2/lib/python3.9/site-packages/gpt4all/llmodel_DO_NOT_MODIFY/build/libllamamodel-mainline-metal.dylib (0x131988208). One of the two will be used. Which one is undefined.  
    


```
[/code]


Test similarity search is working with our local embeddings.

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




    docs[0]  
    


```
[/code]


[code]
```python




        Document(page_content='Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.', metadata={'description': 'Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.\nAgent System Overview In a LLM-powered autonomous agent system, LLM functions as the agent’s brain, complemented by several key components:', 'language': 'en', 'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/', 'title': "LLM Powered Autonomous Agents | Lil'Log"})  
    


```
[/code]


## Model​

### LLaMA2​

Note: new versions of `llama-cpp-python` use GGUF model files (see here).

If you have an existing GGML model, see here for instructions for conversion for GGUF.

And / or, you can download a GGUF converted model (e.g., here).

Finally, as noted in detail here install `llama-cpp-python`

[code]
```python




    pip install llama-cpp-python  
    


```
[/code]


To enable use of GPU on Apple Silicon, follow the steps here to use the Python binding `with Metal support`.

In particular, ensure that `conda` is using the correct virtual environment that you created (`miniforge3`).

E.g., for me:

[code]
```python




    conda activate /Users/rlm/miniforge3/envs/llama  
    


```
[/code]


With this confirmed:

[code]
```python




    CMAKE_ARGS="-DLLAMA_METAL=on" FORCE_CMAKE=1 /Users/rlm/miniforge3/envs/llama/bin/pip install -U llama-cpp-python --no-cache-dir  
    


```
[/code]


[code]
```python




    from langchain.callbacks.manager import CallbackManager  
    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    from langchain.llms import LlamaCpp  
    


```
[/code]


Setting model parameters as noted in the llama.cpp docs.

[code]
```python




    n_gpu_layers = 1  # Metal set to 1 is enough.  
    n_batch = 512  # Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.  
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])  
      
    # Make sure the model path is correct for your system!  
    llm = LlamaCpp(  
        model_path="/Users/rlm/Desktop/Code/llama.cpp/models/llama-2-13b-chat.ggufv3.q4_0.bin",  
        n_gpu_layers=n_gpu_layers,  
        n_batch=n_batch,  
        n_ctx=2048,  
        f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls  
        callback_manager=callback_manager,  
        verbose=True,  
    )  
    


```
[/code]


Note that these indicate that Metal was enabled properly:

[code]
```python




    ggml_metal_init: allocating  
    ggml_metal_init: using MPS  
    


```
[/code]


[code]
```python




    llm("Simulate a rap battle between Stephen Colbert and John Oliver")  
    


```
[/code]


[code]
```python




        Llama.generate: prefix-match hit  
      
      
        by jonathan   
          
        Here's the hypothetical rap battle:  
          
        [Stephen Colbert]: Yo, this is Stephen Colbert, known for my comedy show. I'm here to put some sense in your mind, like an enema do-go. Your opponent? A man of laughter and witty quips, John Oliver! Now let's see who gets the most laughs while taking shots at each other  
          
        [John Oliver]: Yo, this is John Oliver, known for my own comedy show. I'm here to take your mind on an adventure through wit and humor. But first, allow me to you to our contestant: Stephen Colbert! His show has been around since the '90s, but it's time to see who can out-rap whom  
          
        [Stephen Colbert]: You claim to be a witty man, John Oliver, with your British charm and clever remarks. But my knows that I'm America's funnyman! Who's the one taking you? Nobody!  
          
        [John Oliver]: Hey Stephen Colbert, don't get too cocky. You may  
      
          
        llama_print_timings:        load time =  4481.74 ms  
        llama_print_timings:      sample time =   183.05 ms /   256 runs   (    0.72 ms per token,  1398.53 tokens per second)  
        llama_print_timings: prompt eval time =   456.05 ms /    13 tokens (   35.08 ms per token,    28.51 tokens per second)  
        llama_print_timings:        eval time =  7375.20 ms /   255 runs   (   28.92 ms per token,    34.58 tokens per second)  
        llama_print_timings:       total time =  8388.92 ms  
      
      
      
      
      
        "by jonathan \n\nHere's the hypothetical rap battle:\n\n[Stephen Colbert]: Yo, this is Stephen Colbert, known for my comedy show. I'm here to put some sense in your mind, like an enema do-go. Your opponent? A man of laughter and witty quips, John Oliver! Now let's see who gets the most laughs while taking shots at each other\n\n[John Oliver]: Yo, this is John Oliver, known for my own comedy show. I'm here to take your mind on an adventure through wit and humor. But first, allow me to you to our contestant: Stephen Colbert! His show has been around since the '90s, but it's time to see who can out-rap whom\n\n[Stephen Colbert]: You claim to be a witty man, John Oliver, with your British charm and clever remarks. But my knows that I'm America's funnyman! Who's the one taking you? Nobody!\n\n[John Oliver]: Hey Stephen Colbert, don't get too cocky. You may"  
    


```
[/code]


### GPT4All​

Similarly, we can use `GPT4All`.

Download the GPT4All model binary.

The Model Explorer on the GPT4All is a great way to choose and download a model.

Then, specify the path that you downloaded to to.

E.g., for me, the model lives here:

`/Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin`

[code]
```python




    from langchain.llms import GPT4All  
      
    llm = GPT4All(  
        model="/Users/rlm/Desktop/Code/gpt4all/models/nous-hermes-13b.ggmlv3.q4_0.bin",  
        max_tokens=2048,  
    )  
    


```
[/code]


## LLMChain​

Run an `LLMChain` (see here) with either model by passing in the retrieved docs and a simple prompt.

It formats the prompt template using the input key values provided and passes the formatted string to `GPT4All`, `LLama-V2`, or another specified LLM.

In this case, the list of retrieved documents (`docs`) above are pass into `{context}`.

[code]
```python




    from langchain.chains import LLMChain  
    from langchain.prompts import PromptTemplate  
      
    # Prompt  
    prompt = PromptTemplate.from_template(  
        "Summarize the main themes in these retrieved docs: {docs}"  
    )  
      
    # Chain  
    llm_chain = LLMChain(llm=llm, prompt=prompt)  
      
    # Run  
    question = "What are the approaches to Task Decomposition?"  
    docs = vectorstore.similarity_search(question)  
    result = llm_chain(docs)  
      
    # Output  
    result["text"]  
    


```
[/code]


[code]
```python




        Llama.generate: prefix-match hit  
      
      
          
        Based on the retrieved documents, the main themes are:  
        1. Task decomposition: The ability to break down complex tasks into smaller subtasks, which can be handled by an LLM or other components of the agent system.  
        2. LLM as the core controller: The use of a large language model (LLM) as the primary controller of an autonomous agent system, complemented by other key components such as a knowledge graph and a planner.  
        3. Potentiality of LLM: The idea that LLMs have the potential to be used as powerful general problem solvers, not just for generating well-written copies but also for solving complex tasks and achieving human-like intelligence.  
        4. Challenges in long-term planning: The challenges in planning over a lengthy history and effectively exploring the solution space, which are important limitations of current LLM-based autonomous agent systems.  
      
          
        llama_print_timings:        load time =  1191.88 ms  
        llama_print_timings:      sample time =   134.47 ms /   193 runs   (    0.70 ms per token,  1435.25 tokens per second)  
        llama_print_timings: prompt eval time = 39470.18 ms /  1055 tokens (   37.41 ms per token,    26.73 tokens per second)  
        llama_print_timings:        eval time =  8090.85 ms /   192 runs   (   42.14 ms per token,    23.73 tokens per second)  
        llama_print_timings:       total time = 47943.12 ms  
      
      
      
      
      
        '\nBased on the retrieved documents, the main themes are:\n1. Task decomposition: The ability to break down complex tasks into smaller subtasks, which can be handled by an LLM or other components of the agent system.\n2. LLM as the core controller: The use of a large language model (LLM) as the primary controller of an autonomous agent system, complemented by other key components such as a knowledge graph and a planner.\n3. Potentiality of LLM: The idea that LLMs have the potential to be used as powerful general problem solvers, not just for generating well-written copies but also for solving complex tasks and achieving human-like intelligence.\n4. Challenges in long-term planning: The challenges in planning over a lengthy history and effectively exploring the solution space, which are important limitations of current LLM-based autonomous agent systems.'  
    


```
[/code]


## QA Chain​

We can use a `QA chain` to handle our question above.

`chain_type="stuff"` (see here) means that all the docs will be added (stuffed) into a prompt.

We can also use the LangChain Prompt Hub to store and fetch prompts that are model-specific.

This will work with your LangSmith API key.

Let's try with a default RAG prompt, here.

[code]
```python




    pip install langchainhub  
    


```
[/code]


[code]
```python




    # Prompt  
    from langchain import hub  
      
    rag_prompt = hub.pull("rlm/rag-prompt")  
    from langchain.chains.question_answering import load_qa_chain  
      
    # Chain  
    chain = load_qa_chain(llm, chain_type="stuff", prompt=rag_prompt)  
    # Run  
    chain({"input_documents": docs, "question": question}, return_only_outputs=True)  
    


```
[/code]


[code]
```python




        Llama.generate: prefix-match hit  
      
      
          
        Task can be done by down a task into smaller subtasks, using simple prompting like "Steps for XYZ." or task-specific like "Write a story outline" for writing a novel.  
      
          
        llama_print_timings:        load time = 11326.20 ms  
        llama_print_timings:      sample time =    33.03 ms /    47 runs   (    0.70 ms per token,  1422.86 tokens per second)  
        llama_print_timings: prompt eval time =  1387.31 ms /   242 tokens (    5.73 ms per token,   174.44 tokens per second)  
        llama_print_timings:        eval time =  1321.62 ms /    46 runs   (   28.73 ms per token,    34.81 tokens per second)  
        llama_print_timings:       total time =  2801.08 ms  
      
      
      
      
      
        {'output_text': '\nTask can be done by down a task into smaller subtasks, using simple prompting like "Steps for XYZ." or task-specific like "Write a story outline" for writing a novel.'}  
    


```
[/code]


Now, let's try with a prompt specifically for LLaMA, which includes special tokens.

[code]
```python




    # Prompt  
    rag_prompt_llama = hub.pull("rlm/rag-prompt-llama")  
    rag_prompt_llama  
    


```
[/code]


[code]
```python




        ChatPromptTemplate(input_variables=['question', 'context'], output_parser=None, partial_variables={}, messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['question', 'context'], output_parser=None, partial_variables={}, template="[INST]<<SYS>> You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.<</SYS>> \nQuestion: {question} \nContext: {context} \nAnswer: [/INST]", template_format='f-string', validate_template=True), additional_kwargs={})])  
    


```
[/code]


[code]
```python




    # Chain  
    chain = load_qa_chain(llm, chain_type="stuff", prompt=rag_prompt_llama)  
    # Run  
    chain({"input_documents": docs, "question": question}, return_only_outputs=True)  
    


```
[/code]


[code]
```python




        Llama.generate: prefix-match hit  
      
      
          Sure, I'd be happy to help! Based on the context, here are some to task:  
          
        1. LLM with simple prompting: This using a large model (LLM) with simple prompts like "Steps for XYZ" or "What are the subgoals for achieving XYZ?" to decompose tasks into smaller steps.  
        2. Task-specific: Another is to use task-specific, such as "Write a story outline" for writing a novel, to guide the of tasks.  
        3. Human inputs:, human inputs can be used to supplement the process, in cases where the task a high degree of creativity or expertise.  
          
        As fores in long-term and task, one major is that LLMs to adjust plans when faced with errors, making them less robust to humans who learn from trial and error.  
      
          
        llama_print_timings:        load time = 11326.20 ms  
        llama_print_timings:      sample time =   144.81 ms /   207 runs   (    0.70 ms per token,  1429.47 tokens per second)  
        llama_print_timings: prompt eval time =  1506.13 ms /   258 tokens (    5.84 ms per token,   171.30 tokens per second)  
        llama_print_timings:        eval time =  6231.92 ms /   206 runs   (   30.25 ms per token,    33.06 tokens per second)  
        llama_print_timings:       total time =  8158.41 ms  
      
      
      
      
      
        {'output_text': '  Sure, I\'d be happy to help! Based on the context, here are some to task:\n\n1. LLM with simple prompting: This using a large model (LLM) with simple prompts like "Steps for XYZ" or "What are the subgoals for achieving XYZ?" to decompose tasks into smaller steps.\n2. Task-specific: Another is to use task-specific, such as "Write a story outline" for writing a novel, to guide the of tasks.\n3. Human inputs:, human inputs can be used to supplement the process, in cases where the task a high degree of creativity or expertise.\n\nAs fores in long-term and task, one major is that LLMs to adjust plans when faced with errors, making them less robust to humans who learn from trial and error.'}  
    


```
[/code]


## RetrievalQA​

For an even simpler flow, use `RetrievalQA`.

This will use a QA default prompt (shown here) and will retrieve from the vectorDB.

But, you can still pass in a prompt, as before, if desired.

[code]
```python




    from langchain.chains import RetrievalQA  
      
    qa_chain = RetrievalQA.from_chain_type(  
        llm,  
        retriever=vectorstore.as_retriever(),  
        chain_type_kwargs={"prompt": rag_prompt_llama},  
    )  
    


```
[/code]


[code]
```python




    qa_chain({"query": question})  
    


```
[/code]


[code]
```python




        Llama.generate: prefix-match hit  
      
      
          Sure! Based on the context, here's my answer to your:  
          
        There are several to task,:  
          
        1. LLM-based with simple prompting, such as "Steps for XYZ" or "What are the subgoals for achieving XYZ?"  
        2. Task-specific, like "Write a story outline" for writing a novel.  
        3. Human inputs to guide the process.  
          
        These can be used to decompose complex tasks into smaller, more manageable subtasks, which can help improve the and effectiveness of task. However, long-term and task can being due to the need to plan over a lengthy history and explore the space., LLMs may to adjust plans when faced with errors, making them less robust to human learners who can learn from trial and error.  
      
          
        llama_print_timings:        load time = 11326.20 ms  
        llama_print_timings:      sample time =   139.20 ms /   200 runs   (    0.70 ms per token,  1436.76 tokens per second)  
        llama_print_timings: prompt eval time =  1532.26 ms /   258 tokens (    5.94 ms per token,   168.38 tokens per second)  
        llama_print_timings:        eval time =  5977.62 ms /   199 runs   (   30.04 ms per token,    33.29 tokens per second)  
        llama_print_timings:       total time =  7916.21 ms  
      
      
      
      
      
        {'query': 'What are the approaches to Task Decomposition?',  
         'result': '  Sure! Based on the context, here\'s my answer to your:\n\nThere are several to task,:\n\n1. LLM-based with simple prompting, such as "Steps for XYZ" or "What are the subgoals for achieving XYZ?"\n2. Task-specific, like "Write a story outline" for writing a novel.\n3. Human inputs to guide the process.\n\nThese can be used to decompose complex tasks into smaller, more manageable subtasks, which can help improve the and effectiveness of task. However, long-term and task can being due to the need to plan over a lengthy history and explore the space., LLMs may to adjust plans when faced with errors, making them less robust to human learners who can learn from trial and error.'}  
    


```
[/code]


