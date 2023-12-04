

Skip to main content

On this page

# SEC filing

> The SEC filing is a financial statement or other formal document submitted to the U.S. Securities and Exchange Commission (SEC). Public companies, certain insiders, and broker-dealers are required
> to make regular SEC filings. Investors and financial professionals rely on these filings for information about companies they are evaluating for investment purposes.
>
> SEC filings data powered by Kay.ai and Cybersyn via Snowflake Marketplace.

## Setup​

First, you will need to install the `kay` package. You will also need an API key: you can get one for free at https://kay.ai. Once you have an API key, you must set it as an environment variable
`KAY_API_KEY`.

In this example, we're going to use the `KayAiRetriever`. Take a look at the kay notebook for more detailed information for the parameters that it accepts.`

[code]
```python




    # Setup API keys for Kay and OpenAI  
    from getpass import getpass  
      
    KAY_API_KEY = getpass()  
    OPENAI_API_KEY = getpass()  
    


```
[/code]


[code]
```python




         ········  
         ········  
    


```
[/code]


[code]
```python




    import os  
      
    os.environ["KAY_API_KEY"] = KAY_API_KEY  
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY  
    


```
[/code]


## Example​

[code]
```python




    from langchain.chains import ConversationalRetrievalChain  
    from langchain.chat_models import ChatOpenAI  
    from langchain.retrievers import KayAiRetriever  
      
    model = ChatOpenAI(model_name="gpt-3.5-turbo")  
    retriever = KayAiRetriever.create(  
        dataset_id="company", data_types=["10-K", "10-Q"], num_contexts=6  
    )  
    qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)  
    


```
[/code]


[code]
```python




    questions = [  
        "What are patterns in Nvidia's spend over the past three quarters?",  
        # "What are some recent challenges faced by the renewable energy sector?",  
    ]  
    chat_history = []  
      
    for question in questions:  
        result = qa({"question": question, "chat_history": chat_history})  
        chat_history.append((question, result["answer"]))  
        print(f"-> **Question**: {question} \n")  
        print(f"**Answer**: {result['answer']} \n")  
    


```
[/code]


[code]
```python




        -> **Question**: What are patterns in Nvidia's spend over the past three quarters?   
          
        **Answer**: Based on the provided information, here are the patterns in NVIDIA's spend over the past three quarters:  
          
        1. Research and Development Expenses:  
           - Q3 2022: Increased by 34% compared to Q3 2021.  
           - Q1 2023: Increased by 40% compared to Q1 2022.  
           - Q2 2022: Increased by 25% compared to Q2 2021.  
             
           Overall, research and development expenses have been consistently increasing over the past three quarters.  
          
        2. Sales, General and Administrative Expenses:  
           - Q3 2022: Increased by 8% compared to Q3 2021.  
           - Q1 2023: Increased by 14% compared to Q1 2022.  
           - Q2 2022: Decreased by 16% compared to Q2 2021.  
             
           The pattern for sales, general and administrative expenses is not as consistent, with some quarters showing an increase and others showing a decrease.  
          
        3. Total Operating Expenses:  
           - Q3 2022: Increased by 25% compared to Q3 2021.  
           - Q1 2023: Increased by 113% compared to Q1 2022.  
           - Q2 2022: Increased by 9% compared to Q2 2021.  
             
           Total operating expenses have generally been increasing over the past three quarters, with a significant increase in Q1 2023.  
          
        Overall, the pattern indicates a consistent increase in research and development expenses and total operating expenses, while sales, general and administrative expenses show some fluctuations.   
          
    


```
[/code]


