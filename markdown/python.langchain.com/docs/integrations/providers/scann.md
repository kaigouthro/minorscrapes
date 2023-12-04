

Skip to main content

On this page

# Google

All functionality related to Google Cloud Platform and other `Google` products.

## LLMs​

### Vertex AI​

Access `PaLM` LLMs like `text-bison` and `code-bison` via `Google Vertex AI`.

We need to install `google-cloud-aiplatform` python package.

[code]
```python




    pip install google-cloud-aiplatform  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.llms import VertexAI  
    


```
[/code]


### Model Garden​

Access PaLM and hundreds of OSS models via `Vertex AI Model Garden`.

We need to install `google-cloud-aiplatform` python package.

[code]
```python




    pip install google-cloud-aiplatform  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.llms import VertexAIModelGarden  
    


```
[/code]


## Chat models​

### Vertex AI​

Access PaLM chat models like `chat-bison` and `codechat-bison` via Google Cloud.

We need to install `google-cloud-aiplatform` python package.

[code]
```python




    pip install google-cloud-aiplatform  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.chat_models import ChatVertexAI  
    


```
[/code]


## Document Loaders​

### Google BigQuery​

> Google BigQuery is a serverless and cost-effective enterprise data warehouse that works across clouds and scales with your data. `BigQuery` is a part of the `Google Cloud Platform`.

We need to install `google-cloud-bigquery` python package.

[code]
```python




    pip install google-cloud-bigquery  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.document_loaders import BigQueryLoader  
    


```
[/code]


### Google Cloud Storage​

> Google Cloud Storage is a managed service for storing unstructured data.

We need to install `google-cloud-storage` python package.

[code]
```python




    pip install google-cloud-storage  
    


```
[/code]


There are two loaders for the `Google Cloud Storage`: the `Directory` and the `File` loaders.

See a usage example.

[code]
```python




    from langchain.document_loaders import GCSDirectoryLoader  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.document_loaders import GCSFileLoader  
    


```
[/code]


### Google Drive​

> Google Drive is a file storage and synchronization service developed by Google.

Currently, only `Google Docs` are supported.

We need to install several python packages.

[code]
```python




    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.document_loaders import GoogleDriveLoader  
    


```
[/code]


### Speech-to-Text​

> Google Cloud Speech-to-Text is an audio transcription API powered by Google's speech recognition models.

This document loader transcribes audio files and outputs the text results as Documents.

First, we need to install the python package.

[code]
```python




    pip install google-cloud-speech  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.document_loaders import GoogleSpeechToTextLoader  
    


```
[/code]


## Vector Stores​

### Google Vertex AI Vector Search​

> Google Vertex AI Vector Search, formerly known as `Vertex AI Matching Engine`, provides the industry's leading high-scale low latency vector database. These vector databases are commonly referred to
> as vector similarity-matching or an approximate nearest neighbor (ANN) service.

We need to install several python packages.

[code]
```python




    pip install tensorflow google-cloud-aiplatform tensorflow-hub tensorflow-text  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.vectorstores import MatchingEngine  
    


```
[/code]


### Google ScaNN​

> Google ScaNN (Scalable Nearest Neighbors) is a python package.
>
> `ScaNN` is a method for efficient vector similarity search at scale.

> `ScaNN` includes search space pruning and quantization for Maximum Inner Product Search and also supports other distance functions such as Euclidean distance. The implementation is optimized for x86
> processors with AVX2 support. See its Google Research github for more details.

We need to install `scann` python package.

[code]
```python




    pip install scann  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.vectorstores import ScaNN  
    


```
[/code]


## Retrievers​

### Google Drive​

We need to install several python packages.

[code]
```python




    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain_googledrive.retrievers import GoogleDriveRetriever  
    


```
[/code]


### Vertex AI Search​

> Google Cloud Vertex AI Search allows developers to quickly build generative AI powered search engines for customers and employees.

We need to install the `google-cloud-discoveryengine` python package.

[code]
```python




    pip install google-cloud-discoveryengine  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.retrievers import GoogleVertexAISearchRetriever  
    


```
[/code]


### Document AI Warehouse​

> Google Cloud Document AI Warehouse allows enterprises to search, store, govern, and manage documents and their AI-extracted data and metadata in a single platform.
[code]
```python




    from langchain.retrievers import GoogleDocumentAIWarehouseRetriever  
    docai_wh_retriever = GoogleDocumentAIWarehouseRetriever(  
        project_number=...  
    )  
    query = ...  
    documents = docai_wh_retriever.get_relevant_documents(  
        query, user_ldap=...  
    )  
    


```
[/code]


## Tools​

### Google Drive​

We need to install several python packages.

