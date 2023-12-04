

Skip to main content

On this page

# URL

This covers how to load HTML documents from a list of URLs into a document format that we can use downstream.

[code]
```python




    from langchain.document_loaders import UnstructuredURLLoader  
    


```
[/code]


[code]
```python




    urls = [  
        "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-february-8-2023",  
        "https://www.understandingwar.org/backgrounder/russian-offensive-campaign-assessment-february-9-2023",  
    ]  
    


```
[/code]


Pass in ssl_verify=False with headers=headers to get past ssl_verification error.

[code]
```python




    loader = UnstructuredURLLoader(urls=urls)  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


# Selenium URL Loader

This covers how to load HTML documents from a list of URLs using the `SeleniumURLLoader`.

Using selenium allows us to load pages that require JavaScript to render.

## Setup​

To use the `SeleniumURLLoader`, you will need to install `selenium` and `unstructured`.

[code]
```python




    from langchain.document_loaders import SeleniumURLLoader  
    


```
[/code]


[code]
```python




    urls = [  
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  
        "https://goo.gl/maps/NDSHwePEyaHMFGwh8",  
    ]  
    


```
[/code]


[code]
```python




    loader = SeleniumURLLoader(urls=urls)  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


# Playwright URL Loader

This covers how to load HTML documents from a list of URLs using the `PlaywrightURLLoader`.

As in the Selenium case, Playwright allows us to load pages that need JavaScript to render.

## Setup​

To use the `PlaywrightURLLoader`, you will need to install `playwright` and `unstructured`. Additionally, you will need to install the Playwright Chromium browser:

[code]
```python




    # Install playwright  
    pip install "playwright"  
    pip install "unstructured"  
    playwright install  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import PlaywrightURLLoader  
    


```
[/code]


[code]
```python




    urls = [  
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  
        "https://goo.gl/maps/NDSHwePEyaHMFGwh8",  
    ]  
    


```
[/code]


[code]
```python




    loader = PlaywrightURLLoader(urls=urls, remove_selectors=["header", "footer"])  
    


```
[/code]


[code]
```python




    data = loader.load()  
    


```
[/code]


