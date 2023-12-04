

Skip to main content

# Async API

LangChain provides async support by leveraging the asyncio library.

info

Async support is built into all `Runnable` objects (the building block of LangChain Expression Language (LCEL) by default. Using LCEL is preferred to using `Chain`s. Head to Interface for more on the
`Runnable` interface.

[code]
```python




    import asyncio  
    import time  
      
    from langchain.chains import LLMChain  
    from langchain.llms import OpenAI  
    from langchain.prompts import PromptTemplate  
      
      
    def generate_serially():  
        llm = OpenAI(temperature=0.9)  
        prompt = PromptTemplate(  
            input_variables=["product"],  
            template="What is a good name for a company that makes {product}?",  
        )  
        chain = LLMChain(llm=llm, prompt=prompt)  
        for _ in range(5):  
            resp = chain.run(product="toothpaste")  
            print(resp)  
      
      
    async def async_generate(chain):  
        resp = await chain.arun(product="toothpaste")  
        print(resp)  
      
      
    async def generate_concurrently():  
        llm = OpenAI(temperature=0.9)  
        prompt = PromptTemplate(  
            input_variables=["product"],  
            template="What is a good name for a company that makes {product}?",  
        )  
        chain = LLMChain(llm=llm, prompt=prompt)  
        tasks = [async_generate(chain) for _ in range(5)]  
        await asyncio.gather(*tasks)  
      
      
    s = time.perf_counter()  
    # If running this outside of Jupyter, use asyncio.run(generate_concurrently())  
    await generate_concurrently()  
    elapsed = time.perf_counter() - s  
    print("\033[1m" + f"Concurrent executed in {elapsed:0.2f} seconds." + "\033[0m")  
      
    s = time.perf_counter()  
    generate_serially()  
    elapsed = time.perf_counter() - s  
    print("\033[1m" + f"Serial executed in {elapsed:0.2f} seconds." + "\033[0m")  
    


```
[/code]


[code]
```python




          
          
        BrightSmile Toothpaste Company  
          
          
        BrightSmile Toothpaste Co.  
          
          
        BrightSmile Toothpaste  
          
          
        Gleaming Smile Inc.  
          
          
        SparkleSmile Toothpaste  
        Concurrent executed in 1.54 seconds.  
          
          
        BrightSmile Toothpaste Co.  
          
          
        MintyFresh Toothpaste Co.  
          
          
        SparkleSmile Toothpaste.  
          
          
        Pearly Whites Toothpaste Co.  
          
          
        BrightSmile Toothpaste.  
        Serial executed in 6.38 seconds.  
    


```
[/code]


