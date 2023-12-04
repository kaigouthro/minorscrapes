

Skip to main content

On this page

# Tencent COS Directory

This covers how to load document objects from a `Tencent COS Directory`.

```python




    #! pip install cos-python-sdk-v5



```


```python




    from langchain.document_loaders import TencentCOSDirectoryLoader
    from qcloud_cos import CosConfig



```


```python




    conf = CosConfig(
        Region="your cos region",
        SecretId="your cos secret_id",
        SecretKey="your cos secret_key",
    )
    loader = TencentCOSDirectoryLoader(conf=conf, bucket="you_cos_bucket")



```


```python




    loader.load()



```


## Specifying a prefix​

You can also specify a prefix for more finegrained control over what files to load.

```python




    loader = TencentCOSDirectoryLoader(conf=conf, bucket="you_cos_bucket", prefix="fake")



```


```python




    loader.load()



```
