

Skip to main content

On this page

# Replicate

> Replicate runs machine learning models in the cloud. We have a library of open-source models that you can run with a few lines of code. If you're building your own machine learning models, Replicate
> makes it easy to deploy them at scale.

This example goes over how to use LangChain to interact with `Replicate` models

## Setup​

[code]
```python




    # magics to auto-reload external modules in case you are making changes to langchain while working on this notebook  
    %autoreload 2  
    


```
[/code]


To run this notebook, you'll need to create a replicate account and install the replicate python client.

[code]
```python




    poetry run pip install replicate  
    


```
[/code]


[code]
```python




        Collecting replicate  
          Using cached replicate-0.9.0-py3-none-any.whl (21 kB)  
        Requirement already satisfied: packaging in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from replicate) (23.1)  
        Requirement already satisfied: pydantic>1 in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from replicate) (1.10.9)  
        Requirement already satisfied: requests>2 in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from replicate) (2.28.2)  
        Requirement already satisfied: typing-extensions>=4.2.0 in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from pydantic>1->replicate) (4.5.0)  
        Requirement already satisfied: charset-normalizer<4,>=2 in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (3.1.0)  
        Requirement already satisfied: idna<4,>=2.5 in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (3.4)  
        Requirement already satisfied: urllib3<1.27,>=1.21.1 in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (1.26.16)  
        Requirement already satisfied: certifi>=2017.4.17 in /root/Source/github/docugami.langchain/libs/langchain/.venv/lib/python3.9/site-packages (from requests>2->replicate) (2023.5.7)  
        Installing collected packages: replicate  
        Successfully installed replicate-0.9.0  
    


```
[/code]


[code]
```python




    # get a token: https://replicate.com/account  
      
    from getpass import getpass  
      
    REPLICATE_API_TOKEN = getpass()  
    


```
[/code]


[code]
```python




    import os  
      
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN  
    


```
[/code]


[code]
```python




    from langchain.chains import LLMChain  
    from langchain.llms import Replicate  
    from langchain.prompts import PromptTemplate  
    


```
[/code]


## Calling a model​

Find a model on the replicate explore page, and then paste in the model name and version in this format: model_name/version.

For example, here is `LLama-V2`.

[code]
```python




    llm = Replicate(  
        model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",  
        model_kwargs={"temperature": 0.75, "max_length": 500, "top_p": 1},  
    )  
    prompt = """  
    User: Answer the following yes/no question by reasoning step by step. Can a dog drive a car?  
    Assistant:  
    """  
    llm(prompt)  
    


```
[/code]


[code]
```python




        '1. Dogs do not have the ability to operate complex machinery like cars.\n2. Dogs do not have human-like intelligence or cognitive abilities to understand the concept of driving.\n3. Dogs do not have the physical ability to use their paws to press pedals or turn a steering wheel.\n4. Therefore, a dog cannot drive a car.'  
    


```
[/code]


As another example, for this dolly model, click on the API tab. The model name/version would be: `replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5`

Only the `model` param is required, but we can add other model params when initializing.

For example, if we were running stable diffusion and wanted to change the image dimensions:

[code]
```python




    Replicate(model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", input={'image_dimensions': '512x512'})  
    


```
[/code]


 _Note that only the first output of a model will be returned._

[code]
```python




     llm = Replicate(  
        model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5"  
    )  
    


```
[/code]


[code]
```python




    prompt = """  
    Answer the following yes/no question by reasoning step by step.   
    Can a dog drive a car?  
    """  
    llm(prompt)  
    


```
[/code]


[code]
```python




        'No, dogs lack some of the brain functions required to operate a motor vehicle. They cannot focus and react in time to accelerate or brake correctly. Additionally, they do not have enough muscle control to properly operate a steering wheel.\n\n'  
    


```
[/code]


We can call any replicate model using this syntax. For example, we can call stable diffusion.

[code]
```python




    text2image = Replicate(  
        model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",  
        model_kwargs={"image_dimensions": "512x512"},  
    )  
    


```
[/code]


