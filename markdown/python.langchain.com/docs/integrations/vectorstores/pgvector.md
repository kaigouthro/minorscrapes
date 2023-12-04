

Skip to main content

On this page

# PGVector

> PGVector is an open-source vector similarity search for `Postgres`

It supports:

  * exact and approximate nearest neighbor search
  * L2 distance, inner product, and cosine distance

This notebook shows how to use the Postgres vector database (`PGVector`).

See the installation instruction.

[code]
```python




    # Pip install necessary package  
    pip install pgvector  
    pip install openai  
    pip install psycopg2-binary  
    pip install tiktoken  
    


```
[/code]


We want to use `OpenAIEmbeddings` so we have to get the OpenAI API Key.

[code]
```python




    import getpass  
    import os  
      
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")  
    


```
[/code]


[code]
```python




    ## Loading Environment Variables  
    from dotenv import load_dotenv  
      
    load_dotenv()  
    


```
[/code]


[code]
```python




        False  
    


```
[/code]


[code]
```python




    from langchain.docstore.document import Document  
    from langchain.document_loaders import TextLoader  
    from langchain.embeddings.openai import OpenAIEmbeddings  
    from langchain.text_splitter import CharacterTextSplitter  
    from langchain.vectorstores.pgvector import PGVector  
    


```
[/code]


[code]
```python




    loader = TextLoader("../../modules/state_of_the_union.txt")  
    documents = loader.load()  
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)  
    docs = text_splitter.split_documents(documents)  
      
    embeddings = OpenAIEmbeddings()  
    


```
[/code]


[code]
```python




    # PGVector needs the connection string to the database.  
    CONNECTION_STRING = "postgresql+psycopg2://harrisonchase@localhost:5432/test3"  
      
    # # Alternatively, you can create it from environment variables.  
    # import os  
      
    # CONNECTION_STRING = PGVector.connection_string_from_db_params(  
    #     driver=os.environ.get("PGVECTOR_DRIVER", "psycopg2"),  
    #     host=os.environ.get("PGVECTOR_HOST", "localhost"),  
    #     port=int(os.environ.get("PGVECTOR_PORT", "5432")),  
    #     database=os.environ.get("PGVECTOR_DATABASE", "postgres"),  
    #     user=os.environ.get("PGVECTOR_USER", "postgres"),  
    #     password=os.environ.get("PGVECTOR_PASSWORD", "postgres"),  
    # )  
    


```
[/code]


## Similarity Search with Euclidean Distance (Default)​

[code]
```python




    # The PGVector Module will try to create a table with the name of the collection.  
    # So, make sure that the collection name is unique and the user has the permission to create a table.  
      
    COLLECTION_NAME = "state_of_the_union_test"  
      
    db = PGVector.from_documents(  
        embedding=embeddings,  
        documents=docs,  
        collection_name=COLLECTION_NAME,  
        connection_string=CONNECTION_STRING,  
    )  
    


```
[/code]


[code]
```python




    query = "What did the president say about Ketanji Brown Jackson"  
    docs_with_score = db.similarity_search_with_score(query)  
    


```
[/code]


[code]
```python




    for doc, score in docs_with_score:  
        print("-" * 80)  
        print("Score: ", score)  
        print(doc.page_content)  
        print("-" * 80)  
    


```
[/code]


