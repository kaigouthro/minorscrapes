

Skip to main content

On this page

# Fleet AI Libraries Context

The Fleet AI team is on a mission to embed the world's most important data. They've started by embedding the top 1200 Python libraries to enable code generation with up-to-date knowledge. They've been
kind enough to share their embeddings of the LangChain docs and API reference.

Let's take a look at how we can use these embeddings to power a docs retrieval system and ultimately a simple code generating chain!

[code]
```python




    pip install langchain fleet-context openai pandas faiss-cpu # faiss-gpu for CUDA supported GPU  
    


```
[/code]


[code]
```python




    from operator import itemgetter  
    from typing import Any, Optional, Type  
      
    import pandas as pd  
    from langchain.embeddings import OpenAIEmbeddings  
    from langchain.retrievers import MultiVectorRetriever  
    from langchain.schema import Document  
    from langchain.schema.storage import BaseStore  
    from langchain.schema.vectorstore import VectorStore  
    from langchain.vectorstores import FAISS  
      
      
    def load_fleet_retriever(  
        df: pd.DataFrame,  
        *,  
        vectorstore_cls: Type[VectorStore] = FAISS,  
        docstore: Optional[BaseStore] = None,  
        **kwargs: Any,  
    ):  
        vectorstore = _populate_vectorstore(df, vectorstore_cls)  
        if docstore is None:  
            return vectorstore.as_retriever(**kwargs)  
        else:  
            _populate_docstore(df, docstore)  
            return MultiVectorRetriever(  
                vectorstore=vectorstore, docstore=docstore, id_key="parent", **kwargs  
            )  
      
      
    def _populate_vectorstore(  
        df: pd.DataFrame,  
        vectorstore_cls: Type[VectorStore],  
    ) -> VectorStore:  
        if not hasattr(vectorstore_cls, "from_embeddings"):  
            raise ValueError(  
                f"Incompatible vector store class {vectorstore_cls}."  
                "Must implement `from_embeddings` class method."  
            )  
        texts_embeddings = []  
        metadatas = []  
        for _, row in df.iterrows():  
            texts_embeddings.append((row.metadata["text"], row["dense_embeddings"]))  
            metadatas.append(row.metadata)  
        return vectorstore_cls.from_embeddings(  
            texts_embeddings,  
            OpenAIEmbeddings(model="text-embedding-ada-002"),  
            metadatas=metadatas,  
        )  
      
      
    def _populate_docstore(df: pd.DataFrame, docstore: BaseStore) -> None:  
        parent_docs = []  
        df = df.copy()  
        df["parent"] = df.metadata.apply(itemgetter("parent"))  
        for parent_id, group in df.groupby("parent"):  
            sorted_group = group.iloc[  
                group.metadata.apply(itemgetter("section_index")).argsort()  
            ]  
            text = "".join(sorted_group.metadata.apply(itemgetter("text")))  
            metadata = {  
                k: sorted_group.iloc[0].metadata[k] for k in ("title", "type", "url")  
            }  
            text = metadata["title"] + "\n" + text  
            metadata["id"] = parent_id  
            parent_docs.append(Document(page_content=text, metadata=metadata))  
        docstore.mset(((d.metadata["id"], d) for d in parent_docs))  
    


```
[/code]


## Retriever chunks​

As part of their embedding process, the Fleet AI team first chunked long documents before embedding them. This means the vectors correspond to sections of pages in the LangChain docs, not entire
pages. By default, when we spin up a retriever from these embeddings, we'll be retrieving these embedded chunks.

We will be using Fleet Context's `download_embeddings()` to grab Langchain's documentation embeddings. You can view all supported libraries' documentation at https://fleet.so/context.

[code]
```python




    from context import download_embeddings  
      
    df = download_embeddings("langchain")  
    vecstore_retriever = load_fleet_retriever(df)  
    


```
[/code]


[code]
```python




    vecstore_retriever.get_relevant_documents("How does the multi vector retriever work")  
    


```
[/code]


