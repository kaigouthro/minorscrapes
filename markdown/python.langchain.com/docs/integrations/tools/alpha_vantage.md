

Skip to main content

# Alpha Vantage

> Alpha Vantage Alpha Vantage provides realtime and historical financial market data through a set of powerful and developer-friendly data APIs and spreadsheets.

Use the `AlphaVantageAPIWrapper` to get currency exchange rates.

```python




    import getpass
    import os

    os.environ["ALPHAVANTAGE_API_KEY"] = getpass.getpass()



```


```python




         ········



```


```python




    from langchain.utilities.alpha_vantage import AlphaVantageAPIWrapper



```


```python




    alpha_vantage = AlphaVantageAPIWrapper()



```


```python




    alpha_vantage.run("USD", "JPY")



```


```python




        {'1. From_Currency Code': 'USD',
         '2. From_Currency Name': 'United States Dollar',
         '3. To_Currency Code': 'JPY',
         '4. To_Currency Name': 'Japanese Yen',
         '5. Exchange Rate': '144.93000000',
         '6. Last Refreshed': '2023-08-11 21:31:01',
         '7. Time Zone': 'UTC',
         '8. Bid Price': '144.92600000',
         '9. Ask Price': '144.93400000'}



```
