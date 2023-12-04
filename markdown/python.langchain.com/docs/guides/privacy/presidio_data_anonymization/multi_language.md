

Skip to main content

On this page

# Multi-language data anonymization with Microsoft Presidio

## Use case​

Multi-language support in data pseudonymization is essential due to differences in language structures and cultural contexts. Different languages may have varying formats for personal identifiers. For
example, the structure of names, locations and dates can differ greatly between languages and regions. Furthermore, non-alphanumeric characters, accents, and the direction of writing can impact
pseudonymization processes. Without multi-language support, data could remain identifiable or be misinterpreted, compromising data privacy and accuracy. Hence, it enables effective and precise
pseudonymization suited for global operations.

## Overview​

PII detection in Microsoft Presidio relies on several components - in addition to the usual pattern matching (e.g. using regex), the analyser uses a model for Named Entity Recognition (NER) to extract
entities such as:

  * `PERSON`
  * `LOCATION`
  * `DATE_TIME`
  * `NRP`
  * `ORGANIZATION`

[Source]

To handle NER in specific languages, we utilize unique models from the `spaCy` library, recognized for its extensive selection covering multiple languages and sizes. However, it's not restrictive,
allowing for integration of alternative frameworks such as Stanza or transformers when necessary.

## Quickstart​

[code]
```python




    # Install necessary packages  
    # ! pip install langchain langchain-experimental openai presidio-analyzer presidio-anonymizer spacy Faker  
    # ! python -m spacy download en_core_web_lg  
    


```
[/code]


[code]
```python




    from langchain_experimental.data_anonymizer import PresidioReversibleAnonymizer  
      
    anonymizer = PresidioReversibleAnonymizer(  
        analyzed_fields=["PERSON"],  
    )  
    


```
[/code]


By default, `PresidioAnonymizer` and `PresidioReversibleAnonymizer` use a model trained on English texts, so they handle other languages moderately well.

For example, here the model did not detect the person:

[code]
```python




    anonymizer.anonymize("Me llamo Sofía")  # "My name is Sofía" in Spanish  
    


```
[/code]


[code]
```python




        'Me llamo Sofía'  
    


```
[/code]


They may also take words from another language as actual entities. Here, both the word _'Yo'_ ( _'I'_ in Spanish) and _Sofía_ have been classified as `PERSON`:

[code]
```python




    anonymizer.anonymize("Yo soy Sofía")  # "I am Sofía" in Spanish  
    


```
[/code]


[code]
```python




        'Kari Lopez soy Mary Walker'  
    


```
[/code]


If you want to anonymise texts from other languages, you need to download other models and add them to the anonymiser configuration:

[code]
```python




    # Download the models for the languages you want to use  
    # ! python -m spacy download en_core_web_md  
    # ! python -m spacy download es_core_news_md  
    


```
[/code]


[code]
```python




    nlp_config = {  
        "nlp_engine_name": "spacy",  
        "models": [  
            {"lang_code": "en", "model_name": "en_core_web_md"},  
            {"lang_code": "es", "model_name": "es_core_news_md"},  
        ],  
    }  
    


```
[/code]


We have therefore added a Spanish language model. Note also that we have downloaded an alternative model for English as well - in this case we have replaced the large model `en_core_web_lg` (560MB)
with its smaller version `en_core_web_md` (40MB) - the size is therefore reduced by 14 times! If you care about the speed of anonymisation, it is worth considering it.

All models for the different languages can be found in the spaCy documentation.

Now pass the configuration as the `languages_config` parameter to Anonymiser. As you can see, both previous examples work flawlessly:

[code]
```python




    anonymizer = PresidioReversibleAnonymizer(  
        analyzed_fields=["PERSON"],  
        languages_config=nlp_config,  
    )  
      
    print(  
        anonymizer.anonymize("Me llamo Sofía", language="es")  
    )  # "My name is Sofía" in Spanish  
    print(anonymizer.anonymize("Yo soy Sofía", language="es"))  # "I am Sofía" in Spanish  
    


```
[/code]


[code]
```python




        Me llamo Christopher Smith  
        Yo soy Joseph Jenkins  
    


```
[/code]


By default, the language indicated first in the configuration will be used when anonymising text (in this case English):