[code]
```python




    image_output = text2image("A cat riding a motorcycle by Picasso")  
    image_output  
    


```
[/code]


[code]
```python




        'https://pbxt.replicate.delivery/bqQq4KtzwrrYL9Bub9e7NvMTDeEMm5E9VZueTXkLE7kWumIjA/out-0.png'  
    


```
[/code]


The model spits out a URL. Let's render it.

[code]
```python




    poetry run pip install Pillow  
    


```
[/code]


[code]
```python




        Requirement already satisfied: Pillow in /Users/bagatur/langchain/.venv/lib/python3.9/site-packages (9.5.0)  
          
        [notice] A new release of pip is available: 23.2 -> 23.2.1  
        [notice] To update, run: pip install --upgrade pip  
    


```
[/code]


[code]
```python




    from io import BytesIO  
      
    import requests  
    from PIL import Image  
      
    response = requests.get(image_output)  
    img = Image.open(BytesIO(response.content))  
      
    img  
    


```
[/code]


## Streaming Response​

You can optionally stream the response as it is produced, which is helpful to show interactivity to users for time-consuming generations. See detailed docs on Streaming for more information.

[code]
```python




    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
      
    llm = Replicate(  
        streaming=True,  
        callbacks=[StreamingStdOutCallbackHandler()],  
        model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",  
        model_kwargs={"temperature": 0.75, "max_length": 500, "top_p": 1},  
    )  
    prompt = """  
    User: Answer the following yes/no question by reasoning step by step. Can a dog drive a car?  
    Assistant:  
    """  
    _ = llm(prompt)  
    


```
[/code]


[code]
```python




        1. Dogs do not have the physical ability to operate a vehicle.  
    


```
[/code]


# Stop Sequences

You can also specify stop sequences. If you have a definite stop sequence for the generation that you are going to parse with anyway, it is better (cheaper and faster!) to just cancel the generation
once one or more stop sequences are reached, rather than letting the model ramble on till the specified `max_length`. Stop sequences work regardless of whether you are in streaming mode or not, and
Replicate only charges you for the generation up until the stop sequence.

[code]
```python




    import time  
      
    llm = Replicate(  
        model="a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5",  
        model_kwargs={"temperature": 0.01, "max_length": 500, "top_p": 1},  
    )  
      
    prompt = """  
    User: What is the best way to learn python?  
    Assistant:  
    """  
    start_time = time.perf_counter()  
    raw_output = llm(prompt)  # raw output, no stop  
    end_time = time.perf_counter()  
    print(f"Raw output:\n {raw_output}")  
    print(f"Raw output runtime: {end_time - start_time} seconds")  
      
    start_time = time.perf_counter()  
    stopped_output = llm(prompt, stop=["\n\n"])  # stop on double newlines  
    end_time = time.perf_counter()  
    print(f"Stopped output:\n {stopped_output}")  
    print(f"Stopped output runtime: {end_time - start_time} seconds")  
    


```
[/code]


