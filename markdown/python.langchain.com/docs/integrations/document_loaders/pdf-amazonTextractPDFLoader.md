

Skip to main content

On this page

# Amazon Textract

Amazon Textract is a machine learning (ML) service that automatically extracts text, handwriting, and data from scanned documents. It goes beyond simple optical character recognition (OCR) to
identify, understand, and extract data from forms and tables. Today, many companies manually extract data from scanned documents such as PDFs, images, tables, and forms, or through simple OCR software
that requires manual configuration (which often must be updated when the form changes). To overcome these manual and expensive processes, Textract uses ML to read and process any type of document,
accurately extracting text, handwriting, tables, and other data with no manual effort. You can quickly automate document processing and act on the information extracted, whether you’re automating
loans processing or extracting information from invoices and receipts. Textract can extract the data in minutes instead of hours or days.

This sample demonstrates the use of Amazon Textract in combination with LangChain as a DocumentLoader.

Textract supports PDF, TIFF, PNG and JPEG format.

Check https://docs.aws.amazon.com/textract/latest/dg/limits-document.html for supported document sizes, languages and characters.

```python




    # !pip install langchain boto3 openai tiktoken python-dotenv -q
    pip install boto3 openai tiktoken python-dotenv -q
    pip install -e /Users/schadem/code/github/schadem/langchain/libs/langchain



```


