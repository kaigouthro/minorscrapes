

Skip to main content

On this page

# AWS S3 File

> Amazon Simple Storage Service (Amazon S3) is an object storage service.

> AWS S3 Buckets

This covers how to load document objects from an `AWS S3 File` object.

[code]
```python




    from langchain.document_loaders import S3FileLoader  
    


```
[/code]


[code]
```python




    #!pip install boto3  
    


```
[/code]


[code]
```python




    loader = S3FileLoader("testing-hwc", "fake.docx")  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


[code]
```python




        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': 's3://testing-hwc/fake.docx'}, lookup_index=0)]  
    


```
[/code]


## Configuring the AWS Boto3 client​

You can configure the AWS Boto3 client by passing named arguments when creating the S3DirectoryLoader. This is useful for instance when AWS credentials can't be set as environment variables. See the
list of parameters that can be configured.

[code]
```python




    loader = S3FileLoader(  
        "testing-hwc", "fake.docx", aws_access_key_id="xxxx", aws_secret_access_key="yyyy"  
    )  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


