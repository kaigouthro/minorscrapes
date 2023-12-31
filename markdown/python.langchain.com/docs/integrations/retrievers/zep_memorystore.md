

Skip to main content

On this page

# Zep

## Retriever Example for Zep​

### Fast, Scalable Building Blocks for LLM Apps​

Zep is an open source platform for productionizing LLM apps. Go from a prototype built in LangChain or LlamaIndex, or a custom app, to production in minutes without rewriting code.

Key Features:

  *  **Fast!** Zep operates independently of the your chat loop, ensuring a snappy user experience.
  *  **Chat History Memory, Archival, and Enrichment** , populate your prompts with relevant chat history, sumamries, named entities, intent data, and more.
  *  **Vector Search over Chat History and Documents** Automatic embedding of documents, chat histories, and summaries. Use Zep's similarity or native MMR Re-ranked search to find the most relevant.
  *  **Manage Users and their Chat Sessions** Users and their Chat Sessions are first-class citizens in Zep, allowing you to manage user interactions with your bots or agents easily.
  *  **Records Retention and Privacy Compliance** Comply with corporate and regulatory mandates for records retention while ensuring compliance with privacy regulations such as CCPA and GDPR. Fulfill _Right To Be Forgotten_ requests with a single API call

Zep project: https://github.com/getzep/zep Docs: https://docs.getzep.com/

## Retriever Example​

This notebook demonstrates how to search historical chat message histories using the Zep Long-term Memory Store.

We'll demonstrate:

  1. Adding conversation history to the Zep memory store.
  2. Vector search over the conversation history: 
    1. With a similarity search over chat messages
    2. Using maximal marginal relevance re-ranking of a chat message search
    3. Filtering a search using metadata filters
    4. A similarity search over summaries of the chat messages
    5. Using maximal marginal relevance re-ranking of a summary search

[code]
```python




    import getpass  
    import time  
    from uuid import uuid4  
      
    from langchain.memory import ZepMemory  
    from langchain.schema import AIMessage, HumanMessage  
      
    # Set this to your Zep server URL  
    ZEP_API_URL = "http://localhost:8000"  
    


```
[/code]


### Initialize the Zep Chat Message History Class and add a chat message history to the memory store​

 **NOTE:** Unlike other Retrievers, the content returned by the Zep Retriever is session/user specific. A `session_id` is required when instantiating the Retriever.

[code]
```python




    # Provide your Zep API key. Note that this is optional. See https://docs.getzep.com/deployment/auth  
    AUTHENTICATE = False  
      
    zep_api_key = None  
    if AUTHENTICATE:  
        zep_api_key = getpass.getpass()  
    


```
[/code]


[code]
```python




    session_id = str(uuid4())  # This is a unique identifier for the user/session  
      
    # Initialize the Zep Memory Class  
    zep_memory = ZepMemory(session_id=session_id, url=ZEP_API_URL, api_key=zep_api_key)  
    


```
[/code]