[code]
```python




        [Document(page_content="# Vector store-backed retriever A vector store retriever is a retriever that uses a vector store to retrieve documents. It is a lightweight wrapper around the vector store class to make it conform to the retriever interface. It uses the search methods implemented by a vector store, like similarity search and MMR, to query the texts in the vector store. Once you construct a vector store, it's very easy to construct a retriever. Let's walk through an example.", metadata={'id': 'f509f20d-4c63-4a5a-a40a-5c4c0f099839', 'library_id': '4506492b-70de-49f1-ba2e-d65bd7048a28', 'page_id': 'd78cf422-2dab-4860-80fe-d71a3619b02f', 'parent': 'c153ebd9-2611-4a43-9db6-daa1f5f214f6', 'section_id': '', 'section_index': 0, 'text': "# Vector store-backed retriever A vector store retriever is a retriever that uses a vector store to retrieve documents. It is a lightweight wrapper around the vector store class to make it conform to the retriever interface. It uses the search methods implemented by a vector store, like similarity search and MMR, to query the texts in the vector store. Once you construct a vector store, it's very easy to construct a retriever. Let's walk through an example.", 'title': 'Vector store-backed retriever | 🦜️🔗 Langchain', 'type': None, 'url': 'https://python.langchain.com/docs/modules/data_connection/retrievers/vectorstore'}),  
         Document(page_content='# MultiVector Retriever It can often be beneficial to store multiple vectors per document. There are multiple use cases where this is beneficial. LangChain has a base `MultiVectorRetriever` which makes querying this type of setup easy. A lot of the complexity lies in how to create the multiple vectors per document. This notebook covers some of the common ways to create those vectors and use the `MultiVectorRetriever`. The methods to create multiple vectors per document include: - Smaller chunks: split a document into smaller chunks, and embed those (this is ParentDocumentRetriever). - Summary: create a summary for each document, embed that along with (or instead of) the document. - Hypothetical questions: create hypothetical questions that each document would be appropriate to answer, embed those along with (or instead of) the document. Note that this also enables another method of adding embeddings - manually.', metadata={'id': 'e06e6bb5-127a-49f7-9511-247d279d0d83', 'library_id': '4506492b-70de-49f1-ba2e-d65bd7048a28', 'page_id': '7c7dd0de-25e0-4e1d-9237-cfd2674c29d4', 'parent': 'beec5531-16a7-453c-80ab-c5628e0236ce', 'section_id': '', 'section_index': 0, 'text': '# MultiVector Retriever It can often be beneficial to store multiple vectors per document. There are multiple use cases where this is beneficial. LangChain has a base `MultiVectorRetriever` which makes querying this type of setup easy. A lot of the complexity lies in how to create the multiple vectors per document. This notebook covers some of the common ways to create those vectors and use the `MultiVectorRetriever`. The methods to create multiple vectors per document include: - Smaller chunks: split a document into smaller chunks, and embed those (this is ParentDocumentRetriever). - Summary: create a summary for each document, embed that along with (or instead of) the document. - Hypothetical questions: create hypothetical questions that each document would be appropriate to answer, embed those along with (or instead of) the document. Note that this also enables another method of adding embeddings - manually.', 'title': 'MultiVector Retriever | 🦜️🔗 Langchain', 'type': None, 'url': 'https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector'}),  
         Document(page_content='# MultiQueryRetriever Distance-based vector database retrieval embeds (represents) queries in high-dimensional space and finds similar embedded documents based on "distance". But, retrieval may produce different results with subtle changes in query wording or if the embeddings do not capture the semantics of the data well. Prompt engineering / tuning is sometimes done to manually address these problems, but can be tedious. The `MultiQueryRetriever` automates the process of prompt tuning by using an LLM to generate multiple queries from different perspectives for a given user input query. For each query, it retrieves a set of relevant documents and takes the unique union across all queries to get a larger set of potentially relevant documents. By generating multiple perspectives on the same question, the `MultiQueryRetriever` might be able to overcome some of the limitations of the distance-based retrieval and get a richer set of results.', metadata={'id': 'dc3b8e5b-a591-4a46-bfeb-a91b36affae1', 'library_id': '4506492b-70de-49f1-ba2e-d65bd7048a28', 'page_id': '31f80e84-c5db-4da2-939c-bccf519864a3', 'parent': 'f7c20633-6a60-4ca3-96b1-13fee66e321d', 'section_id': '', 'section_index': 0, 'text': '# MultiQueryRetriever Distance-based vector database retrieval embeds (represents) queries in high-dimensional space and finds similar embedded documents based on "distance". But, retrieval may produce different results with subtle changes in query wording or if the embeddings do not capture the semantics of the data well. Prompt engineering / tuning is sometimes done to manually address these problems, but can be tedious. The `MultiQueryRetriever` automates the process of prompt tuning by using an LLM to generate multiple queries from different perspectives for a given user input query. For each query, it retrieves a set of relevant documents and takes the unique union across all queries to get a larger set of potentially relevant documents. By generating multiple perspectives on the same question, the `MultiQueryRetriever` might be able to overcome some of the limitations of the distance-based retrieval and get a richer set of results.', 'title': 'MultiQueryRetriever | 🦜️🔗 Langchain', 'type': None, 'url': 'https://python.langchain.com/docs/modules/data_connection/retrievers/MultiQueryRetriever'}),  
         Document(page_content='# `langchain.retrievers.multi_vector`.MultiVectorRetriever[¶](#langchain-retrievers-multi-vector-multivectorretriever) *class *langchain.retrievers.multi_vector.MultiVectorRetriever[[source]](../_modules/langchain/retrievers/multi_vector.html#MultiVectorRetriever)[¶](#langchain.retrievers.multi_vector.MultiVectorRetriever) # Examples using MultiVectorRetriever[¶](#langchain-retrievers-multi-vector-multivectorretriever) - [MultiVector Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector)', metadata={'id': '1f4ca702-35b8-44c0-b33b-18c09a1f787d', 'library_id': '6254c672-7aa0-4233-b0a6-804bd273752b', 'page_id': '87f5d1fb-a1c6-4080-9d2b-7b88794eb6bf', 'parent': '1820c44d-7783-4846-a11c-106b18da015d', 'section_id': 'langchain-retrievers-multi-vector-multivectorretriever', 'section_index': 0, 'text': '# `langchain.retrievers.multi_vector`.MultiVectorRetriever[¶](#langchain-retrievers-multi-vector-multivectorretriever) *class *langchain.retrievers.multi_vector.MultiVectorRetriever[[source]](../_modules/langchain/retrievers/multi_vector.html#MultiVectorRetriever)[¶](#langchain.retrievers.multi_vector.MultiVectorRetriever) # Examples using MultiVectorRetriever[¶](#langchain-retrievers-multi-vector-multivectorretriever) - [MultiVector Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector)', 'title': 'langchain.retrievers.multi_vector.MultiVectorRetriever — 🦜🔗 LangChain 0.0.322', 'type': None, 'url': 'https://api.python.langchain.com/en/latest/retrievers/langchain.retrievers.multi_vector.MultiVectorRetriever.html#langchain-retrievers-multi-vector-multivectorretriever'})]  
    


```
[/code]


