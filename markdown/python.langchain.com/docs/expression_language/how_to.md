Skip to main content

# How to

## 📄️ Bind runtime args

Sometimes we want to invoke a Runnable within a Runnable sequence with constant arguments that are not part of the output of the preceding Runnable in the sequence, and which are not part of the user
input. We can use Runnable.bind() to easily pass these arguments in.

## 📄️ Configure chain internals at runtime

Oftentimes you may want to experiment with, or even expose to the end user, multiple different ways of doing things.

## 📄️ Add fallbacks

There are many possible points of failure in an LLM application, whether that be issues with LLM API's, poor model outputs, issues with other integrations, etc. Fallbacks help you gracefully handle
and isolate these issues.

## 📄️ Run custom functions

You can use arbitrary functions in the pipeline

## 📄️ Stream custom generator functions

You can use generator functions (ie. functions that use the yield keyword, and behave like iterators) in a LCEL pipeline.

## 📄️ Parallelize steps

RunnableParallel (aka. RunnableMap) makes it easy to execute multiple Runnables in parallel, and to return the output of these Runnables as a map.

## 📄️ Add message history (memory)

The RunnableWithMessageHistory let's us add message history to certain types of chains.

## 📄️ Dynamically route logic based on input

This notebook covers how to do routing in the LangChain Expression Language.
