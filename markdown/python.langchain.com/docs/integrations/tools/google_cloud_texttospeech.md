

Skip to main content

On this page

# Google Cloud Text-to-Speech

This notebook shows how to interact with the `Google Cloud Text-to-Speech API` to achieve speech synthesis capabilities.

First, you need to set up an Google Cloud project. You can follow the instructions here.

```python




    # !pip install google-cloud-text-to-speech



```


## Usage​

```python




    from langchain.tools import GoogleCloudTextToSpeechTool

    text_to_speak = "Hello world!"

    tts = GoogleCloudTextToSpeechTool()
    tts.name



```


We can generate audio, save it to the temporary file and then play it.

```python




    speech_file = tts.run(text_to_speak)



```
