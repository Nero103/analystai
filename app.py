import streamlit as st
import pandas as pd
import ollama
from pypdf import PdfReader

# Configuration
MODEL = "qwen2.5:1.5b" #"phi3:mini"

# Function Extract PDF
def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text

# Function CSV
def analyze_text(df, user_question):
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
    {user_question}

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

# FUNCTION PDF
def analyze_pdf(pdf_text, user_question):
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
    {user_question}

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

st.title("AnalystAI")
## st.write("Upload a PDF or CSV and get an analyst styled brief.")

# Sidebar for input
with st.sidebar:
    st.header("Controls")

    uploaded_file = st.file_uploader(
        "Upload a CSV or PDF",
        type = ["csv", "pdf"]
    )

    user_question = st.text_input(
            "Ask a question about the data",
            placeholder = "Example: what stands out in this dataset?"
    )

# Main area
if uploaded_file is not None:
    #st.success(f"Uploaded: {uploaded_file.name}")

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

        st.success("CSV uploaded successfully")
        st.subheader("CSV Preview")
        st.dataframe(df.head())

        if st.button("Generate Analyst Brief"):
            with st.spinner("Analyze data..."):
                
                question = (
                    user_question 
                    if user_question 
                    else "What stands out in this dataset?"
                )

                brief = analyze_text(df, question)

            st.subheader("Analysis Brief")
            st.write(brief)

            st.download_button(
                label = "Download Analysis Brief",
                data = brief,
                file_name = "analystai_brief.txt",
                mime = "text/plain"
            )

    # Keep all CSV code above here

    elif uploaded_file.name.endswith(".pdf"):

        st.success("PDF uploaded successfully")

        pdf_text = extract_pdf_text(uploaded_file)

        st.subheader("PDF Preview")
        st.text(pdf_text[:2000])

        pdf_question = st.text_input(
            "Ask a question about this PDF",
            placeholder ="Example: What are the key findings?"
        )

        if st.button("Generate PDF Analysis"):
            with st.spinner("Analyzing PDF..."):
                question = (
                    pdf_question
                    if pdf_question 
                    else "Summarize the key points in this PDF."
                )

                pdf_brief = analyze_pdf(pdf_text, question)

            st.subheader("PDF Analysis")
            st.write(pdf_brief)

            st.download_button(
                label = "Download PDF Analysis",
                data = pdf_brief,
                file_name = "analystai_pdf_analysis.txt",
                mime = "text/plain"
            )

else:
    st.info("Upload csv or pdf file to begin analysis.")