```python




        DEPRECATION: amazon-textract-pipeline-pagedimensions 0.0.8 has a non-standard dependency specifier Pillow>=9.4.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of amazon-textract-pipeline-pagedimensions or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063
        DEPRECATION: amazon-textract-pipeline-pagedimensions 0.0.8 has a non-standard dependency specifier pypdf>=2.5.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of amazon-textract-pipeline-pagedimensions or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063

        [notice] A new release of pip is available: 23.2 -> 23.3
        [notice] To update, run: python -m pip install --upgrade pip
        Obtaining file:///Users/schadem/code/github/schadem/langchain/libs/langchain
          Installing build dependencies ... done
          Checking if build backend supports build_editable ... done
          Getting requirements to build editable ... done
          Preparing editable metadata (pyproject.toml) ... done
        Requirement already satisfied: PyYAML>=5.3 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (6.0.1)
        Requirement already satisfied: SQLAlchemy<3,>=1.4 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (2.0.22)
        Requirement already satisfied: aiohttp<4.0.0,>=3.8.3 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (3.8.6)
        Requirement already satisfied: amazon-textract-textractor<2 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (1.4.1)
        Collecting dataclasses-json<0.6.0,>=0.5.7 (from langchain==0.0.267)
          Obtaining dependency information for dataclasses-json<0.6.0,>=0.5.7 from https://files.pythonhosted.org/packages/97/5f/e7cc90f36152810cab08b6c9c1125e8bcb9d76f8b3018d101b5f877b386c/dataclasses_json-0.5.14-py3-none-any.whl.metadata
          Downloading dataclasses_json-0.5.14-py3-none-any.whl.metadata (22 kB)
        Requirement already satisfied: langsmith<0.1.0,>=0.0.21 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (0.0.44)
        Requirement already satisfied: numexpr<3.0.0,>=2.8.4 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (2.8.7)
        Requirement already satisfied: numpy<2,>=1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (1.24.4)
        Requirement already satisfied: pydantic<3,>=1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (1.10.13)
        Requirement already satisfied: requests<3,>=2 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (2.31.0)
        Requirement already satisfied: tenacity<9.0.0,>=8.1.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from langchain==0.0.267) (8.2.3)
        Requirement already satisfied: attrs>=17.3.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.267) (23.1.0)
        Requirement already satisfied: charset-normalizer<4.0,>=2.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.267) (3.3.0)
        Requirement already satisfied: multidict<7.0,>=4.5 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.267) (6.0.4)
        Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.267) (4.0.3)
        Requirement already satisfied: yarl<2.0,>=1.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.267) (1.9.2)
        Requirement already satisfied: frozenlist>=1.1.1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.267) (1.4.0)
        Requirement already satisfied: aiosignal>=1.1.2 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from aiohttp<4.0.0,>=3.8.3->langchain==0.0.267) (1.3.1)
        Requirement already satisfied: Pillow in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-textractor<2->langchain==0.0.267) (10.1.0)
        Requirement already satisfied: XlsxWriter<3.1,>=3.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-textractor<2->langchain==0.0.267) (3.0.9)
        Collecting amazon-textract-caller<0.1.0,>=0.0.27 (from amazon-textract-textractor<2->langchain==0.0.267)
          Using cached amazon_textract_caller-0.0.29-py2.py3-none-any.whl (13 kB)
        Requirement already satisfied: amazon-textract-pipeline-pagedimensions in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-textractor<2->langchain==0.0.267) (0.0.8)
        Requirement already satisfied: amazon-textract-response-parser<0.2.0,>=0.1.45 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-textractor<2->langchain==0.0.267) (0.1.48)
        Requirement already satisfied: editdistance==0.6.2 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-textractor<2->langchain==0.0.267) (0.6.2)
        Requirement already satisfied: tabulate<0.10,>=0.9 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-textractor<2->langchain==0.0.267) (0.9.0)
        Requirement already satisfied: marshmallow<4.0.0,>=3.18.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.267) (3.20.1)
        Requirement already satisfied: typing-inspect<1,>=0.4.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.267) (0.9.0)
        Requirement already satisfied: typing-extensions>=4.2.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from pydantic<3,>=1->langchain==0.0.267) (4.8.0)
        Requirement already satisfied: idna<4,>=2.5 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from requests<3,>=2->langchain==0.0.267) (3.4)
        Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from requests<3,>=2->langchain==0.0.267) (1.26.18)
        Requirement already satisfied: certifi>=2017.4.17 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from requests<3,>=2->langchain==0.0.267) (2023.7.22)
        Requirement already satisfied: boto3>=1.26.35 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-caller<0.1.0,>=0.0.27->amazon-textract-textractor<2->langchain==0.0.267) (1.28.67)
        Requirement already satisfied: botocore in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-caller<0.1.0,>=0.0.27->amazon-textract-textractor<2->langchain==0.0.267) (1.31.67)
        Requirement already satisfied: packaging>=17.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from marshmallow<4.0.0,>=3.18.0->dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.267) (23.2)
        Requirement already satisfied: mypy-extensions>=0.3.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from typing-inspect<1,>=0.4.0->dataclasses-json<0.6.0,>=0.5.7->langchain==0.0.267) (1.0.0)
        Requirement already satisfied: pypdf>=2.5.* in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-pipeline-pagedimensions->amazon-textract-textractor<2->langchain==0.0.267) (3.16.4)
        Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from boto3>=1.26.35->amazon-textract-caller<0.1.0,>=0.0.27->amazon-textract-textractor<2->langchain==0.0.267) (1.0.1)
        Requirement already satisfied: s3transfer<0.8.0,>=0.7.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from boto3>=1.26.35->amazon-textract-caller<0.1.0,>=0.0.27->amazon-textract-textractor<2->langchain==0.0.267) (0.7.0)
        Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from botocore->amazon-textract-caller<0.1.0,>=0.0.27->amazon-textract-textractor<2->langchain==0.0.267) (2.8.2)
        Requirement already satisfied: six>=1.5 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from python-dateutil<3.0.0,>=2.1->botocore->amazon-textract-caller<0.1.0,>=0.0.27->amazon-textract-textractor<2->langchain==0.0.267) (1.16.0)
        Downloading dataclasses_json-0.5.14-py3-none-any.whl (26 kB)
        Building wheels for collected packages: langchain
          Building editable for langchain (pyproject.toml) ... done
          Created wheel for langchain: filename=langchain-0.0.267-py3-none-any.whl size=5553 sha256=daaf68d6658b27d69a4a092aa0a39e31f32b96868ef195102d2a17cf119f9d86
          Stored in directory: /private/var/folders/s4/y_t_mj094c95t80n023c9wym0000gr/T/pip-ephem-wheel-cache-v1ynlirx/wheels/9f/73/28/b1d250633de6bd5759f959e16889c6c841dd0e0ffb6474185a
        Successfully built langchain
        DEPRECATION: amazon-textract-pipeline-pagedimensions 0.0.8 has a non-standard dependency specifier Pillow>=9.4.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of amazon-textract-pipeline-pagedimensions or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063
        DEPRECATION: amazon-textract-pipeline-pagedimensions 0.0.8 has a non-standard dependency specifier pypdf>=2.5.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of amazon-textract-pipeline-pagedimensions or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063
        Installing collected packages: dataclasses-json, amazon-textract-caller, langchain
          Attempting uninstall: dataclasses-json
            Found existing installation: dataclasses-json 0.6.1
            Uninstalling dataclasses-json-0.6.1:
              Successfully uninstalled dataclasses-json-0.6.1
          Attempting uninstall: amazon-textract-caller
            Found existing installation: amazon-textract-caller 0.2.0
            Uninstalling amazon-textract-caller-0.2.0:
              Successfully uninstalled amazon-textract-caller-0.2.0
          Attempting uninstall: langchain
            Found existing installation: langchain 0.0.319
            Uninstalling langchain-0.0.319:
              Successfully uninstalled langchain-0.0.319
        Successfully installed amazon-textract-caller-0.0.29 dataclasses-json-0.5.14 langchain-0.0.267

        [notice] A new release of pip is available: 23.2 -> 23.3
        [notice] To update, run: python -m pip install --upgrade pip



```


