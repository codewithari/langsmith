# LangChain + LangSmith Learning Project

A hands-on learning project from the GenAI course, focused on building a simple LLM application with **Python, LangChain, OpenAI, and LangSmith**.

The current implementation demonstrates the complete flow from environment setup to an OpenAI chat model call through LangChain, with execution tracing in LangSmith and source control through Git/GitHub.

---

## What We Covered

### Python & Environment

- Python 3.12
- Python virtual environment (`.venv`)
- PowerShell-based project setup
- Installing packages with `pip`
- Running Python applications

### Environment Variables & Security

- `.env` for local secrets and configuration
- `python-dotenv` for loading environment variables
- API keys kept outside source code
- `.gitignore` configured to prevent `.env` and `.venv/` from being committed

### OpenAI

- OpenAI API key setup
- API credits and quota/billing awareness
- `gpt-4o-mini`
- Calling OpenAI through **LangChain**, rather than directly through the OpenAI SDK

### LangChain

- `ChatPromptTemplate`
- `ChatOpenAI`
- `StrOutputParser`
- LangChain Expression Language (LCEL)
- Chain composition using the pipe (`|`) operator
- `chain.invoke()`

### LangSmith

- LangSmith API key
- LangSmith project configuration
- Automatic tracing for LangChain runs
- Reviewing prompts, model output, timing, token usage, cost information when available, and errors
- Understanding `@traceable`
- Understanding why `wrap_openai` is not used for this assignment

### Git & GitHub

- `git init`
- `git status`
- `git add`
- `git commit`
- `git branch -M main`
- `git remote add origin`
- `git push`
- GitHub repository setup and verification

---

## Project Structure

```text
Langchain/
├── .venv/          # Local Python virtual environment - not committed
├── .env            # API keys and local configuration - not committed
├── .gitignore      # Git exclusions
├── main.py         # Main LangChain application
└── README.md       # Project documentation
```

---

## 1. Python Environment

The project uses **Python 3.12**.

Create the virtual environment:

```powershell
py -3.12 -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify the version:

```powershell
python --version
```

Expected:

```text
Python 3.12.x
```

---

## 2. Install Dependencies

```powershell
pip install langchain langchain-openai langsmith python-dotenv
```

| Package | Purpose |
|---|---|
| `langchain` | Core LangChain framework |
| `langchain-openai` | OpenAI integration for LangChain |
| `langsmith` | Tracing and observability |
| `python-dotenv` | Loads variables from `.env` |

---

## 3. Environment Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=day-8-langchain
```

### Security rule

**Never hard-code API keys in Python source code or commit `.env` to GitHub.**

The project's `.gitignore` contains:

```gitignore
.venv/
.env
__pycache__/
*.pyc
```

---

## 4. OpenAI Configuration

The application uses:

```text
gpt-4o-mini
```

The API key is read from:

```text
OPENAI_API_KEY
```

The key is not stored in `main.py`.

### Important learning point

A `429` / insufficient-quota error can be a billing or available-credit problem rather than a Python, LangChain, or LangSmith code problem.

During setup, an OpenAI quota issue was encountered and resolved by adding API credit.

---

## 5. LangChain Application Flow

The application uses four main stages:

```text
User Input
    │
    ▼
ChatPromptTemplate
    │
    ▼
ChatOpenAI
    │
    ▼
StrOutputParser
    │
    ▼
Final Response
```

The complete LangChain chain is:

```python
chain = prompt | model | output_parser
```

This is **LCEL — LangChain Expression Language**.

---

## 6. Prompt Template

The prompt is created using `ChatPromptTemplate`:

```python
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one simple sentence."
)
```

The `{topic}` value is supplied when the chain is invoked.

---

## 7. OpenAI Chat Model

The OpenAI model is configured through LangChain:

```python
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)
```

The application therefore follows:

```text
Python Application
       ↓
    LangChain
       ↓
   OpenAI Model
```

Rather than directly calling the OpenAI SDK.

---

## 8. Output Parser

`StrOutputParser` converts the model response into a normal string:

```python
output_parser = StrOutputParser()
```

The three components are then combined:

```python
chain = prompt | model | output_parser
```

---

## 9. Running the Chain

The chain is executed with:

```python
response = chain.invoke({
    "topic": "LangSmith"
})
```

The result is printed to the terminal.

