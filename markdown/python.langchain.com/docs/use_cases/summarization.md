

Skip to main content

On this page

## Use case​

Suppose you have a set of documents (PDFs, Notion pages, customer questions, etc.) and you want to summarize the content.

LLMs are a great tool for this given their proficiency in understanding and synthesizing text.

In this walkthrough we'll go over how to perform document summarization using LLMs.

## Overview​

A central question for building a summarizer is how to pass your documents into the LLM's context window. Two common approaches for this are:

  1. `Stuff`: Simply "stuff" all your documents into a single prompt. This is the simplest approach (see here for more on the `StuffDocumentsChains`, which is used for this method).

  2. `Map-reduce`: Summarize each document on it's own in a "map" step and then "reduce" the summaries into a final summary (see here for more on the `MapReduceDocumentsChain`, which is used for this method).

## Quickstart​

To give you a sneak preview, either pipeline can be wrapped in a single object: `load_summarize_chain`.

Suppose we want to summarize a blog post. We can create this in a few lines of code.

First set environment variables and install packages:

[code]
```python




    pip install openai tiktoken chromadb langchain  
      
    # Set env var OPENAI_API_KEY or load from a .env file  
    # import dotenv  
      
    # dotenv.load_dotenv()  
    


```
[/code]


[code]
```python




        Requirement already satisfied: openai in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (0.27.8)  
        Requirement already satisfied: tiktoken in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (0.4.0)  
        Requirement already satisfied: chromadb in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (0.4.4)  
        Requirement already satisfied: langchain in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (0.0.299)  
        Requirement already satisfied: requests>=2.20 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from openai) (2.31.0)  
        Requirement already satisfied: tqdm in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from openai) (4.64.1)  
        Requirement already satisfied: aiohttp in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from openai) (3.8.5)  
        Requirement already satisfied: regex>=2022.1.18 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from tiktoken) (2023.6.3)  
        Requirement already satisfied: pydantic<2.0,>=1.9 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (1.10.12)  
        Requirement already satisfied: chroma-hnswlib==0.7.2 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (0.7.2)  
        Requirement already satisfied: fastapi<0.100.0,>=0.95.2 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (0.99.1)  
        Requirement already satisfied: uvicorn[standard]>=0.18.3 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (0.23.2)  
        Requirement already satisfied: numpy>=1.21.6 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (1.24.4)  
        Requirement already satisfied: posthog>=2.4.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (3.0.1)  
        Requirement already satisfied: typing-extensions>=4.5.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (4.7.1)  
        Requirement already satisfied: pulsar-client>=3.1.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (3.2.0)  
        Requirement already satisfied: onnxruntime>=1.14.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (1.15.1)  
        Requirement already satisfied: tokenizers>=0.13.2 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (0.13.3)  
        Requirement already satisfied: pypika>=0.48.9 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (0.48.9)  
        Collecting tqdm (from openai)  
          Obtaining dependency information for tqdm from https://files.pythonhosted.org/packages/00/e5/f12a80907d0884e6dff9c16d0c0114d81b8cd07dc3ae54c5e962cc83037e/tqdm-4.66.1-py3-none-any.whl.metadata  
          Downloading tqdm-4.66.1-py3-none-any.whl.metadata (57 kB)  
             ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.6/57.6 kB 2.7 MB/s eta 0:00:00  
        Requirement already satisfied: overrides>=7.3.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (7.4.0)  
        Requirement already satisfied: importlib-resources in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from chromadb) (6.0.0)  
        Requirement already satisfied: PyYAML>=5.3 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (6.0.1)  
        Requirement already satisfied: SQLAlchemy<3,>=1.4 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (2.0.20)  
        Requirement already satisfied: anyio<4.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (3.7.1)  
        Requirement already satisfied: async-timeout<5.0.0,>=4.0.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (4.0.3)  
        Requirement already satisfied: dataclasses-json<0.7,>=0.5.7 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (0.5.9)  
        Requirement already satisfied: jsonpatch<2.0,>=1.33 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (1.33)  
        Requirement already satisfied: langsmith<0.1.0,>=0.0.38 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (0.0.42)  
        Requirement already satisfied: numexpr<3.0.0,>=2.8.4 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (2.8.5)  
        Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from langchain) (8.2.3)  
        Requirement already satisfied: attrs>=17.3.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (23.1.0)  
        Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (3.2.0)  
        Requirement already satisfied: multidict<7.0,>=4.5 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (6.0.4)  
        Requirement already satisfied: yarl<2.0,>=1.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (1.9.2)  
        Requirement already satisfied: frozenlist>=1.1.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (1.4.0)  
        Requirement already satisfied: aiosignal>=1.1.2 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from aiohttp->openai) (1.3.1)  
        Requirement already satisfied: idna>=2.8 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from anyio<4.0->langchain) (3.4)  
        Requirement already satisfied: sniffio>=1.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from anyio<4.0->langchain) (1.3.0)  
        Requirement already satisfied: exceptiongroup in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from anyio<4.0->langchain) (1.1.3)  
        Requirement already satisfied: marshmallow<4.0.0,>=3.3.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from dataclasses-json<0.7,>=0.5.7->langchain) (3.20.1)  
        Requirement already satisfied: marshmallow-enum<2.0.0,>=1.5.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from dataclasses-json<0.7,>=0.5.7->langchain) (1.5.1)  
        Requirement already satisfied: typing-inspect>=0.4.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from dataclasses-json<0.7,>=0.5.7->langchain) (0.9.0)  
        Requirement already satisfied: starlette<0.28.0,>=0.27.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from fastapi<0.100.0,>=0.95.2->chromadb) (0.27.0)  
        Requirement already satisfied: jsonpointer>=1.9 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from jsonpatch<2.0,>=1.33->langchain) (2.4)  
        Requirement already satisfied: coloredlogs in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from onnxruntime>=1.14.1->chromadb) (15.0.1)  
        Requirement already satisfied: flatbuffers in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from onnxruntime>=1.14.1->chromadb) (23.5.26)  
        Requirement already satisfied: packaging in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from onnxruntime>=1.14.1->chromadb) (23.1)  
        Requirement already satisfied: protobuf in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from onnxruntime>=1.14.1->chromadb) (4.23.4)  
        Requirement already satisfied: sympy in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from onnxruntime>=1.14.1->chromadb) (1.12)  
        Requirement already satisfied: six>=1.5 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from posthog>=2.4.0->chromadb) (1.16.0)  
        Requirement already satisfied: monotonic>=1.5 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from posthog>=2.4.0->chromadb) (1.6)  
        Requirement already satisfied: backoff>=1.10.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from posthog>=2.4.0->chromadb) (2.2.1)  
        Requirement already satisfied: python-dateutil>2.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from posthog>=2.4.0->chromadb) (2.8.2)  
        Requirement already satisfied: certifi in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from pulsar-client>=3.1.0->chromadb) (2023.7.22)  
        Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from requests>=2.20->openai) (1.26.16)  
        Requirement already satisfied: click>=7.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from uvicorn[standard]>=0.18.3->chromadb) (8.1.7)  
        Requirement already satisfied: h11>=0.8 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.14.0)  
        Requirement already satisfied: httptools>=0.5.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.6.0)  
        Requirement already satisfied: python-dotenv>=0.13 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from uvicorn[standard]>=0.18.3->chromadb) (1.0.0)  
        Requirement already satisfied: uvloop!=0.15.0,!=0.15.1,>=0.14.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.17.0)  
        Requirement already satisfied: watchfiles>=0.13 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from uvicorn[standard]>=0.18.3->chromadb) (0.19.0)  
        Requirement already satisfied: websockets>=10.4 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from uvicorn[standard]>=0.18.3->chromadb) (11.0.3)  
        Requirement already satisfied: zipp>=3.1.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from importlib-resources->chromadb) (3.16.2)  
        Requirement already satisfied: mypy-extensions>=0.3.0 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from typing-inspect>=0.4.0->dataclasses-json<0.7,>=0.5.7->langchain) (1.0.0)  
        Requirement already satisfied: humanfriendly>=9.1 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from coloredlogs->onnxruntime>=1.14.1->chromadb) (10.0)  
        Requirement already satisfied: mpmath>=0.19 in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (from sympy->onnxruntime>=1.14.1->chromadb) (1.3.0)  
        Using cached tqdm-4.66.1-py3-none-any.whl (78 kB)  
        Installing collected packages: tqdm  
          Attempting uninstall: tqdm  
            Found existing installation: tqdm 4.64.1  
            Uninstalling tqdm-4.64.1:  
              Successfully uninstalled tqdm-4.64.1  
        ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.  
        clarifai 9.8.1 requires tqdm==4.64.1, but you have tqdm 4.66.1 which is incompatible.  
        Successfully installed tqdm-4.66.1  
    


```
[/code]


