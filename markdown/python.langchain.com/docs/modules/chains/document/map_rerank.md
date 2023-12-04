

Skip to main content

On this page

# Map re-rank

The map re-rank documents chain runs an initial prompt on each document, that not only tries to complete a task but also gives a score for how certain it is in its answer. The highest scoring response
is returned.

## Recreating with LCEL​

With LangChain Expression Language we can recreate the `MapRerankDocumentsChain` functionality, with the additional benefit of getting all the built-in LCEL features (batch, async, etc.) and with much
more ability to customize specific parts of the chain.

```python




    from langchain.chat_models import ChatOpenAI
    from langchain.output_parsers.openai_functions import PydanticOutputFunctionsParser
    from langchain.prompts import PromptTemplate
    from langchain.pydantic_v1 import BaseModel, Field
    from langchain.schema.prompt_template import format_document
    from langchain.utils.openai_functions import convert_pydantic_to_openai_function



```


```python




    # Chain to apply to each individual document. Chain
    # provides an answer to the question based on the document
    # and scores it's confidence in the answer.

    map_prompt = PromptTemplate.from_template(
        "Answer the user question using the context."
        "\n\nContext:\n\n{context}\n\nQuestion: {question}"
    )


    class AnswerAndScore(BaseModel):
        """Return the answer to the question and a relevance score."""

        answer: str = Field(
            description="The answer to the question, which is based ONLY on the provided context."
        )
        score: float = Field(
            decsription="A 0.0-1.0 relevance score, where 1.0 indicates the provided context answers the question completely and 0.0 indicates the provided context does not answer the question at all."
        )


    function = convert_pydantic_to_openai_function(AnswerAndScore)
    map_chain = (
        map_prompt
        | ChatOpenAI().bind(
            temperature=0, functions=[function], function_call={"name": "AnswerAndScore"}
        )
        | PydanticOutputFunctionsParser(pydantic_schema=AnswerAndScore)
    ).with_config(run_name="Map")



```


```python




    # Final chain, which after answer and scoring based on
    # each doc return the answer with the highest score.


    def top_answer(scored_answers):
        return max(scored_answers, key=lambda x: x.score).answer


    document_prompt = PromptTemplate.from_template("{page_content}")
    map_rerank_chain = (
        (
            lambda x: [
                {
                    "context": format_document(doc, document_prompt),
                    "question": x["question"],
                }
                for doc in x["docs"]
            ]
        )
        | map_chain.map()
        | top_answer
    ).with_config(run_name="Map rerank")



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




    print(
        map_rerank_chain.invoke({"docs": docs, "question": "How were the vikings powered"})
    )



```


```python




        The Viking missions were powered by radioisotope thermoelectric generators (RTGs). These generators used the heat produced by the natural decay of plutonium-238 to generate electricity.



```
