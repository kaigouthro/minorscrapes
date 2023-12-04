Skip to main content

# Cookbook

Example code for accomplishing common tasks with the LangChain Expression Language (LCEL). These examples show how to compose different Runnable (the core LCEL interface) components to achieve various
tasks. If you're just getting acquainted with LCEL, the Prompt + LLM page is a good place to start.

## 📄️ Prompt + LLM

The most common and valuable composition is taking:

## 📄️ RAG

Let's look at adding in a retrieval step to a prompt and LLM, which adds up to a "retrieval-augmented generation" chain

## 📄️ Multiple chains

Runnables can easily be used to string together multiple Chains

## 📄️ Querying a SQL DB

We can replicate our SQLDatabaseChain with Runnables.

## 📄️ Agents

You can pass a Runnable into an agent.

## 📄️ Code writing

Example of how to use LCEL to write Python code.

## 📄️ Routing by semantic similarity

With LCEL you can easily add custom routing logic to your chain to dynamically determine the chain logic based on user input. All you need to do is define a function that given an input returns a
Runnable.

## 📄️ Adding memory

This shows how to add memory to an arbitrary chain. Right now, you can use the memory classes but need to hook it up manually

## 📄️ Adding moderation

This shows how to add in moderation (or other safeguards) around your LLM application.

## 📄️ Managing prompt size

Agents dynamically call tools. The results of those tool calls are added back to the prompt, so that the agent can plan the next action. Depending on what tools are being used and how they're being
called, the agent prompt can easily grow larger than the model context window.

## 📄️ Using tools

You can use any Tools with Runnables easily.