We can use `chain_type="stuff"`, especially if using larger context window models such as:

  * 16k token OpenAI `gpt-3.5-turbo-1106`
  * 100k token Anthropic Claude-2

We can also supply `chain_type="map_reduce"` or `chain_type="refine"` (read more here).

[code]
```python




    from langchain.chains.summarize import load_summarize_chain  
    from langchain.chat_models import ChatOpenAI  
    from langchain.document_loaders import WebBaseLoader  
      
    loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")  
    docs = loader.load()  
      
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")  
    chain = load_summarize_chain(llm, chain_type="stuff")  
      
    chain.run(docs)  
    


```
[/code]


[code]
```python




        'The article discusses the concept of building autonomous agents powered by large language models (LLMs). It explores the components of such agents, including planning, memory, and tool use. The article provides case studies and proof-of-concept examples of LLM-powered agents in various domains. It also highlights the challenges and limitations of using LLMs in agent systems.'  
    


```
[/code]


## Option 1. Stuff​

When we use `load_summarize_chain` with `chain_type="stuff"`, we will use the StuffDocumentsChain.

The chain will take a list of documents, inserts them all into a prompt, and passes that prompt to an LLM:

[code]
```python




    from langchain.chains.combine_documents.stuff import StuffDocumentsChain  
    from langchain.chains.llm import LLMChain  
    from langchain.prompts import PromptTemplate  
      
    # Define prompt  
    prompt_template = """Write a concise summary of the following:  
    "{text}"  
    CONCISE SUMMARY:"""  
    prompt = PromptTemplate.from_template(prompt_template)  
      
    # Define LLM chain  
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")  
    llm_chain = LLMChain(llm=llm, prompt=prompt)  
      
    # Define StuffDocumentsChain  
    stuff_chain = StuffDocumentsChain(llm_chain=llm_chain, document_variable_name="text")  
      
    docs = loader.load()  
    print(stuff_chain.run(docs))  
    


```
[/code]


