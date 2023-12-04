

Skip to main content

# How to

## 📄️ Async API

LangChain provides async support by leveraging the asyncio library.

## 📄️ Different call methods

All classes inherited from Chain offer a few ways of running chain logic. The most direct one is by using call:

## 📄️ Custom chain

To implement your own custom chain you can subclass Chain and implement the following methods:

## 📄️ Adding memory (state)

Chains can be initialized with a Memory object, which will persist data across calls to the chain. This makes a Chain stateful.

## 📄️ Using OpenAI functions

This walkthrough demonstrates how to incorporate OpenAI function-calling API's in a chain. We'll go over:

