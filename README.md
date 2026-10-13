# AI Business Decision Copilot 📊🤖

A zero-cost, natural-language chat assistant that answers business questions
about sales data — paired with a Power BI dashboard for visual analysis.

Ask things like *"What are the top 5 products by revenue?"* or *"Which region
sold the most in March?"* and get instant, data-grounded answers, generated
by a locally-run open-source LLM (no API keys, no cloud costs).

---

## 🏗️ Architecture

```
 User Question (chat)
        │
        ▼
 Streamlit Chat UI  ──────►  LangChain SQL Agent  ──────►  Ollama (Llama 3.1, local LLM)
        │                          │
        │                          ▼
        │                     SQLite Database (sales.db)
        │                          │
        ▼                          ▼
   Answer displayed        Same data also powers
   in chat window          a Power BI dashboard
```

## 🧰 Tech Stack (100% free)

| Layer | Tool |
|---|---|
| Data | SQLite |
| AI Engine | Ollama + Llama 3.1 (runs locally) |
| Query Translation | LangChain SQL Agent |
| Chat Interface | Streamlit |
| BI Dashboard | Power BI Desktop |
| Version Control | GitHub |

## 📁 Project Structure

```
ai-business-copilot/
├── app.py              # Streamlit chat UI
├── sql_agent.py         # LangChain SQL agent (connects LLM + database)
├── db_setup.py           # Loads CSV data into SQLite
├── requirements.txt      # Python dependencies
├── data/
│   └── sample_sales.csv  # Sample retail sales dataset
└── README.md
```

## 🚀 Setup Instructions

### 1. Clone and create a virtual environment
```bash
git clone <your-repo-url>
cd ai-business-copilot
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Ollama and pull the model
Download Ollama from [ollama.com](https://ollama.com), then run:
```bash
ollama pull llama3.1
```
(For a lighter/faster model on lower-spec machines, use `phi3` instead —
just update `MODEL_NAME` in `sql_agent.py`.)

### 4. Build the database
```bash
python db_setup.py
```
This loads `data/sample_sales.csv` into a local `sales.db` SQLite file.

### 5. Run the app
```bash
streamlit run app.py
```
Open the local URL Streamlit gives you (usually `http://localhost:8501`).

### 6. (Optional) Build the Power BI dashboard
Open Power BI Desktop → Get Data → connect to `sales.db` (via SQLite ODBC
driver) or import `data/sample_sales.csv` directly. Build visuals for:
- Revenue trend over time
- Revenue by category
- Revenue by region
- Top products (ranking table)

## 💡 Example Questions to Demo
- "What are the top 5 products by total revenue?"
- "Which region had the highest sales in March 2025?"
- "What is the total revenue for the Electronics category?"
- "Compare Furniture vs Electronics revenue"
- "Which month had the highest sales?"

## 🔭 Future Scope
This project is architected to scale to production by swapping:
- SQLite → SQL Server / Azure SQL
- Ollama (local LLM) → Azure OpenAI / GPT-4o for higher accuracy on complex queries
- Local Streamlit app → Power BI Embedded + React frontend

## 📌 Notes
- Replace `data/sample_sales.csv` with your own dataset to customize the project.
- Local LLMs (Llama 3.1, Phi-3) are less accurate than GPT-4o on complex,
  multi-join SQL — keep demo questions reasonably simple for reliable results.
