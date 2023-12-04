

Skip to main content

On this page

# LangSmith Walkthrough

LangChain makes it easy to prototype LLM applications and Agents. However, delivering LLM applications to production can be deceptively difficult. You will likely have to heavily customize and iterate
on your prompts, chains, and other components to create a high-quality product.

To aid in this process, we've launched LangSmith, a unified platform for debugging, testing, and monitoring your LLM applications.

When might this come in handy? You may find it useful when you want to:

  * Quickly debug a new chain, agent, or set of tools
  * Visualize how components (chains, llms, retrievers, etc.) relate and are used
  * Evaluate different prompts and LLMs for a single component
  * Run a given chain several times over a dataset to ensure it consistently meets a quality bar
  * Capture usage traces and using LLMs or analytics pipelines to generate insights

## Prerequisites​

 **Create a LangSmith account and create an API key (see bottom left corner). Familiarize yourself with the platform by looking through the docs**

Note LangSmith is in closed beta; we're in the process of rolling it out to more users. However, you can fill out the form on the website for expedited access.

Now, let's get started!

## Log runs to LangSmith​

First, configure your environment variables to tell LangChain to log traces. This is done by setting the `LANGCHAIN_TRACING_V2` environment variable to true. You can tell LangChain which project to
log to by setting the `LANGCHAIN_PROJECT` environment variable (if this isn't set, runs will be logged to the `default` project). This will automatically create the project for you if it doesn't
exist. You must also set the `LANGCHAIN_ENDPOINT` and `LANGCHAIN_API_KEY` environment variables.

For more information on other ways to set up tracing, please reference the LangSmith documentation.

 **NOTE:** You must also set your `OPENAI_API_KEY` environment variables in order to run the following tutorial.

 **NOTE:** You can only access an API key when you first create it. Keep it somewhere safe.

 **NOTE:** You can also use a context manager in python to log traces using

```python




    from langchain.callbacks.manager import tracing_v2_enabled

    with tracing_v2_enabled(project_name="My Project"):
        agent.run("How many people live in canada as of 2023?")



```


However, in this example, we will use environment variables.

```python




    %pip install openai tiktoken pandas duckduckgo-search --quiet



```


```python




    import os
    from uuid import uuid4

    unique_id = uuid4().hex[0:8]
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = f"Tracing Walkthrough - {unique_id}"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = "<YOUR-API-KEY>"  # Update to your API key

    # Used by the agent in this tutorial
    os.environ["OPENAI_API_KEY"] = "<YOUR-OPENAI-API-KEY>"



```


Create the langsmith client to interact with the API

```python




    from langsmith import Client

    client = Client()



```


Create a LangChain component and log runs to the platform. In this example, we will create a ReAct-style agent with access to a general search tool (DuckDuckGo). The agent's prompt can be viewed in
the Hub here.

```python




    from langchain import hub
    from langchain.agents import AgentExecutor
    from langchain.agents.format_scratchpad import format_to_openai_function_messages
    from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
    from langchain.chat_models import ChatOpenAI
    from langchain.tools import DuckDuckGoSearchResults
    from langchain.tools.render import format_tool_to_openai_function

    # Fetches the latest version of this prompt
    prompt = hub.pull("wfh/langsmith-agent-prompt:latest")

    llm = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0,
    )

    tools = [
        DuckDuckGoSearchResults(
            name="duck_duck_go"
        ),  # General internet search using DuckDuckGo
    ]

    llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

    runnable_agent = (
        {
            "input": lambda x: x["input"],
            "agent_scratchpad": lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = AgentExecutor(
        agent=runnable_agent, tools=tools, handle_parsing_errors=True
    )



```


We are running the agent concurrently on multiple inputs to reduce latency. Runs get logged to LangSmith in the background so execution latency is unaffected.

```python




    inputs = [
        "What is LangChain?",
        "What's LangSmith?",
        "When was Llama-v2 released?",
        "What is the langsmith cookbook?",
        "When did langchain first announce the hub?",
    ]

    results = agent_executor.batch([{"input": x} for x in inputs], return_exceptions=True)



```


```python




    results[:2]



```


```python




        [{'input': 'What is LangChain?',
          'output': 'I\'m sorry, but I couldn\'t find any information about "LangChain". Could you please provide more context or clarify your question?'},
         {'input': "What's LangSmith?",
          'output': 'I\'m sorry, but I couldn\'t find any information about "LangSmith". It could be a specific term or a company that is not widely known. Can you provide more context or clarify what you are referring to?'}]



```


Assuming you've successfully set up your environment, your agent traces should show up in the `Projects` section in the app. Congrats!

It looks like the agent isn't effectively using the tools though. Let's evaluate this so we have a baseline.

## Evaluate Agent​

In addition to logging runs, LangSmith also allows you to test and evaluate your LLM applications.

In this section, you will leverage LangSmith to create a benchmark dataset and run AI-assisted evaluators on an agent. You will do so in a few steps:

  1. Create a dataset
  2. Initialize a new agent to benchmark
  3. Configure evaluators to grade an agent's output
  4. Run the agent over the dataset and evaluate the results

### 1\. Create a LangSmith dataset​

Below, we use the LangSmith client to create a dataset from the input questions from above and a list labels. You will use these later to measure performance for a new agent. A dataset is a collection
of examples, which are nothing more than input-output pairs you can use as test cases to your application.

For more information on datasets, including how to create them from CSVs or other files or how to create them in the platform, please refer to the LangSmith documentation.

```python




    outputs = [
        "LangChain is an open-source framework for building applications using large language models. It is also the name of the company building LangSmith.",
        "LangSmith is a unified platform for debugging, testing, and monitoring language model applications and agents powered by LangChain",
        "July 18, 2023",
        "The langsmith cookbook is a github repository containing detailed examples of how to use LangSmith to debug, evaluate, and monitor large language model-powered applications.",
        "September 5, 2023",
    ]



```


```python




    dataset_name = f"agent-qa-{unique_id}"

    dataset = client.create_dataset(
        dataset_name,
        description="An example dataset of questions over the LangSmith documentation.",
    )

    for query, answer in zip(inputs, outputs):
        client.create_example(
            inputs={"input": query}, outputs={"output": answer}, dataset_id=dataset.id
        )



```


### 2\. Initialize a new agent to benchmark​

LangSmith lets you evaluate any LLM, chain, agent, or even a custom function. Conversational agents are stateful (they have memory); to ensure that this state isn't shared between dataset runs, we
will pass in a `chain_factory` (aka a `constructor`) function to initialize for each call.

In this case, we will test an agent that uses OpenAI's function calling endpoints.

```python




    from langchain import hub
    from langchain.agents import AgentExecutor, AgentType, initialize_agent, load_tools
    from langchain.agents.format_scratchpad import format_to_openai_function_messages
    from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
    from langchain.chat_models import ChatOpenAI
    from langchain.tools.render import format_tool_to_openai_function


    # Since chains can be stateful (e.g. they can have memory), we provide
    # a way to initialize a new chain for each row in the dataset. This is done
    # by passing in a factory function that returns a new chain for each row.
    def agent_factory(prompt):
        llm_with_tools = llm.bind(
            functions=[format_tool_to_openai_function(t) for t in tools]
        )
        runnable_agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_to_openai_function_messages(
                    x["intermediate_steps"]
                ),
            }
            | prompt
            | llm_with_tools
            | OpenAIFunctionsAgentOutputParser()
        )
        return AgentExecutor(agent=runnable_agent, tools=tools, handle_parsing_errors=True)



```


### 3\. Configure evaluation​

Manually comparing the results of chains in the UI is effective, but it can be time consuming. It can be helpful to use automated metrics and AI-assisted feedback to evaluate your component's
performance.

Below, we will create some pre-implemented run evaluators that do the following:

  * Compare results against ground truth labels.
  * Measure semantic (dis)similarity using embedding distance
  * Evaluate 'aspects' of the agent's response in a reference-free manner using custom criteria

For a longer discussion of how to select an appropriate evaluator for your use case and how to create your own custom evaluators, please refer to the LangSmith documentation.

```python




    from langchain.evaluation import EvaluatorType
    from langchain.smith import RunEvalConfig

    evaluation_config = RunEvalConfig(
        # Evaluators can either be an evaluator type (e.g., "qa", "criteria", "embedding_distance", etc.) or a configuration for that evaluator
        evaluators=[
            # Measures whether a QA response is "Correct", based on a reference answer
            # You can also select via the raw string "qa"
            EvaluatorType.QA,
            # Measure the embedding distance between the output and the reference answer
            # Equivalent to: EvalConfig.EmbeddingDistance(embeddings=OpenAIEmbeddings())
            EvaluatorType.EMBEDDING_DISTANCE,
            # Grade whether the output satisfies the stated criteria.
            # You can select a default one such as "helpfulness" or provide your own.
            RunEvalConfig.LabeledCriteria("helpfulness"),
            # The LabeledScoreString evaluator outputs a score on a scale from 1-10.
            # You can use default criteria or write our own rubric
            RunEvalConfig.LabeledScoreString(
                {
                    "accuracy": """
    Score 1: The answer is completely unrelated to the reference.
    Score 3: The answer has minor relevance but does not align with the reference.
    Score 5: The answer has moderate relevance but contains inaccuracies.
    Score 7: The answer aligns with the reference but has minor errors or omissions.
    Score 10: The answer is completely accurate and aligns perfectly with the reference."""
                },
                normalize_by=10,
            ),
        ],
        # You can add custom StringEvaluator or RunEvaluator objects here as well, which will automatically be
        # applied to each prediction. Check out the docs for examples.
        custom_evaluators=[],
    )



```


### 4\. Run the agent and evaluators​

Use the run_on_dataset (or asynchronous arun_on_dataset) function to evaluate your model. This will:

  1. Fetch example rows from the specified dataset.
  2. Run your agent (or any custom function) on each example.
  3. Apply evaluators to the resulting run traces and corresponding reference examples to generate automated feedback.

The results will be visible in the LangSmith app.

```python




    from langchain import hub

    # We will test this version of the prompt
    prompt = hub.pull("wfh/langsmith-agent-prompt:798e7324")



```


```python




    import functools

    from langchain.smith import (
        arun_on_dataset,
        run_on_dataset,
    )

    chain_results = run_on_dataset(
        dataset_name=dataset_name,
        llm_or_chain_factory=functools.partial(agent_factory, prompt=prompt),
        evaluation=evaluation_config,
        verbose=True,
        client=client,
        project_name=f"runnable-agent-test-5d466cbc-{unique_id}",
        tags=[
            "testing-notebook",
            "prompt:5d466cbc",
        ],  # Optional, adds a tag to the resulting chain runs
    )

    # Sometimes, the agent will error due to parsing issues, incompatible tool inputs, etc.
    # These are logged as warnings here and captured as errors in the tracing UI.



```


```python




        View the evaluation results for project 'runnable-agent-test-5d466cbc-bf2162aa' at:
        https://smith.langchain.com/o/ebbaf2eb-769b-4505-aca2-d11de10372a4/projects/p/0c3d22fa-f8b0-4608-b086-2187c18361a5
        [>                                                 ] 0/5

        Chain failed for example 54b4fce8-4492-409d-94af-708f51698b39 with inputs {'input': 'Who trained Llama-v2?'}
        Error Type: TypeError, Message: DuckDuckGoSearchResults._run() got an unexpected keyword argument 'arg1'


        [------------------------------------------------->] 5/5
         Eval quantiles:
                                       0.25       0.5      0.75      mean      mode
        embedding_cosine_distance  0.086614  0.118841  0.183672  0.151444  0.050158
        correctness                0.000000  0.500000  1.000000  0.500000  0.000000
        score_string:accuracy      0.775000  1.000000  1.000000  0.775000  1.000000
        helpfulness                0.750000  1.000000  1.000000  0.750000  1.000000



```


### Review the test results​

You can review the test results tracing UI below by clicking the URL in the output above or navigating to the "Testing & Datasets" page in LangSmith **"agent-qa-{unique_id}"** dataset.

This will show the new runs and the feedback logged from the selected evaluators. You can also explore a summary of the results in tabular format below.

```python




    chain_results.to_dataframe()



```


```python




    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }

        .dataframe tbody tr th {
            vertical-align: top;
        }

        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>embedding_cosine_distance</th>
          <th>correctness</th>
          <th>score_string:accuracy</th>
          <th>helpfulness</th>
          <th>input</th>
          <th>output</th>
          <th>reference</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>42b639a2-17c4-4031-88a9-0ce2c45781ce</th>
          <td>0.317938</td>
          <td>0.0</td>
          <td>1.0</td>
          <td>1.0</td>
          <td>{'input': 'What is the langsmith cookbook?'}</td>
          <td>{'input': 'What is the langsmith cookbook?', '...</td>
          <td>{'output': 'September 5, 2023'}</td>
        </tr>
        <tr>
          <th>54b4fce8-4492-409d-94af-708f51698b39</th>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>{'input': 'Who trained Llama-v2?'}</td>
          <td>{'Error': 'TypeError("DuckDuckGoSearchResults....</td>
          <td>{'output': 'The langsmith cookbook is a github...</td>
        </tr>
        <tr>
          <th>8ae5104e-bbb4-42cc-a84e-f9b8cfc92b8e</th>
          <td>0.138916</td>
          <td>1.0</td>
          <td>1.0</td>
          <td>1.0</td>
          <td>{'input': 'When was Llama-v2 released?'}</td>
          <td>{'input': 'When was Llama-v2 released?', 'outp...</td>
          <td>{'output': 'July 18, 2023'}</td>
        </tr>
        <tr>
          <th>678c0363-3ed1-410a-811f-ebadef2e783a</th>
          <td>0.050158</td>
          <td>1.0</td>
          <td>1.0</td>
          <td>1.0</td>
          <td>{'input': 'What's LangSmith?'}</td>
          <td>{'input': 'What's LangSmith?', 'output': 'Lang...</td>
          <td>{'output': 'LangSmith is a unified platform fo...</td>
        </tr>
        <tr>
          <th>762a616c-7aab-419c-9001-b43ab6200d26</th>
          <td>0.098766</td>
          <td>0.0</td>
          <td>0.1</td>
          <td>0.0</td>
          <td>{'input': 'What is LangChain?'}</td>
          <td>{'input': 'What is LangChain?', 'output': 'Lan...</td>
          <td>{'output': 'LangChain is an open-source framew...</td>
        </tr>
      </tbody>
    </table>
    </div>



```


### (Optional) Compare to another prompt​

Now that we have our test run results, we can make changes to our agent and benchmark them. Let's try this again with a different prompt and see the results.

```python




    candidate_prompt = hub.pull("wfh/langsmith-agent-prompt:39f3bbd0")

    chain_results = run_on_dataset(
        dataset_name=dataset_name,
        llm_or_chain_factory=functools.partial(agent_factory, prompt=candidate_prompt),
        evaluation=evaluation_config,
        verbose=True,
        client=client,
        project_name=f"runnable-agent-test-39f3bbd0-{unique_id}",
        tags=[
            "testing-notebook",
            "prompt:39f3bbd0",
        ],  # Optional, adds a tag to the resulting chain runs
    )



```


```python




        View the evaluation results for project 'runnable-agent-test-39f3bbd0-bf2162aa' at:
        https://smith.langchain.com/o/ebbaf2eb-769b-4505-aca2-d11de10372a4/projects/p/fa721ccc-dd0f-41c9-bf80-22215c44efd4
        [------------------------------------------------->] 5/5
         Eval quantiles:
                                       0.25       0.5      0.75      mean      mode
        embedding_cosine_distance  0.059506  0.155538  0.212864  0.157915  0.043119
        correctness                0.000000  0.000000  1.000000  0.400000  0.000000
        score_string:accuracy      0.700000  1.000000  1.000000  0.880000  1.000000
        helpfulness                1.000000  1.000000  1.000000  0.800000  1.000000



```


## Exporting datasets and runs​

LangSmith lets you export data to common formats such as CSV or JSONL directly in the web app. You can also use the client to fetch runs for further analysis, to store in your own database, or to
share with others. Let's fetch the run traces from the evaluation run.

 **Note: It may be a few moments before all the runs are accessible.**

```python




     runs = client.list_runs(project_name=chain_results["project_name"], execution_order=1)



```


```python




    # After some time, these will be populated.
    client.read_project(project_name=chain_results["project_name"]).feedback_stats



```


## Conclusion​

Congratulations! You have successfully traced and evaluated an agent using LangSmith!

This was a quick guide to get started, but there are many more ways to use LangSmith to speed up your developer flow and produce better results.

For more information on how you can get the most out of LangSmith, check out LangSmith documentation, and please reach out with questions, feature requests, or feedback at support@langchain.dev.
