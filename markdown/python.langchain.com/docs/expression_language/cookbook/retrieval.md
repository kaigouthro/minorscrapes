Skip to main content

On this page

# RAG

Let's look at adding in a retrieval step to a prompt and LLM, which adds up to a "retrieval-augmented generation" chain

\[code\]

```python


    pip install langchain openai faiss-cpu tiktoken  
    
```

\[/code\]

\[code\]

```python


    from operator import itemgetter  
      
    from langchain.chat_models import ChatOpenAI  
    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.prompts import ChatPromptTemplate  
    from langchain.schema.output_parser import StrOutputParser  
    from langchain.schema.runnable import RunnableLambda, RunnablePassthrough  
    from langchain.vectorstores import FAISS  
    
```

\[/code\]

\[code\]

```python


    vectorstore = FAISS.from_texts(  
        ["harrison worked at kensho"], embedding=OpenAIEmbeddings()  
    )  
    retriever = vectorstore.as_retriever()  
      
    template = """Answer the question based only on the following context:  
    {context}  
      
    Question: {question}  
    """  
    prompt = ChatPromptTemplate.from_template(template)  
      
    model = ChatOpenAI()  
    
```

\[/code\]

\[code\]

```python


    chain = (  
        {"context": retriever, "question": RunnablePassthrough()}  
        | prompt  
        | model  
        | StrOutputParser()  
    )  
    
```

\[/code\]

\[code\]

```python


    chain.invoke("where did harrison work?")  
    
```

\[/code\]

\[code\]

```python


        'Harrison worked at Kensho.'  
    
```

\[/code\]

\[code\]

```python


    template = """Answer the question based only on the following context:  
    {context}  
      
    Question: {question}  
      
    Answer in the following language: {language}  
    """  
    prompt = ChatPromptTemplate.from_template(template)  
      
    chain = (  
        {  
            "context": itemgetter("question") | retriever,  
            "question": itemgetter("question"),  
            "language": itemgetter("language"),  
        }  
        | prompt  
        | model  
        | StrOutputParser()  
    )  
    
```

\[/code\]

\[code\]

```python


    chain.invoke({"question": "where did harrison work", "language": "italian"})  
    
```

\[/code\]

\[code\]

```python


        'Harrison ha lavorato a Kensho.'  
    
```

\[/code\]

## Conversational Retrieval Chain​

We can easily add in conversation history. This primarily means adding in chat_message_history

\[code\]

```python


    from langchain.schema import format_document  
    from langchain.schema.runnable import RunnableMap  
    
```

\[/code\]

\[code\]

```python


    from langchain.prompts.prompt import PromptTemplate  
      
    _template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.  
      
    Chat History:  
    {chat_history}  
    Follow Up Input: {question}  
    Standalone question:"""  
    CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)  
    
```

\[/code\]

\[code\]

```python


    template = """Answer the question based only on the following context:  
    {context}  
      
    Question: {question}  
    """  
    ANSWER_PROMPT = ChatPromptTemplate.from_template(template)  
    
```

\[/code\]

\[code\]

```python


    DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")  
      
      
    def _combine_documents(  
        docs, document_prompt=DEFAULT_DOCUMENT_PROMPT, document_separator="\n\n"  
    ):  
        doc_strings = [format_document(doc, document_prompt) for doc in docs]  
        return document_separator.join(doc_strings)  
    
```

\[/code\]

\[code\]

```python


    from typing import List, Tuple  
      
      
    def _format_chat_history(chat_history: List[Tuple]) -> str:  
        buffer = ""  
        for dialogue_turn in chat_history:  
            human = "Human: " + dialogue_turn[0]  
            ai = "Assistant: " + dialogue_turn[1]  
            buffer += "\n" + "\n".join([human, ai])  
        return buffer  
    
```

\[/code\]

\[code\]

