

Skip to main content

On this page

# LLMRails

> LLMRails is a API platform for building GenAI applications. It provides an easy-to-use API for document indexing and querying that is managed by LLMRails and is optimized for performance and
> accuracy. See the LLMRails API documentation  for more information on how to use the API.

This notebook shows how to use functionality related to the `LLMRails`'s integration with langchain. Note that unlike many other integrations in this category, LLMRails provides an end-to-end managed
service for retrieval augmented generation, which includes:

  1. A way to extract text from document files and chunk them into sentences.
  2. Its own embeddings model and vector store - each text segment is encoded into a vector embedding and stored in the LLMRails internal vector store
  3. A query service that automatically encodes the query into embedding, and retrieves the most relevant text segments (including support for Hybrid Search)

All of these are supported in this LangChain integration.

# Setup

You will need a LLMRails account to use LLMRails with LangChain. To get started, use the following steps:

  1. Sign up for a LLMRails account if you don't already have one.
  2. Next you'll need to create API keys to access the API. Click on the **"API Keys"** tab in the corpus view and then the **"Create API Key"** button. Give your key a name. Click "Create key" and you now have an active API key. Keep this key confidential. 

To use LangChain with LLMRails, you'll need to have this value: api_key. You can provide those to LangChain in two ways:

  1. Include in your environment these two variables: `LLM_RAILS_API_KEY`, `LLM_RAILS_DATASTORE_ID`.

> For example, you can set these variables using os.environ and getpass as follows:
[code]
```python




    import os  
    import getpass  
      
    os.environ["LLM_RAILS_API_KEY"] = getpass.getpass("LLMRails API Key:")  
    os.environ["LLM_RAILS_DATASTORE_ID"] = getpass.getpass("LLMRails Datastore Id:")  
    


```
[/code]


  1. Provide them as arguments when creating the LLMRails vectorstore object:

[code]
```python




    vectorstore = LLMRails(  
        api_key=llm_rails_api_key,  
        datastore_id=datastore_id  
    )  
    


```
[/code]


## Adding text​

For adding text to your datastore first you have to go to Datastores page and create one. Click Create Datastore button and choose a name and embedding model for your datastore. Then get your
datastore id from newly created datatore settings.

[code]
```python




    import os  
      
    from langchain.vectorstores import LLMRails  
      
    os.environ["LLM_RAILS_DATASTORE_ID"] = "Your datastore id "  
    os.environ["LLM_RAILS_API_KEY"] = "Your API Key"  
      
    llm_rails = LLMRails.from_texts(["Your text here"])  
    


```
[/code]


## Similarity search​

The simplest scenario for using LLMRails is to perform a similarity search.

[code]
```python




    query = "What do you plan to do about national security?"  
    found_docs = llm_rails.similarity_search(query, k=5)  
    


```
[/code]


[code]
```python




    print(found_docs[0].page_content)  
    


```
[/code]


[code]
```python




        Others may not be democratic but nevertheless depend upon a rules-based international system.  
          
        Yet what we share in common, and the prospect of a freer and more open world, makes such a broad coalition necessary and worthwhile.  
          
        We will listen to and consider ideas that our partners suggest about how to do this.  
          
        Building this inclusive coalition requires reinforcing the multilateral system to uphold the founding principles of the United Nations, including respect for international law.  
          
        141 countries expressed support at the United Nations General Assembly for a resolution condemning Russia’s unprovoked aggression against Ukraine.  
          
        We continue to demonstrate this approach by engaging all regions across all issues, not in terms of what we are against but what we are for.  
          
        This year, we partnered with ASEAN to advance clean energy infrastructure and maritime security in the region.  
          
        We kickstarted the Prosper Africa Build Together Campaign to fuel economic growth across the continent and bolster trade and investment in the clean energy, health, and digital technology sectors.  
          
        We are working to develop a partnership with countries on the Atlantic Ocean to establish and carry out a shared approach to advancing our joint development, economic, environmental, scientific, and maritime governance goals.  
          
        We galvanized regional action to address the core challenges facing the Western Hemisphere by spearheading the Americas Partnership for Economic Prosperity to drive economic recovery and by mobilizing the region behind a bold and unprecedented approach to migration through the Los Angeles Declaration on Migration and Protection.  
          
        In the Middle East, we have worked to enhance deterrence toward Iran, de-escalate regional conflicts, deepen integration among a diverse set of partners in the region, and bolster energy stability.  
          
        A prime example of an inclusive coalition is IPEF, which we launched alongside a dozen regional partners that represent 40 percent of the world’s GDP.  
    


```
[/code]


## Similarity search with score​

Sometimes we might want to perform the search, but also obtain a relevancy score to know how good is a particular result.

