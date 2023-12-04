

Skip to main content

On this page

## Using the You.com Retriever​

The retriever from You.com is good for retrieving lots of text. We return multiple of the best text snippets per URL we find to be relevant.

First you just need to initialize the retriever

[code]
```python




    from langchain.chains import RetrievalQA  
    from langchain.llms import OpenAI  
    from langchain.retrievers.you_retriever import YouRetriever  
      
    yr = YouRetriever()  
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce", retriever=yr)  
    


```
[/code]


[code]
```python




    query = "what starting ohio state quarterback most recently went their entire college career without beating Michigan?"  
    qa.run(query)  
    


```
[/code]