[code]
```python




    # Preload some messages into the memory. The default message window is 12 messages. We want to push beyond this to demonstrate auto-summarization.  
    test_history = [  
        {"role": "human", "content": "Who was Octavia Butler?"},  
        {  
            "role": "ai",  
            "content": (  
                "Octavia Estelle Butler (June 22, 1947 – February 24, 2006) was an American"  
                " science fiction author."  
            ),  
        },  
        {"role": "human", "content": "Which books of hers were made into movies?"},  
        {  
            "role": "ai",  
            "content": (  
                "The most well-known adaptation of Octavia Butler's work is the FX series"  
                " Kindred, based on her novel of the same name."  
            ),  
        },  
        {"role": "human", "content": "Who were her contemporaries?"},  
        {  
            "role": "ai",  
            "content": (  
                "Octavia Butler's contemporaries included Ursula K. Le Guin, Samuel R."  
                " Delany, and Joanna Russ."  
            ),  
        },  
        {"role": "human", "content": "What awards did she win?"},  
        {  
            "role": "ai",  
            "content": (  
                "Octavia Butler won the Hugo Award, the Nebula Award, and the MacArthur"  
                " Fellowship."  
            ),  
        },  
        {  
            "role": "human",  
            "content": "Which other women sci-fi writers might I want to read?",  
        },  
        {  
            "role": "ai",  
            "content": "You might want to read Ursula K. Le Guin or Joanna Russ.",  
        },  
        {  
            "role": "human",  
            "content": (  
                "Write a short synopsis of Butler's book, Parable of the Sower. What is it"  
                " about?"  
            ),  
        },  
        {  
            "role": "ai",  
            "content": (  
                "Parable of the Sower is a science fiction novel by Octavia Butler,"  
                " published in 1993. It follows the story of Lauren Olamina, a young woman"  
                " living in a dystopian future where society has collapsed due to"  
                " environmental disasters, poverty, and violence."  
            ),  
        },  
        {"role": "human", "content": "What is the setting of the book?"},  
        {  
            "role": "ai",  
            "content": (  
                "The book is set in a dystopian future in the 2020s, where society has"  
                " collapsed due to climate change and economic crises."  
            ),  
        },  
        {"role": "human", "content": "Who is the protagonist?"},  
        {  
            "role": "ai",  
            "content": (  
                "The protagonist of the book is Lauren Olamina, a young woman who possesses"  
                " 'hyperempathy', the ability to feel pain and other sensations she"  
                " witnesses."  
            ),  
        },  
        {"role": "human", "content": "What is the main theme of the book?"},  
        {  
            "role": "ai",  
            "content": (  
                "The main theme of the book is survival in the face of drastic societal"  
                " change and collapse. It also explores themes of adaptability, community,"  
                " and the human capacity for change."  
            ),  
        },  
        {"role": "human", "content": "What is the 'Parable of the Sower'?"},  
        {  
            "role": "ai",  
            "content": (  
                "The 'Parable of the Sower' is a biblical parable that Butler uses as a"  
                " metaphor in the book. In the parable, a sower scatters seeds, some of"  
                " which fall on fertile ground and grow, while others fall on rocky ground"  
                " or among thorns and fail to grow. The parable is used to illustrate the"  
                " importance of receptivity and preparedness in the face of change."  
            ),  
        },  
        {"role": "human", "content": "What is Butler's writing style like?"},  
        {  
            "role": "ai",  
            "content": (  
                "Butler's writing style is known for its clarity, directness, and"  
                " psychological insight. Her narratives often involve complex, diverse"  
                " characters and explore themes of race, gender, and power."  
            ),  
        },  
        {"role": "human", "content": "What other books has she written?"},  
        {  
            "role": "ai",  
            "content": (  
                "In addition to 'Parable of the Sower', Butler has written several other"  
                " notable works, including 'Kindred', 'Dawn', and 'Parable of the Talents'."  
            ),  
        },  
    ]  
      
    for msg in test_history:  
        zep_memory.chat_memory.add_message(  
            HumanMessage(content=msg["content"])  
            if msg["role"] == "human"  
            else AIMessage(content=msg["content"])  
        )  
      
    time.sleep(  
        10  
    )  # Wait for the messages to be embedded and summarized. Speed depends on OpenAI API latency and your rate limits.  
    


```
[/code]


### Use the Zep Retriever to vector search over the Zep memory​

Zep provides native vector search over historical conversation memory. Embedding happens automatically.

NOTE: Embedding of messages occurs asynchronously, so the first query may not return results. Subsequent queries will return results as the embeddings are generated.

[code]
```python




    from langchain.retrievers import ZepRetriever  
    from langchain.retrievers.zep import SearchScope, SearchType  
      
    zep_retriever = ZepRetriever(  
        session_id=session_id,  # Ensure that you provide the session_id when instantiating the Retriever  
        url=ZEP_API_URL,  
        top_k=5,  
        api_key=zep_api_key,  
    )  
      
    await zep_retriever.aget_relevant_documents("Who wrote Parable of the Sower?")  
    


```
[/code]


