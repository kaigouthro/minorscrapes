

Skip to main content

On this page

# AWS S3 Directory

> Amazon Simple Storage Service (Amazon S3) is an object storage service

> AWS S3 Directory

This covers how to load document objects from an `AWS S3 Directory` object.

```python




    #!pip install boto3



```


```python




    from langchain.document_loaders import S3DirectoryLoader



```


```python




    loader = S3DirectoryLoader("testing-hwc")



```


```python




    loader.load()



```


## Specifying a prefix​

You can also specify a prefix for more finegrained control over what files to load.

```python




    loader = S3DirectoryLoader("testing-hwc", prefix="fake")



```


```python




    loader.load()



```


```python




        [Document(page_content='Lorem ipsum dolor sit amet.', lookup_str='', metadata={'source': 's3://testing-hwc/fake.docx'}, lookup_index=0)]



```


## Configuring the AWS Boto3 client​

You can configure the AWS Boto3 client by passing named arguments when creating the S3DirectoryLoader. This is useful for instance when AWS credentials can't be set as environment variables. See the
list of parameters that can be configured.

```python




    loader = S3DirectoryLoader(
        "testing-hwc", aws_access_key_id="xxxx", aws_secret_access_key="yyyy"
    )



```


```python




    loader.load()



```
