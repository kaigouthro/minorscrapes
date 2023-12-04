

Skip to main content

On this page

# Hugging Face Local Pipelines

Hugging Face models can be run locally through the `HuggingFacePipeline` class.

The Hugging Face Model Hub hosts over 120k models, 20k datasets, and 50k demo apps (Spaces), all open source and publicly available, in an online platform where people can easily collaborate and build
ML together.

These can be called from LangChain either through this local pipeline wrapper or by calling their hosted inference endpoints through the HuggingFaceHub class. For more information on the hosted
pipelines, see the HuggingFaceHub notebook.

To use, you should have the `transformers` python package installed, as well as pytorch. You can also install `xformer` for a more memory-efficient attention implementation.

```python




    %pip install transformers --quiet



```


### Model Loading​

Models can be loaded by specifying the model parameters using the `from_model_id` method.

```python




    from langchain.llms.huggingface_pipeline import HuggingFacePipeline

    hf = HuggingFacePipeline.from_model_id(
        model_id="gpt2",
        task="text-generation",
        pipeline_kwargs={"max_new_tokens": 10},
    )



```


They can also be loaded by passing in an existing `transformers` pipeline directly

```python




    from langchain.llms.huggingface_pipeline import HuggingFacePipeline
    from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

    model_id = "gpt2"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10)
    hf = HuggingFacePipeline(pipeline=pipe)



```


### Create Chain​

With the model loaded into memory, you can compose it with a prompt to form a chain.

```python




    from langchain.prompts import PromptTemplate

    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | hf

    question = "What is electroencephalography?"

    print(chain.invoke({"question": question}))



```


### GPU Inference​

When running on a machine with GPU, you can specify the `device=n` parameter to put the model on the specified device. Defaults to `-1` for CPU inference.

If you have multiple-GPUs and/or the model is too large for a single GPU, you can specify `device_map="auto"`, which requires and uses the Accelerate library to automatically determine how to load the
model weights.

_Note_ : both `device` and `device_map` should not be specified together and can lead to unexpected behavior.

```python




    gpu_llm = HuggingFacePipeline.from_model_id(
        model_id="gpt2",
        task="text-generation",
        device=0,  # replace with device_map="auto" to use the accelerate library.
        pipeline_kwargs={"max_new_tokens": 10},
    )

    gpu_chain = prompt | gpu_llm

    question = "What is electroencephalography?"

    print(gpu_chain.invoke({"question": question}))



```


### Batch GPU Inference​

If running on a device with GPU, you can also run inference on the GPU in batch mode.

```python




    gpu_llm = HuggingFacePipeline.from_model_id(
        model_id="bigscience/bloom-1b7",
        task="text-generation",
        device=0,  # -1 for CPU
        batch_size=2,  # adjust as needed based on GPU map and model size.
        model_kwargs={"temperature": 0, "max_length": 64},
    )

    gpu_chain = prompt | gpu_llm.bind(stop=["\n\n"])

    questions = []
    for i in range(4):
        questions.append({"question": f"What is the number {i} in french?"})

    answers = gpu_chain.batch(questions)
    for answer in answers:
        print(answer)



```