[code]
```python




        --------------------------------------------------------------------------------  
        Score:  0.18456886638850434  
        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   
          
        Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   
          
        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
        --------------------------------------------------------------------------------  
        --------------------------------------------------------------------------------  
        Score:  0.21742627672631343  
        A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans.   
          
        And if we are to advance liberty and justice, we need to secure the Border and fix the immigration system.   
          
        We can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.    
          
        We’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.    
          
        We’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster.   
          
        We’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.  
        --------------------------------------------------------------------------------  
        --------------------------------------------------------------------------------  
        Score:  0.22641793174529334  
        And for our LGBTQ+ Americans, let’s finally get the bipartisan Equality Act to my desk. The onslaught of state laws targeting transgender Americans and their families is wrong.   
          
        As I said last year, especially to our younger transgender Americans, I will always have your back as your President, so you can be yourself and reach your God-given potential.   
          
        While it often appears that we never agree, that isn’t true. I signed 80 bipartisan bills into law last year. From preventing government shutdowns to protecting Asian-Americans from still-too-common hate crimes to reforming military justice.   
          
        And soon, we’ll strengthen the Violence Against Women Act that I first wrote three decades ago. It is important for us to show the nation that we can come together and do big things.   
          
        So tonight I’m offering a Unity Agenda for the Nation. Four big things we can do together.    
          
        First, beat the opioid epidemic.  
        --------------------------------------------------------------------------------  
        --------------------------------------------------------------------------------  
        Score:  0.22670040608054465  
        Tonight, I’m announcing a crackdown on these companies overcharging American businesses and consumers.   
          
        And as Wall Street firms take over more nursing homes, quality in those homes has gone down and costs have gone up.    
          
        That ends on my watch.   
          
        Medicare is going to set higher standards for nursing homes and make sure your loved ones get the care they deserve and expect.   
          
        We’ll also cut costs and keep the economy going strong by giving workers a fair shot, provide more training and apprenticeships, hire them based on their skills not degrees.   
          
        Let’s pass the Paycheck Fairness Act and paid leave.    
          
        Raise the minimum wage to $15 an hour and extend the Child Tax Credit, so no one has to raise a family in poverty.   
          
        Let’s increase Pell Grants and increase our historic support of HBCUs, and invest in what Jill—our First Lady who teaches full-time—calls America’s best-kept secret: community colleges.  
        --------------------------------------------------------------------------------  
    


```
[/code]


## Maximal Marginal Relevance Search (MMR)​

Maximal marginal relevance optimizes for similarity to query AND diversity among selected documents.

[code]
```python




    docs_with_score = db.max_marginal_relevance_search_with_score(query)  
    


```
[/code]


[code]
```python




    for doc, score in docs_with_score:  
        print("-" * 80)  
        print("Score: ", score)  
        print(doc.page_content)  
        print("-" * 80)  
    


```
[/code]


[code]
```python




        --------------------------------------------------------------------------------  
        Score:  0.18453882564037527  
        Tonight. I call on the Senate to: Pass the Freedom to Vote Act. Pass the John Lewis Voting Rights Act. And while you’re at it, pass the Disclose Act so Americans can know who is funding our elections.   
          
        Tonight, I’d like to honor someone who has dedicated his life to serve this country: Justice Stephen Breyer—an Army veteran, Constitutional scholar, and retiring Justice of the United States Supreme Court. Justice Breyer, thank you for your service.   
          
        One of the most serious constitutional responsibilities a President has is nominating someone to serve on the United States Supreme Court.   
          
        And I did that 4 days ago, when I nominated Circuit Court of Appeals Judge Ketanji Brown Jackson. One of our nation’s top legal minds, who will continue Justice Breyer’s legacy of excellence.  
        --------------------------------------------------------------------------------  
        --------------------------------------------------------------------------------  
        Score:  0.23523731441720075  
        We can’t change how divided we’ve been. But we can change how we move forward—on COVID-19 and other issues we must face together.   
          
        I recently visited the New York City Police Department days after the funerals of Officer Wilbert Mora and his partner, Officer Jason Rivera.   
          
        They were responding to a 9-1-1 call when a man shot and killed them with a stolen gun.   
          
        Officer Mora was 27 years old.   
          
        Officer Rivera was 22.   
          
        Both Dominican Americans who’d grown up on the same streets they later chose to patrol as police officers.   
          
        I spoke with their families and told them that we are forever in debt for their sacrifice, and we will carry on their mission to restore the trust and safety every community deserves.   
          
        I’ve worked on these issues a long time.   
          
        I know what works: Investing in crime prevention and community police officers who’ll walk the beat, who’ll know the neighborhood, and who can restore trust and safety.  
        --------------------------------------------------------------------------------  
        --------------------------------------------------------------------------------  
        Score:  0.2448441215698569  
        One was stationed at bases and breathing in toxic smoke from “burn pits” that incinerated wastes of war—medical and hazard material, jet fuel, and more.   
          
        When they came home, many of the world’s fittest and best trained warriors were never the same.   
          
        Headaches. Numbness. Dizziness.   
          
        A cancer that would put them in a flag-draped coffin.   
          
        I know.   
          
        One of those soldiers was my son Major Beau Biden.   
          
        We don’t know for sure if a burn pit was the cause of his brain cancer, or the diseases of so many of our troops.   
          
        But I’m committed to finding out everything we can.   
          
        Committed to military families like Danielle Robinson from Ohio.   
          
        The widow of Sergeant First Class Heath Robinson.    
          
        He was born a soldier. Army National Guard. Combat medic in Kosovo and Iraq.   
          
        Stationed near Baghdad, just yards from burn pits the size of football fields.   
          
        Heath’s widow Danielle is here with us tonight. They loved going to Ohio State football games. He loved building Legos with their daughter.  
        --------------------------------------------------------------------------------  
        --------------------------------------------------------------------------------  
        Score:  0.2513994424701056  
        And I’m taking robust action to make sure the pain of our sanctions  is targeted at Russia’s economy. And I will use every tool at our disposal to protect American businesses and consumers.   
          
        Tonight, I can announce that the United States has worked with 30 other countries to release 60 Million barrels of oil from reserves around the world.    
          
        America will lead that effort, releasing 30 Million barrels from our own Strategic Petroleum Reserve. And we stand ready to do more if necessary, unified with our allies.    
          
        These steps will help blunt gas prices here at home. And I know the news about what’s happening can seem alarming.   
          
        But I want you to know that we are going to be okay.   
          
        When the history of this era is written Putin’s war on Ukraine will have left Russia weaker and the rest of the world stronger.   
          
        While it shouldn’t have taken something so terrible for people around the world to see what’s at stake now everyone sees it clearly.  
        --------------------------------------------------------------------------------  
    


```
[/code]


