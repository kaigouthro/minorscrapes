

Skip to main content

On this page

# SearchApi

This notebook shows examples of how to use SearchApi to search the web. Go to https://www.searchapi.io/ to sign up for a free account and get API key.

```python




    import os

    os.environ["SEARCHAPI_API_KEY"] = ""



```


```python




    from langchain.utilities import SearchApiAPIWrapper



```


```python




    search = SearchApiAPIWrapper()



```


```python




    search.run("Obama's first name?")



```


```python




        'Barack Hussein Obama II'



```


## Using as part of a Self Ask With Search Chain​

```python




    os.environ["OPENAI_API_KEY"] = ""



```


```python




    from langchain.agents import AgentType, Tool, initialize_agent
    from langchain.llms.openai import OpenAI
    from langchain.utilities import SearchApiAPIWrapper

    llm = OpenAI(temperature=0)
    search = SearchApiAPIWrapper()
    tools = [
        Tool(
            name="Intermediate Answer",
            func=search.run,
            description="useful for when you need to ask with search",
        )
    ]

    self_ask_with_search = initialize_agent(
        tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=True
    )
    self_ask_with_search.run("Who lived longer: Plato, Socrates, or Aristotle?")



```


```python






        > Entering new AgentExecutor chain...
         Yes.
        Follow up: How old was Plato when he died?
        Intermediate answer: eighty
        Follow up: How old was Socrates when he died?
        Intermediate answer: | Socrates |
        | -------- |
        | Born | c. 470 BC Deme Alopece, Athens |
        | Died | 399 BC (aged approximately 71) Athens |
        | Cause of death | Execution by forced suicide by poisoning |
        | Spouse(s) | Xanthippe, Myrto |

        Follow up: How old was Aristotle when he died?
        Intermediate answer: 62 years
        So the final answer is: Plato

        > Finished chain.





        'Plato'



```


## Custom parameters​

SearchApi wrapper can be customized to use different engines like Google News, Google Jobs, Google Scholar, or others which can be found in SearchApi documentation. All parameters supported by
SearchApi can be passed when executing the query.

```python




    search = SearchApiAPIWrapper(engine="google_jobs")



```


```python




    search.run("AI Engineer", location="Portugal", gl="pt")[0:500]



```


```python




        'Azure AI Engineer Be an XpanderCandidatar-meCandidatar-meCandidatar-me\n\nShare:\n\nAzure AI Engineer\n\nA área Digital Xperience da Xpand IT é uma equipa tecnológica de rápido crescimento que se concentra em tecnologias Microsoft e Mobile. A sua principal missão é fornecer soluções de software de alta qualidade que atendam às necessidades do utilizador final, num mundo tecnológico continuamente exigente e em ritmo acelerado, proporcionando a melhor experiência em termos de personalização, performance'



```


## Getting results with metadata​

```python




    import pprint



```


```python




    search = SearchApiAPIWrapper(engine="google_scholar")
    results = search.results("Large Language Models")
    pprint.pp(results)



```


