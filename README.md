# 🇮🇳 Smart Government Services Assistant --- Tamil Nadu (Agentic AI)

An **Agentic AI system** designed to help common people in Tamil Nadu
easily understand and apply for government services such as income
certificates, community certificates, and welfare schemes.

This project demonstrates a **multi-agent architecture** using OpenAI
models, tool integrations (MCP-style), FastAPI backend, and a Streamlit
frontend.

------------------------------------------------------------------------

# 🚀 Project Overview

Many citizens struggle with:

-   Understanding eligibility for government schemes
-   Finding the correct portal or process
-   Filling forms properly
-   Language barriers (Tamil ↔ English)

This project solves those problems using an **Agentic AI Assistant**
that:

✅ Understands natural language queries\
✅ Plans multi-step actions\
✅ Retrieves scheme information\
✅ Generates application drafts\
✅ Supports multilingual interaction

------------------------------------------------------------------------

# 🧠 Agentic Architecture

## Agents

-   **Planner Agent** -- Breaks user requests into structured steps.
-   **Scheme Agent** -- Retrieves scheme details using tool
    integrations.
-   **Form Agent** -- Generates a draft application form.
-   **Language Agent** -- Detects Tamil or English automatically.

## Tools (MCP-Style)

-   Web search tool (mock database)
-   Tamil Nadu government API tool (mock)
-   Future-ready for real MCP integrations

------------------------------------------------------------------------

# 🏗️ Project Structure

    project/
    │
    ├── backend/
    │   ├── main.py
    │   ├── agents/
    │   │   ├── planner_agent.py
    │   │   ├── scheme_agent.py
    │   │   ├── form_agent.py
    │   │   └── language_agent.py
    │   └── tools/
    │       ├── web_search_tool.py
    │       └── tn_gov_api_tool.py
    │
    ├── frontend/
    │   └── streamlit_app.py
    │
    ├── config/
    │   └── settings.py
    │
    └── README.md

------------------------------------------------------------------------

# ⚙️ Tech Stack

-   OpenAI API --- Agent reasoning & content generation
-   FastAPI --- Backend orchestration
-   Streamlit --- UI for citizens
-   ChromaDB (optional) --- Memory layer
-   LangDetect --- Language detection

------------------------------------------------------------------------

# 📦 Installation

## 1️⃣ Clone the Repository

    git clone https://github.com/VijayRakkaiah/Smart_Government_Services_Assistant-TN.git
    cd smart-gov-agent

## 2️⃣ Install Dependencies

	pip install -r requirements.txt  

------------------------------------------------------------------------

# 🔐 Environment Variables

Create a `.env` file:

    OPENAI_API_KEY=your_openai_api_key

------------------------------------------------------------------------

# ▶️ Running the Application

## Start Backend

    uvicorn backend.main:app --reload

Backend runs at:

    http://localhost:8000

## Start Frontend

    streamlit run frontend/streamlit_app.py

Open browser:

    http://localhost:8501

------------------------------------------------------------------------

# 💬 Example Queries

-   "How to apply income certificate in Tamil Nadu?"
-   "Community certificate eligibility?"
-   "எப்படி வருமானச் சான்றிதழ் apply செய்வது?"

------------------------------------------------------------------------

# ⚠️ Disclaimer

This project provides informational assistance only and does not submit
applications automatically or provide legal advice.

------------------------------------------------------------------------

# 📜 License

MIT License