## Other packages​

You can download and use other embeddings from this Dropbox link.

## Retrieve parent docs​

The embeddings provided by Fleet AI contain metadata that indicates which embedding chunks correspond to the same original document page. If we'd like we can use this information to retrieve whole
parent documents, and not just embedded chunks. Under the hood, we'll use a MultiVectorRetriever and a BaseStore object to search for relevant chunks and then map them to their parent document.

[code]
```python




    from langchain.storage import InMemoryStore  
      
    parent_retriever = load_fleet_retriever(  
        "https://www.dropbox.com/scl/fi/4rescpkrg9970s3huz47l/libraries_langchain_release.parquet?rlkey=283knw4wamezfwiidgpgptkep&dl=1",  
        docstore=InMemoryStore(),  
    )  
    


```
[/code]


[code]
```python




    parent_retriever.get_relevant_documents("How does the multi vector retriever work")  
    


```
[/code]


[code]
```python




        [Document(page_content='Vector store-backed retriever | 🦜️🔗 Langchain\n# Vector store-backed retriever A vector store retriever is a retriever that uses a vector store to retrieve documents. It is a lightweight wrapper around the vector store class to make it conform to the retriever interface. It uses the search methods implemented by a vector store, like similarity search and MMR, to query the texts in the vector store. Once you construct a vector store, it\'s very easy to construct a retriever. Let\'s walk through an example.Once you construct a vector store, it\'s very easy to construct a retriever. Let\'s walk through an example. ``` from langchain.document_loaders import TextLoaderloader = TextLoader(\'../../../state_of_the_union.txt\') ``` ``` from langchain.text_splitter import CharacterTextSplitterfrom langchain.vectorstores import FAISSfrom langchain.embeddings import OpenAIEmbeddingsdocuments = loader.load()text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)texts = text_splitter.split_documents(documents)embeddings = OpenAIEmbeddings()db = FAISS.from_documents(texts, embeddings) ``` ``` Exiting: Cleaning up .chroma directory ``` ``` retriever = db.as_retriever() ``` ``` docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson") ``` ## Maximum marginal relevance retrieval[\u200b](#maximum-marginal-relevance-retrieval) By default, the vector store retriever uses similarity search.If the underlying vector store supports maximum marginal relevance search, you can specify that as the search type. ``` retriever = db.as_retriever(search_type="mmr") ``` ``` docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson") ``` ## Similarity score threshold retrieval[\u200b](#similarity-score-threshold-retrieval) You can also a retrieval method that sets a similarity score threshold and only returns documents with a score above that threshold. ``` retriever = db.as_retriever(search_type="similarity_score_threshold", search_kwargs={"score_threshold": .5}) ``` ``` docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson") ``` ## Specifying top k[\u200b](#specifying-top-k) You can also specify search kwargs like `k` to use when doing retrieval.``` retriever = db.as_retriever(search_kwargs={"k": 1}) ``` ``` docs = retriever.get_relevant_documents("what did he say about ketanji brown jackson") ``` ``` len(docs) ``` ``` 1 ```', metadata={'title': 'Vector store-backed retriever | 🦜️🔗 Langchain', 'type': None, 'url': 'https://python.langchain.com/docs/modules/data_connection/retrievers/vectorstore', 'id': 'c153ebd9-2611-4a43-9db6-daa1f5f214f6'}),  
         Document(page_content='MultiVector Retriever | 🦜️🔗 Langchain\n# MultiVector Retriever It can often be beneficial to store multiple vectors per document. There are multiple use cases where this is beneficial. LangChain has a base `MultiVectorRetriever` which makes querying this type of setup easy. A lot of the complexity lies in how to create the multiple vectors per document. This notebook covers some of the common ways to create those vectors and use the `MultiVectorRetriever`. The methods to create multiple vectors per document include: - Smaller chunks: split a document into smaller chunks, and embed those (this is ParentDocumentRetriever). - Summary: create a summary for each document, embed that along with (or instead of) the document. - Hypothetical questions: create hypothetical questions that each document would be appropriate to answer, embed those along with (or instead of) the document. Note that this also enables another method of adding embeddings - manually.Note that this also enables another method of adding embeddings - manually. This is great because you can explicitly add questions or queries that should lead to a document being recovered, giving you more control. ``` from langchain.retrievers.multi_vector import MultiVectorRetriever ``` ``` from langchain.vectorstores import Chromafrom langchain.embeddings import OpenAIEmbeddingsfrom langchain.text_splitter import RecursiveCharacterTextSplitterfrom langchain.storage import InMemoryStorefrom langchain.document_loaders import TextLoader ``` ``` loaders = [ TextLoader(\'../../paul_graham_essay.txt\'), TextLoader(\'../../state_of_the_union.txt\'),]docs = []for l in loaders: docs.extend(l.load())text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000)docs = text_splitter.split_documents(docs) ``` ## Smaller chunks[\u200b](#smaller-chunks) Often times it can be useful to retrieve larger chunks of information, but embed smaller chunks.This allows for embeddings to capture the semantic meaning as closely as possible, but for as much context as possible to be passed downstream. Note that this is what the `ParentDocumentRetriever` does. Here we show what is going on under the hood.``` # The vectorstore to use to index the child chunksvectorstore = Chroma( collection_name="full_documents", embedding_function=OpenAIEmbeddings())# The storage layer for the parent documentsstore = InMemoryStore()id_key = "doc_id"# The retriever (empty to start)retriever = MultiVectorRetriever( vectorstore=vectorstore, docstore=store, id_key=id_key,)import uuiddoc_ids = [str(uuid.uuid4()) for _ in docs] ``` ``` # The splitter to use to create smaller chunkschild_text_splitter = RecursiveCharacterTextSplitter(chunk_size=400) ``` ``` sub_docs = []for i, doc in enumerate(docs): _id = doc_ids[i] _sub_docs = child_text_splitter.split_documents([doc]) for _doc in _sub_docs: _doc.metadata[id_key] = _id sub_docs.extend(_sub_docs) ``` ``` retriever.vectorstore.add_documents(sub_docs)retriever.docstore.mset(list(zip(doc_ids, docs))) ``` ``` # Vectorstore alone retrieves the small chunksretriever.vectorstore.similarity_search("justice breyer")[0] ``` ``` Document(page_content=\'Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court.Justice Breyer, thank you for your service. \\n\\nOne of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court. \', metadata={\'doc_id\': \'10e9cbc0-4ba5-4d79-a09b-c033d1ba7b01\', \'source\': \'../../state_of_the_union.txt\'}) ``` ``` # Retriever returns larger chunkslen(retriever.get_relevant_documents("justice breyer")[0].page_content) ``` ``` 9874 ``` ## Summary[\u200b](#summary) Oftentimes a summary may be able to distill more accurately what a chunk is about, leading to better retrieval. Here we show how to create summaries, and then embed those.``` from langchain.chat_models import ChatOpenAIfrom langchain.prompts import ChatPromptTemplatefrom langchain.schema.output_parser import StrOutputParserimport uuidfrom langchain.schema.document import Document ``` ``` chain = ( {"doc": lambda x: x.page_content} | ChatPromptTemplate.from_template("Summarize the following document:\\n\\n{doc}") | ChatOpenAI(max_retries=0) | StrOutputParser()) ``` ``` summaries = chain.batch(docs, {"max_concurrency": 5}) ``` ``` # The vectorstore to use to index the child chunksvectorstore = Chroma( collection_name="summaries", embedding_function=OpenAIEmbeddings())# The storage layer for the parent documentsstore = InMemoryStore()id_key = "doc_id"# The retriever (empty to start)retriever = MultiVectorRetriever( vectorstore=vectorstore, docstore=store, id_key=id_key,)doc_ids = [str(uuid.uuid4()) for _ in docs] ``` ``` summary_docs = [Document(page_content=s,metadata={id_key: doc_ids[i]}) for i, s in enumerate(summaries)] ``` ``` retriever.vectorstore.add_documents(summary_docs)retriever.docstore.mset(list(zip(doc_ids, docs))) ``` ``` # # We can also add the original chunks to the vectorstore if we so want# for i, doc in enumerate(docs):# doc.metadata[id_key] = doc_ids[i]# retriever.vectorstore.add_documents(docs) ``` ``` sub_docs = vectorstore.similarity_search("justice breyer") ``` ``` sub_docs[0] ``` ``` Document(page_content="The document is a transcript of a speech given by the President of the United States.The President discusses several important issues and initiatives, including the nomination of a Supreme Court Justice, border security and immigration reform, protecting women\'s rights, advancing LGBTQ+ equality, bipartisan legislation, addressing the opioid epidemic and mental health, supporting veterans, investigating the health effects of burn pits on military personnel, ending cancer, and the strength and resilience of the American people. ", metadata={\'doc_id\': \'79fa2e9f-28d9-4372-8af3-2caf4f1de312\'}) ``` ``` retrieved_docs = retriever.get_relevant_documents("justice breyer") ``` ``` len(retrieved_docs[0].page_content) ``` ``` 9194 ``` ## Hypothetical Queries[\u200b](#hypothetical-queries) An LLM can also be used to generate a list of hypothetical questions that could be asked of a particular document.These questions can then be embedded ``` functions = [ { "name": "hypothetical_questions", "description": "Generate hypothetical questions", "parameters": { "type": "object", "properties": { "questions": { "type": "array", "items": { "type": "string" }, }, }, "required": ["questions"] } } ] ``` ``` from langchain.output_parsers.openai_functions import JsonKeyOutputFunctionsParserchain = ( {"doc": lambda x: x.page_content} # Only asking for 3 hypothetical questions, but this could be adjusted | ChatPromptTemplate.from_template("Generate a list of 3 hypothetical questions that the below document could be used to answer:\\n\\n{doc}") | ChatOpenAI(max_retries=0, model="gpt-4").bind(functions=functions, function_call={"name": "hypothetical_questions"}) | JsonKeyOutputFunctionsParser(key_name="questions")) ``` ``` chain.invoke(docs[0]) ``` ``` ["What was the author\'s initial impression of philosophy as a field of study, and how did it change when they got to college?", \'Why did the author decide to switch their focus to Artificial Intelligence (AI)? \', "What led to the author\'s disillusionment with the field of AI as it was practiced at the time?"]``` ``` hypothetical_questions = chain.batch(docs, {"max_concurrency": 5}) ``` ``` # The vectorstore to use to index the child chunksvectorstore = Chroma( collection_name="hypo-questions", embedding_function=OpenAIEmbeddings())# The storage layer for the parent documentsstore = InMemoryStore()id_key = "doc_id"# The retriever (empty to start)retriever = MultiVectorRetriever( vectorstore=vectorstore, docstore=store, id_key=id_key,)doc_ids = [str(uuid.uuid4()) for _ in docs] ``` ``` question_docs = []for i, question_list in enumerate(hypothetical_questions): question_docs.extend([Document(page_content=s,metadata={id_key: doc_ids[i]}) for s in question_list]) ``` ``` retriever.vectorstore.add_documents(question_docs)retriever.docstore.mset(list(zip(doc_ids, docs))) ``` ``` sub_docs = vectorstore.similarity_search("justice breyer") ``` ``` sub_docs ``` ``` [Document(page_content="What is the President\'s stance on immigration reform?", metadata={\'doc_id\': \'505d73e3-8350-46ec-a58e-3af032f04ab3\'}), Document(page_content="What is the President\'s stance on immigration reform? ", metadata={\'doc_id\': \'1c9618f0-7660-4b4f-a37c-509cbbbf6dba\'}), Document(page_content="What is the President\'s stance on immigration reform? ", metadata={\'doc_id\': \'82c08209-b904-46a8-9532-edd2380950b7\'}), Document(page_content=\'What measures is the President proposing to protect the rights of LGBTQ+ Americans? \', metadata={\'doc_id\': \'82c08209-b904-46a8-9532-edd2380950b7\'})] ``` ``` retrieved_docs = retriever.get_relevant_documents("justice breyer") ``` ``` len(retrieved_docs[0].page_content) ``` ``` 9194 ```', metadata={'title': 'MultiVector Retriever | 🦜️🔗 Langchain', 'type': None, 'url': 'https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector', 'id': 'beec5531-16a7-453c-80ab-c5628e0236ce'}),  
         Document(page_content='MultiQueryRetriever | 🦜️🔗 Langchain\n# MultiQueryRetriever Distance-based vector database retrieval embeds (represents) queries in high-dimensional space and finds similar embedded documents based on "distance". But, retrieval may produce different results with subtle changes in query wording or if the embeddings do not capture the semantics of the data well. Prompt engineering / tuning is sometimes done to manually address these problems, but can be tedious. The `MultiQueryRetriever` automates the process of prompt tuning by using an LLM to generate multiple queries from different perspectives for a given user input query. For each query, it retrieves a set of relevant documents and takes the unique union across all queries to get a larger set of potentially relevant documents. By generating multiple perspectives on the same question, the `MultiQueryRetriever` might be able to overcome some of the limitations of the distance-based retrieval and get a richer set of results.By generating multiple perspectives on the same question, the `MultiQueryRetriever` might be able to overcome some of the limitations of the distance-based retrieval and get a richer set of results. ``` # Build a sample vectorDBfrom langchain.vectorstores import Chromafrom langchain.document_loaders import WebBaseLoaderfrom langchain.embeddings.openai import OpenAIEmbeddingsfrom langchain.text_splitter import RecursiveCharacterTextSplitter# Load blog postloader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")data = loader.load()# Splittext_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)splits = text_splitter.split_documents(data)# VectorDBembedding = OpenAIEmbeddings()vectordb = Chroma.from_documents(documents=splits, embedding=embedding) ``` #### Simple usage[\u200b](#simple-usage) Specify the LLM to use for query generation, and the retriever will do the rest.``` from langchain.chat_models import ChatOpenAIfrom langchain.retrievers.multi_query import MultiQueryRetrieverquestion = "What are the approaches to Task Decomposition? "llm = ChatOpenAI(temperature=0)retriever_from_llm = MultiQueryRetriever.from_llm( retriever=vectordb.as_retriever(), llm=llm) ``` ``` # Set logging for the queriesimport logginglogging.basicConfig()logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO) ``` ``` unique_docs = retriever_from_llm.get_relevant_documents(query=question)len(unique_docs) ``` ``` INFO:langchain.retrievers.multi_query:Generated queries: [\'1. How can Task Decomposition be approached? \', \'2. What are the different methods for Task Decomposition? \', \'3. What are the various approaches to decomposing tasks?\'] 5 ``` #### Supplying your own prompt[\u200b](#supplying-your-own-prompt) You can also supply a prompt along with an output parser to split the results into a list of queries.5 ``` #### Supplying your own prompt[\u200b](#supplying-your-own-prompt) You can also supply a prompt along with an output parser to split the results into a list of queries. ``` from typing import Listfrom langchain.chains import LLMChainfrom pydantic import BaseModel, Fieldfrom langchain.prompts import PromptTemplatefrom langchain.output_parsers import PydanticOutputParser# Output parser will split the LLM result into a list of queriesclass LineList(BaseModel): # "lines" is the key (attribute name) of the parsed output lines: List[str] = Field(description="Lines of text")class LineListOutputParser(PydanticOutputParser): def __init__(self) -> None: super().__init__(pydantic_object=LineList) def parse(self, text: str) -> LineList: lines = text.strip().split("\\n") return LineList(lines=lines)output_parser = LineListOutputParser()QUERY_PROMPT = PromptTemplate( input_variables=["question"], template="""You are an AI language model assistant.Your task is to generate five different versions of the given user question to retrieve relevant documents from a vector database. By generating multiple perspectives on the user question, your goal is to help the user overcome some of the limitations of the distance-based similarity search. Provide these alternative questions separated by newlines. Original question: {question}""",)llm = ChatOpenAI(temperature=0)# Chainllm_chain = LLMChain(llm=llm, prompt=QUERY_PROMPT, output_parser=output_parser)# Other inputsquestion = "What are the approaches to Task Decomposition?" ``` ``` # Runretriever = MultiQueryRetriever( retriever=vectordb.as_retriever(), llm_chain=llm_chain, parser_key="lines") # "lines" is the key (attribute name) of the parsed output# Resultsunique_docs = retriever.get_relevant_documents( query="What does the course say about regression? ")len(unique_docs) ``` ``` INFO:langchain.retrievers.multi_query:Generated queries: ["1.")len(unique_docs) ``` ``` INFO:langchain.retrievers.multi_query:Generated queries: ["1. What is the course\'s perspective on regression? ", \'2. Can you provide information on regression as discussed in the course? \', \'3. How does the course cover the topic of regression? \', "4. What are the course\'s teachings on regression? ", \'5. In relation to the course, what is mentioned about regression?\'] 11 ```', metadata={'title': 'MultiQueryRetriever | 🦜️🔗 Langchain', 'type': None, 'url': 'https://python.langchain.com/docs/modules/data_connection/retrievers/MultiQueryRetriever', 'id': 'f7c20633-6a60-4ca3-96b1-13fee66e321d'}),  
         Document(page_content='langchain.retrievers.multi_vector.MultiVectorRetriever — 🦜🔗 LangChain 0.0.322\n# `langchain.retrievers.multi_vector`.MultiVectorRetriever[¶](#langchain-retrievers-multi-vector-multivectorretriever) *class *langchain.retrievers.multi_vector.MultiVectorRetriever[[source]](../_modules/langchain/retrievers/multi_vector.html#MultiVectorRetriever)[¶](#langchain.retrievers.multi_vector.MultiVectorRetriever) # Examples using MultiVectorRetriever[¶](#langchain-retrievers-multi-vector-multivectorretriever) - [MultiVector Retriever](https://python.langchain.com/docs/modules/data_connection/retrievers/multi_vector)', metadata={'title': 'langchain.retrievers.multi_vector.MultiVectorRetriever — 🦜🔗 LangChain 0.0.322', 'type': None, 'url': 'https://api.python.langchain.com/en/latest/retrievers/langchain.retrievers.multi_vector.MultiVectorRetriever.html#langchain-retrievers-multi-vector-multivectorretriever', 'id': '1820c44d-7783-4846-a11c-106b18da015d'})]  
    