[code]
```python




        The article discusses the concept of building autonomous agents powered by large language models (LLMs). It explores the components of such agents, including planning, memory, and tool use. The article provides case studies and proof-of-concept examples of LLM-powered agents in various domains, such as scientific discovery and generative agents simulation. It also highlights the challenges and limitations of using LLMs in agent systems.  
    


```
[/code]


Great! We can see that we reproduce the earlier result using the `load_summarize_chain`.

### Go deeper​

  * You can easily customize the prompt. 
  * You can easily try different LLMs, (e.g., Claude) via the `llm` parameter.

## Option 2. Map-Reduce​

Let's unpack the map reduce approach. For this, we'll first map each document to an individual summary using an `LLMChain`. Then we'll use a `ReduceDocumentsChain` to combine those summaries into a
single global summary.

First, we specify the LLMChain to use for mapping each document to an individual summary:

[code]
```python




    from langchain.chains import MapReduceDocumentsChain, ReduceDocumentsChain  
    from langchain.text_splitter import CharacterTextSplitter  
      
    llm = ChatOpenAI(temperature=0)  
      
    # Map  
    map_template = """The following is a set of documents  
    {docs}  
    Based on this list of docs, please identify the main themes   
    Helpful Answer:"""  
    map_prompt = PromptTemplate.from_template(map_template)  
    map_chain = LLMChain(llm=llm, prompt=map_prompt)  
    


```
[/code]


We can also use the Prompt Hub to store and fetch prompts.

This will work with your LangSmith API key.

For example, see the map prompt here.

[code]
```python




    from langchain import hub  
      
    map_prompt = hub.pull("rlm/map-prompt")  
    map_chain = LLMChain(llm=llm, prompt=map_prompt)  
    


```
[/code]


The `ReduceDocumentsChain` handles taking the document mapping results and reducing them into a single output. It wraps a generic `CombineDocumentsChain` (like `StuffDocumentsChain`) but adds the
ability to collapse documents before passing it to the `CombineDocumentsChain` if their cumulative size exceeds `token_max`. In this example, we can actually re-use our chain for combining our docs to
also collapse our docs.

