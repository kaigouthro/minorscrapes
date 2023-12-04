

Skip to main content

On this page

# rag-aws-kendra

This template is an application that utilizes Amazon Kendra, a machine learning powered search service, and Anthropic Claude for text generation. The application retrieves documents using a Retrieval
chain to answer questions from your documents.

It uses the `boto3` library to connect with the Bedrock service.

For more context on building RAG applications with Amazon Kendra, check this page.

## Environment Setup​

Please ensure to setup and configure `boto3` to work with your AWS account.

You can follow the guide here.

You should also have a Kendra Index set up before using this template.

You can use this Cloudformation template to create a sample index.

This includes sample data containing AWS online documentation for Amazon Kendra, Amazon Lex, and Amazon SageMaker. Alternatively, you can use your own Amazon Kendra index if you have indexed your own
dataset.

The following environment variables need to be set:

  * `AWS_DEFAULT_REGION` \- This should reflect the correct AWS region. Default is `us-east-1`.
  * `AWS_PROFILE` \- This should reflect your AWS profile. Default is `default`.
  * `KENDRA_INDEX_ID` \- This should have the Index ID of the Kendra index. Note that the Index ID is a 36 character alphanumeric value that can be found in the index detail page.

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




    langchain app new my-app --package rag-aws-kendra  
    


```
[/code]


If you want to add this to an existing project, you can just run:

[code]
```python




    langchain app add rag-aws-kendra  
    


```
[/code]


And add the following code to your `server.py` file:

[code]
```python




    from rag_aws_kendra.chain import chain as rag_aws_kendra_chain  
      
    add_routes(app, rag_aws_kendra_chain, path="/rag-aws-kendra")  
    


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

We can see all templates at http://127.0.0.1:8000/docs We can access the playground at http://127.0.0.1:8000/rag-aws-kendra/playground

We can access the template from code with:

[code]
```python




    from langserve.client import RemoteRunnable  
      
    runnable = RemoteRunnable("http://localhost:8000/rag-aws-kendra")  
    


```
[/code]


