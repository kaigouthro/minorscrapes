

Skip to main content

On this page

# Azure Document Intelligence

Azure Document Intelligence (formerly known as Azure Forms Recognizer) is machine-learning based service that extracts text (including handwriting), tables or key-value-pairs from scanned documents or
images.

This current implementation of a loader using Document Intelligence is able to incorporate content page-wise and turn it into LangChain documents.

Document Intelligence supports PDF, JPEG, PNG, BMP, or TIFF.

Further documentation is available at https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/?view=doc-intel-3.1.0.

[code]
```python




    %pip install langchain azure-ai-formrecognizer -q  
    


```
[/code]


## Example 1​

The first example uses a local file which will be sent to Azure Document Intelligence.

First, an instance of a DocumentAnalysisClient is created with endpoint and key for the Azure service.

[code]
```python




    from azure.ai.formrecognizer import DocumentAnalysisClient  
    from azure.core.credentials import AzureKeyCredential  
      
    document_analysis_client = DocumentAnalysisClient(  
        endpoint="<service_endpoint>", credential=AzureKeyCredential("<service_key>")  
    )  
    


```
[/code]


With the initialized document analysis client, we can proceed to create an instance of the DocumentIntelligenceLoader:

[code]
```python




    from langchain.document_loaders.pdf import DocumentIntelligenceLoader  
      
    loader = DocumentIntelligenceLoader(  
        "<Local_filename>", client=document_analysis_client, model="<model_name>"  
    )  # e.g. prebuilt-document  
      
    documents = loader.load()  
    


```
[/code]


The output contains each page of the source document as a LangChain document:

[code]
```python




    documents  
    


```
[/code]


[code]
```python




        [Document(page_content='...', metadata={'source': '...', 'page': 1})]  
    


```
[/code]