```python


    _inputs = RunnableMap(  
        standalone_question=RunnablePassthrough.assign(  
            chat_history=lambda x: _format_chat_history(x["chat_history"])  
        )  
        | CONDENSE_QUESTION_PROMPT  
        | ChatOpenAI(temperature=0)  
        | StrOutputParser(),  
    )  
    _context = {  
        "context": itemgetter("standalone_question") | retriever | _combine_documents,  
        "question": lambda x: x["standalone_question"],  
    }  
    conversational_qa_chain = _inputs | _context | ANSWER_PROMPT | ChatOpenAI()  
    
```

\[/code\]

\[code\]

```python


    conversational_qa_chain.invoke(  
        {  
            "question": "where did harrison work?",  
            "chat_history": [],  
        }  
    )  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content='Harrison was employed at Kensho.', additional_kwargs={}, example=False)  
    
```

\[/code\]

\[code\]

```python


    conversational_qa_chain.invoke(  
        {  
            "question": "where did he work?",  
            "chat_history": [("Who wrote this notebook?", "Harrison")],  
        }  
    )  
    
```

\[/code\]

\[code\]

```python


        AIMessage(content='Harrison worked at Kensho.', additional_kwargs={}, example=False)  
    
```

\[/code\]

### With Memory and returning source documents​

This shows how to use memory with the above. For memory, we need to manage that outside at the memory. For returning the retrieved documents, we just need to pass them through all the way.

\[code\]

```python


    from operator import itemgetter  
      
    from langchain.memory import ConversationBufferMemory  
    
```

\[/code\]

\[code\]

```python


    memory = ConversationBufferMemory(  
        return_messages=True, output_key="answer", input_key="question"  
    )  
    
```

\[/code\]

\[code\]

```python


    # First we add a step to load memory  
    # This adds a "memory" key to the input object  
    loaded_memory = RunnablePassthrough.assign(  
        chat_history=RunnableLambda(memory.load_memory_variables) | itemgetter("history"),  
    )  
    # Now we calculate the standalone question  
    standalone_question = {  
        "standalone_question": {  
            "question": lambda x: x["question"],  
            "chat_history": lambda x: _format_chat_history(x["chat_history"]),  
        }  
        | CONDENSE_QUESTION_PROMPT  
        | ChatOpenAI(temperature=0)  
        | StrOutputParser(),  
    }  
    # Now we retrieve the documents  
    retrieved_documents = {  
        "docs": itemgetter("standalone_question") | retriever,  
        "question": lambda x: x["standalone_question"],  
    }  
    # Now we construct the inputs for the final prompt  
    final_inputs = {  
        "context": lambda x: _combine_documents(x["docs"]),  
        "question": itemgetter("question"),  
    }  
    # And finally, we do the part that returns the answers  
    answer = {  
        "answer": final_inputs | ANSWER_PROMPT | ChatOpenAI(),  
        "docs": itemgetter("docs"),  
    }  
    # And now we put it all together!  
    final_chain = loaded_memory | standalone_question | retrieved_documents | answer  
    
```

\[/code\]

\[code\]

```python


    inputs = {"question": "where did harrison work?"}  
    result = final_chain.invoke(inputs)  
    result  
    
```

\[/code\]

\[code\]

```python


        {'answer': AIMessage(content='Harrison was employed at Kensho.', additional_kwargs={}, example=False),  
         'docs': [Document(page_content='harrison worked at kensho', metadata={})]}  
    
```

\[/code\]

\[code\]

```python


    # Note that the memory does not save automatically  
    # This will be improved in the future  
    # For now you need to save it yourself  
    memory.save_context(inputs, {"answer": result["answer"].content})  
    
```

\[/code\]

\[code\]

```python


    memory.load_memory_variables({})  
    
```

\[/code\]

\[code\]

```python


        {'history': [HumanMessage(content='where did harrison work?', additional_kwargs={}, example=False),  
          AIMessage(content='Harrison was employed at Kensho.', additional_kwargs={}, example=False)]}  
    
```

\[/code\]
