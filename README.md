# Autonomous TODO list Agent

An autonomous AI agent system that understands natural language requests, creates its own execution plan, completes the required tasks, and generates a professionally formatted Microsoft Word (`.docx`) document.

This project demonstrates an end-to-end AI agent workflow using **FastAPI, LangGraph, Groq LLM, LangChain Tool Calling, and Python DOCX generation**.

---

## Overview

Traditional AI applications directly generate responses from user prompts.  
This project follows an agent-based approach where the system can:

- Understand a user's goal
- Dynamically create a TODO / execution plan
- Execute planned tasks
- Use external tools
- Generate a structured Word document

The agent is domain-independent and can generate:

- Business proposals
- Technical design documents
- Project plans
- SOP documents
- Meeting summaries
- Travel plans
- Learning roadmaps
- Personal productivity plans

---

## Architecture

```text
                 User

                  |
                  v

          Streamlit Interface

                  |
                  v

             FastAPI API

                  |
                  v

          LangGraph Workflow

                  |
        ---------------------
        |                   |
        v                   v

 Planner Agent       Executor Agent

        |                   |
        ----------- --------
                  |
                  v

          DOCX Generation Tool

                  |
                  v

        Microsoft Word Document
```

---

## Agent Workflow

### 1. User Request

Example:

```json
{
  "request": "Create a one week budget travel plan for Mumbai"
}
```

The user only provides the final goal.

No predefined steps or templates are required.

---

## 2. Planner Agent

The Planner Agent analyzes the request and creates an execution plan dynamically.

Example generated plan:

```text
Analyze travel requirements

Create seven day itinerary

Prepare budget recommendations

Generate checklist
```

This demonstrates autonomous planning.

---

## 3. Executor Agent

The Executor Agent receives:

- Original user request
- Generated execution plan

It completes all planned steps and creates structured content.

The executor adapts automatically:

| Request Type | Output |
|-------------|--------|
| Business | Proposal / Strategy |
| Technical | Architecture Document |
| Travel | Itinerary |
| Learning | Roadmap |
| Personal | Action Plan |

---

## 4. Tool Calling

The agent uses a dedicated document generation tool.

The LLM focuses on:

- Reasoning
- Planning
- Content generation

The tool handles:

- DOCX creation
- Formatting
- Headings
- Bullet points
- File generation

---

# Technology Stack

## Backend

- Python
- FastAPI
- Pydantic

## Agent Framework

- LangGraph
- LangChain

## LLM

- Groq API
- Llama 3.1 8B Instant

## Document Processing

- python-docx

## Frontend

- Streamlit

---

# Project Structure

```text
ai_agent/

│
├── agent/
│   ├── graph.py
│   ├── planner.py
│   ├── executor.py
│   └── state.py
│
├── llm/
│   └── model.py
│
├── tools/
│   └── document_tool.py
│
├── output/
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# API Endpoint

## POST /agent

Request:

```json
{
 "request":"Create an AI chatbot proposal"
}
```

Response:

```json
{
 "status":"completed",

 "execution_plan":[
    "Analyze requirements",
    "Prepare solution",
    "Create roadmap"
 ],

 "document":"output/generated_document.docx"
}
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <repository-url>
```

Move inside project:

```bash
cd ai_agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

# Run Application

## Start FastAPI Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

API docs:

```text
http://127.0.0.1:8000/docs
```

---

## Start Streamlit Frontend

Open another terminal:

```bash
streamlit run streamlit_app.py
```

---

# Test Examples

## Business Request

```text
Create an AI chatbot implementation proposal for an ecommerce company
```

Output:

- Execution plan
- Business proposal DOCX

---

## Complex Request

```text
Create a one week minimum budget travel plan for Mumbai
```

Output:

- Travel planning tasks
- Seven day itinerary document

---

# Engineering Improvement Implemented

## Multi-Step Planning + Tool Calling

Implemented:

- Autonomous task planning
- External document generation tool

Reason:

Real AI agents should not only generate text. They should:

1. Understand goals
2. Decide actions
3. Execute tasks
4. Use tools

---

# Architecture Optimization

Initial design:

```text
Planner

↓

Multiple Task Executors

↓

Document Tool
```

This provided detailed execution but increased:

- LLM calls
- Token usage
- Response time

Optimized design:

```text
Planner

↓

Smart Executor

↓

Document Tool
```

Benefits:

- Reduced unnecessary LLM calls
- Faster execution
- Lower token usage
- Better reliability

---

# Key Features

- Autonomous TODO generation
- LangGraph workflow orchestration
- LLM based reasoning
- Tool calling architecture
- Professional Word document generation
- FastAPI based API design
- Streamlit interface
- Modular and scalable code structure

---

# Future Improvements

- Add RAG for factual document generation
- Add conversation memory
- Add multiple specialized agents
- Add document templates
- Add database storage
- Add authentication layer

---

# Conclusion

This project demonstrates an autonomous AI agent capable of moving beyond simple text generation by combining planning, reasoning, tool usage, and document creation into a complete production-style workflow.