```
[/code]


## Putting it in a chain​

Let's try using our retrieval systems in a simple chain!

[code]
```python




    from langchain.chat_models import ChatOpenAI  
    from langchain.prompts import ChatPromptTemplate  
    from langchain.schema import StrOutputParser  
    from langchain.schema.runnable import RunnablePassthrough  
      
    prompt = ChatPromptTemplate.from_messages(  
        [  
            (  
                "system",  
                """You are a great software engineer who is very familiar \  
    with Python. Given a user question or request about a new Python library called LangChain and \  
    parts of the LangChain documentation, answer the question or generate the requested code. \  
    Your answers must be accurate, should include code whenever possible, and should assume anything \  
    about LangChain which is note explicitly stated in the LangChain documentation. If the required \  
    information is not available, just say so.  
      
    LangChain Documentation  
    ------------------  
      
    {context}""",  
            ),  
            ("human", "{question}"),  
        ]  
    )  
      
    model = ChatOpenAI(model="gpt-3.5-turbo-16k")  
      
    chain = (  
        {  
            "question": RunnablePassthrough(),  
            "context": parent_retriever  
            | (lambda docs: "\n\n".join(d.page_content for d in docs)),  
        }  
        | prompt  
        | model  
        | StrOutputParser()  
    )  
    


```
[/code]


[code]
```python




    for chunk in chain.invoke(  
        "How do I create a FAISS vector store retriever that returns 10 documents per search query"  
    ):  
        print(chunk, end="", flush=True)  
    


```
[/code]


[code]
```python




        To create a FAISS vector store retriever that returns 10 documents per search query, you can use the following code:  
          
        ```python  
        from langchain.embeddings import OpenAIEmbeddings  
        from langchain.vectorstores import FAISS  
          
        # Assuming you have already loaded and split your documents  
        # into `texts` and initialized your `embeddings` object  
          
        # Create the FAISS vector store  
        db = FAISS.from_documents(texts, embeddings)  
          
        # Create the retriever with the desired search kwargs  
        retriever = db.as_retriever(search_kwargs={"k": 10})  
        ```  
          
        Now, you can use the `retriever` object to get relevant documents using the `get_relevant_documents` method. For example:  
          
        ```python  
        docs = retriever.get_relevant_documents("your search query")  
        ```  
          
        This will return a list of 10 documents that are most relevant to the given search query.  
    


```
[/code]