Example:

```text
Sending prompt to OpenAI through LangChain...

Model response:
--------------------------------------------------
LangSmith is a platform designed to help developers
build, manage, and optimize language models and AI
applications efficiently.
--------------------------------------------------
```

---

## 10. LangSmith Tracing

LangSmith tracing is enabled through environment variables:

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=day-8-langchain
```

No additional tracing code is required for this basic LangChain flow.

After running the application, the execution can be viewed in the LangSmith project:

```text
day-8-langchain
```

A trace can provide information such as:

- Input
- Prompt
- Model execution
- Model output
- Execution time
- Token usage
- Cost information when available
- Errors

The complete observability flow is:

```text
Application
     │
     ▼
  LangChain
     │
     ▼
   OpenAI
     │
     └──────────────► LangSmith Trace
```

---

## 11. `@traceable` and `wrap_openai`

LangSmith also supports other tracing approaches.

### `@traceable`

`@traceable` can be used to trace custom Python functions. This becomes useful when application logic exists outside the standard LangChain chain.

### `wrap_openai`

LangSmith can also trace direct OpenAI SDK calls using `wrap_openai`.

That approach is **not used in this assignment** because the requirement is to communicate with OpenAI through LangChain.

Current approach:

```text
ChatPromptTemplate
        ↓
   ChatOpenAI
        ↓
 StrOutputParser
```

---

## 12. Why LangChain?

The assignment requires LangChain rather than a direct OpenAI SDK implementation.

This gives a foundation for future GenAI application patterns such as:

- Prompt templates
- Chains
- Output parsers
- Structured output
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector stores
- Tool calling
- Agents
- Application observability

The goal is to understand the building blocks first and introduce more advanced patterns as they become necessary.

---

## 13. Git Workflow

Initialize the repository:

```powershell
git init
```

Check status:

```powershell
git status
```

Stage files:

```powershell
git add .gitignore main.py
```

Create the first commit:

```powershell
git commit -m "Build LangChain and LangSmith example"
```

Use `main` as the branch:

```powershell
git branch -M main
```

Connect the GitHub repository:

```powershell
git remote add origin https://github.com/codewithari/langsmith.git
```

Push the branch:

```powershell
git push -u origin main
```

Verify the working tree:

```powershell
git status
```

Expected:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

---

## 14. GitHub Repository

Repository:

**codewithari/langsmith**

The repository should contain source/documentation files such as:

```text
.gitignore
main.py
README.md
```

It should **not** contain:

```text
.env
.venv/
__pycache__/
```

---

## 15. Assignment 5 Checklist

- [x] Python environment created
- [x] Python 3.12 configured
- [x] Required packages installed
- [x] `.env` configured
- [x] OpenAI API key configured
- [x] LangSmith API key configured
- [x] LangSmith tracing enabled
- [x] LangChain connected to OpenAI
- [x] Prompt template created
- [x] `ChatOpenAI` configured
- [x] `StrOutputParser` configured
- [x] LCEL chain created
- [x] Application executed successfully
- [x] LangSmith project configured
- [x] Git repository initialized
- [x] GitHub repository connected
- [x] Code committed
- [x] Code pushed to GitHub
- [x] `.env` excluded from Git

---

## 16. Learning Flow So Far

The practical learning path covered in this assignment is:

```text
Python
  │
  ▼
Virtual Environment
  │
  ▼
Environment Variables
  │
  ▼
OpenAI API
  │
  ▼
LangChain
  │
  ├── ChatPromptTemplate
  │
  ├── ChatOpenAI
  │
  └── StrOutputParser
  │
  ▼
LCEL Chain
  │
  ▼
LangSmith Tracing
  │
  ▼
Git
  │
  ▼
GitHub
```

---

## 17. Next Learning Topics

Possible next steps after this foundation:

1. More LangChain chains
2. Prompt engineering
3. Structured output
4. Document loading
5. Text splitting
6. Embeddings
7. Vector stores
8. Retrieval-Augmented Generation (RAG)
9. Agents and tools
10. FastAPI and Streamlit integration
11. Local LLM integration
12. Production-oriented GenAI application patterns

---

## Learning Note

This repository is primarily a **learning and experimentation project**. The implementation is intentionally simple so that the underlying GenAI concepts are clear before introducing more advanced architecture.
