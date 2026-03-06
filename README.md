# clara_agent_builder
Clara AI Assignment submission


This project implements an automated pipeline
that converts customer call transcripts into
structured configurations for a Clara AI voice agent.

The goal is to simulate how Clara Answers transforms
real-world conversations with service companies into
deployable AI receptionist configurations.

---
\# Problem Context
Service trade companies receive many phone calls:
\- emergency service requests

\- inspection scheduling

\- general inquiries

\- after-hours calls

Clara Answers provides an AI voice agent that can handle

these calls automatically.
However, each business has different:



\- services

\- call routing rules

\- emergency definitions

\- integrations

\- business hours
Therefore we need a system that can convert messy
human conversations into structured AI agent configurations.



---



\# What This System Does



This system takes a call transcript and automatically:
1\. Extracts business information from the transcript

2\. Converts it into a structured account memo

3\. Generates a voice agent configuration

4\. Stores the configuration as versioned output



The goal is to demonstrate how onboarding conversations
can be converted into production-ready agent specifications.
---
\# Architecture Overview
The pipeline works as follows:
Transcript

→ LLM Extraction

→ Structured Account Memo

→ Agent Prompt Generator

→ Agent Configuration JSON

→ Stored Output

Each step is automated through Python scripts.
---

\# Pipeline Steps

\## Step 1 – Input Transcript

Demo call transcripts are stored in:
transcripts/demo/

These represent conversations where a customer explain
their business and call handling needs.

Example:

\- electrical contractor

\- fire protection company

\- HVAC service provider

---

\## Step 2 – Structured Information Extraction

The script: scripts/llm\_extract.py
uses a language model prompt to extract structured
business information from the transcript.

Example fields:

\- company name

\- services supported

\- integrations

\- emergency definitions

\- unknown information

The extraction step intentionally avoids guessing
unknown information.

Missing data is placed in:

questions\_or\_unknowns
This prevents hallucination.

---

\## Step 3 – Prompt Generation


The script:

scripts/prompt\_builder.py

creates the voice agent system prompt.
The prompt defines how the AI agent should behave during calls.
The prompt includes two flows:
\### Business Hours Flow

\- greet caller

\- identify request

\- collect contact details

\- route or schedule service

\### After Hours Flow



\- determine emergency

\- collect address

\- attempt transfer

\- confirm follow-up



This structure follows the behavior described in the

assignment instructions.



---



\## Step 4 – Agent Configuration Generation



The script:





scripts/generate\_agent.py





combines the extracted account memo and generated prompt

into a deployable agent configuration.



The output contains:



\- agent name

\- version

\- system prompt

\- key variables



---



\## Step 5 – Store Results



Generated files are stored in:





outputs/<account\_id>/





Example output:





outputs/ben\_penoyer/



memo.json

agent.json





This makes the system easy to inspect and debug.



---



\# Logging



Pipeline logs are written to:





logs/pipeline.log





Logs include:



\- transcript processing

\- agent generation

\- pipeline execution steps



This helps with debugging and monitoring.



---



\# Dashboard



A simple Streamlit dashboard is included.



File:





dashboard.py





The dashboard allows reviewers to:



\- view generated account memos

\- inspect agent configurations

\- verify extracted information



---



\# Folder Structure





clara-agent-builder/



scripts/

llm\_extract.py

generate\_agent.py

prompt\_builder.py

logger.py



transcripts/

demo/

sample\_demo.txt

onboarding/



outputs/



logs/



run\_pipeline.py

dashboard.py

requirements.txt

README.md





---



\# How to Run



Install dependencies:





pip install -r requirements.txt





Run the pipeline:





python run\_pipeline.py





Launch dashboard:





streamlit run dashboard.py





---



\# Design Decisions



\### Local Processing



The system uses a local language model rather than

paid APIs to keep the solution zero-cost.



\### Structured Schema



All extracted information is converted into JSON

so that agent configurations can be generated reliably.



\### Explicit Unknown Fields



Missing information is never guessed.



Instead it is placed in:





questions\_or\_unknowns





This ensures safe automation.



---



\# Limitations



\- Extraction accuracy depends on transcript clarity

\- emergency routing rules may require manual confirmation

\- integration logic is mocked for demonstration



---



\# Future Improvements



With production access the system could include:



\- direct integration with Retell API

\- automatic CRM integration

\- advanced routing rule generation

\- UI for onboarding configuration



---

## Versioning and Diff

The system generates a v1 agent configuration from the demo call.

When onboarding data becomes available the pipeline would:

1. Update the account memo
2. Generate a v2 agent configuration
3. Produce a changelog highlighting differences between versions.

Example structure:

outputs/accounts/<account_id>/
    v1/
    v2/
    changelog.md

    ## Task Tracking

GitHub Issues can be used as the task tracking system.

Each account processing step can be logged as an issue
tracking the pipeline progress from demo call to onboarding update.



\# Summary



This project demonstrates how conversational

business information can be transformed into

structured AI voice agent configurations through

a repeatable automation pipeline.



The solution emphasizes:



\- system design

\- structured data extraction

\- safe handling of missing information

\- reproducible automation