[code]
```python




    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.utilities.google_drive import GoogleDriveAPIWrapper  
    from langchain.tools.google_drive.tool import GoogleDriveSearchTool  
    


```
[/code]


### Google Places​

We need to install a python package.

[code]
```python




    pip install googlemaps  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.tools import GooglePlacesTool  
    


```
[/code]


### Google Search​

We need to install a python package.

[code]
```python




    pip install google-api-python-client  
    


```
[/code]


  * Set up a Custom Search Engine, following these instructions
  * Get an API Key and Custom Search Engine ID from the previous step, and set them as environment variables `GOOGLE_API_KEY` and `GOOGLE_CSE_ID` respectively

[code]
```python




    from langchain.utilities import GoogleSearchAPIWrapper  
    


```
[/code]


For a more detailed walkthrough of this wrapper, see this notebook.

We can easily load this wrapper as a Tool (to use with an Agent). We can do this with:

[code]
```python




    from langchain.agents import load_tools  
    tools = load_tools(["google-search"])  
    


```
[/code]


## Document Transformers​

### Google Document AI​

> Document AI is a `Google Cloud Platform` service that transforms unstructured data from documents into structured data, making it easier to understand, analyze, and consume.

We need to set up a `GCS` bucket and create your own OCR processor  
The `GCS_OUTPUT_PATH` should be a path to a folder on GCS (starting with `gs://`) and a processor name should look like `projects/PROJECT_NUMBER/locations/LOCATION/processors/PROCESSOR_ID`. We can get
it either programmatically or copy from the `Prediction endpoint` section of the `Processor details` tab in the Google Cloud Console.

[code]
```python




    pip install google-cloud-documentai  
    pip install google-cloud-documentai-toolbox  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.document_loaders.blob_loaders import Blob  
    from langchain.document_loaders.parsers import DocAIParser  
    


```
[/code]


### Google Translate​

> Google Translate is a multilingual neural machine translation service developed by Google to translate text, documents and websites from one language into another.

The `GoogleTranslateTransformer` allows you to translate text and HTML with the Google Cloud Translation API.

To use it, you should have the `google-cloud-translate` python package installed, and a Google Cloud project with the Translation API enabled. This transformer uses the Advanced edition (v3).

First, we need to install the python package.

[code]
```python




    pip install google-cloud-translate  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.document_transformers import GoogleTranslateTransformer  
    


```
[/code]


## Toolkits​

### GMail​

> Gmail is a free email service provided by Google. This toolkit works with emails through the `Gmail API`.

We need to install several python packages.

[code]
```python




    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.agents.agent_toolkits import GmailToolkit  
    


```
[/code]


### Google Drive​

This toolkit uses the `Google Drive API`.

We need to install several python packages.

[code]
```python




    pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain_googledrive.utilities.google_drive import GoogleDriveAPIWrapper  
    from langchain_googledrive.tools.google_drive.tool import GoogleDriveSearchTool  
    


```
[/code]


## Chat Loaders​

### GMail​

> Gmail is a free email service provided by Google. This loader works with emails through the `Gmail API`.

We need to install several python packages.

[code]
```python




    pip install google-api-python-client google-auth-oauthlib google-auth-httplib2  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.chat_loaders.gmail import GMailLoader  
    


```
[/code]


## 3rd Party Integrations​

### SerpAPI​

> SerpApi provides a 3rd-party API to access Google search results.

See a usage example and authorization instructions.

[code]
```python




    from langchain.utilities import GoogleSerperAPIWrapper  
    


```
[/code]


### YouTube​

> YouTube Search package searches `YouTube` videos avoiding using their heavily rate-limited API.
>
> It uses the form on the YouTube homepage and scrapes the resulting page.

We need to install a python package.

[code]
```python




    pip install youtube_search  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.tools import YouTubeSearchTool  
    


```
[/code]


### YouTube audio​

> YouTube is an online video sharing and social media platform created by `Google`.

Use `YoutubeAudioLoader` to fetch / download the audio files.

Then, use `OpenAIWhisperParser` to transcribe them to text.

We need to install several python packages.

[code]
```python




    pip install yt_dlp pydub librosa  
    


```
[/code]


See a usage example and authorization instructions.

[code]
```python




    from langchain.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader  
    from langchain.document_loaders.parsers import OpenAIWhisperParser, OpenAIWhisperParserLocal  
    


```
[/code]


### YouTube transcripts​

> YouTube is an online video sharing and social media platform created by `Google`.

We need to install `youtube-transcript-api` python package.

[code]
```python




    pip install youtube-transcript-api  
    


```
[/code]


See a usage example.

[code]
```python




    from langchain.document_loaders import YoutubeLoader  
    


```
[/code]


