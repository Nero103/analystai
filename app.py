import streamlit as st
import pandas as pd
from ai_engine import analyze_text, analyze_pdf
from document_utils import extract_pdf_text
from config import MODEL, PDF_LIMIT

# ------------------
# UI
# ------------------

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