```python




    pip install "amazon-textract-caller>=0.2.0"



```


```python




        Collecting amazon-textract-caller>=0.2.0
          Obtaining dependency information for amazon-textract-caller>=0.2.0 from https://files.pythonhosted.org/packages/35/42/17daacf400060ee1f768553980b7bd6bb77d5b80bcb8a82d8a9665e5bb9b/amazon_textract_caller-0.2.0-py2.py3-none-any.whl.metadata
          Using cached amazon_textract_caller-0.2.0-py2.py3-none-any.whl.metadata (7.1 kB)
        Requirement already satisfied: boto3>=1.26.35 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-caller>=0.2.0) (1.28.67)
        Requirement already satisfied: botocore in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-caller>=0.2.0) (1.31.67)
        Requirement already satisfied: amazon-textract-response-parser>=0.1.39 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-caller>=0.2.0) (0.1.48)
        Requirement already satisfied: marshmallow<4,>=3.14 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from amazon-textract-response-parser>=0.1.39->amazon-textract-caller>=0.2.0) (3.20.1)
        Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from boto3>=1.26.35->amazon-textract-caller>=0.2.0) (1.0.1)
        Requirement already satisfied: s3transfer<0.8.0,>=0.7.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from boto3>=1.26.35->amazon-textract-caller>=0.2.0) (0.7.0)
        Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from botocore->amazon-textract-caller>=0.2.0) (2.8.2)
        Requirement already satisfied: urllib3<2.1,>=1.25.4 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from botocore->amazon-textract-caller>=0.2.0) (1.26.18)
        Requirement already satisfied: packaging>=17.0 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from marshmallow<4,>=3.14->amazon-textract-response-parser>=0.1.39->amazon-textract-caller>=0.2.0) (23.2)
        Requirement already satisfied: six>=1.5 in /Users/schadem/.pyenv/versions/3.11.1/envs/langchain/lib/python3.11/site-packages (from python-dateutil<3.0.0,>=2.1->botocore->amazon-textract-caller>=0.2.0) (1.16.0)
        Using cached amazon_textract_caller-0.2.0-py2.py3-none-any.whl (13 kB)
        DEPRECATION: amazon-textract-pipeline-pagedimensions 0.0.8 has a non-standard dependency specifier Pillow>=9.4.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of amazon-textract-pipeline-pagedimensions or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063
        DEPRECATION: amazon-textract-pipeline-pagedimensions 0.0.8 has a non-standard dependency specifier pypdf>=2.5.*. pip 23.3 will enforce this behaviour change. A possible replacement is to upgrade to a newer version of amazon-textract-pipeline-pagedimensions or contact the author to suggest that they release a version with a conforming dependency specifiers. Discussion can be found at https://github.com/pypa/pip/issues/12063
        Installing collected packages: amazon-textract-caller
          Attempting uninstall: amazon-textract-caller
            Found existing installation: amazon-textract-caller 0.0.29
            Uninstalling amazon-textract-caller-0.0.29:
              Successfully uninstalled amazon-textract-caller-0.0.29
        ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
        amazon-textract-textractor 1.4.1 requires amazon-textract-caller<0.1.0,>=0.0.27, but you have amazon-textract-caller 0.2.0 which is incompatible.
        Successfully installed amazon-textract-caller-0.2.0

        [notice] A new release of pip is available: 23.2 -> 23.3
        [notice] To update, run: python -m pip install --upgrade pip



```


## Sample 1​

The first example uses a local file, which internally will be send to Amazon Textract sync API DetectDocumentText.

Local files or URL endpoints like HTTP:// are limited to one page documents for Textract. Multi-page documents have to reside on S3. This sample file is a jpeg.

```python




    from langchain.document_loaders import AmazonTextractPDFLoader

    loader = AmazonTextractPDFLoader("example_data/alejandro_rosalez_sample-small.jpeg")
    documents = loader.load()



```


