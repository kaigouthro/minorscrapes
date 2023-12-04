

Skip to main content

On this page

# RePhraseQuery

`RePhraseQuery` is a simple retriever that applies an LLM between the user input and the query passed by the retriever.

It can be used to pre-process the user input in any way.

## Example​

### Setting up​

Create a vector store.

[code]
```python




    import logging  
      
    from langchain.chat_models import ChatOpenAI  
    from langchain.document_loaders import WebBaseLoader  
    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.retrievers import RePhraseQueryRetriever  
    from langchain.text_splitter import RecursiveCharacterTextSplitter  
    from langchain.vectorstores import Chroma  
    


```
[/code]


[code]
```python




    logging.basicConfig()  
    logging.getLogger("langchain.retrievers.re_phraser").setLevel(logging.INFO)  
      
    loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")  
    data = loader.load()  
      
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)  
    all_splits = text_splitter.split_documents(data)  
      
    vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())  
    


```
[/code]


### Using the default prompt​

The default prompt used in the `from_llm` classmethod:

[code]
```python




    DEFAULT_TEMPLATE = """You are an assistant tasked with taking a natural language \  
    query from a user and converting it into a query for a vectorstore. \  
    In this process, you strip out information that is not relevant for \  
    the retrieval task. Here is the user query: {question}"""  
    


```
[/code]


[code]
```python




    llm = ChatOpenAI(temperature=0)  
    retriever_from_llm = RePhraseQueryRetriever.from_llm(  
        retriever=vectorstore.as_retriever(), llm=llm  
    )  
    


```
[/code]


[code]
```python




    docs = retriever_from_llm.get_relevant_documents(  
        "Hi I'm Lance. What are the approaches to Task Decomposition?"  
    )  
    


```
[/code]


[code]
```python




        INFO:langchain.retrievers.re_phraser:Re-phrased question: The user query can be converted into a query for a vectorstore as follows:  
          
        "approaches to Task Decomposition"  
    


```
[/code]


[code]
```python




    docs = retriever_from_llm.get_relevant_documents(  
        "I live in San Francisco. What are the Types of Memory?"  
    )  
    


```
[/code]


[code]
```python




        INFO:langchain.retrievers.re_phraser:Re-phrased question: Query for vectorstore: "Types of Memory"  
    


```
[/code]


### Custom prompt​

[code]
```python




    from langchain.chains import LLMChain  
    from langchain.prompts import PromptTemplate  
      
    QUERY_PROMPT = PromptTemplate(  
        input_variables=["question"],  
        template="""You are an assistant tasked with taking a natural languge query from a user  
        and converting it into a query for a vectorstore. In the process, strip out all   
        information that is not relevant for the retrieval task and return a new, simplified  
        question for vectorstore retrieval. The new user query should be in pirate speech.  
        Here is the user query: {question} """,  
    )  
    llm = ChatOpenAI(temperature=0)  
    llm_chain = LLMChain(llm=llm, prompt=QUERY_PROMPT)  
    


```
[/code]


[code]
```python




    retriever_from_llm_chain = RePhraseQueryRetriever(  
        retriever=vectorstore.as_retriever(), llm_chain=llm_chain  
    )  
    


```
[/code]


[code]
```python




    docs = retriever_from_llm_chain.get_relevant_documents(  
        "Hi I'm Lance. What is Maximum Inner Product Search?"  
    )  
    


```
[/code]


[code]
```python




        INFO:langchain.retrievers.re_phraser:Re-phrased question: Ahoy matey! What be Maximum Inner Product Search, ye scurvy dog?  
    


```
[/code]


