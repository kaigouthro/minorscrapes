

Skip to main content

On this page

# Retrieval-augmented generation (RAG)

## Overview​

### What is RAG?​

RAG is a technique for augmenting LLM knowledge with additional, often private or real-time, data.

LLMs can reason about wide-ranging topics, but their knowledge is limited to the public data up to a specific point in time that they were trained on. If you want to build AI applications that can
reason about private data or data introduced after a model's cutoff date, you need to augment the knowledge of the model with the specific information it needs. The process of bringing the appropriate
information and inserting it into the model prompt is known as Retrieval Augmented Generation (RAG).

### What's in this guide?​

LangChain has a number of components specifically designed to help build RAG applications. To familiarize ourselves with these, we'll build a simple question-answering application over a text data
source. Specifically, we'll build a QA bot over the LLM Powered Autonomous Agents blog post by Lilian Weng. Along the way we'll go over a typical QA architecture, discuss the relevant LangChain
components, and highlight additional resources for more advanced QA techniques. We'll also see how LangSmith can help us trace and understand our application. LangSmith will become increasingly
helpful as our application grows in complexity.

 **Note** Here we focus on RAG for unstructured data. Two RAG use cases which we cover elsewhere are:

  * QA over structured data (e.g., SQL)
  * QA over code (e.g., Python)

## Architecture​

A typical RAG application has two main components:

 **Indexing** : a pipeline for ingesting data from a source and indexing it. _This usually happen offline._

 **Retrieval and generation** : the actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.

The most common full sequence from raw data to answer looks like:

#### Indexing​

  1.  **Load** : First we need to load our data. We'll use DocumentLoaders for this.
  2.  **Split** : Text splitters break large `Documents` into smaller chunks. This is useful both for indexing data and for passing it in to a model, since large chunks are harder to search over and won't in a model's finite context window.
  3.  **Store** : We need somewhere to store and index our splits, so that they can later be searched over. This is often done using a VectorStore and Embeddings model.

#### Retrieval and generation​

  4.  **Retrieve** : Given a user input, relevant splits are retrieved from storage using a Retriever.
  5.  **Generate** : A ChatModel / LLM produces an answer using a prompt that includes the question and the retrieved data

## Setup​

### Dependencies​

We'll use an OpenAI chat model and embeddings and a Chroma vector store in this walkthrough, but everything shown here works with any ChatModel or LLM, Embeddings, and VectorStore or Retriever.

We'll use the following packages:

```python




    pip install -U langchain openai chromadb langchainhub bs4



```


We need to set environment variable `OPENAI_API_KEY`, which can be done directly or loaded from a `.env` file like so:

```python




    import getpass
    import os

    os.environ["OPENAI_API_KEY"] = getpass.getpass()

    # import dotenv

    # dotenv.load_dotenv()



```


### LangSmith​

Many of the applications you build with LangChain will contain multiple steps with multiple invocations of LLM calls. As these applications get more and more complex, it becomes crucial to be able to
inspect what exactly is going on inside your chain or agent. The best way to do this is with LangSmith.

Note that LangSmith is not needed, but it is helpful. If you do want to use LangSmith, after you sign up at the link above, make sure to set your environment variables to start logging traces:

```python




    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()



```


## Quickstart​

Suppose we want to build a QA app over the LLM Powered Autonomous Agents blog post by Lilian Weng. We can create a simple pipeline for this in ~20 lines of code:

```python




    import bs4
    from langchain import hub
    from langchain.chat_models import ChatOpenAI
    from langchain.document_loaders import WebBaseLoader
    from langchain.embeddings import OpenAIEmbeddings
    from langchain.schema import StrOutputParser
    from langchain.schema.runnable import RunnablePassthrough
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain.vectorstores import Chroma



```


```python




    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())
    retriever = vectorstore.as_retriever()

    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )



```


```python




    rag_chain.invoke("What is Task Decomposition?")



```


```python




        'Task decomposition is a technique used to break down complex tasks into smaller and simpler steps. It can be done through prompting techniques like Chain of Thought or Tree of Thoughts, or by using task-specific instructions or human inputs. Task decomposition helps agents plan ahead and manage complicated tasks more effectively.'



```


```python




    # cleanup
    vectorstore.delete_collection()



```


Check out the LangSmith trace

## Detailed walkthrough​

Let's go through the above code step-by-step to really understand what's going on.

## Step 1. Load​

We need to first load the blog post contents. We can use `DocumentLoader`s for this, which are objects that load in data from a source as `Documents`. A `Document` is an object with `page_content`
(str) and `metadata` (dict) attributes.

In this case we'll use the `WebBaseLoader`, which uses `urllib` and `BeautifulSoup` to load and parse the passed in web urls, returning one `Document` per url. We can customize the html -> text
parsing by passing in parameters to the `BeautifulSoup` parser via `bs_kwargs` (see BeautifulSoup docs). In this case only HTML tags with class "post-content", "post-title", or "post-header" are
relevant, so we'll remove all others.