```python




        ---------------------------------------------------------------------------

        ImportError                               Traceback (most recent call last)

        Cell In[6], line 1
        ----> 1 from langchain.document_loaders import AmazonTextractPDFLoader
              2 loader = AmazonTextractPDFLoader("example_data/alejandro_rosalez_sample-small.jpeg")
              3 documents = loader.load()


        File ~/code/github/schadem/langchain/libs/langchain/langchain/document_loaders/__init__.py:46
             44 from langchain.document_loaders.bigquery import BigQueryLoader
             45 from langchain.document_loaders.bilibili import BiliBiliLoader
        ---> 46 from langchain.document_loaders.blackboard import BlackboardLoader
             47 from langchain.document_loaders.blob_loaders import (
             48     Blob,
             49     BlobLoader,
             50     FileSystemBlobLoader,
             51     YoutubeAudioLoader,
             52 )
             53 from langchain.document_loaders.blockchain import BlockchainDocumentLoader


        File ~/code/github/schadem/langchain/libs/langchain/langchain/document_loaders/blackboard.py:9
              7 from langchain.docstore.document import Document
              8 from langchain.document_loaders.directory import DirectoryLoader
        ----> 9 from langchain.document_loaders.pdf import PyPDFLoader
             10 from langchain.document_loaders.web_base import WebBaseLoader
             13 class BlackboardLoader(WebBaseLoader):


        File ~/code/github/schadem/langchain/libs/langchain/langchain/document_loaders/pdf.py:17
             15 from langchain.document_loaders.base import BaseLoader
             16 from langchain.document_loaders.blob_loaders import Blob
        ---> 17 from langchain.document_loaders.parsers.pdf import (
             18     AmazonTextractPDFParser,
             19     DocumentIntelligenceParser,
             20     PDFMinerParser,
             21     PDFPlumberParser,
             22     PyMuPDFParser,
             23     PyPDFium2Parser,
             24     PyPDFParser,
             25 )
             26 from langchain.document_loaders.unstructured import UnstructuredFileLoader
             27 from langchain.utils import get_from_dict_or_env


        ImportError: cannot import name 'DocumentIntelligenceParser' from 'langchain.document_loaders.parsers.pdf' (/Users/schadem/code/github/schadem/langchain/libs/langchain/langchain/document_loaders/parsers/pdf.py)



```


Output from the file

```python




    documents



```


```python




        [Document(page_content='Patient Information First Name: ALEJANDRO Last Name: ROSALEZ Date of Birth: 10/10/1982 Sex: M Marital Status: MARRIED Email Address: Address: 123 ANY STREET City: ANYTOWN State: CA Zip Code: 12345 Phone: 646-555-0111 Emergency Contact 1: First Name: CARLOS Last Name: SALAZAR Phone: 212-555-0150 Relationship to Patient: BROTHER Emergency Contact 2: First Name: JANE Last Name: DOE Phone: 650-555-0123 Relationship FRIEND to Patient: Did you feel fever or feverish lately? Yes No Are you having shortness of breath? Yes No Do you have a cough? Yes No Did you experience loss of taste or smell? Yes No Where you in contact with any confirmed COVID-19 positive patients? Yes No Did you travel in the past 14 days to any regions affected by COVID-19? Yes No Patient Information First Name: ALEJANDRO Last Name: ROSALEZ Date of Birth: 10/10/1982 Sex: M Marital Status: MARRIED Email Address: Address: 123 ANY STREET City: ANYTOWN State: CA Zip Code: 12345 Phone: 646-555-0111 Emergency Contact 1: First Name: CARLOS Last Name: SALAZAR Phone: 212-555-0150 Relationship to Patient: BROTHER Emergency Contact 2: First Name: JANE Last Name: DOE Phone: 650-555-0123 Relationship FRIEND to Patient: Did you feel fever or feverish lately? Yes No Are you having shortness of breath? Yes No Do you have a cough? Yes No Did you experience loss of taste or smell? Yes No Where you in contact with any confirmed COVID-19 positive patients? Yes No Did you travel in the past 14 days to any regions affected by COVID-19? Yes No ', metadata={'source': 'example_data/alejandro_rosalez_sample-small.jpeg', 'page': 1})]



```


## Sample 2​

The next sample loads a file from an HTTPS endpoint. It has to be single page, as Amazon Textract requires all multi-page documents to be stored on S3.

```python




    from langchain.document_loaders import AmazonTextractPDFLoader

    loader = AmazonTextractPDFLoader(
        "https://amazon-textract-public-content.s3.us-east-2.amazonaws.com/langchain/alejandro_rosalez_sample_1.jpg"
    )
    documents = loader.load()



```


```python




    documents



```


