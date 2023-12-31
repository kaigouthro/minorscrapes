

Skip to main content

On this page

# Amazon Kendra

> Amazon Kendra is an intelligent search service provided by `Amazon Web Services` (`AWS`). It utilizes advanced natural language processing (NLP) and machine learning algorithms to enable powerful
> search capabilities across various data sources within an organization. `Kendra` is designed to help users find the information they need quickly and accurately, improving productivity and decision-
> making.

> With `Kendra`, users can search across a wide range of content types, including documents, FAQs, knowledge bases, manuals, and websites. It supports multiple languages and can understand complex
> queries, synonyms, and contextual meanings to provide highly relevant search results.

## Using the Amazon Kendra Index Retriever​

[code]
```python




    %pip install boto3  
    


```
[/code]


[code]
```python




    from langchain.retrievers import AmazonKendraRetriever  
    


```
[/code]


Create New Retriever

[code]
```python




    retriever = AmazonKendraRetriever(index_id="c0806df7-e76b-4bce-9b5c-d5582f6b1a03")  
    


```
[/code]


Now you can use retrieved documents from Kendra index

[code]
```python




    retriever.get_relevant_documents("what is langchain")  
    


```
[/code]


