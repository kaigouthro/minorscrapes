

Skip to main content

On this page

# Azure AI Data

> Azure AI Studio provides the capability to upload data assets to cloud storage and register existing data assets from the following sources:

  * Microsoft OneLake
  * Azure Blob Storage
  * Azure Data Lake gen 2

The benefit of this approach over `AzureBlobStorageContainerLoader` and `AzureBlobStorageFileLoader` is that authentication is handled seamlessly to cloud storage. You can use either _identity-based_
data access control to the data or _credential-based_ (e.g. SAS token, account key). In the case of credential-based data access you do not need to specify secrets in your code or set up key vaults -
the system handles that for you.

This notebook covers how to load document objects from a data asset in AI Studio.

[code]
```python




    #!pip install azureml-fsspec, azure-ai-generative  
    


```
[/code]


[code]
```python




    from azure.ai.resources.client import AIClient  
    from azure.identity import DefaultAzureCredential  
    from langchain.document_loaders import AzureAIDataLoader  
    


```
[/code]


[code]
```python




    # Create a connection to your project  
    client = AIClient(  
        credential=DefaultAzureCredential(),  
        subscription_id="<subscription_id>",  
        resource_group_name="<resource_group_name>",  
        project_name="<project_name>",  
    )  
    


```
[/code]


[code]
```python




    # get the latest version of your data asset  
    data_asset = client.data.get(name="<data_asset_name>", label="latest")  
    


```
[/code]


[code]
```python




    # load the data asset  
    loader = AzureAIDataLoader(url=data_asset.path)  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


[code]
```python




        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpaa9xl6ch/fake.docx'}, lookup_index=0)]  
    


```
[/code]


## Specifying a glob pattern​

You can also specify a glob pattern for more finegrained control over what files to load. In the example below, only files with a `pdf` extension will be loaded.

[code]
```python




    loader = AzureAIDataLoader(url=data_asset.path, glob="*.pdf")  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


[code]
```python




        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': '/var/folders/y6/8_bzdg295ld6s1_97_12m4lr0000gn/T/tmpujbkzf_l/fake.docx'}, lookup_index=0)]  
    


```
[/code]


