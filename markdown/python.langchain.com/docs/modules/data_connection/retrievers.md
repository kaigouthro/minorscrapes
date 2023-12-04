

Skip to main content

On this page

info

Head to Integrations for documentation on built-in retriever integrations with 3rd-party tools.

A retriever is an interface that returns documents given an unstructured query. It is more general than a vector store. A retriever does not need to be able to store documents, only to return (or
retrieve) them. Vector stores can be used as the backbone of a retriever, but there are other types of retrievers as well.

Retrievers implement the Runnable interface, the basic building block of the LangChain Expression Language (LCEL). This means they support `invoke`, `ainvoke`, `stream`, `astream`, `batch`, `abatch`,
`astream_log` calls.

Retrievers accept a string query as input and return a list of `Document`'s as output.

## Get started​

In this example we'll use a `Chroma` vector store-backed retriever. To get setup we'll need to run:

[code]
```python




    pip install chromadb  
    


```
[/code]


And download the state_of_the_union.txt file here.

[code]
```python




    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import Chroma  
      
    full_text = open("state_of_the_union.txt", "r").read()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)  
    texts = text_splitter.split_text(full_text)  
      
    embeddings = OpenAIEmbeddings()  
    db = Chroma.from_texts(texts, embeddings)  
    retriever = db.as_retriever()  
    


```
[/code]


[code]
```python




    retrieved_docs = retriever.invoke(  
        "What did the president say about Ketanji Brown Jackson?"  
    )  
    print(retrieved_docs[0].page_content)  
    


```
[/code]


[code]
```python




        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.   
          
        A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans.   
          
        And if we are to advance liberty and justice, we need to secure the Border and fix the immigration system.   
          
        We can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.    
          
        We’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.  
    


```
[/code]


## LCEL​

Since retrievers are `Runnable`'s, we can easily compose them with other `Runnable` objects:

[code]
```python




    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts import ChatPromptTemplate  
    from langchain.schema import StrOutputParser  
    from langchain.schema.runnable import RunnablePassthrough  
      
    template = """Answer the question based only on the following context:  
      
    {context}  
      
    Question: {question}  
    """  
    prompt = ChatPromptTemplate.from_template(template)  
    model = ChatOpenAI()  
      
      
    def format_docs(docs):  
        return "\n\n".join([d.page_content for d in docs])  
      
      
    chain = (  
        {"context": retriever | format_docs, "question": RunnablePassthrough()}  
        | prompt  
        | model  
        | StrOutputParser()  
    )  
    


```
[/code]


[code]
```python




    chain.invoke("What did the president say about technology?")  
    


```
[/code]


[code]
```python




        'The president said that technology plays a crucial role in the future and that passing the Bipartisan Innovation Act will make record investments in emerging technologies and American manufacturing. The president also mentioned Intel\'s plans to build a semiconductor "mega site" and increase their investment from $20 billion to $100 billion, which would be one of the biggest investments in manufacturing in American history.'  
    


```
[/code]


