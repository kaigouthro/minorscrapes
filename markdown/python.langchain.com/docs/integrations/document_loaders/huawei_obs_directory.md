

Skip to main content

On this page

# Huawei OBS Directory

The following code demonstrates how to load objects from the Huawei OBS (Object Storage Service) as documents.

[code]
```python




    # Install the required package  
    # pip install esdk-obs-python  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import OBSDirectoryLoader  
    


```
[/code]


[code]
```python




    endpoint = "your-endpoint"  
    


```
[/code]


[code]
```python




    # Configure your access credentials\n  
    config = {"ak": "your-access-key", "sk": "your-secret-key"}  
    loader = OBSDirectoryLoader("your-bucket-name", endpoint=endpoint, config=config)  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


## Specify a Prefix for Loading​

If you want to load objects with a specific prefix from the bucket, you can use the following code:

[code]
```python




    loader = OBSDirectoryLoader(  
        "your-bucket-name", endpoint=endpoint, config=config, prefix="test_prefix"  
    )  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


## Get Authentication Information from ECS​

If your langchain is deployed on Huawei Cloud ECS and Agency is set up, the loader can directly get the security token from ECS without needing access key and secret key.

[code]
```python




    config = {"get_token_from_ecs": True}  
    loader = OBSDirectoryLoader("your-bucket-name", endpoint=endpoint, config=config)  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


## Use a Public Bucket​

If your bucket's bucket policy allows anonymous access (anonymous users have `listBucket` and `GetObject` permissions), you can directly load the objects without configuring the `config` parameter.

[code]
```python




    loader = OBSDirectoryLoader("your-bucket-name", endpoint=endpoint)  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