[code]
```python




        [Document(page_content="What is the 'Parable of the Sower'?", metadata={'score': 0.9250216484069824, 'uuid': '4cbfb1c0-6027-4678-af43-1e18acb224bb', 'created_at': '2023-11-01T00:32:40.224256Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 34, 'Start': 13, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}]}}, 'token_count': 13}),  
         Document(page_content='Parable of the Sower is a science fiction novel by Octavia Butler, published in 1993. It follows the story of Lauren Olamina, a young woman living in a dystopian future where society has collapsed due to environmental disasters, poverty, and violence.', metadata={'score': 0.8897348046302795, 'uuid': '3dd9f5ed-9dc9-4427-9da6-aba1b8278a5c', 'created_at': '2023-11-01T00:32:40.192527Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'GPE', 'Matches': [{'End': 20, 'Start': 15, 'Text': 'Sower'}], 'Name': 'Sower'}, {'Label': 'PERSON', 'Matches': [{'End': 65, 'Start': 51, 'Text': 'Octavia Butler'}], 'Name': 'Octavia Butler'}, {'Label': 'DATE', 'Matches': [{'End': 84, 'Start': 80, 'Text': '1993'}], 'Name': '1993'}, {'Label': 'PERSON', 'Matches': [{'End': 124, 'Start': 110, 'Text': 'Lauren Olamina'}], 'Name': 'Lauren Olamina'}], 'intent': 'Providing information'}}, 'token_count': 56}),  
         Document(page_content="Write a short synopsis of Butler's book, Parable of the Sower. What is it about?", metadata={'score': 0.8856019973754883, 'uuid': '81761dcb-38f3-4686-a4f5-6cb1007eaf29', 'created_at': '2023-11-01T00:32:40.187543Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'entities': [{'Label': 'ORG', 'Matches': [{'End': 32, 'Start': 26, 'Text': 'Butler'}], 'Name': 'Butler'}, {'Label': 'WORK_OF_ART', 'Matches': [{'End': 61, 'Start': 41, 'Text': 'Parable of the Sower'}], 'Name': 'Parable of the Sower'}], 'intent': "The subject is asking for a brief summary of Butler's book, Parable of the Sower, and what it is about."}}, 'token_count': 23}),  
         Document(page_content="The 'Parable of the Sower' is a biblical parable that Butler uses as a metaphor in the book. In the parable, a sower scatters seeds, some of which fall on fertile ground and grow, while others fall on rocky ground or among thorns and fail to grow. The parable is used to illustrate the importance of receptivity and preparedness in the face of change.", metadata={'score': 0.8781436681747437, 'uuid': '1a8c5f99-2fec-425d-bc37-176ab91e7080', 'created_at': '2023-11-01T00:32:40.22836Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 26, 'Start': 5, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}, {'Label': 'ORG', 'Matches': [{'End': 60, 'Start': 54, 'Text': 'Butler'}], 'Name': 'Butler'}]}}, 'token_count': 84}),  
         Document(page_content="In addition to 'Parable of the Sower', Butler has written several other notable works, including 'Kindred', 'Dawn', and 'Parable of the Talents'.", metadata={'score': 0.8745182752609253, 'uuid': '45d8aa08-85ab-432f-8902-81712fe363b9', 'created_at': '2023-11-01T00:32:40.245081Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 37, 'Start': 16, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}, {'Label': 'ORG', 'Matches': [{'End': 45, 'Start': 39, 'Text': 'Butler'}], 'Name': 'Butler'}, {'Label': 'GPE', 'Matches': [{'End': 105, 'Start': 98, 'Text': 'Kindred'}], 'Name': 'Kindred'}, {'Label': 'WORK_OF_ART', 'Matches': [{'End': 144, 'Start': 121, 'Text': "Parable of the Talents'"}], 'Name': "Parable of the Talents'"}]}}, 'token_count': 39})]  
    


```
[/code]


We can also use the Zep sync API to retrieve results:

[code]
```python




    zep_retriever.get_relevant_documents("Who wrote Parable of the Sower?")  
    


```
[/code]


