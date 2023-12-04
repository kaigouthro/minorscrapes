

Skip to main content

On this page

# Refine

The Refine documents chain constructs a response by looping over the input documents and iteratively updating its answer. For each document, it passes all non-document inputs, the current document,
and the latest intermediate answer to an LLM chain to get a new answer.

Since the Refine chain only passes a single document to the LLM at a time, it is well-suited for tasks that require analyzing more documents than can fit in the model's context. The obvious tradeoff
is that this chain will make far more LLM calls than, for example, the Stuff documents chain. There are also certain tasks which are difficult to accomplish iteratively. For example, the Refine chain
can perform poorly when documents frequently cross-reference one another or when a task requires detailed information from many documents.

## Recreating with LCEL​

With LangChain Expression Language we can easily recreate the `RefineDocumentsChain`, with the additional benefit of getting all the built-in LCEL features (batch, async, etc.) and with much more
ability to customize specific parts of the chain.

```python




    from functools import partial
    from operator import itemgetter

    from langchain.callbacks.manager import trace_as_chain_group
    from langchain.chat_models import ChatAnthropic
    from langchain.prompts import PromptTemplate
    from langchain.schema import StrOutputParser
    from langchain.schema.prompt_template import format_document



```


```python




    # Chain for generating initial summary based on the first document

    llm = ChatAnthropic()
    first_prompt = PromptTemplate.from_template("Summarize this content:\n\n{context}")
    document_prompt = PromptTemplate.from_template("{page_content}")
    partial_format_doc = partial(format_document, prompt=document_prompt)
    summary_chain = {"context": partial_format_doc} | first_prompt | llm | StrOutputParser()



```


```python




    # Chain for refining an existing summary based on
    # an additional document

    refine_prompt = PromptTemplate.from_template(
        "Here's your first summary: {prev_response}. "
        "Now add to it based on the following context: {context}"
    )
    refine_chain = (
        {
            "prev_response": itemgetter("prev_response"),
            "context": lambda x: partial_format_doc(x["doc"]),
        }
        | refine_prompt
        | llm
        | StrOutputParser()
    )



```


```python




    # The final refine loop, which generates an initial summary
    # then iteratively refines it based on each of the rest of the documents


    def refine_loop(docs):
        with trace_as_chain_group("refine loop", inputs={"input": docs}) as manager:
            summary = summary_chain.invoke(
                docs[0], config={"callbacks": manager, "run_name": "initial summary"}
            )
            for i, doc in enumerate(docs[1:]):
                summary = refine_chain.invoke(
                    {"prev_response": summary, "doc": doc},
                    config={"callbacks": manager, "run_name": f"refine {i}"},
                )
            manager.on_chain_end({"output": summary})
        return summary



```


## Example run​

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
        for split in text.split("\n\n")
    ]



```


```python




    print(refine_loop(docs))



```


```python




         Here is the updated summary with the additional context:

        Here is a summary of the key points about nuclear power in space:

        - Nuclear power is used in space for electricity, heat, and scientific observation. The most common type is a radioisotope thermoelectric generator (RTG), which uses radioactive decay to generate electricity. RTGs have powered space probes and crewed lunar missions.

        - Small nuclear fission reactors have also been used to power Earth observation satellites, like the TOPAZ reactor. The United States tested the SNAP-10A nuclear reactor in space for 43 days in 1965.

        - After a ground-based test of the experimental 1965 Romashka reactor, which used uranium and direct thermoelectric conversion to electricity, the USSR sent about 40 nuclear-electric satellites into space, mostly powered by the BES-5 reactor. The more powerful TOPAZ-II reactor produced 10 kilowatts of electricity.

        - Radioisotope heater units use radioactive decay for heat. They can keep components warm enough to function over decades.

        - Nuclear power concepts have also been proposed and tested for space propulsion. Examples include the nuclear electric rocket (nuclear powered ion thruster(s)), the radioisotope



```
