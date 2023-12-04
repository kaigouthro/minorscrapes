

Skip to main content

On this page

# Bedrock (Knowledge Bases)

> Knowledge bases for Amazon Bedrock is an Amazon Web Services (AWS) offering which lets you quickly build RAG applications by using your private data to customize FM response.

> Implementing `RAG` requires organizations to perform several cumbersome steps to convert data into embeddings (vectors), store the embeddings in a specialized vector database, and build custom
> integrations into the database to search and retrieve text relevant to the user’s query. This can be time-consuming and inefficient.

> With `Knowledge Bases for Amazon Bedrock`, simply point to the location of your data in `Amazon S3`, and `Knowledge Bases for Amazon Bedrock` takes care of the entire ingestion workflow into your
> vector database. If you do not have an existing vector database, Amazon Bedrock creates an Amazon OpenSearch Serverless vector store for you. For retrievals, use the Langchain - Amazon Bedrock
> integration via the Retrieve API to retrieve relevant results for a user query from knowledge bases.

> Knowledge base can be configured through AWS Console or by using AWS SDKs.

## Using the Knowledge Bases Retriever​

[code]
```python




    %pip install boto3  
    


```
[/code]


[code]
```python




    from langchain.retrievers import AmazonKnowledgeBasesRetriever  
      
    retriever = AmazonKnowledgeBasesRetriever(  
        knowledge_base_id="PUIJP4EQUA",  
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 4}},  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown?"  
      
    retriever.get_relevant_documents(query=query)  
    


```
[/code]


### Using in a QA Chain​

[code]
```python




    from botocore.client import Config  
    from langchain.chains import RetrievalQA  
    from langchain.llms import Bedrock  
      
    model_kwargs_claude = {"temperature": 0, "top_k": 10, "max_tokens_to_sample": 3000}  
      
    llm = Bedrock(model_id="anthropic.claude-v2", model_kwargs=model_kwargs_claude)  
      
    qa = RetrievalQA.from_chain_type(  
        llm=llm, retriever=retriever, return_source_documents=True  
    )  
      
    qa(query)  
    


```
[/code]


