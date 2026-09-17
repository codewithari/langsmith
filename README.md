LangChain + LangSmith Learning Project

This repository contains my hands-on learning work for the GenAI course, focused on building a simple application with Python, LangChain, OpenAI, and LangSmith.

The current project demonstrates how to send a prompt to an OpenAI chat model through LangChain and automatically trace the execution in LangSmith.

Topics Covered

Python Environment

Python virtual environment (.venv)

Installing dependencies with pip

Running Python applications from PowerShell

Keeping dependencies isolated

Environment Variables

Using .env for local configuration

Loading variables with python-dotenv

Keeping API keys outside source code

Preventing .env from being committed to GitHub

OpenAI

Creating and configuring an OpenAI API key

Understanding API billing/credits

Using gpt-4o-mini

Calling OpenAI through LangChain instead of the direct OpenAI SDK

LangChain

ChatPromptTemplate

ChatOpenAI

StrOutputParser

LangChain Expression Language (LCEL)

Application flow:

Input
  ↓
ChatPromptTemplate
  ↓
ChatOpenAI
  ↓
StrOutputParser
  ↓
Output

LangSmith

Creating a LangSmith API key

Enabling tracing

Setting a LangSmith project

Tracking LangChain executions

Inspecting prompts, responses, timing, tokens and other run information

Git and GitHub

Initializing a local Git repository

Creating and connecting a GitHub repository

Staging files

Creating commits

Renaming the branch to main

Pushing to GitHub

Verifying repository status

Project Structure

Langchain/
├── .venv/          # Python virtual environment - not committed
├── .env            # API keys and local configuration - not committed
├── .gitignore      # Files excluded from Git
├── main.py         # Main LangChain application
└── README.md       # Project documentation

Python Environment

The project uses Python 3.12.

Create the environment:

py -3.12 -m venv .venv

Activate it:

.\.venv\Scripts\Activate.ps1

Verify:

python --version

Install Dependencies

pip install langchain langchain-openai langsmith python-dotenv

Package

Purpose

langchain

Core LangChain framework

langchain-openai

OpenAI integration for LangChain

langsmith

Tracing and observability

python-dotenv

Loads variables from .env

Environment Configuration

Create .env in the project root:

OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=day-8-langchain

Never hard-code API keys in Python or commit .env to GitHub.

.gitignore:

.venv/
.env
__pycache__/
*.pyc

LangChain Application

The main application uses:

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

Prompt Template

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one simple sentence."
)

Model

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

Output Parser

output_parser = StrOutputParser()

LCEL Chain

chain = prompt | model | output_parser

Conceptually:

Prompt Template
      ↓
OpenAI Chat Model
      ↓
String Output Parser
      ↓
Final Response

The chain is executed with:

response = chain.invoke({
    "topic": "LangSmith"
})

Running the Application

Activate the environment:

.\.venv\Scripts\Activate.ps1

Run:

python main.py

Example output:

Sending prompt to OpenAI through LangChain...

Model response:
--------------------------------------------------
LangSmith is a platform designed to help developers
build, manage, and optimize language models and AI
applications efficiently.
--------------------------------------------------

LangSmith Tracing

The LangSmith configuration is:

LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=day-8-langchain

After running the application, open the day-8-langchain project in LangSmith and verify the latest run.

The trace can provide information such as:

Input

Prompt

Model execution

Model output

Execution timing

Token usage

Cost information when available

Errors

This confirms the flow:

Python Application
       ↓
LangChain
       ↓
OpenAI
       ↓
LangSmith Trace

Why LangChain Instead of Direct OpenAI API?

This assignment intentionally uses LangChain to communicate with OpenAI.

Instead of:

Application → OpenAI SDK → OpenAI

we use:

Application
    ↓
LangChain
    ↓
OpenAI

This provides a foundation for later topics such as prompt templates, chains, output parsers, RAG, tools, agents and model/provider abstraction.

LangSmith @traceable

LangSmith also provides @traceable for tracing custom Python functions. For this assignment, automatic LangChain tracing is sufficient. @traceable becomes useful when custom application logic outside the standard LangChain chain needs to be observed.

Direct OpenAI Tracing vs LangChain Tracing

LangSmith can also trace OpenAI SDK calls using mechanisms such as wrap_openai. That approach is not used here because the assignment requires the application to use LangChain to communicate with OpenAI.

Current approach:

ChatPromptTemplate
        ↓
ChatOpenAI
        ↓
StrOutputParser

Setup Issue and Lesson Learned

The first API execution produced an OpenAI quota/billing error (429 / insufficient quota). The important lesson was that such an error can be related to API billing or available credits rather than the Python, LangChain or LangSmith code itself.

After adding API credit, the application executed successfully.

Security Practices

Do

Store API keys in .env

Load them through environment variables

Keep .env out of Git

Use .gitignore

Rotate/revoke a key if it is accidentally exposed

Do Not

Hard-code API keys in Python

Commit .env

Push API keys to GitHub

Share API keys in screenshots or messages

Git Workflow Used

Initialize:

git init

Check status:

git status

Stage files:

git add .gitignore main.py README.md

Commit:

git commit -m "Build LangChain and LangSmith example"

Rename branch:

git branch -M main

Connect GitHub:

git remote add origin https://github.com/codewithari/langsmith.git

Push:

git push -u origin main

Verify:

git status

Expected:

On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

Assignment 5 Completion Checklist

Python environment created

Python 3.12 configured

Required packages installed

.env configured

OpenAI API key configured

LangSmith API key configured

LangSmith tracing enabled

LangChain connected to OpenAI

Prompt template created

ChatOpenAI configured

StrOutputParser configured

LCEL chain created

Application executed successfully

LangSmith project configured

Git repository initialized

GitHub repository connected

Code committed

Code pushed to GitHub

.env excluded from Git

Current Learning Flow

Python
  ↓
Virtual Environment
  ↓
Environment Variables
  ↓
OpenAI API
  ↓
LangChain
  ↓
Prompt Template
  ↓
Chat Model
  ↓
Output Parser
  ↓
LCEL Chain
  ↓
LangSmith Tracing
  ↓
Git
  ↓
GitHub

Next Learning Direction

Potential next topics:

More LangChain chains

Prompt engineering

Structured output

Document loading

Text splitting

Embeddings

Vector stores

Retrieval-Augmented Generation (RAG)

Agents and tools

FastAPI/Streamlit GenAI applications

Local LLM integration

Production-oriented GenAI application patterns

Learning Note

This repository is primarily a learning and experimentation project. The goal is to understand the concepts by building them practically, keeping the implementation simple first and introducing more advanced architecture only when it becomes necessary.