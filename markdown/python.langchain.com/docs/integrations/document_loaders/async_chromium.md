

Skip to main content

# Async Chromium

Chromium is one of the browsers supported by Playwright, a library used to control browser automation.

By running `p.chromium.launch(headless=True)`, we are launching a headless instance of Chromium.

Headless mode means that the browser is running without a graphical user interface.

`AsyncChromiumLoader` load the page, and then we use `Html2TextTransformer` to trasnform to text.

```python




    pip install -q playwright beautifulsoup4
     playwright install



```


```python




    from langchain.document_loaders import AsyncChromiumLoader

    urls = ["https://www.wsj.com"]
    loader = AsyncChromiumLoader(urls)
    docs = loader.load()
    docs[0].page_content[0:100]



```


```python




        '<!DOCTYPE html><html lang="en"><head><script src="https://s0.2mdn.net/instream/video/client.js" asyn'



```


```python




    from langchain.document_transformers import Html2TextTransformer

    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(docs)
    docs_transformed[0].page_content[0:500]



```


```python




        "Skip to Main ContentSkip to SearchSkip to... Select * Top News * What's News *\nFeatured Stories * Retirement * Life & Arts * Hip-Hop * Sports * Video *\nEconomy * Real Estate * Sports * CMO * CIO * CFO * Risk & Compliance *\nLogistics Report * Sustainable Business * Heard on the Street * Barron’s *\nMarketWatch * Mansion Global * Penta * Opinion * Journal Reports * Sponsored\nOffers Explore Our Brands * WSJ * * * * * Barron's * * * * * MarketWatch * * *\n* * IBD # The Wall Street Journal SubscribeSig"



```
