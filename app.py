import streamlit as st
import pandas as pd
import ollama

def analyze_text(df, user_question):
    prompt = f"""
    You are a senior data analyst working for a Fortune 500 company.

    Your job is to analyze datasets and produce executve-level summaries.

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
            model = "qwen2.5:0.5b",
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


st.title("AnalystAI")
## st.write("Upload a PDF or CSV and get an analyst styled brief.")

# Sidebar for input
with st.sidebar:
    st.header("Controls")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type = ["csv"]
    )

    user_question = st.text_input(
            "Ask a question about the data",
            placeholder = "Example: what stands out in this dataset?"
    )

# Main area
if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

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
else:
    st.info("Upload csv file to begin analysis.")