[code]
```python




        [Document(page_content="What is the 'Parable of the Sower'?", metadata={'score': 0.9250596761703491, 'uuid': '4cbfb1c0-6027-4678-af43-1e18acb224bb', 'created_at': '2023-11-01T00:32:40.224256Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 34, 'Start': 13, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}]}}, 'token_count': 13}),  
         Document(page_content='Parable of the Sower is a science fiction novel by Octavia Butler, published in 1993. It follows the story of Lauren Olamina, a young woman living in a dystopian future where society has collapsed due to environmental disasters, poverty, and violence.', metadata={'score': 0.8897120952606201, 'uuid': '3dd9f5ed-9dc9-4427-9da6-aba1b8278a5c', 'created_at': '2023-11-01T00:32:40.192527Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'GPE', 'Matches': [{'End': 20, 'Start': 15, 'Text': 'Sower'}], 'Name': 'Sower'}, {'Label': 'PERSON', 'Matches': [{'End': 65, 'Start': 51, 'Text': 'Octavia Butler'}], 'Name': 'Octavia Butler'}, {'Label': 'DATE', 'Matches': [{'End': 84, 'Start': 80, 'Text': '1993'}], 'Name': '1993'}, {'Label': 'PERSON', 'Matches': [{'End': 124, 'Start': 110, 'Text': 'Lauren Olamina'}], 'Name': 'Lauren Olamina'}], 'intent': 'Providing information'}}, 'token_count': 56}),  
         Document(page_content="Write a short synopsis of Butler's book, Parable of the Sower. What is it about?", metadata={'score': 0.885666012763977, 'uuid': '81761dcb-38f3-4686-a4f5-6cb1007eaf29', 'created_at': '2023-11-01T00:32:40.187543Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'entities': [{'Label': 'ORG', 'Matches': [{'End': 32, 'Start': 26, 'Text': 'Butler'}], 'Name': 'Butler'}, {'Label': 'WORK_OF_ART', 'Matches': [{'End': 61, 'Start': 41, 'Text': 'Parable of the Sower'}], 'Name': 'Parable of the Sower'}], 'intent': "The subject is asking for a brief summary of Butler's book, Parable of the Sower, and what it is about."}}, 'token_count': 23}),  
         Document(page_content="The 'Parable of the Sower' is a biblical parable that Butler uses as a metaphor in the book. In the parable, a sower scatters seeds, some of which fall on fertile ground and grow, while others fall on rocky ground or among thorns and fail to grow. The parable is used to illustrate the importance of receptivity and preparedness in the face of change.", metadata={'score': 0.878172755241394, 'uuid': '1a8c5f99-2fec-425d-bc37-176ab91e7080', 'created_at': '2023-11-01T00:32:40.22836Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 26, 'Start': 5, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}, {'Label': 'ORG', 'Matches': [{'End': 60, 'Start': 54, 'Text': 'Butler'}], 'Name': 'Butler'}]}}, 'token_count': 84}),  
         Document(page_content="In addition to 'Parable of the Sower', Butler has written several other notable works, including 'Kindred', 'Dawn', and 'Parable of the Talents'.", metadata={'score': 0.8745154142379761, 'uuid': '45d8aa08-85ab-432f-8902-81712fe363b9', 'created_at': '2023-11-01T00:32:40.245081Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 37, 'Start': 16, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}, {'Label': 'ORG', 'Matches': [{'End': 45, 'Start': 39, 'Text': 'Butler'}], 'Name': 'Butler'}, {'Label': 'GPE', 'Matches': [{'End': 105, 'Start': 98, 'Text': 'Kindred'}], 'Name': 'Kindred'}, {'Label': 'WORK_OF_ART', 'Matches': [{'End': 144, 'Start': 121, 'Text': "Parable of the Talents'"}], 'Name': "Parable of the Talents'"}]}}, 'token_count': 39})]  
    


```
[/code]


### Reranking using MMR (Maximal Marginal Relevance)​

Zep has native, SIMD-accelerated support for reranking results using MMR. This is useful for removing redundancy in results.

[code]
```python




    zep_retriever = ZepRetriever(  
        session_id=session_id,  # Ensure that you provide the session_id when instantiating the Retriever  
        url=ZEP_API_URL,  
        top_k=5,  
        api_key=zep_api_key,  
        search_type=SearchType.mmr,  
        mmr_lambda=0.5,  
    )  
      
    await zep_retriever.aget_relevant_documents("Who wrote Parable of the Sower?")  
    


```
[/code]