```python




        [Document(page_content='Patient Information First Name: ALEJANDRO Last Name: ROSALEZ Date of Birth: 10/10/1982 Sex: M Marital Status: MARRIED Email Address: Address: 123 ANY STREET City: ANYTOWN State: CA Zip Code: 12345 Phone: 646-555-0111 Emergency Contact 1: First Name: CARLOS Last Name: SALAZAR Phone: 212-555-0150 Relationship to Patient: BROTHER Emergency Contact 2: First Name: JANE Last Name: DOE Phone: 650-555-0123 Relationship FRIEND to Patient: Did you feel fever or feverish lately? Yes No Are you having shortness of breath? Yes No Do you have a cough? Yes No Did you experience loss of taste or smell? Yes No Where you in contact with any confirmed COVID-19 positive patients? Yes No Did you travel in the past 14 days to any regions affected by COVID-19? Yes No Patient Information First Name: ALEJANDRO Last Name: ROSALEZ Date of Birth: 10/10/1982 Sex: M Marital Status: MARRIED Email Address: Address: 123 ANY STREET City: ANYTOWN State: CA Zip Code: 12345 Phone: 646-555-0111 Emergency Contact 1: First Name: CARLOS Last Name: SALAZAR Phone: 212-555-0150 Relationship to Patient: BROTHER Emergency Contact 2: First Name: JANE Last Name: DOE Phone: 650-555-0123 Relationship FRIEND to Patient: Did you feel fever or feverish lately? Yes No Are you having shortness of breath? Yes No Do you have a cough? Yes No Did you experience loss of taste or smell? Yes No Where you in contact with any confirmed COVID-19 positive patients? Yes No Did you travel in the past 14 days to any regions affected by COVID-19? Yes No ', metadata={'source': 'example_data/alejandro_rosalez_sample-small.jpeg', 'page': 1})]



```


## Sample 3​

Processing a multi-page document requires the document to be on S3. The sample document resides in a bucket in us-east-2 and Textract needs to be called in that same region to be successful, so we set
the region_name on the client and pass that in to the loader to ensure Textract is called from us-east-2. You could also to have your notebook running in us-east-2, setting the AWS_DEFAULT_REGION set
to us-east-2 or when running in a different environment, pass in a boto3 Textract client with that region name like in the cell below.

```python




    import boto3

    textract_client = boto3.client("textract", region_name="us-east-2")

    file_path = "s3://amazon-textract-public-content/langchain/layout-parser-paper.pdf"
    loader = AmazonTextractPDFLoader(file_path, client=textract_client)
    documents = loader.load()



```


Now getting the number of pages to validate the response (printing out the full response would be quite long...). We expect 16 pages.

```python




    len(documents)



```


```python




        16



```


## Using the AmazonTextractPDFLoader in an LangChain chain (e. g. OpenAI)​

The AmazonTextractPDFLoader can be used in a chain the same way the other loaders are used. Textract itself does have a Query feature, which offers similar functionality to the QA chain in this
sample, which is worth checking out as well.

```python




    # You can store your OPENAI_API_KEY in a .env file as well
    # import os
    # from dotenv import load_dotenv

    # load_dotenv()



```


```python




    # Or set the OpenAI key in the environment directly
    import os

    os.environ["OPENAI_API_KEY"] = "your-OpenAI-API-key"



```


```python




    from langchain.chains.question_answering import load_qa_chain
    from langchain.llms import OpenAI

    chain = load_qa_chain(llm=OpenAI(), chain_type="map_reduce")
    query = ["Who are the autors?"]

    chain.run(input_documents=documents, question=query)



```


```python




        ' The authors are Zejiang Shen, Ruochen Zhang, Melissa Dell, Benjamin Charles Germain Lee, Jacob Carlson, Weining Li, Gardner, M., Grus, J., Neumann, M., Tafjord, O., Dasigi, P., Liu, N., Peters, M., Schmitz, M., Zettlemoyer, L., Lukasz Garncarek, Powalski, R., Stanislawek, T., Topolski, B., Halama, P., Gralinski, F., Graves, A., Fernández, S., Gomez, F., Schmidhuber, J., Harley, A.W., Ufkes, A., Derpanis, K.G., He, K., Gkioxari, G., Dollár, P., Girshick, R., He, K., Zhang, X., Ren, S., Sun, J., Kay, A., Lamiroy, B., Lopresti, D., Mears, J., Jakeway, E., Ferriter, M., Adams, C., Yarasavage, N., Thomas, D., Zwaard, K., Li, M., Cui, L., Huang,'



```
