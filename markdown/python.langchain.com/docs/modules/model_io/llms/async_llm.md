

Skip to main content

# Async API

All `LLM`s implement the `Runnable` interface, which comes with default implementations of all methods, ie. ainvoke, batch, abatch, stream, astream. This gives all `LLM`s basic support for
asynchronous calls.

Async support defaults to calling the `LLM`'s respective sync method in asyncio's default thread pool executor. This lets other async functions in your application make progress while the `LLM` is
being executed, by moving this call to a background thread. Where `LLM`s providers have native implementations for async, that is used instead of the default `LLM` implementation.

See which integrations provide native async support here.

[code]
```python




    import asyncio  
    import time  
      
    from langchain.llms import OpenAI  
      
    llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)  
      
      
    def invoke_serially():  
        for _ in range(10):  
            resp = llm.invoke("Hello, how are you?")  
      
      
    async def async_invoke(llm):  
        resp = await llm.ainvoke("Hello, how are you?")  
      
      
    async def invoke_concurrently():  
        tasks = [async_invoke(llm) for _ in range(10)]  
        await asyncio.gather(*tasks)  
      
      
    s = time.perf_counter()  
    # If running this outside of Jupyter, use asyncio.run(generate_concurrently())  
    await invoke_concurrently()  
    elapsed = time.perf_counter() - s  
    print("\033[1m" + f"Concurrent executed in {elapsed:0.2f} seconds." + "\033[0m")  
      
    s = time.perf_counter()  
    invoke_serially()  
    elapsed = time.perf_counter() - s  
    print("\033[1m" + f"Serial executed in {elapsed:0.2f} seconds." + "\033[0m")  
    


```
[/code]


[code]
```python




        Concurrent executed in 1.03 seconds.  
        Serial executed in 6.80 seconds.  
    


```
[/code]


To simplify things we could also just use `abatch` to run a batch concurrently:

[code]
```python




    s = time.perf_counter()  
    # If running this outside of Jupyter, use asyncio.run(generate_concurrently())  
    await llm.abatch(["Hello, how are you?"] * 10)  
    elapsed = time.perf_counter() - s  
    print("\033[1m" + f"Batch executed in {elapsed:0.2f} seconds." + "\033[0m")  
    


```
[/code]


[code]
```python




        Batch executed in 1.31 seconds.  
    


```
[/code]


