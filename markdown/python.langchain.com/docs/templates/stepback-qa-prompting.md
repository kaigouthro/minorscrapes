

Skip to main content

On this page

# stepback-qa-prompting

This template replicates the "Step-Back" prompting technique that improves performance on complex questions by first asking a "step back" question.

This technique can be combined with regular question-answering applications by doing retrieval on both the original and step-back question.

Read more about this in the paper here and an excellent blog post by Cobus Greyling here

We will modify the prompts slightly to work better with chat models in this template.

## Environment Setup​

Set the `OPENAI_API_KEY` environment variable to access the OpenAI models.

## Usage​

To use this package, you should first have the LangChain CLI installed:

[code]
```python




    pip install -U langchain-cli  
    


```
[/code]


To create a new LangChain project and install this as the only package, you can do:

[code]
```python




    langchain app new my-app --package stepback-qa-prompting  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add stepback-qa-prompting  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from stepback_qa_prompting.chain import chain as stepback_qa_prompting_chain  
      
    add_routes(app, stepback_qa_prompting_chain, path="/stepback-qa-prompting")  
    


```
[/code]


(Optional) Let's now configure LangSmith. LangSmith will help us trace, monitor and debug LangChain applications. LangSmith is currently in private beta, you can sign up here. If you don't have
access, you can skip this section

[code]
```python




    export LANGCHAIN_TRACING_V2=true  
    export LANGCHAIN_API_KEY=<your-api-key>  
    export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"  
    


```
[/code]


If you are inside this directory, then you can spin up a LangServe instance directly by:

[code]
```python




    langchain serve  
    


```
[/code]


This will start the FastAPI app with a server running locally at http://localhost:8000

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/stepback-qa-prompting/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/stepback-qa-prompting")  
    


```
[/code]


