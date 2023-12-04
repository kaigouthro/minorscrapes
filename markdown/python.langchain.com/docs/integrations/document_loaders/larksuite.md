

Skip to main content

# LarkSuite (FeiShu)

> LarkSuite is an enterprise collaboration platform developed by ByteDance.

This notebook covers how to load data from the `LarkSuite` REST API into a format that can be ingested into LangChain, along with example usage for text summarization.

The LarkSuite API requires an access token (tenant_access_token or user_access_token), checkout LarkSuite open platform document for API details.

[code]
```python




    from getpass import getpass  
      
    from langchain.document_loaders.larksuite import LarkSuiteDocLoader  
      
    DOMAIN = input("larksuite domain")  
    ACCESS_TOKEN = getpass("larksuite tenant_access_token or user_access_token")  
    DOCUMENT_ID = input("larksuite document id")  
    


```
[/code]


[code]
```python




    from pprint import pprint  
      
    larksuite_loader = LarkSuiteDocLoader(DOMAIN, ACCESS_TOKEN, DOCUMENT_ID)  
    docs = larksuite_loader.load()  
      
    pprint(docs)  
    


```
[/code]


[code]
```python




        [Document(page_content='Test Doc\nThis is a Test Doc\n\n1\n2\n3\n\n', metadata={'document_id': 'V76kdbd2HoBbYJxdiNNccajunPf', 'revision_id': 11, 'title': 'Test Doc'})]  
    


```
[/code]


[code]
```python




    # see https://python.langchain.com/docs/use_cases/summarization for more details  
    from langchain.chains.summarize import load_summarize_chain  
      
    chain = load_summarize_chain(llm, chain_type="map_reduce")  
    chain.run(docs)  
    


```
[/code]


