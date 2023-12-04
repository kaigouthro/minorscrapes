

Skip to main content

On this page

# DeepSparse

This page covers how to use the DeepSparse inference runtime within LangChain. It is broken into two parts: installation and setup, and then examples of DeepSparse usage.

## Installation and Setup​

  * Install the Python package with `pip install deepsparse`
  * Choose a SparseZoo model or export a support model to ONNX using Optimum

There exists a DeepSparse LLM wrapper, that provides a unified interface for all models:

```python




    from langchain.llms import DeepSparse

    llm = DeepSparse(
        model="zoo:nlg/text_generation/codegen_mono-350m/pytorch/huggingface/bigpython_bigquery_thepile/base-none"
    )

    print(llm("def fib():"))



```


Additional parameters can be passed using the `config` parameter:

```python




    config = {"max_generated_tokens": 256}

    llm = DeepSparse(
        model="zoo:nlg/text_generation/codegen_mono-350m/pytorch/huggingface/bigpython_bigquery_thepile/base-none",
        config=config,
    )



```
