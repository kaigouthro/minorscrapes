

Skip to main content

# Tencent COS File

This covers how to load document object from a `Tencent COS File`.

[code]
```python




    #! pip install cos-python-sdk-v5  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import TencentCOSFileLoader  
    from qcloud_cos import CosConfig  
    


```
[/code]


[code]
```python




    conf = CosConfig(  
        Region="your cos region",  
        SecretId="your cos secret_id",  
        SecretKey="your cos secret_key",  
    )  
    loader = TencentCOSFileLoader(conf=conf, bucket="you_cos_bucket", key="fake.docx")  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


