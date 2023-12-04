

Skip to main content

On this page

The stuff documents chain ("stuff" as in "to stuff" or "to fill") is the most straightforward of the document chains. It takes a list of documents, inserts them all into a prompt and passes that
prompt to an LLM.

This chain is well-suited for applications where documents are small and only a few are passed in for most calls.

## Recreating with LCEL​

With LangChain Expression Language we can easily recreate the `StuffDocumentsChain` functionality, with the additional benefit of getting all the built-in LCEL features (batch, async, etc.) and with
much more ability to customize specific parts of the chain.

```python




    from langchain.chat_models import ChatAnthropic
    from langchain.prompts import PromptTemplate
    from langchain.schema import StrOutputParser
    from langchain.schema.prompt_template import format_document



```


```python




    doc_prompt = PromptTemplate.from_template("{page_content}")

    chain = (
        {
            "content": lambda docs: "\n\n".join(
                format_document(doc, doc_prompt) for doc in docs
            )
        }
        | PromptTemplate.from_template("Summarize the following content:\n\n{content}")
        | ChatAnthropic()
        | StrOutputParser()
    )



```


### Example run​

Lets run this summarization chain on some sample data.

```python




    from langchain.schema import Document

    text = """Nuclear power in space is the use of nuclear power in outer space, typically either small fission systems or radioactive decay for electricity or heat. Another use is for scientific observation, as in a Mössbauer spectrometer. The most common type is a radioisotope thermoelectric generator, which has been used on many space probes and on crewed lunar missions. Small fission reactors for Earth observation satellites, such as the TOPAZ nuclear reactor, have also been flown.[1] A radioisotope heater unit is powered by radioactive decay and can keep components from becoming too cold to function, potentially over a span of decades.[2]

    The United States tested the SNAP-10A nuclear reactor in space for 43 days in 1965,[3] with the next test of a nuclear reactor power system intended for space use occurring on 13 September 2012 with the Demonstration Using Flattop Fission (DUFF) test of the Kilopower reactor.[4]

    After a ground-based test of the experimental 1965 Romashka reactor, which used uranium and direct thermoelectric conversion to electricity,[5] the USSR sent about 40 nuclear-electric satellites into space, mostly powered by the BES-5 reactor. The more powerful TOPAZ-II reactor produced 10 kilowatts of electricity.[3]

    Examples of concepts that use nuclear power for space propulsion systems include the nuclear electric rocket (nuclear powered ion thruster(s)), the radioisotope rocket, and radioisotope electric propulsion (REP).[6] One of the more explored concepts is the nuclear thermal rocket, which was ground tested in the NERVA program. Nuclear pulse propulsion was the subject of Project Orion.[7]

    Regulation and hazard prevention[edit]
    After the ban of nuclear weapons in space by the Outer Space Treaty in 1967, nuclear power has been discussed at least since 1972 as a sensitive issue by states.[8] Particularly its potential hazards to Earth's environment and thus also humans has prompted states to adopt in the U.N. General Assembly the Principles Relevant to the Use of Nuclear Power Sources in Outer Space (1992), particularly introducing safety principles for launches and to manage their traffic.[8]

    Benefits

    Both the Viking 1 and Viking 2 landers used RTGs for power on the surface of Mars. (Viking launch vehicle pictured)
    While solar power is much more commonly used, nuclear power can offer advantages in some areas. Solar cells, although efficient, can only supply energy to spacecraft in orbits where the solar flux is sufficiently high, such as low Earth orbit and interplanetary destinations close enough to the Sun. Unlike solar cells, nuclear power systems function independently of sunlight, which is necessary for deep space exploration. Nuclear-based systems can have less mass than solar cells of equivalent power, allowing more compact spacecraft that are easier to orient and direct in space. In the case of crewed spaceflight, nuclear power concepts that can power both life support and propulsion systems may reduce both cost and flight time.[9]

    Selected applications and/or technologies for space include:

    Radioisotope thermoelectric generator
    Radioisotope heater unit
    Radioisotope piezoelectric generator
    Radioisotope rocket
    Nuclear thermal rocket
    Nuclear pulse propulsion
    Nuclear electric rocket
    """

    docs = [
        Document(
            page_content=split,
            metadata={"source": "https://en.wikipedia.org/wiki/Nuclear_power_in_space"},
        )
        for split in text.split()
    ]



```


```python




    print(chain.invoke(docs))



```


```python




         Here is a summary of the key points:

        - Nuclear power has been used in space for electricity, heat, and scientific observation. The most common type is a radioisotope thermoelectric generator, used on many probes and lunar missions.

        - Small fission reactors have been used for Earth observation satellites. Radioisotope heater units use radioactive decay to keep components warm for decades.

        - The US tested a nuclear reactor in space in 1965. The Soviet Union launched around 40 nuclear-powered satellites, mostly with BES-5 reactors.

        - Concepts for nuclear propulsion include nuclear thermal rockets, nuclear electric rockets, and nuclear pulse propulsion. The NERVA program ground tested nuclear thermal rockets.

        - After the 1967 Outer Space Treaty banned nuclear weapons in space, safety principles were introduced for nuclear power launch and traffic management.

        - Benefits of nuclear power in space include functioning independently of sunlight needed for deep space exploration, less mass than equivalent solar power, and ability to power both life support and propulsion.



```
