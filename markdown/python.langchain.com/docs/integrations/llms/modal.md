

Skip to main content

# Modal

The Modal cloud platform provides convenient, on-demand access to serverless cloud compute from Python scripts on your local computer. Use `modal` to run your own custom LLM models instead of
depending on LLM APIs.

This example goes over how to use LangChain to interact with a `modal` HTTPS web endpoint.

 _Question-answering with LangChain_ is another example of how to use LangChain alonside `Modal`. In that example, Modal runs the LangChain application end-to-end and uses OpenAI as its LLM API.

```python




    pip install modal



```


```python




    # Register an account with Modal and get a new token.
    modal token new



```


```python




        Launching login page in your browser window...
        If this is not showing up, please copy this URL into your web browser manually:
        https://modal.com/token-flow/tf-Dzm3Y01234mqmm1234Vcu3



```


The `langchain.llms.modal.Modal` integration class requires that you deploy a Modal application with a web endpoint that complies with the following JSON interface:

  1. The LLM prompt is accepted as a `str` value under the key `"prompt"`
  2. The LLM response returned as a `str` value under the key `"prompt"`

 **Example request JSON:**

```python




     {
        "prompt": "Identify yourself, bot!",
        "extra": "args are allowed",
    }



```


 **Example response JSON:**

```python




     {
        "prompt": "This is the LLM speaking",
    }



```


An example 'dummy' Modal web endpoint function fulfilling this interface would be

```python




    ...
    ...

    class Request(BaseModel):
        prompt: str

    @stub.function()
    @modal.web_endpoint(method="POST")
    def web(request: Request):
        _ = request  # ignore input
        return {"prompt": "hello world"}



```


  * See Modal's web endpoints guide for the basics of setting up an endpoint that fulfils this interface.
  * See Modal's 'Run Falcon-40B with AutoGPTQ' open-source LLM example as a starting point for your custom LLM!

Once you have a deployed Modal web endpoint, you can pass its URL into the `langchain.llms.modal.Modal` LLM class. This class can then function as a building block in your chain.

```python




    from langchain.chains import LLMChain
    from langchain.llms import Modal
    from langchain.prompts import PromptTemplate



```


```python




    template = """Question: {question}

    Answer: Let's think step by step."""

    prompt = PromptTemplate(template=template, input_variables=["question"])



```


```python




    endpoint_url = "https://ecorp--custom-llm-endpoint.modal.run"  # REPLACE ME with your deployed Modal web endpoint's URL
    llm = Modal(endpoint_url=endpoint_url)



```


```python




    llm_chain = LLMChain(prompt=prompt, llm=llm)



```


```python




    question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

    llm_chain.run(question)



```
