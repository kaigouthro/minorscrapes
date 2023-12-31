

Skip to main content

On this page

# Google Speech-to-Text Audio Transcripts

The `GoogleSpeechToTextLoader` allows to transcribe audio files with the Google Cloud Speech-to-Text API and loads the transcribed text into documents.

To use it, you should have the `google-cloud-speech` python package installed, and a Google Cloud project with the Speech-to-Text API enabled.

  * Bringing the power of large models to Google Cloud’s Speech API

## Installation & setup​

First, you need to install the `google-cloud-speech` python package.

You can find more info about it on the Speech-to-Text client libraries page.

Follow the quickstart guide in the Google Cloud documentation to create a project and enable the API.

```python




    %pip install google-cloud-speech



```


## Example​

The `GoogleSpeechToTextLoader` must include the `project_id` and `file_path` arguments. Audio files can be specified as a Google Cloud Storage URI (`gs://...`) or a local file path.

Only synchronous requests are supported by the loader, which has a limit of 60 seconds or 10MB per audio file.

```python




    from langchain.document_loaders import GoogleSpeechToTextLoader

    project_id = "<PROJECT_ID>"
    file_path = "gs://cloud-samples-data/speech/audio.flac"
    # or a local file path: file_path = "./audio.wav"

    loader = GoogleSpeechToTextLoader(project_id=project_id, file_path=file_path)

    docs = loader.load()



```


Note: Calling `loader.load()` blocks until the transcription is finished.

The transcribed text is available in the `page_content`:

```python




    docs[0].page_content



```


```python




    "How old is the Brooklyn Bridge?"



```


The `metadata` contains the full JSON response with more meta information:

```python




    docs[0].metadata



```


```python




    {
      'language_code': 'en-US',
      'result_end_offset': datetime.timedelta(seconds=1)
    }



```


## Recognition Config​

You can specify the `config` argument to use different speech recognition models and enable specific features.

Refer to the Speech-to-Text recognizers documentation and the `RecognizeRequest` API reference for information on how to set a custom configuation.

If you don't specify a `config`, the following options will be selected automatically:

  * Model: Chirp Universal Speech Model
  * Language: `en-US`
  * Audio Encoding: Automatically Detected
  * Automatic Punctuation: Enabled

```python




    from google.cloud.speech_v2 import (
        AutoDetectDecodingConfig,
        RecognitionConfig,
        RecognitionFeatures,
    )
    from langchain.document_loaders import GoogleSpeechToTextLoader

    project_id = "<PROJECT_ID>"
    location = "global"
    recognizer_id = "<RECOGNIZER_ID>"
    file_path = "./audio.wav"

    config = RecognitionConfig(
        auto_decoding_config=AutoDetectDecodingConfig(),
        language_codes=["en-US"],
        model="long",
        features=RecognitionFeatures(
            enable_automatic_punctuation=False,
            profanity_filter=True,
            enable_spoken_punctuation=True,
            enable_spoken_emojis=True,
        ),
    )

    loader = GoogleSpeechToTextLoader(
        project_id=project_id,
        location=location,
        recognizer_id=recognizer_id,
        file_path=file_path,
        config=config,
    )



```