So if the cumulative number of tokens in our mapped documents exceeds 4000 tokens, then we'll recursively pass in the documents in batches of < 4000 tokens to our `StuffDocumentsChain` to create
batched summaries. And once those batched summaries are cumulatively less than 4000 tokens, we'll pass them all one last time to the `StuffDocumentsChain` to create the final summary.

[code]
```python




    # Reduce  
    reduce_template = """The following is set of summaries:  
    {docs}  
    Take these and distill it into a final, consolidated summary of the main themes.   
    Helpful Answer:"""  
    reduce_prompt = PromptTemplate.from_template(reduce_template)  
    


```
[/code]


[code]
```python




    # Note we can also get this from the prompt hub, as noted above  
    reduce_prompt = hub.pull("rlm/map-prompt")  
    


```
[/code]


[code]
```python




    reduce_prompt  
    


```
[/code]


[code]
```python




        ChatPromptTemplate(input_variables=['docs'], messages=[HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['docs'], template='The following is a set of documents:\n{docs}\nBased on this list of docs, please identify the main themes \nHelpful Answer:'))])  
    


```
[/code]


[code]
```python




    # Run chain  
    reduce_chain = LLMChain(llm=llm, prompt=reduce_prompt)  
      
    # Takes a list of documents, combines them into a single string, and passes this to an LLMChain  
    combine_documents_chain = StuffDocumentsChain(  
        llm_chain=reduce_chain, document_variable_name="docs"  
    )  
      
    # Combines and iteravely reduces the mapped documents  
    reduce_documents_chain = ReduceDocumentsChain(  
        # This is final chain that is called.  
        combine_documents_chain=combine_documents_chain,  
        # If documents exceed context for `StuffDocumentsChain`  
        collapse_documents_chain=combine_documents_chain,  
        # The maximum number of tokens to group documents into.  
        token_max=4000,  
    )  
    


```
[/code]


Combining our map and reduce chains into one:

[code]
```python




    # Combining documents by mapping a chain over them, then combining results  
    map_reduce_chain = MapReduceDocumentsChain(  
        # Map chain  
        llm_chain=map_chain,  
        # Reduce chain  
        reduce_documents_chain=reduce_documents_chain,  
        # The variable name in the llm_chain to put the documents in  
        document_variable_name="docs",  
        # Return the results of the map steps in the output  
        return_intermediate_steps=False,  
    )  
      
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(  
        chunk_size=1000, chunk_overlap=0  
    )  
    split_docs = text_splitter.split_documents(docs)  
    


```
[/code]


[code]
```python




        Created a chunk of size 1003, which is longer than the specified 1000  
    


```
[/code]


[code]
```python




    print(map_reduce_chain.run(split_docs))  
    


```
[/code]


[code]
```python




        Based on the list of documents provided, the main themes can be identified as follows:  
          
        1. LLM-powered autonomous agents: The documents discuss the concept of building agents with LLM as their core controller and highlight the potential of LLM beyond generating written content. They explore the capabilities of LLM as a general problem solver.  
          
        2. Agent system overview: The documents provide an overview of the components that make up a LLM-powered autonomous agent system, including planning, memory, and tool use. Each component is explained in detail, highlighting its role in enhancing the agent's capabilities.  
          
        3. Planning: The documents discuss how the agent breaks down large tasks into smaller subgoals and utilizes self-reflection to improve the quality of its actions and results.  
          
        4. Memory: The documents explain the importance of both short-term and long-term memory in an agent system. Short-term memory is utilized for in-context learning, while long-term memory allows the agent to retain and recall information over extended periods.  
          
        5. Tool use: The documents highlight the agent's ability to call external APIs for additional information and resources that may be missing from its pre-trained model weights. This includes accessing current information, executing code, and retrieving proprietary information.  
          
        6. Case studies and proof-of-concept examples: The documents provide examples of how LLM-powered autonomous agents can be applied in various domains, such as scientific discovery and generative agent simulations. These case studies serve as examples of the capabilities and potential applications of such agents.  
          
        7. Challenges: The documents acknowledge the challenges associated with building and utilizing LLM-powered autonomous agents, although specific challenges are not mentioned in the given set of documents.  
          
        8. Citation and references: The documents include a citation and reference section, indicating that the information presented is based on existing research and sources.  
          
        Overall, the main themes in the provided documents revolve around LLM-powered autonomous agents, their components and capabilities, planning, memory, tool use, case studies, and challenges.  
    


```
[/code]


