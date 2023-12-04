

Skip to main content

# BiliBili

> Bilibili is one of the most beloved long-form video sites in China.

This loader utilizes the bilibili-api to fetch the text transcript from `Bilibili`.

With this BiliBiliLoader, users can easily obtain the transcript of their desired video content on the platform.

[code]
```python




    #!pip install bilibili-api-python  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import BiliBiliLoader  
    


```
[/code]


[code]
```python




    loader = BiliBiliLoader(["https://www.bilibili.com/video/BV1xt411o7Xu/"])  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


