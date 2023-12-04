

Skip to main content

On this page

# GPT4All

GitHub:nomic-ai/gpt4all an ecosystem of open-source chatbots trained on a massive collections of clean assistant data including code, stories and dialogue.

This example goes over how to use LangChain to interact with `GPT4All` models.

[code]
```python




    %pip install gpt4all > /dev/null  
    


```
[/code]


[code]
```python




        Note: you may need to restart the kernel to use updated packages.  
    


```
[/code]


### Import GPT4All​

[code]
```python




    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
    from langchain.chains import LLMChain  
    from langchain.llms import GPT4All  
    from langchain.prompts import PromptTemplate  
    


```
[/code]


### Set Up Question to pass to LLM​

[code]
```python




    template = """Question: {question}  
      
    Answer: Let's think step by step."""  
      
    prompt = PromptTemplate(template=template, input_variables=["question"])  
    


```
[/code]


### Specify Model​

To run locally, download a compatible ggml-formatted model.

The gpt4all page has a useful `Model Explorer` section:

  * Select a model of interest
  * Download using the UI and move the `.bin` to the `local_path` (noted below)

For more info, visit https://github.com/nomic-ai/gpt4all.

* * *
[code]
```python




    local_path = (  
        "./models/ggml-gpt4all-l13b-snoozy.bin"  # replace with your desired local file path  
    )  
    


```
[/code]


[code]
```python




    # Callbacks support token-wise streaming  
    callbacks = [StreamingStdOutCallbackHandler()]  
      
    # Verbose is required to pass to the callback manager  
    llm = GPT4All(model=local_path, callbacks=callbacks, verbose=True)  
      
    # If you want to use a custom model add the backend parameter  
    # Check https://docs.gpt4all.io/gpt4all_python.html for supported backends  
    llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)  
    


```
[/code]


[code]
```python




    llm_chain = LLMChain(prompt=prompt, llm=llm)  
    


```
[/code]


[code]
```python




    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"  
      
    llm_chain.run(question)  
    


```
[/code]


Justin Bieber was born on March 1, 1994. In 1994, The Cowboys won Super Bowl XXVIII.