[code]
```python




    query = "What is your approach to national defense"  
    found_docs = llm_rails.similarity_search_with_score(  
        query,  
        k=5,  
    )  
    


```
[/code]


[code]
```python




    document, score = found_docs[0]  
    print(document.page_content)  
    print(f"\nScore: {score}")  
    


```
[/code]


[code]
```python




        But we will do so as the last resort and only when the objectives and mission are clear and achievable, consistent with our values and laws, alongside non-military tools, and the mission is undertaken with the informed consent of the American people.  
          
        Our approach to national defense is described in detail in the 2022 National Defense Strategy.  
          
        Our starting premise is that a powerful U.S. military helps advance and safeguard vital U.S. national interests by backstopping diplomacy, confronting aggression, deterring conflict, projecting strength, and protecting the American people and their economic interests.  
          
        Amid intensifying competition, the military’s role is to maintain and gain warfighting advantages while limiting those of our competitors.  
          
        The military will act urgently to sustain and strengthen deterrence, with the PRC as its pacing challenge.  
          
        We will make disciplined choices regarding our national defense and focus our attention on the military’s primary responsibilities: to defend the homeland, and deter attacks and aggression against the United States, our allies and partners, while being prepared to fight and win the Nation’s wars should diplomacy and deterrence fail.  
          
        To do so, we will combine our strengths to achieve maximum effect in deterring acts of aggression—an approach we refer to as integrated deterrence (see text box on page 22).  
          
        We will operate our military using a campaigning mindset—sequencing logically linked military activities to advance strategy-aligned priorities.  
          
        And, we will build a resilient force and defense ecosystem to ensure we can perform these functions for decades to come.  
          
        We ended America’s longest war in Afghanistan, and with it an era of major military operations to remake other societies, even as we have maintained the capacity to address terrorist threats to the American people as they emerge.  
          
        20  NATIONAL SECURITY STRATEGY Page 21   
          
        A combat-credible military is the foundation of deterrence and America’s ability to prevail in conflict.  
          
        Score: 0.5040982687179959  
    


```
[/code]


## LLMRails as a Retriever​

LLMRails, as all the other LangChain vectorstores, is most often used as a LangChain Retriever:

[code]
```python




    retriever = llm_rails.as_retriever()  
    retriever  
    


```
[/code]


[code]
```python




        LLMRailsRetriever(tags=None, metadata=None, vectorstore=<langchain.vectorstores.llm_rails.LLMRails object at 0x107b9c040>, search_type='similarity', search_kwargs={'k': 5})  
    


```
[/code]


[code]
```python




    query = "What is your approach to national defense"  
    retriever.get_relevant_documents(query)[0]  
    


```
[/code]


[code]
```python




        Document(page_content='But we will do so as the last resort and only when the objectives and mission are clear and achievable, consistent with our values and laws, alongside non-military tools, and the mission is undertaken with the informed consent of the American people.\n\nOur approach to national defense is described in detail in the 2022 National Defense Strategy.\n\nOur starting premise is that a powerful U.S. military helps advance and safeguard vital U.S. national interests by backstopping diplomacy, confronting aggression, deterring conflict, projecting strength, and protecting the American people and their economic interests.\n\nAmid intensifying competition, the military’s role is to maintain and gain warfighting advantages while limiting those of our competitors.\n\nThe military will act urgently to sustain and strengthen deterrence, with the PRC as its pacing challenge.\n\nWe will make disciplined choices regarding our national defense and focus our attention on the military’s primary responsibilities: to defend the homeland, and deter attacks and aggression against the United States, our allies and partners, while being prepared to fight and win the Nation’s wars should diplomacy and deterrence fail.\n\nTo do so, we will combine our strengths to achieve maximum effect in deterring acts of aggression—an approach we refer to as integrated deterrence (see text box on page 22).\n\nWe will operate our military using a campaigning mindset—sequencing logically linked military activities to advance strategy-aligned priorities.\n\nAnd, we will build a resilient force and defense ecosystem to ensure we can perform these functions for decades to come.\n\nWe ended America’s longest war in Afghanistan, and with it an era of major military operations to remake other societies, even as we have maintained the capacity to address terrorist threats to the American people as they emerge.\n\n20  NATIONAL SECURITY STRATEGY Page 21 \x90\x90\x90\x90\x90\x90\n\nA combat-credible military is the foundation of deterrence and America’s ability to prevail in conflict.', metadata={'type': 'file', 'url': 'https://cdn.llmrails.com/dst_d94b490c-4638-4247-ad5e-9aa0e7ef53c1/c2d63a2ea3cd406cb522f8312bc1535d', 'name': 'Biden-Harris-Administrations-National-Security-Strategy-10.2022.pdf'})  
    


```
[/code]


