

Skip to main content

# Iugu

> Iugu is a Brazilian services and software as a service (SaaS) company. It offers payment-processing software and application programming interfaces for e-commerce websites and mobile applications.

This notebook covers how to load data from the `Iugu REST API` into a format that can be ingested into LangChain, along with example usage for vectorization.

```python




    from langchain.document_loaders import IuguLoader
    from langchain.indexes import VectorstoreIndexCreator



```


The Iugu API requires an access token, which can be found inside of the Iugu dashboard.

This document loader also requires a `resource` option which defines what data you want to load.

Following resources are available:

`Documentation` Documentation

```python




    iugu_loader = IuguLoader("charges")



```


```python




    # Create a vectorstore retriever from the loader
    # see https://python.langchain.com/en/latest/modules/data_connection/getting_started.html for more details

    index = VectorstoreIndexCreator().from_loaders([iugu_loader])
    iugu_doc_retriever = index.vectorstore.as_retriever()



```