```python




    from langchain.document_loaders import WebBaseLoader

    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs={
            "parse_only": bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        },
    )
    docs = loader.load()



```


```python




    len(docs[0].page_content)



```


```python




        42824



```


```python




    print(docs[0].page_content[:500])



```


```python






              LLM Powered Autonomous Agents

        Date: June 23, 2023  |  Estimated Reading Time: 31 min  |  Author: Lilian Weng


        Building agents with LLM (large language model) as its core controller is a cool concept. Several proof-of-concepts demos, such as AutoGPT, GPT-Engineer and BabyAGI, serve as inspiring examples. The potentiality of LLM extends beyond generating well-written copies, stories, essays and programs; it can be framed as a powerful general problem solver.
        Agent System Overview#
        In



```


### Go deeper​

`DocumentLoader`: Object that load data from a source as `Documents`.

  * Docs: Further documentation on how to use `DocumentLoader`s.
  * Integrations: Find the relevant `DocumentLoader` integration (of the > 160 of them) for your use case.

## Step 2. Split​

Our loaded document is over 42k characters long. This is too long to fit in the context window of many models. And even for those models that could fit the full post in their context window,
empirically models struggle to find the relevant context in very long prompts.

So we'll split the `Document` into chunks for embedding and vector storage. This should help us retrieve only the most relevant bits of the blog post at run time.

In this case we'll split our documents into chunks of 1000 characters with 200 characters of overlap between chunks. The overlap helps mitigate the possibility of separating a statement from important
context related to it. We use the `RecursiveCharacterTextSplitter`, which will (recursively) split the document using common separators (like new lines) until each chunk is the appropriate size.

```python




    from langchain.text_splitter import RecursiveCharacterTextSplitter

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    all_splits = text_splitter.split_documents(docs)



```


```python




    len(all_splits)



```


```python




        66



```


```python




    len(all_splits[0].page_content)



```


```python




        969



```


```python




    all_splits[10].metadata



```


```python




        {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/',
         'start_index': 7056}



```


### Go deeper​

`DocumentSplitter`: Object that splits a list of `Document`s into smaller chunks. Subclass of `DocumentTransformer`s.

  * Explore `Context-aware splitters`, which keep the location ("context") of each split in the original `Document`:
    * Markdown files
    * Code (py or js)
    * Scientific papers

`DocumentTransformer`: Object that performs a transformation on a list of `Document`s.

  * Docs: Further documentation on how to use `DocumentTransformer`s
  * Integrations

## Step 3. Store​

Now that we've got 66 text chunks in memory, we need to store and index them so that we can search them later in our RAG app. The most common way to do this is to embed the contents of each document
split and upload those embeddings to a vector store.

Then, when we want to search over our splits, we take the search query, embed it as well, and perform some sort of "similarity" search to identify the stored splits with the most similar embeddings to
our query embedding. The simplest similarity measure is cosine similarity — we measure the cosine of the angle between each pair of embeddings (which are just very high dimensional vectors).

We can embed and store all of our document splits in a single command using the `Chroma` vector store and `OpenAIEmbeddings` model.

```python




    from langchain.embeddings import OpenAIEmbeddings
    from langchain.vectorstores import Chroma

    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())



```


### Go deeper​

`Embeddings`: Wrapper around a text embedding model, used for converting text to embeddings.

  * Docs: Further documentation on the interface.
  * Integrations: Browse the > 30 text embedding integrations

`VectorStore`: Wrapper around a vector database, used for storing and querying embeddings.

  * Docs: Further documentation on the interface.
  * Integrations: Browse the > 40 `VectorStore` integrations.

This completes the **Indexing** portion of the pipeline. At this point we have an query-able vector store containing the chunked contents of our blog post. Given a user question, we should ideally be
able to return the snippets of the blog post that answer the question:

## Step 4. Retrieve​

Now let's write the actual application logic. We want to create a simple application that let's the user ask a question, searches for documents relevant to that question, passes the retrieved
documents and initial question to a model, and finally returns an answer.

LangChain defines a `Retriever` interface which wraps an index that can return relevant documents given a string query. All retrievers implement a common method `get_relevant_documents()` (and its
asynchronous variant `aget_relevant_documents()`).

The most common type of `Retriever` is the `VectorStoreRetriever`, which uses the similarity search capabilities of a vector store to facillitate retrieval. Any `VectorStore` can easily be turned into
a `Retriever`:

```python




    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})



```


```python




    retrieved_docs = retriever.get_relevant_documents(
        "What are the approaches to Task Decomposition?"
    )



```


```python




    len(retrieved_docs)



```