[code]
```python




        [Document(page_content="What is the 'Parable of the Sower'?", metadata={'score': 0.9250596761703491, 'uuid': '4cbfb1c0-6027-4678-af43-1e18acb224bb', 'created_at': '2023-11-01T00:32:40.224256Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 34, 'Start': 13, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}]}}, 'token_count': 13}),  
         Document(page_content='What other books has she written?', metadata={'score': 0.77488774061203, 'uuid': '1b3c5079-9cab-46f3-beae-fb56c572e0fd', 'created_at': '2023-11-01T00:32:40.240135Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'token_count': 9}),  
         Document(page_content="In addition to 'Parable of the Sower', Butler has written several other notable works, including 'Kindred', 'Dawn', and 'Parable of the Talents'.", metadata={'score': 0.8745154142379761, 'uuid': '45d8aa08-85ab-432f-8902-81712fe363b9', 'created_at': '2023-11-01T00:32:40.245081Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 37, 'Start': 16, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}, {'Label': 'ORG', 'Matches': [{'End': 45, 'Start': 39, 'Text': 'Butler'}], 'Name': 'Butler'}, {'Label': 'GPE', 'Matches': [{'End': 105, 'Start': 98, 'Text': 'Kindred'}], 'Name': 'Kindred'}, {'Label': 'WORK_OF_ART', 'Matches': [{'End': 144, 'Start': 121, 'Text': "Parable of the Talents'"}], 'Name': "Parable of the Talents'"}]}}, 'token_count': 39}),  
         Document(page_content='Parable of the Sower is a science fiction novel by Octavia Butler, published in 1993. It follows the story of Lauren Olamina, a young woman living in a dystopian future where society has collapsed due to environmental disasters, poverty, and violence.', metadata={'score': 0.8897120952606201, 'uuid': '3dd9f5ed-9dc9-4427-9da6-aba1b8278a5c', 'created_at': '2023-11-01T00:32:40.192527Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'GPE', 'Matches': [{'End': 20, 'Start': 15, 'Text': 'Sower'}], 'Name': 'Sower'}, {'Label': 'PERSON', 'Matches': [{'End': 65, 'Start': 51, 'Text': 'Octavia Butler'}], 'Name': 'Octavia Butler'}, {'Label': 'DATE', 'Matches': [{'End': 84, 'Start': 80, 'Text': '1993'}], 'Name': '1993'}, {'Label': 'PERSON', 'Matches': [{'End': 124, 'Start': 110, 'Text': 'Lauren Olamina'}], 'Name': 'Lauren Olamina'}], 'intent': 'Providing information'}}, 'token_count': 56}),  
         Document(page_content='Who is the protagonist?', metadata={'score': 0.7858647704124451, 'uuid': 'ee514b37-a0b0-4d24-b0c9-3e9f8ad9d52d', 'created_at': '2023-11-01T00:32:40.203891Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'intent': 'The subject is asking about the identity of the protagonist in a specific context, such as a story, movie, or game.'}}, 'token_count': 7})]  
    


```
[/code]


### Using metadata filters to refine search results​

Zep supports filtering results by metadata. This is useful for filtering results by entity type, or other metadata.

More information here: https://docs.getzep.com/sdk/search_query/

[code]
```python




    filter = {"where": {"jsonpath": '$[*] ? (@.Label == "WORK_OF_ART")'}}  
      
    await zep_retriever.aget_relevant_documents(  
        "Who wrote Parable of the Sower?", metadata=filter  
    )  
    


```
[/code]


[code]
```python




        [Document(page_content="What is the 'Parable of the Sower'?", metadata={'score': 0.9251098036766052, 'uuid': '4cbfb1c0-6027-4678-af43-1e18acb224bb', 'created_at': '2023-11-01T00:32:40.224256Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 34, 'Start': 13, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}]}}, 'token_count': 13}),  
         Document(page_content='What other books has she written?', metadata={'score': 0.7747920155525208, 'uuid': '1b3c5079-9cab-46f3-beae-fb56c572e0fd', 'created_at': '2023-11-01T00:32:40.240135Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'token_count': 9}),  
         Document(page_content="In addition to 'Parable of the Sower', Butler has written several other notable works, including 'Kindred', 'Dawn', and 'Parable of the Talents'.", metadata={'score': 0.8745266795158386, 'uuid': '45d8aa08-85ab-432f-8902-81712fe363b9', 'created_at': '2023-11-01T00:32:40.245081Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'WORK_OF_ART', 'Matches': [{'End': 37, 'Start': 16, 'Text': "Parable of the Sower'"}], 'Name': "Parable of the Sower'"}, {'Label': 'ORG', 'Matches': [{'End': 45, 'Start': 39, 'Text': 'Butler'}], 'Name': 'Butler'}, {'Label': 'GPE', 'Matches': [{'End': 105, 'Start': 98, 'Text': 'Kindred'}], 'Name': 'Kindred'}, {'Label': 'WORK_OF_ART', 'Matches': [{'End': 144, 'Start': 121, 'Text': "Parable of the Talents'"}], 'Name': "Parable of the Talents'"}]}}, 'token_count': 39}),  
         Document(page_content='Parable of the Sower is a science fiction novel by Octavia Butler, published in 1993. It follows the story of Lauren Olamina, a young woman living in a dystopian future where society has collapsed due to environmental disasters, poverty, and violence.', metadata={'score': 0.8897372484207153, 'uuid': '3dd9f5ed-9dc9-4427-9da6-aba1b8278a5c', 'created_at': '2023-11-01T00:32:40.192527Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'ai', 'metadata': {'system': {'entities': [{'Label': 'GPE', 'Matches': [{'End': 20, 'Start': 15, 'Text': 'Sower'}], 'Name': 'Sower'}, {'Label': 'PERSON', 'Matches': [{'End': 65, 'Start': 51, 'Text': 'Octavia Butler'}], 'Name': 'Octavia Butler'}, {'Label': 'DATE', 'Matches': [{'End': 84, 'Start': 80, 'Text': '1993'}], 'Name': '1993'}, {'Label': 'PERSON', 'Matches': [{'End': 124, 'Start': 110, 'Text': 'Lauren Olamina'}], 'Name': 'Lauren Olamina'}], 'intent': 'Providing information'}}, 'token_count': 56}),  
         Document(page_content='Who is the protagonist?', metadata={'score': 0.7858127355575562, 'uuid': 'ee514b37-a0b0-4d24-b0c9-3e9f8ad9d52d', 'created_at': '2023-11-01T00:32:40.203891Z', 'updated_at': '0001-01-01T00:00:00Z', 'role': 'human', 'metadata': {'system': {'intent': 'The subject is asking about the identity of the protagonist in a specific context, such as a story, movie, or game.'}}, 'token_count': 7})]  
    


```
[/code]


