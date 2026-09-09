# Code Fix Agent

An agent that fixes broken Python code by running it, reading the real error, and retrying until the tests pass.

It executes the code, checks the actual result, and sends the resulting error back to the LLM when another fix is needed.

## What It Does

The agent takes a broken Python function and assertions that define its expected behavior.

1. Runs the code and captures the output and error.
2. Sends the broken function and error to the LLM.
3. Receives a proposed fix.
4. Reattaches the original assertions.
5. Runs the fixed code again.
6. Repeats until the assertions pass or the attempt limit is reached.

## How It Works

```
Broken code + assertions
          ↓
      subprocess
          ↓
    error / output
          ↓
         LLM
          ↓
    proposed fix
          ↓
 reattach assertions
          ↓
      subprocess
          ↓
    pass / retry
```

The assertions are kept separate from the function sent to the LLM and reattached afterward. This prevents the model from modifying or removing the tests used to verify its fix.

## Example

A broken function:

```python
def sum_range(n):
    total = 0
    for i in range(n):
        total += i
    return total

assert sum_range(5) == 15
```

The function returns `10` instead of `15`.

The agent runs the code, captures the failing assertion, sends the error to the LLM, and retries with the proposed fix. The process continues until the original assertion passes.

## Project Structure

```
code-fix-agent/
├── agent/
│   ├── fixer.py
│   ├── loop.py
│   └── stopping.py
│
├── llm/
│   ├── llm.py
│   └── prompt.py
│
├── sandbox/
│   └── runner.py
│
├── tests/
│   ├── sample_broken/
│   └── fixed/
│
├── data/
│   └── evaluation/
│
├── config.py
├── main.py
├── requirements.txt
└── .env.example
```

## File Responsibilities

| File / Directory | Purpose |
|---|---|
| `agent/fixer.py` | Sends broken code and the execution error to the LLM and returns the proposed fix. |
| `agent/loop.py` | Controls the run, fix, retry, and verification cycle. |
| `agent/stopping.py` | Controls the maximum number of fix attempts. |
| `llm/llm.py` | Configures the Groq LLM client and handles model calls. |
| `llm/prompt.py` | Builds the prompt used to request a code fix. |
| `sandbox/runner.py` | Runs Python files with subprocess and captures stdout, stderr, and the return code. |
| `tests/sample_broken/` | Contains broken Python examples and their assertions. |
| `tests/fixed/` | Stores generated fix attempts without modifying the original test cases. |
| `data/evaluation/` | Stores evaluation results from agent runs. |
| `config.py` | Contains project configuration. |
| `main.py` | Runs the agent across the sample test cases. |

## Tech Stack

- **Language:** Python
- **LLM:** OpenAI GPT-OSS-120B via Groq
- **Orchestration:** LangChain
- **LLM integration:** ChatGroq and PromptTemplate
- **Execution:** Python `subprocess`

## Requirements

- Python 3.12+
- A Groq API key
- pip

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/UzairAtiq/code-fix-agent.git
cd code-fix-agent
```

**2. Create a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure the API key**

Copy the example environment file:

```bash
cp .env.example .env
```

Add your Groq API key to `.env`:

```
GROQ_API_KEY=your_api_key_here
```

## Running the Agent

Run the included evaluation cases with:

```bash
python -m main
```

The agent processes the files in `tests/sample_broken/`.

Evaluation results are stored in `data/evaluation/evaluate.json`.

## Testing Your Own Code

To test your own example:

1. Create a Python file in `tests/sample_broken/`.
2. Include the broken function.
3. Add assertions describing the expected behavior.
4. Run the agent.

Example:

```python
def multiply(a, b):
    return a + b

assert multiply(3, 4) == 12
```

The agent uses the failed assertion and execution output as feedback when generating a fix.

## Evaluation

The agent was tested against 10 broken Python functions covering cases such as:

- Off-by-one errors
- Incorrect comparison operators
- Mutable default arguments
- Missing f-string prefixes
- Integer division truncation
- Out-of-range indexing
- Other small functional bugs

**10/10 test cases passed their assertions on the first LLM-generated fix.**

Detailed evaluation results, including execution errors and proposed fixes, are stored in `data/evaluation/evaluate.json`.

## Limitations

### Assertions Are Required

The agent relies on assertions to determine whether a fix is correct. Without meaningful assertions, successful execution does not necessarily mean the code is correct.

### No Sandboxing

The executor currently runs Python code directly through subprocess without isolation. Do not run untrusted code with this project.

### Limited Test Scope

The current evaluation focuses on small, single-function bugs. Multi-function projects, complex dependencies, external services, and bugs that only appear with real-world data have not been evaluated.

## License

Add a license to the repository if you plan to distribute or reuse the project publicly.