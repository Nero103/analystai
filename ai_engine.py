import ollama
from config import MODEL


# ------------------------
# CSV ANALSIS PROMPT
# ------------------------

def analyze_text(df, question):
    prompt = f"""
    You are a senior data analyst working for a Fortune 500 company.

    Your job is to analyze datasets and produce execuitve-level summaries.

    RULES:
    - Be precise and data-driven
    - Do NOT guess missing information
    - Focus on patterns, anomalies, and explanations
    - Prioritize business impact over statistics
    - Write clear for executives (non-technical audience)
    - Do NOT sound stuffy

    DATASET:

    Rows: {len(df)}
    Columns: {len(df.columns)}
    
    Column names: 
    {list(df.columns)}
    
    Data types: 
    {df.dtypes.to_string()}

    Missing Values: 
    {df.isnull().sum().to_string()}

    First 10 rows: 
    {df.head(10).to_string()}

    Summary Statistics:
    {df.describe(include="all").to_string()}

    User Question:
    {question}

    OUTPUT FORMAT:

    1. Executive Answer (direct response to question)
    2. Key Insights (bullet points)
    3. Data Evidence (what supports your answer)
    4. Risks / Concerns
    5. Recommended Next Actions
    """

    try:
        response = ollama.chat(
            model = MODEL,
            messages = [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"AI analysis failed. Error: {e}"

# ------------------------
# PDF ANALSIS PROMPT
# ------------------------

def analyze_pdf(pdf_text, question):
    prompt = f"""
    You are a senior reseach and business analyst.

    Analyze the PDF content below and answer the user's questions.

    RULES:
    - Use only the PDF content provided
    - Do not invent facts
    - If PDF does not contain enough information, say so
    - Focus on key ideas, risks, findings, useful takeaways
    - Write clearly for a non-technical audience

    PDF CONTENT:
    {pdf_text[:8000]}

    USER QUESTION:
    {question}

    OUTPUT:
    1. Executive Summary
    2. Direct Answer
    3. Key Findings
    4. Risks / Concerns
    5. Recommeneded Next Actions
    """

    try:
        response = ollama.chat(
            model = MODEL,
            messages = [{"role": "user", "content": prompt}]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"PDF analysis failed. Error: {e}"
