

Skip to main content

On this page

# Eden AI

Eden AI is revolutionizing the AI landscape by uniting the best AI providers, empowering users to unlock limitless possibilities and tap into the true potential of artificial intelligence. With an
all-in-one comprehensive and hassle-free platform, it allows users to deploy AI features to production lightning fast, enabling effortless access to the full breadth of AI capabilities via a single
API. (website: https://edenai.co/)

This example goes over how to use LangChain to interact with Eden AI models

* * *

Accessing the EDENAI's API requires an API key,

which you can get by creating an account https://app.edenai.run/user/register and heading here https://app.edenai.run/admin/account/settings

Once we have a key we'll want to set it as an environment variable by running:

```python




    export EDENAI_API_KEY="..."



```


If you'd prefer not to set an environment variable you can pass the key in directly via the edenai_api_key named parameter

when initiating the EdenAI LLM class:

```python




    from langchain.llms import EdenAI



```


```python




    llm = EdenAI(edenai_api_key="...", provider="openai", temperature=0.2, max_tokens=250)



```


## Calling a model​

The EdenAI API brings together various providers, each offering multiple models.

To access a specific model, you can simply add 'model' during instantiation.

For instance, let's explore the models provided by OpenAI, such as GPT3.5

### text generation​

```python




    from langchain.chains import LLMChain
    from langchain.prompts import PromptTemplate

    llm = EdenAI(
        feature="text",
        provider="openai",
        model="text-davinci-003",
        temperature=0.2,
        max_tokens=250,
    )

    prompt = """
    User: Answer the following yes/no question by reasoning step by step. Can a dog drive a car?
    Assistant:
    """

    llm(prompt)



```


### image generation​

```python




    import base64
    from io import BytesIO

    from PIL import Image


    def print_base64_image(base64_string):
        # Decode the base64 string into binary data
        decoded_data = base64.b64decode(base64_string)

        # Create an in-memory stream to read the binary data
        image_stream = BytesIO(decoded_data)

        # Open the image using PIL
        image = Image.open(image_stream)

        # Display the image
        image.show()



```


```python




    text2image = EdenAI(feature="image", provider="openai", resolution="512x512")



```


```python




    image_output = text2image("A cat riding a motorcycle by Picasso")



```


```python




    print_base64_image(image_output)



```


### text generation with callback​

```python




    from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    from langchain.llms import EdenAI

    llm = EdenAI(
        callbacks=[StreamingStdOutCallbackHandler()],
        feature="text",
        provider="openai",
        temperature=0.2,
        max_tokens=250,
    )
    prompt = """
    User: Answer the following yes/no question by reasoning step by step. Can a dog drive a car?
    Assistant:
    """
    print(llm(prompt))



```


## Chaining Calls​

```python




    from langchain.chains import LLMChain, SimpleSequentialChain
    from langchain.prompts import PromptTemplate



```


```python




    llm = EdenAI(feature="text", provider="openai", temperature=0.2, max_tokens=250)
    text2image = EdenAI(feature="image", provider="openai", resolution="512x512")



```


```python




    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )

    chain = LLMChain(llm=llm, prompt=prompt)



```


```python




    second_prompt = PromptTemplate(
        input_variables=["company_name"],
        template="Write a description of a logo for this company: {company_name}, the logo should not contain text at all ",
    )
    chain_two = LLMChain(llm=llm, prompt=second_prompt)



```


```python




    third_prompt = PromptTemplate(
        input_variables=["company_logo_description"],
        template="{company_logo_description}",
    )
    chain_three = LLMChain(llm=text2image, prompt=third_prompt)



```


```python




    # Run the chain specifying only the input variable for the first chain.
    overall_chain = SimpleSequentialChain(
        chains=[chain, chain_two, chain_three], verbose=True
    )
    output = overall_chain.run("hats")



```


```python




    # print the image
    print_base64_image(output)



```