```python




        6



```


```python




    print(retrieved_docs[0].page_content)



```


```python




        Tree of Thoughts (Yao et al. 2023) extends CoT by exploring multiple reasoning possibilities at each step. It first decomposes the problem into multiple thought steps and generates multiple thoughts per step, creating a tree structure. The search process can be BFS (breadth-first search) or DFS (depth-first search) with each state evaluated by a classifier (via a prompt) or majority vote.
        Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1.", "What are the subgoals for achieving XYZ?", (2) by using task-specific instructions; e.g. "Write a story outline." for writing a novel, or (3) with human inputs.



```


### Go deeper​

Vector stores are commonly used for retrieval, but there are plenty of other ways to do retrieval.

`Retriever`: An object that returns `Document`s given a text query

  * Docs: Further documentation on the interface and built-in retrieval techniques. Some of which include:
    * `MultiQueryRetriever` generates variants of the input question to improve retrieval hit rate.
    * `MultiVectorRetriever` (diagram below) instead generates variants of the embeddings, also in order to improve retrieval hit rate.
    * `Max marginal relevance` selects for relevance and diversity among the retrieved documents to avoid passing in duplicate context.
    * Documents can be filtered during vector store retrieval using `metadata` filters.
  * Integrations: Integrations with retrieval services.

## Step 5. Generate​

Let's put it all together into a chain that takes a question, retrieves relevant documents, constructs a prompt, passes that to a model, and parses the output.

We'll use the gpt-3.5-turbo OpenAI chat model, but any LangChain `LLM` or `ChatModel` could be substituted in.

```python




    from langchain.chat_models import ChatOpenAI

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)



```


We'll use a prompt for RAG that is checked into the LangChain prompt hub (here).

```python




    from langchain import hub

    prompt = hub.pull("rlm/rag-prompt")



```


```python




    print(
        prompt.invoke(
            {"context": "filler context", "question": "filler question"}
        ).to_string()
    )



```


```python




        Human: You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.
        Question: filler question
        Context: filler context
        Answer:



```


We'll use the LCEL Runnable protocol to define the chain, allowing us to

  * pipe together components and functions in a transparent way
  * automatically trace our chain in LangSmith
  * get streaming, async, and batched calling out of the box

```python




    from langchain.schema import StrOutputParser
    from langchain.schema.runnable import RunnablePassthrough


    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)


    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )



```


```python




    for chunk in rag_chain.stream("What is Task Decomposition?"):
        print(chunk, end="", flush=True)



```


```python




        Task decomposition is a technique used to break down complex tasks into smaller and simpler steps. It can be done through methods like Chain of Thought (CoT) or Tree of Thoughts, which involve dividing the task into manageable subtasks and exploring multiple reasoning possibilities at each step. Task decomposition can be performed by AI models with prompting, task-specific instructions, or human inputs.



```


Check out the LangSmith trace

### Go deeper​

#### Choosing LLMs​

`ChatModel`: An LLM-backed chat model wrapper. Takes in a sequence of messages and returns a message.

  * Docs
  * Integrations: Explore over 25 `ChatModel` integrations.

`LLM`: A text-in-text-out LLM. Takes in a string and returns a string.

  * Docs
  * Integrations: Explore over 75 `LLM` integrations.

See a guide on RAG with locally-running models here.

#### Customizing the prompt​

As shown above, we can load prompts (e.g., this RAG prompt) from the prompt hub. The prompt can also be easily customized:

```python




    from langchain.prompts import PromptTemplate

    template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Use three sentences maximum and keep the answer as concise as possible.
    Always say "thanks for asking!" at the end of the answer.
    {context}
    Question: {question}
    Helpful Answer:"""
    rag_prompt_custom = PromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | rag_prompt_custom
        | llm
        | StrOutputParser()
    )

    rag_chain.invoke("What is Task Decomposition?")



```


```python




        'Task decomposition is the process of breaking down a complex task into smaller and simpler steps. It can be done through techniques like Chain of Thought (CoT) or Tree of Thoughts, which involve dividing the problem into multiple thought steps and generating multiple thoughts per step. Task decomposition helps in enhancing model performance and understanding the thinking process of the model. Thanks for asking!'



```


Check out the LangSmith trace

### Adding sources​

With LCEL it's easy to return the retrieved documents or certain source metadata from the documents:

```python




    from operator import itemgetter

    from langchain.schema.runnable import RunnableMap

    rag_chain_from_docs = (
        {
            "context": lambda input: format_docs(input["documents"]),
            "question": itemgetter("question"),
        }
        | rag_prompt_custom
        | llm
        | StrOutputParser()
    )
    rag_chain_with_source = RunnableMap(
        {"documents": retriever, "question": RunnablePassthrough()}
    ) | {
        "documents": lambda input: [doc.metadata for doc in input["documents"]],
        "answer": rag_chain_from_docs,
    }

    rag_chain_with_source.invoke("What is Task Decomposition")



```


