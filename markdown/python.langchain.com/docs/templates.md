

Skip to main content

On this page

# Templates

Highlighting a few different categories of templates

## ⭐ Popular​

These are some of the more popular templates to get started with.

  * Retrieval Augmented Generation Chatbot: Build a chatbot over your data. Defaults to OpenAI and Pinecone.
  * Extraction with OpenAI Functions: Do extraction of structured data from unstructured data. Uses OpenAI function calling.
  * Local Retrieval Augmented Generation: Build a chatbot over your data. Uses only local tooling: Ollama, GPT4all, Chroma.
  * OpenAI Functions Agent: Build a chatbot that can take actions. Uses OpenAI function calling and Tavily.
  * XML Agent: Build a chatbot that can take actions. Uses Anthropic and You.com.

## 📥 Advanced Retrieval​

These templates cover advanced retrieval techniques, which can be used for chat and QA over databases or documents.

  * Reranking: This retrieval technique uses Cohere's reranking endpoint to rerank documents from an initial retrieval step.
  * Anthropic Iterative Search: This retrieval technique uses iterative prompting to determine what to retrieve and whether the retriever documents are good enough.
  *  **Parent Document Retrieval** using Neo4j or MongoDB: This retrieval technique stores embeddings for smaller chunks, but then returns larger chunks to pass to the model for generation.
  * Semi-Structured RAG: The template shows how to do retrieval over semi-structured data (e.g. data that involves both text and tables).
  * Temporal RAG: The template shows how to do hybrid search over data with a time-based component using Timescale Vector.

## 🔍Advanced Retrieval - Query Transformation​

A selection of advanced retrieval methods that involve transforming the original user query, which can improve retrieval quality.

  * Hypothetical Document Embeddings: A retrieval technique that generates a hypothetical document for a given query, and then uses the embedding of that document to do semantic search. Paper.
  * Rewrite-Retrieve-Read: A retrieval technique that rewrites a given query before passing it to a search engine. Paper.
  * Step-back QA Prompting: A retrieval technique that generates a "step-back" question and then retrieves documents relevant to both that question and the original question. Paper.
  * RAG-Fusion: A retrieval technique that generates multiple queries and then reranks the retrieved documents using reciprocal rank fusion. Article.
  * Multi-Query Retriever: This retrieval technique uses an LLM to generate multiple queries and then fetches documents for all queries.

## 🧠Advanced Retrieval - Query Construction​

A selection of advanced retrieval methods that involve constructing a query in a separate DSL from natural language, which enable natural languge chat over various structured databases.

  * Elastic Query Generator: Generate elastic search queries from natural language.
  * Neo4j Cypher Generation: Generate cypher statements from natural language. Available with a "full text" option as well.
  * Supabase Self Query: Parse a natural language query into a semantic query as well as a metadata filter for Supabase.

## 🦙 OSS Models​

These templates use OSS models, which enable privacy for sensitive data.

  * Local Retrieval Augmented Generation: Build a chatbot over your data. Uses only local tooling: Ollama, GPT4all, Chroma.
  * SQL Question Answering (Replicate): Question answering over a SQL database, using Llama2 hosted on Replicate.
  * SQL Question Answering (LlamaCpp): Question answering over a SQL database, using Llama2 through LlamaCpp.
  * SQL Question Answering (Ollama): Question answering over a SQL database, using Llama2 through Ollama.

## ⛏️ Extraction​

These templates extract data in a structured format based upon a user-specified schema.

  * Extraction Using OpenAI Functions: Extract information from text using OpenAI Function Calling.
  * Extraction Using Anthropic Functions: Extract information from text using a LangChain wrapper around the Anthropic endpoints intended to simulate function calling.
  * Extract BioTech Plate Data: Extract microplate data from messy Excel spreadsheets into a more normalized format.

## ⛏️Summarization and tagging​

These templates summarize or categorize documents and text.

  * Summarization using Anthropic: Uses Anthropic's Claude2 to summarize long documents.

## 🤖 Agents​

These templates build chatbots that can take actions, helping to automate tasks.

  * OpenAI Functions Agent: Build a chatbot that can take actions. Uses OpenAI function calling and Tavily.
  * XML Agent: Build a chatbot that can take actions. Uses Anthropic and You.com.

## 🚨 Safety and evaluation​

These templates enable moderation or evaluation of LLM outputs.

  * Guardrails Output Parser: Use guardrails-ai to validate LLM output.
  * Chatbot Feedback: Use LangSmith to evaluate chatbot responses.

