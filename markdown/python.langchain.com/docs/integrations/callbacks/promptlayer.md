

Skip to main content

On this page

# PromptLayer

PromptLayer is a an LLM observability platform that lets you visualize requests, version prompts, and track usage. In this guide we will go over how to setup the `PromptLayerCallbackHandler`.

While PromptLayer does have LLMs that integrate directly with LangChain (e.g. `PromptLayerOpenAI`), this callback is the recommended way to integrate PromptLayer with LangChain.

See our docs for more information.

## Installation and Setup​

```python




    pip install promptlayer --upgrade



```


### Getting API Credentials​

If you do not have a PromptLayer account, create one on promptlayer.com. Then get an API key by clicking on the settings cog in the navbar and set it as an environment variabled called
`PROMPTLAYER_API_KEY`

### Usage​

Getting started with `PromptLayerCallbackHandler` is fairly simple, it takes two optional arguments:

  1. `pl_tags` \- an optional list of strings that will be tracked as tags on PromptLayer.
  2. `pl_id_callback` \- an optional function that will take `promptlayer_request_id` as an argument. This ID can be used with all of PromptLayer's tracking features to track, metadata, scores, and prompt usage.

### Simple OpenAI Example​

In this simple example we use `PromptLayerCallbackHandler` with `ChatOpenAI`. We add a PromptLayer tag named `chatopenai`

```python




    import promptlayer  # Don't forget this 🍰
    from langchain.callbacks import PromptLayerCallbackHandler
    from langchain.chat_models import ChatOpenAI
    from langchain.schema import (
        HumanMessage,
    )

    chat_llm = ChatOpenAI(
        temperature=0,
        callbacks=[PromptLayerCallbackHandler(pl_tags=["chatopenai"])],
    )
    llm_results = chat_llm(
        [
            HumanMessage(content="What comes after 1,2,3 ?"),
            HumanMessage(content="Tell me another joke?"),
        ]
    )
    print(llm_results)



```


### GPT4All Example​

```python




    import promptlayer  # Don't forget this 🍰
    from langchain.callbacks import PromptLayerCallbackHandler
    from langchain.llms import GPT4All

    model = GPT4All(model="./models/gpt4all-model.bin", n_ctx=512, n_threads=8)

    response = model(
        "Once upon a time, ",
        callbacks=[PromptLayerCallbackHandler(pl_tags=["langchain", "gpt4all"])],
    )



```


### Full Featured Example​

In this example we unlock more of the power of PromptLayer.

PromptLayer allows you to visually create, version, and track prompt templates. Using the Prompt Registry, we can programmatically fetch the prompt template called `example`.

We also define a `pl_id_callback` function which takes in the `promptlayer_request_id` and logs a score, metadata and links the prompt template used. Read more about tracking on our docs.

```python




    import promptlayer  # Don't forget this 🍰
    from langchain.callbacks import PromptLayerCallbackHandler
    from langchain.llms import OpenAI


    def pl_id_callback(promptlayer_request_id):
        print("prompt layer id ", promptlayer_request_id)
        promptlayer.track.score(
            request_id=promptlayer_request_id, score=100
        )  # score is an integer 0-100
        promptlayer.track.metadata(
            request_id=promptlayer_request_id, metadata={"foo": "bar"}
        )  # metadata is a dictionary of key value pairs that is tracked on PromptLayer
        promptlayer.track.prompt(
            request_id=promptlayer_request_id,
            prompt_name="example",
            prompt_input_variables={"product": "toasters"},
            version=1,
        )  # link the request to a prompt template


    openai_llm = OpenAI(
        model_name="text-davinci-002",
        callbacks=[PromptLayerCallbackHandler(pl_id_callback=pl_id_callback)],
    )

    example_prompt = promptlayer.prompts.get("example", version=1, langchain=True)
    openai_llm(example_prompt.format(product="toasters"))



```


That is all it takes! After setup all your requests will show up on the PromptLayer dashboard. This callback also works with any LLM implemented on LangChain.
