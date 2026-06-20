import streamlit as st
import pandas as pd
import ollama

def analyze_text(text):
    prompt = f"""
    You are a senior business analyst.

    Analyze the information below and provide:

    1. Executive summary
    2. Key findings
    3. Risks
    4. Opportunities
    5. Recommended next steps

    Information:

    {text}
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



##if api_key:
##    print("Api key loaded successfully!")
##else:
##    print("Api key NOT found")

st.title("AnalystAI")
st.write("Upload a PDF or CSV and get an analyst styled brief.")

uploaded_file = st.file_uploader(
    "Choose a file",
    type = ["pdf", "csv"]
)

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

        st.subheader("CSV Preview")
        st.dataframe(df.head())

        csv_summary = f"""

        Rows: {len(df)}
        Columns: {len(df.columns)}
        Column names: {list(df.columns)}

        Missing Values: {df.isnull().sum().to_string()}

        Summary Statistics:
        {df.describe(include="all").to_string()}
        """

        if st.button("Generate Analyst Brief"):
            with st.spinner("Analyze data..."):
                brief = analyze_text(csv_summary)

            st.subheader("Analyze Brief")
            st.write(brief)


