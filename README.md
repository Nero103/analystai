# AnalystAI
<img width="1918" height="517" alt="image" src="https://github.com/user-attachments/assets/5e5dfcb6-bf85-441d-be02-4b0323f260be" />

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
- Qwen2.5 model (lightweight local model)

## How It Works

1. Upload a CSV file
2. Dataset is processed using Pandas
3. Summary + metadata is sent to a local AI model (Ollama)
4. AI generates a structured analyst report
5. User can download the final report

<img width="1901" height="760" alt="image" src="https://github.com/user-attachments/assets/7edc3f90-20db-41db-898c-6eb9645fbf6e" />

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
ollama pull qwen2.5:0.5b
```

### 5. Run the App
```bash
streamlit run app.py
```

## Author

AnalystAI was built by **[Nero103](https://github.com/Nero103)** as a portfolio project focused on AI-powered data analysis and analyst automation. PLEASE GIVE CREDIT