[code]
```python




    print(anonymizer.anonymize("My name is John"))  
    


```
[/code]


[code]
```python




        My name is Shawna Bennett  
    


```
[/code]


## Usage with other frameworks​

### Language detection​

One of the drawbacks of the presented approach is that we have to pass the **language** of the input text directly. However, there is a remedy for that - _language detection_ libraries.

We recommend using one of the following frameworks:

  * fasttext (recommended)
  * langdetect

From our experience _fasttext_ performs a bit better, but you should verify it on your use case.

[code]
```python




    # Install necessary packages  
    # ! pip install fasttext langdetect  
    


```
[/code]


### langdetect​

[code]
```python




    import langdetect  
    from langchain.schema import runnable  
      
      
    def detect_language(text: str) -> dict:  
        language = langdetect.detect(text)  
        print(language)  
        return {"text": text, "language": language}  
      
      
    chain = runnable.RunnableLambda(detect_language) | (  
        lambda x: anonymizer.anonymize(x["text"], language=x["language"])  
    )  
    


```
[/code]


[code]
```python




    chain.invoke("Me llamo Sofía")  
    


```
[/code]


[code]
```python




        es  
      
      
      
      
      
        'Me llamo Michael Perez III'  
    


```
[/code]


[code]
```python




    chain.invoke("My name is John Doe")  
    


```
[/code]


[code]
```python




        en  
      
      
      
      
      
        'My name is Ronald Bennett'  
    


```
[/code]


### fasttext​

You need to download the fasttext model first from https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz

[code]
```python




    import fasttext  
      
    model = fasttext.load_model("lid.176.ftz")  
      
      
    def detect_language(text: str) -> dict:  
        language = model.predict(text)[0][0].replace("__label__", "")  
        print(language)  
        return {"text": text, "language": language}  
      
      
    chain = runnable.RunnableLambda(detect_language) | (  
        lambda x: anonymizer.anonymize(x["text"], language=x["language"])  
    )  
    


```
[/code]


[code]
```python




        Warning : `load_model` does not return WordVectorModel or SupervisedModel any more, but a `FastText` object which is very similar.  
    


```
[/code]


[code]
```python




    chain.invoke("Yo soy Sofía")  
    


```
[/code]


[code]
```python




        es  
      
      
      
      
      
        'Yo soy Angela Werner'  
    


```
[/code]


[code]
```python




    chain.invoke("My name is John Doe")  
    


```
[/code]


[code]
```python




        en  
      
      
      
      
      
        'My name is Carlos Newton'  
    


```
[/code]


This way you only need to initialize the model with the engines corresponding to the relevant languages, but using the tool is fully automated.

## Advanced usage​

### Custom labels in NER model​

It may be that the spaCy model has different class names than those supported by the Microsoft Presidio by default. Take Polish, for example:

[code]
```python




    # ! python -m spacy download pl_core_news_md  
      
    import spacy  
      
    nlp = spacy.load("pl_core_news_md")  
    doc = nlp("Nazywam się Wiktoria")  # "My name is Wiktoria" in Polish  
      
    for ent in doc.ents:  
        print(  
            f"Text: {ent.text}, Start: {ent.start_char}, End: {ent.end_char}, Label: {ent.label_}"  
        )  
    


```
[/code]


[code]
```python




        Text: Wiktoria, Start: 12, End: 20, Label: persName  
    


```
[/code]


The name _Victoria_ was classified as `persName`, which does not correspond to the default class names `PERSON`/`PER` implemented in Microsoft Presidio (look for `CHECK_LABEL_GROUPS` in
SpacyRecognizer implementation).

You can find out more about custom labels in spaCy models (including your own, trained ones) in this thread.

That's why our sentence will not be anonymized:

[code]
```python




    nlp_config = {  
        "nlp_engine_name": "spacy",  
        "models": [  
            {"lang_code": "en", "model_name": "en_core_web_md"},  
            {"lang_code": "es", "model_name": "es_core_news_md"},  
            {"lang_code": "pl", "model_name": "pl_core_news_md"},  
        ],  
    }  
      
    anonymizer = PresidioReversibleAnonymizer(  
        analyzed_fields=["PERSON", "LOCATION", "DATE_TIME"],  
        languages_config=nlp_config,  
    )  
      
    print(  
        anonymizer.anonymize("Nazywam się Wiktoria", language="pl")  
    )  # "My name is Wiktoria" in Polish  
    


```
[/code]