### Searching over Summaries with MMR Reranking​

Zep automatically generates summaries of chat messages. These summaries can be searched over using the Zep Retriever. Since a summary is a distillation of a conversation, they're more likely to match
your search query and offer rich, succinct context to the LLM.

Successive summaries may include similar content, with Zep's similarity search returning the highest matching results but with little diversity. MMR re-ranks the results to ensure that the summaries
you populate into your prompt are both relevant and each offers additional information to the LLM.

[code]
```python




    zep_retriever = ZepRetriever(  
        session_id=session_id,  # Ensure that you provide the session_id when instantiating the Retriever  
        url=ZEP_API_URL,  
        top_k=3,  
        api_key=zep_api_key,  
        search_scope=SearchScope.summary,  
        search_type=SearchType.mmr,  
        mmr_lambda=0.5,  
    )  
      
    await zep_retriever.aget_relevant_documents("Who wrote Parable of the Sower?")  
    


```
[/code]


[code]
```python




        [Document(page_content='The human asks about Octavia Butler and the AI informs them that she was an American science fiction author. The human\nasks which of her books were made into movies and the AI mentions the FX series Kindred. The human then asks about her\ncontemporaries and the AI lists Ursula K. Le Guin, Samuel R. Delany, and Joanna Russ. The human also asks about the awards\nshe won and the AI mentions the Hugo Award, the Nebula Award, and the MacArthur Fellowship. The human asks about other women sci-fi writers to read and the AI suggests Ursula K. Le Guin and Joanna Russ. The human then asks for a synopsis of Butler\'s book "Parable of the Sower" and the AI describes it.', metadata={'score': 0.7882999777793884, 'uuid': '3c95a29a-52dc-4112-b8a7-e6b1dc414d45', 'created_at': '2023-11-01T00:32:47.76449Z', 'token_count': 155}),  
         Document(page_content='The human asks about Octavia Butler. The AI informs the human that Octavia Estelle Butler was an American science \nfiction author. The human then asks which books of hers were made into movies and the AI mentions the FX series Kindred, \nbased on her novel of the same name.', metadata={'score': 0.7407922744750977, 'uuid': '0e027f4d-d71f-42ae-977f-696b8948b8bf', 'created_at': '2023-11-01T00:32:41.637098Z', 'token_count': 59}),  
         Document(page_content='The human asks about Octavia Butler and the AI informs them that she was an American science fiction author. The human\nasks which of her books were made into movies and the AI mentions the FX series Kindred. The human then asks about her\ncontemporaries and the AI lists Ursula K. Le Guin, Samuel R. Delany, and Joanna Russ. The human also asks about the awards\nshe won and the AI mentions the Hugo Award, the Nebula Award, and the MacArthur Fellowship.', metadata={'score': 0.7436535358428955, 'uuid': 'b3500d1b-1a78-4aef-9e24-6b196cfa83cb', 'created_at': '2023-11-01T00:32:44.24744Z', 'token_count': 104})]  
    


```
[/code]