### Go deeper​

 **Customization**

  * As shown above, you can customize the LLMs and prompts for map and reduce stages.

 **Real-world use-case**

  * See this blog post case-study on analyzing user interactions (questions about LangChain documentation)! 
  * The blog post and associated repo also introduce clustering as a means of summarization.
  * This opens up a third path beyond the `stuff` or `map-reduce` approaches that is worth considering.

## Option 3. Refine​

Refine is similar to map-reduce:

> The refine documents chain constructs a response by looping over the input documents and iteratively updating its answer. For each document, it passes all non-document inputs, the current document,
> and the latest intermediate answer to an LLM chain to get a new answer.

This can be easily run with the `chain_type="refine"` specified.

[code]
```python




    chain = load_summarize_chain(llm, chain_type="refine")  
    chain.run(split_docs)  
    


```
[/code]


[code]
```python




        'The article explores the concept of building autonomous agents powered by large language models (LLMs) and their potential as problem solvers. It discusses different approaches to task decomposition, the integration of self-reflection into LLM-based agents, and the use of external classical planners for long-horizon planning. The new context introduces the Chain of Hindsight (CoH) approach and Algorithm Distillation (AD) for training models to produce better outputs. It also discusses different types of memory and the use of external memory for fast retrieval. The article explores the concept of tool use and introduces the MRKL system and experiments on fine-tuning LLMs to use external tools. It introduces HuggingGPT, a framework that uses ChatGPT as a task planner, and discusses the challenges of using LLM-powered agents in real-world scenarios. The article concludes with case studies on scientific discovery agents and the use of LLM-powered agents in anticancer drug discovery. It also introduces the concept of generative agents that combine LLM with memory, planning, and reflection mechanisms. The conversation samples provided discuss the implementation of a game architecture and the challenges in building LLM-centered agents. The article provides references to related research papers and resources for further exploration.'  
    


```
[/code]


It's also possible to supply a prompt and return intermediate steps.

[code]
```python




    prompt_template = """Write a concise summary of the following:  
    {text}  
    CONCISE SUMMARY:"""  
    prompt = PromptTemplate.from_template(prompt_template)  
      
    refine_template = (  
        "Your job is to produce a final summary\n"  
        "We have provided an existing summary up to a certain point: {existing_answer}\n"  
        "We have the opportunity to refine the existing summary"  
        "(only if needed) with some more context below.\n"  
        "------------\n"  
        "{text}\n"  
        "------------\n"  
        "Given the new context, refine the original summary in Italian"  
        "If the context isn't useful, return the original summary."  
    )  
    refine_prompt = PromptTemplate.from_template(refine_template)  
    chain = load_summarize_chain(  
        llm=llm,  
        chain_type="refine",  
        question_prompt=prompt,  
        refine_prompt=refine_prompt,  
        return_intermediate_steps=True,  
        input_key="input_documents",  
        output_key="output_text",  
    )  
    result = chain({"input_documents": split_docs}, return_only_outputs=True)  
    


```
[/code]


[code]
```python




    print(result["output_text"])  
    


```
[/code]


[code]
```python




        Il presente articolo discute il concetto di costruire agenti autonomi utilizzando LLM (large language model) come controller principale. Esplora i diversi componenti di un sistema di agenti alimentato da LLM, tra cui la pianificazione, la memoria e l'uso degli strumenti. Dimostrazioni di concetto come AutoGPT mostrano il potenziale di LLM come risolutore generale di problemi. Approcci come Chain of Thought, Tree of Thoughts, LLM+P, ReAct e Reflexion consentono agli agenti autonomi di pianificare, riflettere su se stessi e migliorarsi iterativamente. Tuttavia, ci sono sfide da affrontare, come la limitata capacità di contesto che limita l'inclusione di informazioni storiche dettagliate e la difficoltà di pianificazione a lungo termine e decomposizione delle attività. Inoltre, l'affidabilità dell'interfaccia di linguaggio naturale tra LLM e componenti esterni come la memoria e gli strumenti è incerta, poiché i LLM possono commettere errori di formattazione e mostrare comportamenti ribelli. Nonostante ciò, il sistema AutoGPT viene menzionato come esempio di dimostrazione di concetto che utilizza LLM come controller principale per agenti autonomi. Questo articolo fa riferimento a diverse fonti che esplorano approcci e applicazioni specifiche di LLM nell'ambito degli agenti autonomi.  
    


```
[/code]