[code]
```python




        Nazywam się Wiktoria  
    


```
[/code]


To address this, create your own `SpacyRecognizer` with your own class mapping and add it to the anonymizer:

[code]
```python




    from presidio_analyzer.predefined_recognizers import SpacyRecognizer  
      
    polish_check_label_groups = [  
        ({"LOCATION"}, {"placeName", "geogName"}),  
        ({"PERSON"}, {"persName"}),  
        ({"DATE_TIME"}, {"date", "time"}),  
    ]  
      
    spacy_recognizer = SpacyRecognizer(  
        supported_language="pl",  
        check_label_groups=polish_check_label_groups,  
    )  
      
    anonymizer.add_recognizer(spacy_recognizer)  
    


```
[/code]


Now everything works smoothly:

[code]
```python




    print(  
        anonymizer.anonymize("Nazywam się Wiktoria", language="pl")  
    )  # "My name is Wiktoria" in Polish  
    


```
[/code]


[code]
```python




        Nazywam się Morgan Walters  
    


```
[/code]


Let's try on more complex example:

[code]
```python




    print(  
        anonymizer.anonymize(  
            "Nazywam się Wiktoria. Płock to moje miasto rodzinne. Urodziłam się dnia 6 kwietnia 2001 roku",  
            language="pl",  
        )  
    )  # "My name is Wiktoria. Płock is my home town. I was born on 6 April 2001" in Polish  
    


```
[/code]


[code]
```python




        Nazywam się Ernest Liu. New Taylorburgh to moje miasto rodzinne. Urodziłam się 1987-01-19  
    


```
[/code]


As you can see, thanks to class mapping, the anonymiser can cope with different types of entities.

### Custom language-specific operators​

In the example above, the sentence has been anonymised correctly, but the fake data does not fit the Polish language at all. Custom operators can therefore be added, which will resolve the issue:

[code]
```python




    from faker import Faker  
    from presidio_anonymizer.entities import OperatorConfig  
      
    fake = Faker(locale="pl_PL")  # Setting faker to provide Polish data  
      
    new_operators = {  
        "PERSON": OperatorConfig("custom", {"lambda": lambda _: fake.first_name_female()}),  
        "LOCATION": OperatorConfig("custom", {"lambda": lambda _: fake.city()}),  
    }  
      
    anonymizer.add_operators(new_operators)  
    


```
[/code]


[code]
```python




    print(  
        anonymizer.anonymize(  
            "Nazywam się Wiktoria. Płock to moje miasto rodzinne. Urodziłam się dnia 6 kwietnia 2001 roku",  
            language="pl",  
        )  
    )  # "My name is Wiktoria. Płock is my home town. I was born on 6 April 2001" in Polish  
    


```
[/code]


[code]
```python




        Nazywam się Marianna. Szczecin to moje miasto rodzinne. Urodziłam się 1976-11-16  
    


```
[/code]


### Limitations​

Remember - results are as good as your recognizers and as your NER models!

Look at the example below - we downloaded the small model for Spanish (12MB) and it no longer performs as well as the medium version (40MB):

[code]
```python




    # ! python -m spacy download es_core_news_sm  
      
    for model in ["es_core_news_sm", "es_core_news_md"]:  
        nlp_config = {  
            "nlp_engine_name": "spacy",  
            "models": [  
                {"lang_code": "es", "model_name": model},  
            ],  
        }  
      
        anonymizer = PresidioReversibleAnonymizer(  
            analyzed_fields=["PERSON"],  
            languages_config=nlp_config,  
        )  
      
        print(  
            f"Model: {model}. Result: {anonymizer.anonymize('Me llamo Sofía', language='es')}"  
        )  
    


```
[/code]


[code]
```python




        Model: es_core_news_sm. Result: Me llamo Sofía  
        Model: es_core_news_md. Result: Me llamo Lawrence Davis  
    


```
[/code]


In many cases, even the larger models from spaCy will not be sufficient - there are already other, more complex and better methods of detecting named entities, based on transformers. You can read more
about this here.

