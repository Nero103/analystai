import streamlit as st
import pandas as pd
from ai_engine import analyze_text, analyze_pdf
from document_utils import extract_pdf_text
from config import MODEL, PDF_LIMIT

# ------------------
# UI
# ------------------

st.title("📊 AnalystAI")
st.caption("AI-Powered Business & Document Intelligence")
st.divider()
st.markdown("""
### Turn raw files into analytical insights

Upload a CSV or PDF, ask a question, and generate a structured AI-powered report using a local language model.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 CSV Analysis\n\nAnalyze datasets, trneds, missing values, and business risks.")

with col2:
    st.info("📄 PDF Intelligence\n\nSummarize documents and ask questions about report content.")

with col3:
    st.info("💾 Download Reports\n\nExport analyst outputs as text files")

# Sidebar for input
with st.sidebar:
    st.header("📂 Controls")
    st.caption("Configure your analysis")
    st.divider()
    uploaded_file = st.file_uploader(
        "Upload a CSV or PDF",
        type = ["csv", "pdf"]
    )

    user_question = st.text_input(
            "Ask a question about the data",
            placeholder = "Example: what stands out in this dataset?"
    )
    st.divider()
    st.markdown("### 🤖 model")
    st.info(MODEL)

# Main area
if uploaded_file is not None:
    #st.success(f"Uploaded: {uploaded_file.name}")

    # ------------------
    # CSV
    # ------------------

    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)

        st.success("✅ CSV uploaded successfully")
        st.caption(f"File: {uploaded_file.name}")

        left_col, right_col = st.columns([1, 1])

        with left_col:

            st.subheader("CSV Preview")
            st.dataframe(df.head(3))

        with right_col:

            st.subheader("🤖 Analysis")

            if st.button("Generate Analyst Brief"):
                with st.spinner("Analyze data..."):
                    
                    question = (
                        user_question 
                        if user_question 
                        else "What stands out in this dataset?"
                    )

                    brief = analyze_text(df, question)

                st.subheader("Analysis Brief")

                with st.container(border= True):
                    st.markdown(brief)
                #st.write(brief)

                st.download_button(
                    label = "Download Analysis Brief",
                    data = brief,
                    file_name = "analystai_brief.txt",
                    mime = "text/plain"
                )

    # --------------------
    # PDF Area
    #---------------------

    elif uploaded_file.name.endswith(".pdf"):

        st.success("✅ PDF uploaded successfully")
        st.caption(f"File: {uploaded_file.name}")

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



