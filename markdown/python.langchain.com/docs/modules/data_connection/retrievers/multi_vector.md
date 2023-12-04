

Skip to main content

On this page

# MultiVector Retriever

It can often be beneficial to store multiple vectors per document. There are multiple use cases where this is beneficial. LangChain has a base `MultiVectorRetriever` which makes querying this type of
setup easy. A lot of the complexity lies in how to create the multiple vectors per document. This notebook covers some of the common ways to create those vectors and use the `MultiVectorRetriever`.

The methods to create multiple vectors per document include:

  * Smaller chunks: split a document into smaller chunks, and embed those (this is ParentDocumentRetriever).
  * Summary: create a summary for each document, embed that along with (or instead of) the document.
  * Hypothetical questions: create hypothetical questions that each document would be appropriate to answer, embed those along with (or instead of) the document.

Note that this also enables another method of adding embeddings - manually. This is great because you can explicitly add questions or queries that should lead to a document being recovered, giving you
more control.

[code]
```python




    from langchain.retrievers.multi_vector import MultiVectorRetriever  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TextLoader  
    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.storage import InMemoryStore  
    from langchain.text_splitter import RecursiveCharacterTextSplitter  
    from langchain.vectorstores import Chroma  
    


```
[/code]


[code]
```python




    loaders = [  
        TextLoader("../../paul_graham_essay.txt"),  
        TextLoader("../../state_of_the_union.txt"),  
    ]  
    docs = []  
    for l in loaders:  
        docs.extend(l.load())  
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000)  
    docs = text_splitter.split_documents(docs)  
    


```
[/code]


## Smaller chunks​

Often times it can be useful to retrieve larger chunks of information, but embed smaller chunks. This allows for embeddings to capture the semantic meaning as closely as possible, but for as much
context as possible to be passed downstream. Note that this is what the `ParentDocumentRetriever` does. Here we show what is going on under the hood.

[code]
```python




    # The vectorstore to use to index the child chunks  
    vectorstore = Chroma(  
        collection_name="full_documents", embedding_function=OpenAIEmbeddings()  
    )  
    # The storage layer for the parent documents  
    store = InMemoryStore()  
    id_key = "doc_id"  
    # The retriever (empty to start)  
    retriever = MultiVectorRetriever(  
        vectorstore=vectorstore,  
        docstore=store,  
        id_key=id_key,  
    )  
    import uuid  
      
    doc_ids = [str(uuid.uuid4()) for _ in docs]  
    


```
[/code]


[code]
```python




    # The splitter to use to create smaller chunks  
    child_text_splitter = RecursiveCharacterTextSplitter(chunk_size=400)  
    


```
[/code]


[code]
```python




    sub_docs = []  
    for i, doc in enumerate(docs):  
        _id = doc_ids[i]  
        _sub_docs = child_text_splitter.split_documents([doc])  
        for _doc in _sub_docs:  
            _doc.metadata[id_key] = _id  
        sub_docs.extend(_sub_docs)  
    


```
[/code]


[code]
```python




    retriever.vectorstore.add_documents(sub_docs)  
    retriever.docstore.mset(list(zip(doc_ids, docs)))  
    


```
[/code]


[code]
```python




    # Vectorstore alone retrieves the small chunks  
    retriever.vectorstore.similarity_search("justice breyer")[0]  
    


```
[/code]


[code]
```python




        Document(page_content='Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service. \n\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.', metadata={'doc_id': '455205f7-bb7d-4c36-b442-d1d6f9f701ed', 'source': '../../state_of_the_union.txt'})  
    


```
[/code]


[code]
```python




    # Retriever returns larger chunks  
    len(retriever.get_relevant_documents("justice breyer")[0].page_content)  
    


```
[/code]


[code]
```python




        9875  
    


```
[/code]


The default search type the retriever performs on the vector database is a similarity search. LangChain Vector Stores also support searching via Max Marginal Relevance so if you want this instead you
can just set the `search_type` property as follows:

[code]
```python




    from langchain.retrievers.multi_vector import SearchType  
      
    retriever.search_type = SearchType.mmr  
      
    len(retriever.get_relevant_documents("justice breyer")[0].page_content)  
    


```
[/code]


[code]
```python




        9875  
    


```
[/code]


## Summary​

Oftentimes a summary may be able to distill more accurately what a chunk is about, leading to better retrieval. Here we show how to create summaries, and then embed those.

[code]
```python




    import uuid  
      
    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts import ChatPromptTemplate  
    from langchain.schema.document import Document  
    from langchain.schema.output_parser import StrOutputParser  
    


```
[/code]


[code]
```python




    chain = (  
        {"doc": lambda x: x.page_content}  
        | ChatPromptTemplate.from_template("Summarize the following document:\n\n{doc}")  
        | ChatOpenAI(max_retries=0)  
        | StrOutputParser()  
    )  
    


```
[/code]


[code]
```python




    summaries = chain.batch(docs, {"max_concurrency": 5})  
    


```
[/code]


[code]
```python




    # The vectorstore to use to index the child chunks  
    vectorstore = Chroma(collection_name="summaries", embedding_function=OpenAIEmbeddings())  
    # The storage layer for the parent documents  
    store = InMemoryStore()  
    id_key = "doc_id"  
    # The retriever (empty to start)  
    retriever = MultiVectorRetriever(  
        vectorstore=vectorstore,  
        docstore=store,  
        id_key=id_key,  
    )  
    doc_ids = [str(uuid.uuid4()) for _ in docs]  
    


```
[/code]