```python




        {'documents': [{'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/',
           'start_index': 1585},
          {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/',
           'start_index': 2192},
          {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/',
           'start_index': 17804},
          {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/',
           'start_index': 17414},
          {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/',
           'start_index': 29630},
          {'source': 'https://lilianweng.github.io/posts/2023-06-23-agent/',
           'start_index': 19373}],
         'answer': 'Task decomposition is a technique used to break down complex tasks into smaller and simpler steps. It involves transforming big tasks into multiple manageable tasks, allowing for a more systematic and organized approach to problem-solving. Thanks for asking!'}



```


Check out the LangSmith trace

### Adding memory​

Suppose we want to create a stateful application that remembers past user inputs. There are two main things we need to do to support this.

  1. Add a messages placeholder to our chain which allows us to pass in historical messages
  2. Add a chain that takes the latest user query and reformulates it in the context of the chat history into a standalone question that can be passed to our retriever.

Let's start with 2. We can build a "condense question" chain that looks something like this:

```python




    from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

    condense_q_system_prompt = """Given a chat history and the latest user question \
    which might reference the chat history, formulate a standalone question \
    which can be understood without the chat history. Do NOT answer the question, \
    just reformulate it if needed and otherwise return it as is."""
    condense_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", condense_q_system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )
    condense_q_chain = condense_q_prompt | llm | StrOutputParser()



```


```python




    from langchain.schema.messages import AIMessage, HumanMessage

    condense_q_chain.invoke(
        {
            "chat_history": [
                HumanMessage(content="What does LLM stand for?"),
                AIMessage(content="Large language model"),
            ],
            "question": "What is meant by large",
        }
    )



```


```python




        'What is the definition of "large" in the context of a language model?'



```


```python




    condense_q_chain.invoke(
        {
            "chat_history": [
                HumanMessage(content="What does LLM stand for?"),
                AIMessage(content="Large language model"),
            ],
            "question": "How do transformers work",
        }
    )



```


```python




        'How do transformer models function?'



```


And now we can build our full QA chain. Notice we add some routing functionality to only run the "condense question chain" when our chat history isn't empty.

```python




    qa_system_prompt = """You are an assistant for question-answering tasks. \
    Use the following pieces of retrieved context to answer the question. \
    If you don't know the answer, just say that you don't know. \
    Use three sentences maximum and keep the answer concise.\

    {context}"""
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )


    def condense_question(input: dict):
        if input.get("chat_history"):
            return condense_q_chain
        else:
            return input["question"]


    rag_chain = (
        RunnablePassthrough.assign(context=condense_question | retriever | format_docs)
        | qa_prompt
        | llm
    )



```


```python




    chat_history = []

    question = "What is Task Decomposition?"
    ai_msg = rag_chain.invoke({"question": question, "chat_history": chat_history})
    chat_history.extend([HumanMessage(content=question), ai_msg])

    second_question = "What are common ways of doing it?"
    rag_chain.invoke({"question": second_question, "chat_history": chat_history})



```


```python




        AIMessage(content='Common ways of task decomposition include:\n\n1. Using Chain of Thought (CoT): CoT is a prompting technique that instructs the model to "think step by step" and decompose complex tasks into smaller and simpler steps. It utilizes more test-time computation and sheds light on the model\'s thinking process.\n\n2. Prompting with LLM: Language Model (LLM) can be used to prompt the model with simple instructions like "Steps for XYZ" or "What are the subgoals for achieving XYZ?" This allows the model to generate a sequence of subtasks or thought steps.\n\n3. Task-specific instructions: For certain tasks, task-specific instructions can be provided to guide the model in decomposing the task. For example, for writing a novel, the instruction "Write a story outline" can be given to break down the task into manageable steps.\n\n4. Human inputs: In some cases, human inputs can be used to assist in task decomposition. Humans can provide their expertise and knowledge to identify and break down complex tasks into smaller subtasks.')



```


Check out the LangSmith trace

Here we've gone over how to add chain logic for incorporating historical outputs. But how do we actually store and retrieve historical outputs for different sessions? For that check out the LCEL How
to add message history (memory) page.

## Next steps​

That's a lot of content we've covered in a short amount of time. There's plenty of nuances, features, integrations, etc to explore in each of the above sections. Aside from the sources mentioned
above, good next steps include:

  * Reading up on more advanced retrieval techniques in the Retrievers section.
  * Learning about the LangChain Indexing API, which helps repeatedly sync data sources and vector stores without redundant computation or storage.
  * Exploring RAG LangChain Templates, which are reference applications that can easily be deployed with LangServe.
  * Learning about evaluating RAG applications with LangSmith.