## Working with vectorstore​

Above, we created a vectorstore from scratch. However, often times we want to work with an existing vectorstore. In order to do that, we can initialize it directly.

[code]
```python




    store = PGVector(  
        collection_name=COLLECTION_NAME,  
        connection_string=CONNECTION_STRING,  
        embedding_function=embeddings,  
    )  
    


```
[/code]


### Add documents​

We can add documents to the existing vectorstore.

[code]
```python




    store.add_documents([Document(page_content="foo")])  
    


```
[/code]


[code]
```python




        ['048c2e14-1cf3-11ee-8777-e65801318980']  
    


```
[/code]


[code]
```python




    docs_with_score = db.similarity_search_with_score("foo")  
    


```
[/code]


[code]
```python




    docs_with_score[0]  
    


```
[/code]


[code]
```python




        (Document(page_content='foo', metadata={}), 3.3203430005457335e-09)  
    


```
[/code]


[code]
```python




    docs_with_score[1]  
    


```
[/code]


[code]
```python




        (Document(page_content='A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans. \n\nAnd if we are to advance liberty and justice, we need to secure the Border and fix the immigration system. \n\nWe can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.  \n\nWe’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.  \n\nWe’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster. \n\nWe’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.', metadata={'source': '../../../state_of_the_union.txt'}),  
         0.2404395365581814)  
    


```
[/code]


### Overriding a vectorstore​

If you have an existing collection, you override it by doing `from_documents` and setting `pre_delete_collection` = True

[code]
```python




    db = PGVector.from_documents(  
        documents=docs,  
        embedding=embeddings,  
        collection_name=COLLECTION_NAME,  
        connection_string=CONNECTION_STRING,  
        pre_delete_collection=True,  
    )  
    


```
[/code]


[code]
```python




    docs_with_score = db.similarity_search_with_score("foo")  
    


```
[/code]


[code]
```python




    docs_with_score[0]  
    


```
[/code]


[code]
```python




        (Document(page_content='A former top litigator in private practice. A former federal public defender. And from a family of public school educators and police officers. A consensus builder. Since she’s been nominated, she’s received a broad range of support—from the Fraternal Order of Police to former judges appointed by Democrats and Republicans. \n\nAnd if we are to advance liberty and justice, we need to secure the Border and fix the immigration system. \n\nWe can do both. At our border, we’ve installed new technology like cutting-edge scanners to better detect drug smuggling.  \n\nWe’ve set up joint patrols with Mexico and Guatemala to catch more human traffickers.  \n\nWe’re putting in place dedicated immigration judges so families fleeing persecution and violence can have their cases heard faster. \n\nWe’re securing commitments and supporting partners in South and Central America to host more refugees and secure their own borders.', metadata={'source': '../../../state_of_the_union.txt'}),  
         0.2404115088144465)  
    


```
[/code]


### Using a VectorStore as a Retriever​

[code]
```python




    retriever = store.as_retriever()  
    


```
[/code]


[code]
```python




    print(retriever)  
    


```
[/code]


[code]
```python




        tags=None metadata=None vectorstore=<langchain.vectorstores.pgvector.PGVector object at 0x29f94f880> search_type='similarity' search_kwargs={}  
    


```
[/code]


