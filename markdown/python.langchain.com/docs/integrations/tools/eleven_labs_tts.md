

Skip to main content

On this page

# Eleven Labs Text2Speech

This notebook shows how to interact with the `ElevenLabs API` to achieve text-to-speech capabilities.

First, you need to set up an ElevenLabs account. You can follow the instructions here.

```python




    # !pip install elevenlabs



```


```python




    import os

    os.environ["ELEVEN_API_KEY"] = ""



```


## Usage​

```python




    from langchain.tools import ElevenLabsText2SpeechTool

    text_to_speak = "Hello world! I am the real slim shady"

    tts = ElevenLabsText2SpeechTool()
    tts.name



```


```python




        'eleven_labs_text2speech'



```


We can generate audio, save it to the temporary file and then play it.

```python




    speech_file = tts.run(text_to_speak)
    tts.play(speech_file)



```


Or stream audio directly.

```python




    tts.stream_speech(text_to_speak)



```


## Use within an Agent​

```python




    from langchain.agents import AgentType, initialize_agent, load_tools
    from langchain.llms import OpenAI



```


```python




    llm = OpenAI(temperature=0)
    tools = load_tools(["eleven_labs_text2speech"])
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )



```


```python




    audio_file = agent.run("Tell me a joke and read it out for me.")



```


```python






        > Entering new AgentExecutor chain...
        Action:
        ```
        {
          "action": "eleven_labs_text2speech",
          "action_input": {
            "query": "Why did the chicken cross the playground? To get to the other slide!"
          }
        }
        ```


        Observation: /tmp/tmpsfg783f1.wav
        Thought: I have the audio file ready to be sent to the human
        Action:
        ```
        {
          "action": "Final Answer",
          "action_input": "/tmp/tmpsfg783f1.wav"
        }
        ```



        > Finished chain.



```


```python




    tts.play(audio_file)



```
