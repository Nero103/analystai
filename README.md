# AnalystAI
<img width="1918" height="867" alt="Screenshot 2026-07-03 181630" src="https://github.com/user-attachments/assets/0c2d1d7b-6d79-4493-8f3a-15d891cec123" />

AnalystAI is a local AI-powered data analysis tool that transforms CSV files into structured business insights using Streamlit and Ollama.

It allows users to upload datasets, ask questions in natural language, and receive AI-generated analyst-style reports with downloadable outputs.

## Features

- Upload and preview CSV files
- Ask natural language questions about your data
- AI-generated analyst reports (executive-level)
- Structured insights (findings, risks, recommendations)
- Download analysis as a `.txt` file
- Fully local AI processing using Ollama (no API costs)

## Tech Stack

- Python
- Streamlit (UI)
- Pandas (data processing)
- Ollama (local LLM inference)
- Phi3:mini model (lightweight local model)

## How It Works

1. Upload a CSV file
2. Dataset is processed using Pandas
3. Summary + metadata is sent to a local AI model (Ollama)
4. AI generates a structured analyst report
5. User can download the final report

1. Upload a PDF
2. Document is processed using PdfReader
3. Summary + metadata is sent to a local AI model (Ollama)
4. AI generates a structured 8000 limit preview
5. User can download the full final report

<img width="1918" height="867" alt="Screenshot 2026-07-03 181655" src="https://github.com/user-attachments/assets/e3e57677-06e7-4710-a2bd-a6b73e957470" />

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/analystai.git
cd analystai
```

### 2. Create virtual environment
```bash
python -m venv venv
```

### 3. For Windows
```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama
Download Ollama then install the model
```bash
ollama pull phi3:mini
```

### 5. Run the App
```bash
streamlit run app.py
```

## Author

AnalystAI was built by **[Nero103](https://github.com/Nero103)** as a portfolio project focused on AI-powered data analysis and analyst automation. PLEASE GIVE CREDIT
