

Skip to main content

On this page

# YouTube transcripts

> YouTube is an online video sharing and social media platform created by Google.

This notebook covers how to load documents from `YouTube transcripts`.

[code]
```python




    from langchain.document_loaders import YoutubeLoader  
    


```
[/code]


[code]
```python




    # !pip install youtube-transcript-api  
    


```
[/code]


[code]
```python




    loader = YoutubeLoader.from_youtube_url(  
        "https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True  
    )  
    


```
[/code]


[code]
```python




    loader.load()  
    


```
[/code]


### Add video info​

[code]
```python




    # ! pip install pytube  
    


```
[/code]


[code]
```python




    loader = YoutubeLoader.from_youtube_url(  
        "https://www.youtube.com/watch?v=QsYGlZkevEg", add_video_info=True  
    )  
    loader.load()  
    


```
[/code]


### Add language preferences​

Language param : It's a list of language codes in a descending priority, `en` by default.

translation param : It's a translate preference, you can translate available transcript to your preferred language.

[code]
```python




    loader = YoutubeLoader.from_youtube_url(  
        "https://www.youtube.com/watch?v=QsYGlZkevEg",  
        add_video_info=True,  
        language=["en", "id"],  
        translation="en",  
    )  
    loader.load()  
    


```
[/code]


## YouTube loader from Google Cloud​

### Prerequisites​

  1. Create a Google Cloud project or use an existing project
  2. Enable the Youtube Api
  3. Authorize credentials for desktop app
  4. `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib youtube-transcript-api`

### 🧑 Instructions for ingesting your Google Docs data​

By default, the `GoogleDriveLoader` expects the `credentials.json` file to be `~/.credentials/credentials.json`, but this is configurable using the `credentials_file` keyword argument. Same thing with
`token.json`. Note that `token.json` will be created automatically the first time you use the loader.

`GoogleApiYoutubeLoader` can load from a list of Google Docs document ids or a folder id. You can obtain your folder and document id from the URL: Note depending on your set up, the
`service_account_path` needs to be set up. See here for more details.

[code]
```python




    # Init the GoogleApiClient  
    from pathlib import Path  
      
    from langchain.document_loaders import GoogleApiClient, GoogleApiYoutubeLoader  
      
    google_api_client = GoogleApiClient(credentials_path=Path("your_path_creds.json"))  
      
      
    # Use a Channel  
    youtube_loader_channel = GoogleApiYoutubeLoader(  
        google_api_client=google_api_client,  
        channel_name="Reducible",  
        captions_language="en",  
    )  
      
    # Use Youtube Ids  
      
    youtube_loader_ids = GoogleApiYoutubeLoader(  
        google_api_client=google_api_client, video_ids=["TrdevFK_am4"], add_video_info=True  
    )  
      
    # returns a list of Documents  
    youtube_loader_channel.load()  
    


```
[/code]