```python




        {'search_metadata': {'id': 'search_qVdXG2jzvrlqTzayeYoaOb8A',
                             'status': 'Success',
                             'created_at': '2023-09-25T15:22:30Z',
                             'request_time_taken': 3.21,
                             'parsing_time_taken': 0.03,
                             'total_time_taken': 3.24,
                             'request_url': 'https://scholar.google.com/scholar?q=Large+Language+Models&hl=en',
                             'html_url': 'https://www.searchapi.io/api/v1/searches/search_qVdXG2jzvrlqTzayeYoaOb8A.html',
                             'json_url': 'https://www.searchapi.io/api/v1/searches/search_qVdXG2jzvrlqTzayeYoaOb8A'},
         'search_parameters': {'engine': 'google_scholar',
                               'q': 'Large Language Models',
                               'hl': 'en'},
         'search_information': {'query_displayed': 'Large Language Models',
                                'total_results': 6420000,
                                'page': 1,
                                'time_taken_displayed': 0.06},
         'organic_results': [{'position': 1,
                              'title': 'ChatGPT for good? On opportunities and '
                                       'challenges of large language models for '
                                       'education',
                              'data_cid': 'uthwmf2nU3EJ',
                              'link': 'https://www.sciencedirect.com/science/article/pii/S1041608023000195',
                              'publication': 'E Kasneci, K Seßler, S Küchemann, M '
                                             'Bannert… - Learning and individual …, '
                                             '2023 - Elsevier',
                              'snippet': '… state of large language models and their '
                                         'applications. We then highlight how these '
                                         'models can be … With regard to challenges, '
                                         'we argue that large language models in '
                                         'education require …',
                              'inline_links': {'cited_by': {'cites_id': '8166055256995715258',
                                                            'total': 410,
                                                            'link': 'https://scholar.google.com/scholar?cites=8166055256995715258&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '8166055256995715258',
                                                            'total': 10,
                                                            'link': 'https://scholar.google.com/scholar?cluster=8166055256995715258&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:uthwmf2nU3EJ:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'edarxiv.org',
                                           'format': 'PDF',
                                           'link': 'https://edarxiv.org/5er8f/download?format=pdf'},
                              'authors': [{'name': 'E Kasneci',
                                           'id': 'bZVkVvoAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=bZVkVvoAAAAJ&hl=en&oi=sra'},
                                          {'name': 'K Seßler',
                                           'id': 'MbMBoN4AAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=MbMBoN4AAAAJ&hl=en&oi=sra'},
                                          {'name': 'S Küchemann',
                                           'id': 'g1jX5QUAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=g1jX5QUAAAAJ&hl=en&oi=sra'},
                                          {'name': 'M Bannert',
                                           'id': 'TjfQ8QkAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=TjfQ8QkAAAAJ&hl=en&oi=sra'}]},
                             {'position': 2,
                              'title': 'Large language models in medicine',
                              'data_cid': 'Ph9AwHTmhzAJ',
                              'link': 'https://www.nature.com/articles/s41591-023-02448-8',
                              'publication': 'AJ Thirunavukarasu, DSJ Ting, K '
                                             'Elangovan… - Nature medicine, 2023 - '
                                             'nature.com',
                              'snippet': '… HuggingChat offers a free-to-access '
                                         'chatbot with a similar interface to ChatGPT '
                                         'but uses Large Language Model Meta AI '
                                         '(LLaMA) as its backend model 30 . Finally, '
                                         'cheap imitations of …',
                              'inline_links': {'cited_by': {'cites_id': '3497017024792502078',
                                                            'total': 25,
                                                            'link': 'https://scholar.google.com/scholar?cites=3497017024792502078&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '3497017024792502078',
                                                            'total': 3,
                                                            'link': 'https://scholar.google.com/scholar?cluster=3497017024792502078&hl=en&as_sdt=0,33'}},
                              'authors': [{'name': 'AJ Thirunavukarasu',
                                           'id': '3qb1AYwAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=3qb1AYwAAAAJ&hl=en&oi=sra'},
                                          {'name': 'DSJ Ting',
                                           'id': 'KbrpC8cAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=KbrpC8cAAAAJ&hl=en&oi=sra'},
                                          {'name': 'K Elangovan',
                                           'id': 'BE_lVTQAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=BE_lVTQAAAAJ&hl=en&oi=sra'}]},
                             {'position': 3,
                              'title': 'Extracting training data from large language '
                                       'models',
                              'data_cid': 'mEYsWK6bWKoJ',
                              'link': 'https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting',
                              'publication': 'N Carlini, F Tramer, E Wallace, M '
                                             'Jagielski… - 30th USENIX Security …, '
                                             '2021 - usenix.org',
                              'snippet': '… language model trained on scrapes of the '
                                         'public Internet, and are able to extract '
                                         'hundreds of verbatim text sequences from the '
                                         'model’… models are more vulnerable than '
                                         'smaller models. …',
                              'inline_links': {'cited_by': {'cites_id': '12274731957504198296',
                                                            'total': 742,
                                                            'link': 'https://scholar.google.com/scholar?cites=12274731957504198296&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '12274731957504198296',
                                                            'total': 8,
                                                            'link': 'https://scholar.google.com/scholar?cluster=12274731957504198296&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:mEYsWK6bWKoJ:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33',
                                               'cached_page_link': 'https://scholar.googleusercontent.com/scholar?q=cache:mEYsWK6bWKoJ:scholar.google.com/+Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'usenix.org',
                                           'format': 'PDF',
                                           'link': 'https://www.usenix.org/system/files/sec21-carlini-extracting.pdf'},
                              'authors': [{'name': 'N Carlini',
                                           'id': 'q4qDvAoAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=q4qDvAoAAAAJ&hl=en&oi=sra'},
                                          {'name': 'F Tramer',
                                           'id': 'ijH0-a8AAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=ijH0-a8AAAAJ&hl=en&oi=sra'},
                                          {'name': 'E Wallace',
                                           'id': 'SgST3LkAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=SgST3LkAAAAJ&hl=en&oi=sra'},
                                          {'name': 'M Jagielski',
                                           'id': '_8rw_GMAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=_8rw_GMAAAAJ&hl=en&oi=sra'}]},
                             {'position': 4,
                              'title': 'Emergent abilities of large language models',
                              'data_cid': 'hG0iVOrOguoJ',
                              'link': 'https://arxiv.org/abs/2206.07682',
                              'publication': 'J Wei, Y Tay, R Bommasani, C Raffel, B '
                                             'Zoph… - arXiv preprint arXiv …, 2022 - '
                                             'arxiv.org',
                              'snippet': 'Scaling up language models has been shown to '
                                         'predictably improve performance and sample '
                                         'efficiency on a wide range of downstream '
                                         'tasks. This paper instead discusses an …',
                              'inline_links': {'cited_by': {'cites_id': '16898296257676733828',
                                                            'total': 621,
                                                            'link': 'https://scholar.google.com/scholar?cites=16898296257676733828&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '16898296257676733828',
                                                            'total': 12,
                                                            'link': 'https://scholar.google.com/scholar?cluster=16898296257676733828&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:hG0iVOrOguoJ:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33',
                                               'cached_page_link': 'https://scholar.googleusercontent.com/scholar?q=cache:hG0iVOrOguoJ:scholar.google.com/+Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'arxiv.org',
                                           'format': 'PDF',
                                           'link': 'https://arxiv.org/pdf/2206.07682.pdf?trk=cndc-detail'},
                              'authors': [{'name': 'J Wei',
                                           'id': 'wA5TK_0AAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=wA5TK_0AAAAJ&hl=en&oi=sra'},
                                          {'name': 'Y Tay',
                                           'id': 'VBclY_cAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=VBclY_cAAAAJ&hl=en&oi=sra'},
                                          {'name': 'R Bommasani',
                                           'id': 'WMBXw1EAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=WMBXw1EAAAAJ&hl=en&oi=sra'},
                                          {'name': 'C Raffel',
                                           'id': 'I66ZBYwAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=I66ZBYwAAAAJ&hl=en&oi=sra'},
                                          {'name': 'B Zoph',
                                           'id': 'NL_7iTwAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=NL_7iTwAAAAJ&hl=en&oi=sra'}]},
                             {'position': 5,
                              'title': 'A survey on evaluation of large language '
                                       'models',
                              'data_cid': 'ZYohnzOz-XgJ',
                              'link': 'https://arxiv.org/abs/2307.03109',
                              'publication': 'Y Chang, X Wang, J Wang, Y Wu, K Zhu… - '
                                             'arXiv preprint arXiv …, 2023 - arxiv.org',
                              'snippet': '… 3.1 Natural Language Processing Tasks … '
                                         'the development of language models, '
                                         'particularly large language models, was to '
                                         'enhance performance on natural language '
                                         'processing tasks, …',
                              'inline_links': {'cited_by': {'cites_id': '8717195588046785125',
                                                            'total': 31,
                                                            'link': 'https://scholar.google.com/scholar?cites=8717195588046785125&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '8717195588046785125',
                                                            'total': 3,
                                                            'link': 'https://scholar.google.com/scholar?cluster=8717195588046785125&hl=en&as_sdt=0,33'},
                                               'cached_page_link': 'https://scholar.googleusercontent.com/scholar?q=cache:ZYohnzOz-XgJ:scholar.google.com/+Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'arxiv.org',
                                           'format': 'PDF',
                                           'link': 'https://arxiv.org/pdf/2307.03109'},
                              'authors': [{'name': 'X Wang',
                                           'id': 'Q7Ieos8AAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=Q7Ieos8AAAAJ&hl=en&oi=sra'},
                                          {'name': 'J Wang',
                                           'id': 'YomxTXQAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=YomxTXQAAAAJ&hl=en&oi=sra'},
                                          {'name': 'Y Wu',
                                           'id': 'KVeRu2QAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=KVeRu2QAAAAJ&hl=en&oi=sra'},
                                          {'name': 'K Zhu',
                                           'id': 'g75dFLYAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=g75dFLYAAAAJ&hl=en&oi=sra'}]},
                             {'position': 6,
                              'title': 'Evaluating large language models trained on '
                                       'code',
                              'data_cid': '3tNvW3l5nU4J',
                              'link': 'https://arxiv.org/abs/2107.03374',
                              'publication': 'M Chen, J Tworek, H Jun, Q Yuan, HPO '
                                             'Pinto… - arXiv preprint arXiv …, 2021 - '
                                             'arxiv.org',
                              'snippet': '… We introduce Codex, a GPT language model '
                                         'finetuned on publicly available code from '
                                         'GitHub, and study its Python code-writing '
                                         'capabilities. A distinct production version '
                                         'of Codex …',
                              'inline_links': {'cited_by': {'cites_id': '5664817468434011102',
                                                            'total': 941,
                                                            'link': 'https://scholar.google.com/scholar?cites=5664817468434011102&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '5664817468434011102',
                                                            'total': 2,
                                                            'link': 'https://scholar.google.com/scholar?cluster=5664817468434011102&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:3tNvW3l5nU4J:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33',
                                               'cached_page_link': 'https://scholar.googleusercontent.com/scholar?q=cache:3tNvW3l5nU4J:scholar.google.com/+Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'arxiv.org',
                                           'format': 'PDF',
                                           'link': 'https://arxiv.org/pdf/2107.03374.pdf?trk=public_post_comment-text'},
                              'authors': [{'name': 'M Chen',
                                           'id': '5fU-QMwAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=5fU-QMwAAAAJ&hl=en&oi=sra'},
                                          {'name': 'J Tworek',
                                           'id': 'ZPuESCQAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=ZPuESCQAAAAJ&hl=en&oi=sra'},
                                          {'name': 'Q Yuan',
                                           'id': 'B059m2EAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=B059m2EAAAAJ&hl=en&oi=sra'}]},
                             {'position': 7,
                              'title': 'Large language models in machine translation',
                              'data_cid': 'sY5m_Y3-0Y4J',
                              'link': 'http://research.google/pubs/pub33278.pdf',
                              'publication': 'T Brants, AC Popat, P Xu, FJ Och, J Dean '
                                             '- 2007 - research.google',
                              'snippet': '… the benefits of largescale statistical '
                                         'language modeling in ma… trillion tokens, '
                                         'resulting in language models having up to '
                                         '300 … is inexpensive to train on large data '
                                         'sets and approaches the …',
                              'type': 'PDF',
                              'inline_links': {'cited_by': {'cites_id': '10291286509313494705',
                                                            'total': 737,
                                                            'link': 'https://scholar.google.com/scholar?cites=10291286509313494705&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '10291286509313494705',
                                                            'total': 31,
                                                            'link': 'https://scholar.google.com/scholar?cluster=10291286509313494705&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:sY5m_Y3-0Y4J:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33',
                                               'cached_page_link': 'https://scholar.googleusercontent.com/scholar?q=cache:sY5m_Y3-0Y4J:scholar.google.com/+Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'research.google',
                                           'format': 'PDF',
                                           'link': 'http://research.google/pubs/pub33278.pdf'},
                              'authors': [{'name': 'FJ Och',
                                           'id': 'ITGdg6oAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=ITGdg6oAAAAJ&hl=en&oi=sra'},
                                          {'name': 'J Dean',
                                           'id': 'NMS69lQAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=NMS69lQAAAAJ&hl=en&oi=sra'}]},
                             {'position': 8,
                              'title': 'A watermark for large language models',
                              'data_cid': 'BlSyLHT4iiEJ',
                              'link': 'https://arxiv.org/abs/2301.10226',
                              'publication': 'J Kirchenbauer, J Geiping, Y Wen, J '
                                             'Katz… - arXiv preprint arXiv …, 2023 - '
                                             'arxiv.org',
                              'snippet': '… To derive this watermark, we examine what '
                                         'happens in the language model just before it '
                                         'produces a probability vector. The last '
                                         'layer of the language model outputs a vector '
                                         'of logits l(t). …',
                              'inline_links': {'cited_by': {'cites_id': '2417017327887471622',
                                                            'total': 104,
                                                            'link': 'https://scholar.google.com/scholar?cites=2417017327887471622&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '2417017327887471622',
                                                            'total': 4,
                                                            'link': 'https://scholar.google.com/scholar?cluster=2417017327887471622&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:BlSyLHT4iiEJ:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33',
                                               'cached_page_link': 'https://scholar.googleusercontent.com/scholar?q=cache:BlSyLHT4iiEJ:scholar.google.com/+Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'arxiv.org',
                                           'format': 'PDF',
                                           'link': 'https://arxiv.org/pdf/2301.10226.pdf?curius=1419'},
                              'authors': [{'name': 'J Kirchenbauer',
                                           'id': '48GJrbsAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=48GJrbsAAAAJ&hl=en&oi=sra'},
                                          {'name': 'J Geiping',
                                           'id': '206vNCEAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=206vNCEAAAAJ&hl=en&oi=sra'},
                                          {'name': 'Y Wen',
                                           'id': 'oUYfjg0AAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=oUYfjg0AAAAJ&hl=en&oi=sra'},
                                          {'name': 'J Katz',
                                           'id': 'yPw4WjoAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=yPw4WjoAAAAJ&hl=en&oi=sra'}]},
                             {'position': 9,
                              'title': 'ChatGPT and other large language models are '
                                       'double-edged swords',
                              'data_cid': 'So0q8TRvxhYJ',
                              'link': 'https://pubs.rsna.org/doi/full/10.1148/radiol.230163',
                              'publication': 'Y Shen, L Heacock, J Elias, KD Hentel, B '
                                             'Reig, G Shih… - Radiology, 2023 - '
                                             'pubs.rsna.org',
                              'snippet': '… Large Language Models (LLMs) are deep '
                                         'learning models trained to understand and '
                                         'generate natural language. Recent studies '
                                         'demonstrated that LLMs achieve great success '
                                         'in a …',
                              'inline_links': {'cited_by': {'cites_id': '1641121387398204746',
                                                            'total': 231,
                                                            'link': 'https://scholar.google.com/scholar?cites=1641121387398204746&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '1641121387398204746',
                                                            'total': 3,
                                                            'link': 'https://scholar.google.com/scholar?cluster=1641121387398204746&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:So0q8TRvxhYJ:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33'},
                              'authors': [{'name': 'Y Shen',
                                           'id': 'XaeN2zgAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=XaeN2zgAAAAJ&hl=en&oi=sra'},
                                          {'name': 'L Heacock',
                                           'id': 'tYYM5IkAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=tYYM5IkAAAAJ&hl=en&oi=sra'}]},
                             {'position': 10,
                              'title': 'Pythia: A suite for analyzing large language '
                                       'models across training and scaling',
                              'data_cid': 'aaIDvsMAD8QJ',
                              'link': 'https://proceedings.mlr.press/v202/biderman23a.html',
                              'publication': 'S Biderman, H Schoelkopf… - '
                                             'International …, 2023 - '
                                             'proceedings.mlr.press',
                              'snippet': '… large language models, we prioritize '
                                         'consistency in model … out the most '
                                         'performance from each model. For example, we '
                                         '… models, as it is becoming widely used for '
                                         'the largest models, …',
                              'inline_links': {'cited_by': {'cites_id': '14127511396791067241',
                                                            'total': 89,
                                                            'link': 'https://scholar.google.com/scholar?cites=14127511396791067241&as_sdt=5,33&sciodt=0,33&hl=en'},
                                               'versions': {'cluster_id': '14127511396791067241',
                                                            'total': 3,
                                                            'link': 'https://scholar.google.com/scholar?cluster=14127511396791067241&hl=en&as_sdt=0,33'},
                                               'related_articles_link': 'https://scholar.google.com/scholar?q=related:aaIDvsMAD8QJ:scholar.google.com/&scioq=Large+Language+Models&hl=en&as_sdt=0,33',
                                               'cached_page_link': 'https://scholar.googleusercontent.com/scholar?q=cache:aaIDvsMAD8QJ:scholar.google.com/+Large+Language+Models&hl=en&as_sdt=0,33'},
                              'resource': {'name': 'mlr.press',
                                           'format': 'PDF',
                                           'link': 'https://proceedings.mlr.press/v202/biderman23a/biderman23a.pdf'},
                              'authors': [{'name': 'S Biderman',
                                           'id': 'bO7H0DAAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=bO7H0DAAAAAJ&hl=en&oi=sra'},
                                          {'name': 'H Schoelkopf',
                                           'id': 'XLahYIYAAAAJ',
                                           'link': 'https://scholar.google.com/citations?user=XLahYIYAAAAJ&hl=en&oi=sra'}]}],
         'related_searches': [{'query': 'large language models machine',
                               'highlighted': ['machine'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=1&q=large+language+models+machine&qst=ib'},
                              {'query': 'large language models pruning',
                               'highlighted': ['pruning'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=2&q=large+language+models+pruning&qst=ib'},
                              {'query': 'large language models multitask learners',
                               'highlighted': ['multitask learners'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=3&q=large+language+models+multitask+learners&qst=ib'},
                              {'query': 'large language models speech recognition',
                               'highlighted': ['speech recognition'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=4&q=large+language+models+speech+recognition&qst=ib'},
                              {'query': 'large language models machine translation',
                               'highlighted': ['machine translation'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=5&q=large+language+models+machine+translation&qst=ib'},
                              {'query': 'emergent abilities of large language models',
                               'highlighted': ['emergent abilities of'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=6&q=emergent+abilities+of+large+language+models&qst=ir'},
                              {'query': 'language models privacy risks',
                               'highlighted': ['privacy risks'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=7&q=language+models+privacy+risks&qst=ir'},
                              {'query': 'language model fine tuning',
                               'highlighted': ['fine tuning'],
                               'link': 'https://scholar.google.com/scholar?hl=en&as_sdt=0,33&qsp=8&q=language+model+fine+tuning&qst=ir'}],
         'pagination': {'current': 1,
                        'next': 'https://scholar.google.com/scholar?start=10&q=Large+Language+Models&hl=en&as_sdt=0,33',
                        'other_pages': {'2': 'https://scholar.google.com/scholar?start=10&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '3': 'https://scholar.google.com/scholar?start=20&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '4': 'https://scholar.google.com/scholar?start=30&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '5': 'https://scholar.google.com/scholar?start=40&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '6': 'https://scholar.google.com/scholar?start=50&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '7': 'https://scholar.google.com/scholar?start=60&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '8': 'https://scholar.google.com/scholar?start=70&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '9': 'https://scholar.google.com/scholar?start=80&q=Large+Language+Models&hl=en&as_sdt=0,33',
                                        '10': 'https://scholar.google.com/scholar?start=90&q=Large+Language+Models&hl=en&as_sdt=0,33'}}}



```