[code]
```python




    summary_docs = [  
        Document(page_content=s, metadata={id_key: doc_ids[i]})  
        for i, s in enumerate(summaries)  
    ]  
    


```
[/code]


[code]
```python




    retriever.vectorstore.add_documents(summary_docs)  
    retriever.docstore.mset(list(zip(doc_ids, docs)))  
    


```
[/code]


[code]
```python




    # # We can also add the original chunks to the vectorstore if we so want  
    # for i, doc in enumerate(docs):  
    #     doc.metadata[id_key] = doc_ids[i]  
    # retriever.vectorstore.add_documents(docs)  
    


```
[/code]


[code]
```python




    sub_docs = vectorstore.similarity_search("justice breyer")  
    


```
[/code]


[code]
```python




    sub_docs[0]  
    


```
[/code]


[code]
```python




        Document(page_content="The document is a transcript of a speech given by the President of the United States. The President discusses several important issues and initiatives, including the nomination of a Supreme Court Justice, border security and immigration reform, protecting women's rights, advancing LGBTQ+ equality, bipartisan legislation, addressing the opioid epidemic and mental health, supporting veterans, investigating the health effects of burn pits on military personnel, ending cancer, and the strength and resilience of the American people.", metadata={'doc_id': '79fa2e9f-28d9-4372-8af3-2caf4f1de312'})  
    


```
[/code]


[code]
```python




    retrieved_docs = retriever.get_relevant_documents("justice breyer")  
    


```
[/code]


[code]
```python




    len(retrieved_docs[0].page_content)  
    


```
[/code]


[code]
```python




        9194  
    


```
[/code]


## Hypothetical Queries​

An LLM can also be used to generate a list of hypothetical questions that could be asked of a particular document. These questions can then be embedded

[code]
```python




    functions = [  
        {  
            "name": "hypothetical_questions",  
            "description": "Generate hypothetical questions",  
            "parameters": {  
                "type": "object",  
                "properties": {  
                    "questions": {  
                        "type": "array",  
                        "items": {"type": "string"},  
                    },  
                },  
                "required": ["questions"],  
            },  
        }  
    ]  
    


```
[/code]


[code]
```python




    from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParser  
      
    chain = (  
        {"doc": lambda x: x.page_content}  
        # Only asking for 3 hypothetical questions, but this could be adjusted  
        | ChatPromptTemplate.from_template(  
            "Generate a list of 3 hypothetical questions that the below document could be used to answer:\n\n{doc}"  
        )  
        | ChatOpenAI(max_retries=0, model="gpt-4").bind(  
            functions=functions, function_call={"name": "hypothetical_questions"}  
        )  
        | JsonKeyOutputFunctionsParser(key_name="questions")  
    )  
    


```
[/code]


[code]
```python




    chain.invoke(docs[0])  
    


```
[/code]


[code]
```python




        ["What was the author's initial impression of philosophy as a field of study, and how did it change when they got to college?",  
         'Why did the author decide to switch their focus to Artificial Intelligence (AI)?',  
         "What led to the author's disillusionment with the field of AI as it was practiced at the time?"]  
    


```
[/code]


[code]
```python




    hypothetical_questions = chain.batch(docs, {"max_concurrency": 5})  
    


```
[/code]


[code]
```python




    # The vectorstore to use to index the child chunks  
    vectorstore = Chroma(  
        collection_name="hypo-questions", embedding_function=OpenAIEmbeddings()  
    )  
    # The storage layer for the parent documents  
    store = InMemoryStore()  
    id_key = "doc_id"  
    # The retriever (empty to start)  
    retriever = MultiVectorRetriever(  
        vectorstore=vectorstore,  
        docstore=store,  
        id_key=id_key,  
    )  
    doc_ids = [str(uuid.uuid4()) for _ in docs]  
    


```
[/code]


[code]
```python




    question_docs = []  
    for i, question_list in enumerate(hypothetical_questions):  
        question_docs.extend(  
            [Document(page_content=s, metadata={id_key: doc_ids[i]}) for s in question_list]  
        )  
    


```
[/code]


[code]
```python




    retriever.vectorstore.add_documents(question_docs)  
    retriever.docstore.mset(list(zip(doc_ids, docs)))  
    


```
[/code]


[code]
```python




    sub_docs = vectorstore.similarity_search("justice breyer")  
    


```
[/code]


[code]
```python




    sub_docs  
    


```
[/code]


[code]
```python




        [Document(page_content="What is the President's stance on immigration reform?", metadata={'doc_id': '505d73e3-8350-46ec-a58e-3af032f04ab3'}),  
         Document(page_content="What is the President's stance on immigration reform?", metadata={'doc_id': '1c9618f0-7660-4b4f-a37c-509cbbbf6dba'}),  
         Document(page_content="What is the President's stance on immigration reform?", metadata={'doc_id': '82c08209-b904-46a8-9532-edd2380950b7'}),  
         Document(page_content='What measures is the President proposing to protect the rights of LGBTQ+ Americans?', metadata={'doc_id': '82c08209-b904-46a8-9532-edd2380950b7'})]  
    


```
[/code]


[code]
```python




    retrieved_docs = retriever.get_relevant_documents("justice breyer")  
    


```
[/code]


[code]
```python




    len(retrieved_docs[0].page_content)  
    


```
[/code]


[code]
```python




        9194  
    


```
[/code]


