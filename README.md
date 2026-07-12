# 🛡️ Multi-Agent Arbitration Engine Workspace

A performance-optimized, zero-cost multi-agent validation gateway that runs **Llama 3.3 (70B)** and **Gemini 2.0 Flash** concurrently. The platform accepts unstructured document inputs (plain text or PDF uploads) and routes them through a deterministic arbitration layer to reconcile model discrepancies with higher reliability and consistency.

🔗 **Live Demo:** https://multi-agent-arbitration-gateway-zfwztuorkxhdjtqpichrmh.streamlit.app/

---

## 📌 Overview

Traditional AI applications rely on a single large language model, creating a single point of failure and increasing the risk of hallucinations or inconsistent outputs.

This project introduces a **Multi-Agent Arbitration Architecture** that executes multiple LLMs in parallel, validates their responses, and generates a consensus-based structured output through an intelligent arbitration layer.

The result is a more reliable, transparent, and fault-tolerant AI workflow suitable for real-world document analysis.

---

## 🏗️ Core Architecture

### 1️⃣ Parallel Extraction Layer
- Executes **Groq (Llama 3.3 70B)** and **Gemini 2.0 Flash** simultaneously.
- Built using Python's `ThreadPoolExecutor`.
- Reduces overall inference latency by processing requests in parallel.
- Improves robustness by comparing outputs from independent models.

### 2️⃣ Deterministic Arbitration Engine
- Receives structured responses from both models.
- Applies consensus-driven validation rules.
- Resolves conflicts and discrepancies automatically.
- Produces a single verified output schema.

### 3️⃣ Fail-Open Routing Strategy
- Detects API failures and rate-limit issues.
- Automatically falls back to available providers.
- Maintains application availability even under free-tier restrictions.
- Ensures uninterrupted document processing.

---

## 🎯 Supported Industry Domains

### ⚖️ Legal Analysis
Extracts and validates:
- Liability clauses
- Indemnification terms
- Payment obligations
- Contract risks
- Service agreement details

### 🏥 Medical Analysis
Identifies:
- Symptoms
- Existing medications
- Drug interactions
- Critical health warnings
- Medical risk indicators

### 📊 E-Commerce Intelligence
Analyzes:
- Product listings
- Pricing structures
- Shipping timelines
- Marketplace data
- Competitive insights

---

## 🛠️ Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Validation | Pydantic v2 |
| LLM Providers | Gemini 2.0 Flash, Llama 3.3 70B |
| API Layer | Google GenAI SDK, Groq Cloud |
| Document Processing | PyPDF |
| Concurrency | ThreadPoolExecutor |
| Language | Python |

---

## ✨ Key Features

- Multi-agent AI validation workflow
- Parallel LLM execution
- Deterministic arbitration engine
- PDF document processing
- Structured schema validation
- Failover routing mechanism
- Zero-cost deployment architecture
- Streamlit-based interactive interface

---

## 📂 Project Structure

```text
multi-agent-arbitration-gateway/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── utils/
├── schemas/
├── agents/
├── arbitration/
└── assets/
```

---

## 🚀 Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/MohibAhmadButt/multi-agent-arbitration-gateway.git
cd multi-agent-arbitration-gateway
```

### Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY="your_groq_api_key"
GEMINI_API_KEY="your_gemini_api_key"
```

### Run the Application

```bash
streamlit run app.py
```

The application will launch locally in your browser.

---

## 🔄 Processing Workflow

```text
User Input
     │
     ▼
PDF/Text Upload
     │
     ▼
Parallel Model Execution
 ┌───────────────┐
 │ Gemini Flash │
 └───────────────┘
         │
         │
 ┌───────────────┐
 │ Llama 3.3 70B│
 └───────────────┘
         │
         ▼
 Arbitration Engine
         │
         ▼
 Consensus Output
         │
         ▼
 Structured Results
```

---

## 📈 Performance Highlights

- Up to **50% lower latency** through concurrent model execution.
- Increased reliability through multi-model validation.
- Graceful degradation during API rate-limit events.
- Schema-enforced outputs using Pydantic validation.

---

## 🔒 Reliability & Safety

The arbitration layer is designed to:

- Reduce hallucinations through cross-model verification.
- Enforce structured outputs.
- Handle conflicting responses safely.
- Improve trustworthiness of extracted information.
- Maintain uptime during provider outages or quota restrictions.

---

## 🌐 Live Demo

Try the deployed application:

👉 https://multi-agent-arbitration-gateway-zfwztuorkxhdjtqpichrmh.streamlit.app/

---

## 👨‍💻 Author

**Mohib Ahmad Butt**

- BS Artificial Intelligence, SZABIST Islamabad
- AI Engineer & Multi-Agent Systems Developer
- Python • LLM Engineering • Agentic AI • Automation

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and research purposes.
