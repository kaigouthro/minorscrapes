

Skip to main content

On this page

# Huawei OBS File

The following code demonstrates how to load an object from the Huawei OBS (Object Storage Service) as document.

[code]
```python




    # Install the required package  
    # pip install esdk-obs-python  
    


```
[/code]


[code]
```python




    from langchain.document_loaders.obs_file import OBSFileLoader  
    


```
[/code]


[code]
```python




    endpoint = "your-endpoint"  
    


```
[/code]


[code]
```python




    from obs import ObsClient  
      
    obs_client = ObsClient(  
        access_key_id="your-access-key",  
        secret_access_key="your-secret-key",  
        server=endpoint,  
    )  
    loader = OBSFileLoader("your-bucket-name", "your-object-key", client=obs_client)  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


## Each Loader with Separate Authentication Information​

If you don't need to reuse OBS connections between different loaders, you can directly configure the `config`. The loader will use the config information to initialize its own OBS client.

[code]
```python




    # Configure your access credentials\n  
    config = {"ak": "your-access-key", "sk": "your-secret-key"}  
    loader = OBSFileLoader(  
        "your-bucket-name", "your-object-key", endpoint=endpoint, config=config  
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
    loader = OBSFileLoader(  
        "your-bucket-name", "your-object-key", endpoint=endpoint, config=config  
    )  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


## Access a Publicly Accessible Object​

If the object you want to access allows anonymous user access (anonymous users have `GetObject` permission), you can directly load the object without configuring the `config` parameter.

[code]
```python




    loader = OBSFileLoader("your-bucket-name", "your-object-key", endpoint=endpoint)  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


