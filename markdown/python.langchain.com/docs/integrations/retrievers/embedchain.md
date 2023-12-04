

Skip to main content

# Embedchain

Embedchain is a RAG framework to create data pipelines. It loads, indexes, retrieves and syncs all the data.

It is available as an open source package and as a hosted platform solution.

This notebook shows how to use a retriever that uses Embedchain.

# Installation

First you will need to install the `embedchain` package.

You can install the package by running

[code]
```python




    #!pip install --upgrade embedchain  
    


```
[/code]


# Create New Retriever

`EmbedchainRetriever` has a static `.create()` factory method that takes the following arguments:

  * `yaml_path: string` optional -- Path to the YAML configuration file. If not provided, a default configuration is used. You can browse the docs to explore various customization options.

[code]
```python




    # Setup API Key  
      
    import os  
    from getpass import getpass  
      
    os.environ["OPENAI_API_KEY"] = getpass()  
    


```
[/code]


[code]
```python




         ········  
    


```
[/code]


[code]
```python




    from langchain.retrievers import EmbedchainRetriever  
      
    # create retriever with default options  
    retriever = EmbedchainRetriever.create()  
      
    # or if you want to customize, pass the yaml config path  
    # retriever = EmbedchainRetiever.create(yaml_path="config.yaml")  
    


```
[/code]


# Add Data

In embedchain, you can as many supported data types as possible. You can browse our docs to see the data types supported.

Embedchain automatically deduces the types of the data. So you can add a string, URL or local file path.

[code]
```python




    retriever.add_texts(  
        [  
            "https://en.wikipedia.org/wiki/Elon_Musk",  
            "https://www.forbes.com/profile/elon-musk",  
            "https://www.youtube.com/watch?v=RcYjXbSJBN8",  
        ]  
    )  
    


```
[/code]


[code]
```python




        Inserting batches in chromadb: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:08<00:00,  2.22s/it]  
      
      
        Successfully saved https://en.wikipedia.org/wiki/Elon_Musk (DataType.WEB_PAGE). New chunks count: 378  
      
      
        Inserting batches in chromadb: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:01<00:00,  1.17s/it]  
      
      
        Successfully saved https://www.forbes.com/profile/elon-musk (DataType.WEB_PAGE). New chunks count: 13  
      
      
        Inserting batches in chromadb: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:02<00:00,  2.25s/it]  
      
        Successfully saved https://www.youtube.com/watch?v=RcYjXbSJBN8 (DataType.YOUTUBE_VIDEO). New chunks count: 53  
      
      
          
      
      
      
      
      
        ['1eab8dd1ffa92906f7fc839862871ca5',  
         '8cf46026cabf9b05394a2658bd1fe890',  
         'da3227cdbcedb018e05c47b774d625f6']  
    


```
[/code]


# Use Retriever

You can now use the retrieve to find relevant documents given a query

[code]
```python




    result = retriever.get_relevant_documents(  
        "How many companies does Elon Musk run and name those?"  
    )  
    


```
[/code]


[code]
```python




    result  
    


```
[/code]


[code]
```python




        [Document(page_content='Views Filmography Companies Zip2 X.com PayPal SpaceX Starlink Tesla, Inc. Energycriticismlitigation OpenAI Neuralink The Boring Company Thud X Corp. Twitteracquisitiontenure as CEO xAI In popular culture Elon Musk (Isaacson) Elon Musk (Vance) Ludicrous Power Play "Members Only" "The Platonic Permutation" "The Musk Who Fell to Earth" "One Crew over the Crewcoo\'s Morty" Elon Musk\'s Crash Course Related Boring Test Tunnel Hyperloop Musk family Musk vs. Zuckerberg SolarCity Tesla Roadster in space', metadata={'source': 'https://en.wikipedia.org/wiki/Elon_Musk', 'document_id': 'c33c05d0-5028-498b-b5e3-c43a4f9e8bf8--3342161a0fbc19e91f6bf387204aa30fbb2cea05abc81882502476bde37b9392'}),  
         Document(page_content='Elon Musk PROFILEElon MuskCEO, Tesla$241.2B$508M (0.21%)Real Time Net Worthas of 11/18/23Reflects change since 5 pm ET of prior trading day. 1 in the world todayPhoto by Martin Schoeller for ForbesAbout Elon MuskElon Musk cofounded six companies, including electric car maker Tesla, rocket producer SpaceX and tunneling startup Boring Company.He owns about 21% of Tesla between stock and options, but has pledged more than half his shares as collateral for personal loans of up to $3.5', metadata={'source': 'https://www.forbes.com/profile/elon-musk', 'document_id': 'c33c05d0-5028-498b-b5e3-c43a4f9e8bf8--3c8573134c575fafc025e9211413723e1f7a725b5936e8ee297fb7fb63bdd01a'}),  
         Document(page_content='to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion, and that same year, with $100 million of the money he made, Musk founded SpaceX, a spaceflight services company. In 2004, he became an early investor in electric vehicle manufacturer Tesla Motors, Inc. (now Tesla, Inc.). He became its chairman and product architect, assuming the position of CEO in 2008. In 2006, Musk helped create SolarCity, a solar-energy company that was acquired by Tesla in 2016 and became Tesla Energy.', metadata={'source': 'https://en.wikipedia.org/wiki/Elon_Musk', 'document_id': 'c33c05d0-5028-498b-b5e3-c43a4f9e8bf8--3342161a0fbc19e91f6bf387204aa30fbb2cea05abc81882502476bde37b9392'})]  
    


```
[/code]