[code]
```python




        Raw output:  
         There are several ways to learn Python, and the best method for you will depend on your learning style and goals. Here are a few suggestions:  
          
        1. Online tutorials and courses: Websites such as Codecademy, Coursera, and edX offer interactive coding lessons and courses that can help you get started with Python. These courses are often designed for beginners and cover the basics of Python programming.  
        2. Books: There are many books available that can teach you Python, ranging from introductory texts to more advanced manuals. Some popular options include "Python Crash Course" by Eric Matthes, "Automate the Boring Stuff with Python" by Al Sweigart, and "Python for Data Analysis" by Wes McKinney.  
        3. Videos: YouTube and other video platforms have a wealth of tutorials and lectures on Python programming. Many of these videos are created by experienced programmers and can provide detailed explanations and examples of Python concepts.  
        4. Practice: One of the best ways to learn Python is to practice writing code. Start with simple programs and gradually work your way up to more complex projects. As you gain experience, you'll become more comfortable with the language and develop a better understanding of its capabilities.  
        5. Join a community: There are many online communities and forums dedicated to Python programming, such as Reddit's r/learnpython community. These communities can provide support, resources, and feedback as you learn.  
        6. Take online courses: Many universities and organizations offer online courses on Python programming. These courses can provide a structured learning experience and often include exercises and assignments to help you practice your skills.  
        7. Use a Python IDE: An Integrated Development Environment (IDE) is a software application that provides an interface for writing, debugging, and testing code. Popular Python IDEs include PyCharm, Visual Studio Code, and Spyder. These tools can help you write more efficient code and provide features such as code completion, debugging, and project management.  
          
          
        Which of the above options do you think is the best way to learn Python?  
        Raw output runtime: 25.27470933299992 seconds  
        Stopped output:  
         There are several ways to learn Python, and the best method for you will depend on your learning style and goals. Here are some suggestions:  
        Stopped output runtime: 25.77039254200008 seconds  
    


```
[/code]


## Chaining Calls​

The whole point of langchain is to... chain! Here's an example of how do that.

[code]
```python




    from langchain.chains import SimpleSequentialChain  
    


```
[/code]


First, let's define the LLM for this model as a flan-5, and text2image as a stable diffusion model.

[code]
```python




    dolly_llm = Replicate(  
        model="replicate/dolly-v2-12b:ef0e1aefc61f8e096ebe4db6b2bacc297daf2ef6899f0f7e001ec445893500e5"  
    )  
    text2image = Replicate(  
        model="stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf"  
    )  
    


```
[/code]


First prompt in the chain

[code]
```python




    prompt = PromptTemplate(  
        input_variables=["product"],  
        template="What is a good name for a company that makes {product}?",  
    )  
      
    chain = LLMChain(llm=dolly_llm, prompt=prompt)  
    


```
[/code]


Second prompt to get the logo for company description

[code]
```python




    second_prompt = PromptTemplate(  
        input_variables=["company_name"],  
        template="Write a description of a logo for this company: {company_name}",  
    )  
    chain_two = LLMChain(llm=dolly_llm, prompt=second_prompt)  
    


```
[/code]


Third prompt, let's create the image based on the description output from prompt 2

[code]
```python




    third_prompt = PromptTemplate(  
        input_variables=["company_logo_description"],  
        template="{company_logo_description}",  
    )  
    chain_three = LLMChain(llm=text2image, prompt=third_prompt)  
    


```
[/code]


Now let's run it!

[code]
```python




    # Run the chain specifying only the input variable for the first chain.  
    overall_chain = SimpleSequentialChain(  
        chains=[chain, chain_two, chain_three], verbose=True  
    )  
    catchphrase = overall_chain.run("colorful socks")  
    print(catchphrase)  
    


```
[/code]


[code]
```python




          
          
        > Entering new SimpleSequentialChain chain...  
        Colorful socks could be named after a song by The Beatles or a color (yellow, blue, pink). A good combination of letters and digits would be 6399. Apple also owns the domain 6399.com so this could be reserved for the Company.  
          
          
        A colorful sock with the numbers 3, 9, and 99 screen printed in yellow, blue, and pink, respectively.  
          
          
        https://pbxt.replicate.delivery/P8Oy3pZ7DyaAC1nbJTxNw95D1A3gCPfi2arqlPGlfG9WYTkRA/out-0.png  
          
        > Finished chain.  
        https://pbxt.replicate.delivery/P8Oy3pZ7DyaAC1nbJTxNw95D1A3gCPfi2arqlPGlfG9WYTkRA/out-0.png  
    


```
[/code]


[code]
```python




    response = requests.get(  
        "https://replicate.delivery/pbxt/682XgeUlFela7kmZgPOf39dDdGDDkwjsCIJ0aQ0AO5bTbbkiA/out-0.png"  
    )  
    img = Image.open(BytesIO(response.content))  
    img  
    


```
[/code]