[code]
```python




    print("\n\n".join(result["intermediate_steps"][:3]))  
    


```
[/code]


[code]
```python




        This article discusses the concept of building autonomous agents using LLM (large language model) as the core controller. The article explores the different components of an LLM-powered agent system, including planning, memory, and tool use. It also provides examples of proof-of-concept demos and highlights the potential of LLM as a general problem solver.  
          
        Questo articolo discute del concetto di costruire agenti autonomi utilizzando LLM (large language model) come controller principale. L'articolo esplora i diversi componenti di un sistema di agenti alimentato da LLM, inclusa la pianificazione, la memoria e l'uso degli strumenti. Vengono forniti anche esempi di dimostrazioni di proof-of-concept e si evidenzia il potenziale di LLM come risolutore generale di problemi. Inoltre, vengono presentati approcci come Chain of Thought, Tree of Thoughts, LLM+P, ReAct e Reflexion che consentono agli agenti autonomi di pianificare, riflettere su se stessi e migliorare iterativamente.  
          
        Questo articolo discute del concetto di costruire agenti autonomi utilizzando LLM (large language model) come controller principale. L'articolo esplora i diversi componenti di un sistema di agenti alimentato da LLM, inclusa la pianificazione, la memoria e l'uso degli strumenti. Vengono forniti anche esempi di dimostrazioni di proof-of-concept e si evidenzia il potenziale di LLM come risolutore generale di problemi. Inoltre, vengono presentati approcci come Chain of Thought, Tree of Thoughts, LLM+P, ReAct e Reflexion che consentono agli agenti autonomi di pianificare, riflettere su se stessi e migliorare iterativamente. Il nuovo contesto riguarda l'approccio Chain of Hindsight (CoH) che permette al modello di migliorare autonomamente i propri output attraverso un processo di apprendimento supervisionato. Viene anche presentato l'approccio Algorithm Distillation (AD) che applica lo stesso concetto alle traiettorie di apprendimento per compiti di reinforcement learning.  
    


```
[/code]


## Splitting and summarizing in a single chain​

For convenience, we can wrap both the text splitting of our long document and summarizing in a single `AnalyzeDocumentsChain`.

[code]
```python




    from langchain.chains import AnalyzeDocumentChain  
      
    summarize_document_chain = AnalyzeDocumentChain(  
        combine_docs_chain=chain, text_splitter=text_splitter  
    )  
    summarize_document_chain.run(docs[0].page_content)  
    


```
[/code]


[code]
```python




        ---------------------------------------------------------------------------  
      
        ValueError                                Traceback (most recent call last)  
      
        Cell In[17], line 4  
              1 from langchain.chains import AnalyzeDocumentChain  
              3 summarize_document_chain = AnalyzeDocumentChain(combine_docs_chain=chain, text_splitter=text_splitter)  
        ----> 4 summarize_document_chain.run(docs[0])  
      
      
        File ~/langchain/libs/langchain/langchain/chains/base.py:496, in Chain.run(self, callbacks, tags, metadata, *args, **kwargs)  
            459 """Convenience method for executing chain.  
            460   
            461 The main difference between this method and `Chain.__call__` is that this  
           (...)  
            493         # -> "The temperature in Boise is..."  
            494 """  
            495 # Run at start to make sure this is possible/defined  
        --> 496 _output_key = self._run_output_key  
            498 if args and not kwargs:  
            499     if len(args) != 1:  
      
      
        File ~/langchain/libs/langchain/langchain/chains/base.py:445, in Chain._run_output_key(self)  
            442 @property  
            443 def _run_output_key(self) -> str:  
            444     if len(self.output_keys) != 1:  
        --> 445         raise ValueError(  
            446             f"`run` not supported when there is not exactly "  
            447             f"one output key. Got {self.output_keys}."  
            448         )  
            449     return self.output_keys[0]  
      
      
        ValueError: `run` not supported when there is not exactly one output key. Got ['output_text', 'intermediate_steps'].  
    


```
[/code]


