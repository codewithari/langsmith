import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


def main():
    load_dotenv()

    required_variables = [
        "OPENAI_API_KEY",
        "LANGSMITH_API_KEY",
    ]

    missing_variables = [
        variable
        for variable in required_variables
        if not os.getenv(variable)
    ]

    if missing_variables:
        print(
            "Missing required environment variables: "
            + ", ".join(missing_variables)
        )
        return

    prompt = ChatPromptTemplate.from_template(
        "Explain {topic} in one simple sentence."
    )

    model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    print("Sending prompt to OpenAI through LangChain...")

    response = chain.invoke({
        "topic": "LangSmith"
    })

    print("\nModel response:")
    print("-" * 50)
    print(response)
    print("-" * 50)


if __name__ == "__main__":
    main()