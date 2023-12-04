

Skip to main content

# Alibaba Cloud OpenSearch

> Alibaba Cloud Opensearch is a one-stop platform to develop intelligent search services. `OpenSearch` was built on the large-scale distributed search engine developed by `Alibaba`. `OpenSearch`
> serves more than 500 business cases in Alibaba Group and thousands of Alibaba Cloud customers. `OpenSearch` helps develop search services in different search scenarios, including e-commerce, O2O,
> multimedia, the content industry, communities and forums, and big data query in enterprises.

> `OpenSearch` helps you develop high quality, maintenance-free, and high performance intelligent search services to provide your users with high search efficiency and accuracy.

> `OpenSearch` provides the vector search feature. In specific scenarios, especially test question search and image search scenarios, you can use the vector search feature together with the multimodal
> search feature to improve the accuracy of search results.

This notebook shows how to use functionality related to the `Alibaba Cloud OpenSearch Vector Search Edition`. To run, you should have an OpenSearch Vector Search Edition instance up and running:

Read the help document to quickly familiarize and configure OpenSearch Vector Search Edition instance.

After the instance is up and running, follow these steps to split documents, get embeddings, connect to the alibaba cloud opensearch instance, index documents, and perform vector retrieval.

We need to install the following Python packages first.

[code]
```python




    #!pip install alibabacloud_ha3engine_vector  
    


```
[/code]


We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

[code]
```python




    import getpass  
    import os  
      
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores import (  
        AlibabaCloudOpenSearch,  
        AlibabaCloudOpenSearchSettings,  
    )  
    


```
[/code]


Split documents and get embeddings.

[code]
```python




    from langchain.document_loaders import TextLoader  
      
    loader = TextLoader("../../../state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


Create opensearch settings.

[code]
```python




    settings = AlibabaCloudOpenSearchSettings(  
        endpoint=" The endpoint of opensearch instance, You can find it from the console of Alibaba Cloud OpenSearch.",  
        instance_id="The identify of opensearch instance, You can find it from the console of Alibaba Cloud OpenSearch.",  
        protocol="Communication Protocol between SDK and Server, default is http.",  
        username="The username specified when purchasing the instance.",  
        password="The password specified when purchasing the instance.",  
        namespace="The instance data will be partitioned based on the namespace field. If the namespace is enabled, you need to specify the namespace field name during initialization. Otherwise, the queries cannot be executed correctly.",  
        tablename="The table name specified during instance configuration.",  
        embedding_field_separator="Delimiter specified for writing vector field data, default is comma.",  
        output_fields="Specify the field list returned when invoking OpenSearch, by default it is the value list of the field mapping field.",  
        field_name_mapping={  
            "id": "id",  # The id field name mapping of index document.  
            "document": "document",  # The text field name mapping of index document.  
            "embedding": "embedding",  # The embedding field name mapping of index document.  
            "name_of_the_metadata_specified_during_search": "opensearch_metadata_field_name,=",  
            # The metadata field name mapping of index document, could specify multiple, The value field contains mapping name and operator, the operator would be used when executing metadata filter query,  
            # Currently supported logical operators are: > (greater than), < (less than), = (equal to), <= (less than or equal to), >= (greater than or equal to), != (not equal to).  
            # Refer to this link: https://help.aliyun.com/zh/open-search/vector-search-edition/filter-expression  
        },  
    )  
      
    # for example  
      
    # settings = AlibabaCloudOpenSearchSettings(  
    #     endpoint='ha-cn-5yd3fhdm102.public.ha.aliyuncs.com',  
    #     instance_id='ha-cn-5yd3fhdm102',  
    #     username='instance user name',  
    #     password='instance password',  
    #     table_name='test_table',  
    #     field_name_mapping={  
    #         "id": "id",  
    #         "document": "document",  
    #         "embedding": "embedding",  
    #         "string_field": "string_filed,=",  
    #         "int_field": "int_filed,=",  
    #         "float_field": "float_field,=",  
    #         "double_field": "double_field,="  
    #  
    #     },  
    # )  
    


```
[/code]


Create an opensearch access instance by settings.

[code]
```python




    # Create an opensearch instance and index docs.  
    opensearch = AlibabaCloudOpenSearch.from_texts(  
        texts=docs, embedding=embeddings, config=settings  
    )  
    


```
[/code]


or

[code]
```python




    # Create an opensearch instance.  
    opensearch = AlibabaCloudOpenSearch(embedding=embeddings, config=settings)  
    


```
[/code]


Add texts and build index.

[code]
```python




    metadatas = [  
        {"string_field": "value1", "int_field": 1, "float_field": 1.0, "double_field": 2.0},  
        {"string_field": "value2", "int_field": 2, "float_field": 3.0, "double_field": 4.0},  
        {"string_field": "value3", "int_field": 3, "float_field": 5.0, "double_field": 6.0},  
    ]  
    # the key of metadatas must match field_name_mapping in settings.  
    opensearch.add_texts(texts=docs, ids=[], metadatas=metadatas)  
    


```
[/code]


Query and retrieve data.

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs = opensearch.similarity_search(query)  
    print(docs[0].page_content)  
    


```
[/code]


Query and retrieve data with metadata.

[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    metadata = {  
        "string_field": "value1",  
        "int_field": 1,  
        "float_field": 1.0,  
        "double_field": 2.0,  
    }  
    docs = opensearch.similarity_search(query, filter=metadata)  
    print(docs[0].page_content)  
    


```
[/code]


If you encounter any problems during use, please feel free to contact xingshaomin.xsm@alibaba-inc.com, and we will do our best to provide you with assistance and support.

